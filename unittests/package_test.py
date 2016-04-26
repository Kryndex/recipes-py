#!/usr/bin/env python
# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import copy
import doctest
import os
import subprocess
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THIRD_PARTY = os.path.join(ROOT_DIR, 'recipe_engine', 'third_party')
sys.path.insert(0, os.path.join(THIRD_PARTY, 'mock-1.0.1'))
sys.path.insert(0, THIRD_PARTY)
sys.path.insert(0, ROOT_DIR)

import mock
from recipe_engine import package

import repo_test_util


TEST_AUTHOR = 'foo@example.com'


class MockIOThings(object):
  def setUp(self):
    super(MockIOThings, self).setUp()

    self.mock_os_patcher = mock.patch('recipe_engine.package.os')
    self.mock_os = self.mock_os_patcher.start()
    self.mock_os.path.join = os.path.join
    self.mock_os.path.dirname = os.path.dirname
    self.mock_os.sep = os.sep

    self.orig_subprocess = subprocess
    self.mock_subprocess_patcher = mock.patch(
        'recipe_engine.package.subprocess')
    self.mock_subprocess = self.mock_subprocess_patcher.start()
    self.mock_subprocess.PIPE = self.orig_subprocess.PIPE

  def tearDown(self):
    self.mock_subprocess_patcher.stop()
    self.mock_os_patcher.stop()

    super(MockIOThings, self).tearDown()


class TestGitRepoSpec(repo_test_util.RepoTest):
  def test_commit_infos(self):
    repos = self.repo_setup({'a': []})

    spec = package.GitRepoSpec(
        'a', repos['a']['root'], 'master', repos['a']['revision'], '')
    self.assertEqual(
        [],
        [ci.dump() for ci in spec.commit_infos(self._context, 'HEAD')])

    c1 = self.commit_in_repo(
        repos['a'], message='c1', author_email=TEST_AUTHOR)
    self.reset_repo(repos['a'], repos['a']['revision'])
    self.assertEqual([
            {
                'repo_id': 'a',
                'revision': c1['revision'],
                'message': 'c1',
                'author': TEST_AUTHOR
            },
        ],
        [ci.dump() for ci in spec.commit_infos(self._context, c1['revision'])])

    self.reset_repo(repos['a'], c1['revision'])
    c2 = self.commit_in_repo(
        repos['a'], message='c2', author_email=TEST_AUTHOR)
    self.reset_repo(repos['a'], repos['a']['revision'])
    self.assertEqual([
            {
                'repo_id': 'a',
                'revision': c1['revision'],
                'message': 'c1',
                'author': TEST_AUTHOR
            },
            {
                'repo_id': 'a',
                'revision': c2['revision'],
                'message': 'c2',
                'author': TEST_AUTHOR
            },
        ],
        [ci.dump() for ci in spec.commit_infos(self._context, c2['revision'])])

  def test_raw_updates(self):
    repos = self.repo_setup({'a': []})

    spec = package.GitRepoSpec(
        'a', repos['a']['root'], 'master', repos['a']['revision'], '')
    self.assertEqual([], spec.raw_updates(self._context, 'HEAD'))

    c1 = self.commit_in_repo(repos['a'], message='c1')
    self.reset_repo(repos['a'], repos['a']['revision'])
    self.assertEqual([
        c1['revision']],
        spec.raw_updates(self._context, c1['revision']))

    self.reset_repo(repos['a'], c1['revision'])
    c2 = self.commit_in_repo(repos['a'], message='c2')
    self.reset_repo(repos['a'], repos['a']['revision'])
    self.assertEqual([
        c1['revision'], c2['revision']],
        spec.raw_updates(self._context, c2['revision']))

    self.reset_repo(repos['a'], c2['revision'])
    c3 = self.commit_in_repo(repos['a'], message='c3')
    self.reset_repo(repos['a'], repos['a']['revision'])
    self.assertEqual([
        c1['revision'], c2['revision'], c3['revision']],
        spec.raw_updates(self._context, c3['revision']))

  def test_get_more_recent_revision(self):
    repos = self.repo_setup({'a': []})

    spec = package.GitRepoSpec(
        'a', repos['a']['root'], 'master', repos['a']['revision'], '')

    c1 = self.commit_in_repo(repos['a'], message='c1')
    c2 = self.commit_in_repo(repos['a'], message='c2')

    self.assertEqual(
        c2['revision'],
        spec.get_more_recent_revision(
            self._context, c1['revision'], c2['revision']))

    self.assertEqual(
        c2['revision'],
        spec.get_more_recent_revision(
            self._context, c2['revision'], c1['revision']))


class TestRollCandidate(repo_test_util.RepoTest):
  def test_trivial(self):
    repos = self.repo_setup({
        'a': [],
        'b': ['a'],
    })
    root_repo_spec = self.get_root_repo_spec(repos['b'])
    a_repo_spec = self.get_git_repo_spec(repos['a'])
    b_package_spec = self.get_package_spec(repos['b'])

    # Create a new commit in the A repo.
    a_c1 = self.commit_in_repo(repos['a'], message='c1')
    self.reset_repo(repos['a'], repos['a']['revision'])
    a_updates = a_repo_spec.updates(self._context, a_c1['revision'])
    self.assertEqual(
        ['a@%s' % a_c1['revision']],
        [str(u) for u in a_updates])

    # Create a roll candidate to roll the new A commit into B.
    candidate = package.RollCandidate(
        b_package_spec, self._context, a_updates[0])

    # Verify it's the only roll candidate in this situation.
    roll_candidates, rejected_candidates = b_package_spec.roll_candidates(
        root_repo_spec, self._context)
    self.assertEqual([candidate], roll_candidates)
    self.assertEqual([], rejected_candidates)

    original_candidate = copy.deepcopy(candidate)
    self.assertTrue(candidate.make_consistent(root_repo_spec))
    rolled_spec = candidate.get_rolled_spec()

    # Original roll should already be consistent, so that make_consistent
    # is a no-op.
    self.assertEqual(original_candidate.get_rolled_spec().dump(),
                     rolled_spec.dump())

    # The roll should make package spec different from the original
    # by changing the revision to use for the A repo.
    self.assertNotEqual(b_package_spec.dump(),
                        rolled_spec.dump())
    self.assertEqual(
        str(b_package_spec.dump()).replace(
            repos['a']['revision'], a_c1['revision']),
        str(rolled_spec.dump()))

    self.assertEqual(
        {'a': [a_c1['revision']]},
        {project_id: [ci.revision for ci in cis] for project_id, cis in
         candidate.get_commit_infos().iteritems()})

  def test_nontrivial(self):
    repos = self.repo_setup({
        'a': [],
        'b': ['a'],
        'c': ['b', 'a'],
    })
    root_repo_spec = self.get_root_repo_spec(repos['c'])
    a_repo_spec = self.get_git_repo_spec(repos['a'])
    b_repo_spec = self.get_git_repo_spec(repos['b'])
    c_package_spec = self.get_package_spec(repos['c'])

    # Create some commits in the A repo.
    a_c1 = self.commit_in_repo(repos['a'], message='c1')
    a_c2 = self.commit_in_repo(repos['a'], message='c2')
    self.reset_repo(repos['a'], repos['a']['revision'])
    a_updates = a_repo_spec.updates(self._context, a_c2['revision'])
    self.assertEqual(
        ['a@%s' % a_c1['revision'], 'a@%s' % a_c2['revision']],
        [str(u) for u in a_updates])
    self.reset_repo(repos['a'], a_c2['revision'])

    # Create commits in the B repo that pull different A repo revisions.
    b_c1_rev = self.update_recipes_cfg(
        'b', self.updated_package_spec_pb(repos['b'], 'a', a_c1['revision']))
    b_c2_rev = self.update_recipes_cfg(
        'b', self.updated_package_spec_pb(repos['b'], 'a', a_c2['revision']))
    self.reset_repo(repos['b'], repos['b']['revision'])
    b_updates = b_repo_spec.updates(self._context, b_c2_rev)
    self.assertEqual(
        ['b@%s' % b_c1_rev, 'b@%s' % b_c2_rev],
        [str(u) for u in b_updates])
    self.reset_repo(repos['b'], b_c2_rev)

    # Create a roll candidate to roll some B commits into C.
    candidate = package.RollCandidate(
        c_package_spec, self._context, b_updates[1])
    self.assertTrue(candidate.make_consistent(root_repo_spec))

    # The roll should make package spec different from the original
    # by changing the revision to use for the A repo.
    rolled_spec = candidate.get_rolled_spec()
    self.assertNotEqual(c_package_spec.dump(),
                        rolled_spec.dump())
    self.assertEqual(
        str(c_package_spec.dump()).replace(
            repos['b']['revision'], b_c2_rev).replace(
            repos['a']['revision'], a_c2['revision']),
        str(rolled_spec.dump()))

    self.assertEqual(
        {
            'a': [a_c1['revision'], a_c2['revision']],
            'b': [b_c1_rev, b_c2_rev],
        },
        {project_id: [ci.revision for ci in cis] for project_id, cis in
         candidate.get_commit_infos().iteritems()})

    # There's an alternative, smaller roll possible. Make sure it was
    # considered.
    alternative_candidate = package.RollCandidate(
        c_package_spec, self._context, b_updates[0])
    self.assertTrue(alternative_candidate.make_consistent(root_repo_spec))

    self.assertEqual(
        {
            'a': [a_c1['revision']],
            'b': [b_c1_rev],
        },
        {project_id: [ci.revision for ci in cis] for project_id, cis in
         alternative_candidate.get_commit_infos().iteritems()})

    roll_candidates, _ = c_package_spec.roll_candidates(
        root_repo_spec, self._context)
    self.assertEqual([candidate, alternative_candidate], roll_candidates)

  def test_roll_candidates(self):
    """Tests that we consider all consistent rolls, not just a subset.
    This differentiates the new roll algorithm from previous one.
    """
    repos = self.repo_setup({
        'a': [],
        'b': ['a'],
        'c': ['b', 'a'],
    })
    root_repo_spec = self.get_root_repo_spec(repos['c'])
    a_repo_spec = self.get_git_repo_spec(repos['a'])
    b_repo_spec = self.get_git_repo_spec(repos['b'])
    c_package_spec = self.get_package_spec(repos['c'])

    # Create some commits in the A repo.
    a_c1 = self.commit_in_repo(repos['a'], message='c1')
    a_c2 = self.commit_in_repo(repos['a'], message='c2')
    a_c3 = self.commit_in_repo(repos['a'], message='c3')
    self.reset_repo(repos['a'], repos['a']['revision'])
    a_updates = a_repo_spec.updates(self._context, a_c3['revision'])
    self.assertEqual(
        [
            'a@%s' % a_c1['revision'],
            'a@%s' % a_c2['revision'],
            'a@%s' % a_c3['revision']
        ],
        [str(u) for u in a_updates])
    self.reset_repo(repos['a'], a_c3['revision'])

    # Create a commit in the B repo that uses the same revision of A.
    b_c1_rev = self.commit_in_repo(repos['b'], message='c1')['revision']
    # Create commits in the B repo that pull different A repo revisions.
    b_c2_rev = self.update_recipes_cfg(
        'b', self.updated_package_spec_pb(repos['b'], 'a', a_c2['revision']))
    b_c3_rev = self.update_recipes_cfg(
        'b', self.updated_package_spec_pb(repos['b'], 'a', a_c3['revision']))
    self.reset_repo(repos['b'], repos['b']['revision'])
    b_updates = b_repo_spec.updates(self._context, b_c3_rev)
    self.assertEqual(
        ['b@%s' % b_c1_rev, 'b@%s' % b_c2_rev, 'b@%s' % b_c3_rev],
        [str(u) for u in b_updates])
    self.reset_repo(repos['b'], b_c3_rev)

    candidate1 = package.RollCandidate(
        c_package_spec, self._context, b_updates[2])
    self.assertTrue(candidate1.make_consistent(root_repo_spec))
    self.assertEqual(
        {
            'a': [a_c1['revision'], a_c2['revision'], a_c3['revision']],
            'b': [b_c1_rev, b_c2_rev, b_c3_rev],
        },
        {project_id: [ci.revision for ci in cis] for project_id, cis in
         candidate1.get_commit_infos().iteritems()})

    candidate2 = package.RollCandidate(
        c_package_spec, self._context, b_updates[1])
    self.assertTrue(candidate2.make_consistent(root_repo_spec))
    self.assertEqual(
        {
            'a': [a_c1['revision'], a_c2['revision']],
            'b': [b_c1_rev, b_c2_rev],
        },
        {project_id: [ci.revision for ci in cis] for project_id, cis in
         candidate2.get_commit_infos().iteritems()})

    candidate3 = package.RollCandidate(
        c_package_spec, self._context, b_updates[0])
    self.assertTrue(candidate3.make_consistent(root_repo_spec))
    self.assertEqual(
        {
            'b': [b_c1_rev],
        },
        {project_id: [ci.revision for ci in cis] for project_id, cis in
         candidate3.get_commit_infos().iteritems()})

    roll_candidates, _ = c_package_spec.roll_candidates(
        root_repo_spec, self._context)
    self.assertEqual([candidate1, candidate2, candidate3], roll_candidates)

  def test_no_backwards_roll(self):
    """Tests that we never roll backwards.
    """
    repos = self.repo_setup({
        'a': [],
        'b': ['a'],
        'c': ['b', 'a'],
    })
    root_repo_spec = self.get_root_repo_spec(repos['c'])
    b_repo_spec = self.get_git_repo_spec(repos['b'])

    # Create a new commit in A repo. Roll it to C but not B.
    a_c1 = self.commit_in_repo(repos['a'], message='c1')
    c_c1_rev = self.update_recipes_cfg(
        'c', self.updated_package_spec_pb(repos['c'], 'a', a_c1['revision']))

    # Create a commit in the B repo (which will use an older revision of A).
    b_c1 = self.commit_in_repo(repos['b'], message='c1')
    self.reset_repo(repos['b'], repos['b']['revision'])
    b_updates = b_repo_spec.updates(self._context, b_c1['revision'])
    self.assertEqual(
        ['b@%s' % b_c1['revision']],
        [str(u) for u in b_updates])
    self.reset_repo(repos['b'], b_c1['revision'])

    c_package_spec = self.get_package_spec(repos['c'])
    candidate = package.RollCandidate(
        c_package_spec, self._context, b_updates[0])
    self.assertFalse(candidate.make_consistent(root_repo_spec))


class MockProtoFile(package.ProtoFile):
  def __init__(self, path, text):
    super(MockProtoFile, self).__init__(path)
    self._text = text

  @property
  def path(self):
    return self._path

  def read_text(self):
    return self._text

  def write(self, buf):
    pass


class TestPackageSpec(MockIOThings, unittest.TestCase):
  def setUp(self):
    super(TestPackageSpec, self).setUp()

    self.proto_text = """
api_version: 1
project_id: "super_main_package"
recipes_path: "path/to/recipes"
deps {
  project_id: "bar"
  url: "https://repo.com/bar.git"
  branch: "superbar"
  revision: "deadd00d"
}
deps {
  project_id: "foo"
  url: "https://repo.com/foo.git"
  branch: "master"
  revision: "cafebeef"
}
""".lstrip()
    self.proto_file = MockProtoFile('repo/root/infra/config/recipes.cfg',
                                    self.proto_text)
    self.context = package.PackageContext.from_proto_file(
        'repo/root', self.proto_file, allow_fetch=False)

  def test_dump_load_inverses(self):
    # Doubles as a test for equality reflexivity.
    package_spec = package.PackageSpec.load_proto(self.proto_file)
    self.assertEqual(self.proto_file.to_text(package_spec.dump()),
                     self.proto_text)
    self.assertEqual(package.PackageSpec.load_proto(self.proto_file),
                     package_spec)

  def test_updates_merged(self):
    """Tests that updates are monotone in each dependency's history and
    that dep rolls stay in their proper dependency."""

    def trivial_proto(project_id):
      return lambda context: MockProtoFile('infra/config/recipes.cfg', """
api_version: 1
project_id: "%s"
recipes_path: ""
""".lstrip() % project_id)

    package_spec = package.PackageSpec.load_proto(self.proto_file)
    foo_revs = [ "aaaaaa", "123456", "cdabfe" ]
    bar_revs = [ "0156ff", "ffaaff", "aa0000" ]
    package_spec.deps['bar'].raw_updates = mock.Mock(return_value=bar_revs)
    package_spec.deps['bar'].proto_file = trivial_proto('bar')
    package_spec.deps['foo'].raw_updates = mock.Mock(return_value=foo_revs)
    package_spec.deps['foo'].proto_file = trivial_proto('foo')

    updates = package_spec.updates(self.context)
    foo_update_ixs = [
        (['cafebeef'] + foo_revs).index(update.spec.deps['foo'].revision)
        for update in updates ]
    bar_update_ixs = [
        (['deadd00d'] + bar_revs).index(update.spec.deps['bar'].revision)
        for update in updates ]
    self.assertEqual(len(updates), 6)
    self.assertEqual(foo_update_ixs, sorted(foo_update_ixs))
    self.assertEqual(bar_update_ixs, sorted(bar_update_ixs))

  def test_no_version(self):
    proto_text = """\
project_id: "foo"
recipes_path: "path/to/recipes"
"""
    proto_file = MockProtoFile('repo/root/infra/config/recipes.cfg', proto_text)

    with self.assertRaises(AssertionError):
      package.PackageSpec.load_proto(proto_file)

  def test_unsupported_version(self):
    proto_text = """\
api_version: 99999999
project_id: "fizzbar"
recipes_path: "path/to/recipes"
"""
    proto_file = MockProtoFile('repo/root/infra/config/recipes.cfg', proto_text)

    with self.assertRaises(AssertionError):
      package.PackageSpec.load_proto(proto_file)


class TestPackageDeps(MockIOThings, unittest.TestCase):

  def test_create_with_overrides(self):
    base_proto_text = """
api_version: 1
project_id: "base_package"
recipes_path: "path/to/recipes"
deps {
  project_id: "foo"
  url: "https://repo.com/foo.git"
  branch: "foobranch"
  revision: "deadd00d"
}
"""
    base_proto_file = MockProtoFile('base/infra/config/recipes.cfg',
                                    base_proto_text)

    foo_proto_text = """
api_version: 1
project_id: "foo"
recipes_path: "path/to/recipes"
"""
    foo_proto_file = MockProtoFile('foo/infra/config/recipes.cfg',
                                   foo_proto_text)

    with mock.patch.object(package.GitRepoSpec, 'proto_file',
                           return_value=foo_proto_file):
      deps = package.PackageDeps.create('base', base_proto_file, overrides={
        'foo': '/path/to/local/foo',
      })

    foo_deps = deps.get_package('foo')
    self.assertIsInstance(foo_deps.repo_spec, package.PathRepoSpec)
    self.assertEqual(foo_deps.repo_spec.path, '/path/to/local/foo')


def load_tests(_loader, tests, _ignore):
  tests.addTests(doctest.DocTestSuite(package))
  return tests


if __name__ == '__main__':
  result = unittest.main()