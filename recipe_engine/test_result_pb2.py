# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_result.proto',
  package='recipe_engine',
  syntax='proto3',
  serialized_pb=_b('\n\x11test_result.proto\x12\rrecipe_engine\"\xd0\x08\n\nTestResult\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\r\n\x05valid\x18\x02 \x01(\x08\x12J\n\x11\x63overage_failures\x18\x03 \x03(\x0b\x32/.recipe_engine.TestResult.CoverageFailuresEntry\x12\x42\n\rtest_failures\x18\x04 \x03(\x0b\x32+.recipe_engine.TestResult.TestFailuresEntry\x12\x19\n\x11uncovered_modules\x18\x05 \x03(\t\x12\x1b\n\x13unused_expectations\x18\x06 \x03(\t\x1a*\n\x0f\x43overageFailure\x12\x17\n\x0funcovered_lines\x18\x01 \x03(\x03\x1a\x62\n\x15\x43overageFailuresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).recipe_engine.TestResult.CoverageFailure:\x02\x38\x01\x1a\r\n\x0b\x44iffFailure\x1a\xcd\x01\n\x0c\x43heckFailure\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x66unc\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x42\n\x06kwargs\x18\x04 \x03(\x0b\x32\x32.recipe_engine.TestResult.CheckFailure.KwargsEntry\x12\x10\n\x08\x66ilename\x18\x05 \x01(\t\x12\x0e\n\x06lineno\x18\x06 \x01(\x03\x1a-\n\x0bKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x0e\n\x0c\x43rashFailure\x1a\x11\n\x0fInternalFailure\x1a\xa1\x02\n\x0bTestFailure\x12=\n\x0c\x64iff_failure\x18\x01 \x01(\x0b\x32%.recipe_engine.TestResult.DiffFailureH\x00\x12?\n\rcheck_failure\x18\x02 \x01(\x0b\x32&.recipe_engine.TestResult.CheckFailureH\x00\x12\x45\n\x10internal_failure\x18\x03 \x01(\x0b\x32).recipe_engine.TestResult.InternalFailureH\x00\x12?\n\rcrash_failure\x18\x04 \x01(\x0b\x32&.recipe_engine.TestResult.CrashFailureH\x00\x42\n\n\x08\x66\x61ilures\x1aG\n\x0cTestFailures\x12\x37\n\x08\x66\x61ilures\x18\x01 \x03(\x0b\x32%.recipe_engine.TestResult.TestFailure\x1a[\n\x11TestFailuresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.recipe_engine.TestResult.TestFailures:\x02\x38\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTRESULT_COVERAGEFAILURE = _descriptor.Descriptor(
  name='CoverageFailure',
  full_name='recipe_engine.TestResult.CoverageFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uncovered_lines', full_name='recipe_engine.TestResult.CoverageFailure.uncovered_lines', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=325,
)

_TESTRESULT_COVERAGEFAILURESENTRY = _descriptor.Descriptor(
  name='CoverageFailuresEntry',
  full_name='recipe_engine.TestResult.CoverageFailuresEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='recipe_engine.TestResult.CoverageFailuresEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='recipe_engine.TestResult.CoverageFailuresEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=425,
)

_TESTRESULT_DIFFFAILURE = _descriptor.Descriptor(
  name='DiffFailure',
  full_name='recipe_engine.TestResult.DiffFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=440,
)

_TESTRESULT_CHECKFAILURE_KWARGSENTRY = _descriptor.Descriptor(
  name='KwargsEntry',
  full_name='recipe_engine.TestResult.CheckFailure.KwargsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='recipe_engine.TestResult.CheckFailure.KwargsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='recipe_engine.TestResult.CheckFailure.KwargsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=648,
)

_TESTRESULT_CHECKFAILURE = _descriptor.Descriptor(
  name='CheckFailure',
  full_name='recipe_engine.TestResult.CheckFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='recipe_engine.TestResult.CheckFailure.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func', full_name='recipe_engine.TestResult.CheckFailure.func', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='recipe_engine.TestResult.CheckFailure.args', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='recipe_engine.TestResult.CheckFailure.kwargs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='recipe_engine.TestResult.CheckFailure.filename', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineno', full_name='recipe_engine.TestResult.CheckFailure.lineno', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTRESULT_CHECKFAILURE_KWARGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=648,
)

_TESTRESULT_CRASHFAILURE = _descriptor.Descriptor(
  name='CrashFailure',
  full_name='recipe_engine.TestResult.CrashFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=650,
  serialized_end=664,
)

_TESTRESULT_INTERNALFAILURE = _descriptor.Descriptor(
  name='InternalFailure',
  full_name='recipe_engine.TestResult.InternalFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=683,
)

_TESTRESULT_TESTFAILURE = _descriptor.Descriptor(
  name='TestFailure',
  full_name='recipe_engine.TestResult.TestFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diff_failure', full_name='recipe_engine.TestResult.TestFailure.diff_failure', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_failure', full_name='recipe_engine.TestResult.TestFailure.check_failure', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='internal_failure', full_name='recipe_engine.TestResult.TestFailure.internal_failure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crash_failure', full_name='recipe_engine.TestResult.TestFailure.crash_failure', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='failures', full_name='recipe_engine.TestResult.TestFailure.failures',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=686,
  serialized_end=975,
)

_TESTRESULT_TESTFAILURES = _descriptor.Descriptor(
  name='TestFailures',
  full_name='recipe_engine.TestResult.TestFailures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failures', full_name='recipe_engine.TestResult.TestFailures.failures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=977,
  serialized_end=1048,
)

_TESTRESULT_TESTFAILURESENTRY = _descriptor.Descriptor(
  name='TestFailuresEntry',
  full_name='recipe_engine.TestResult.TestFailuresEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='recipe_engine.TestResult.TestFailuresEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='recipe_engine.TestResult.TestFailuresEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1050,
  serialized_end=1141,
)

_TESTRESULT = _descriptor.Descriptor(
  name='TestResult',
  full_name='recipe_engine.TestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='recipe_engine.TestResult.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid', full_name='recipe_engine.TestResult.valid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coverage_failures', full_name='recipe_engine.TestResult.coverage_failures', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_failures', full_name='recipe_engine.TestResult.test_failures', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uncovered_modules', full_name='recipe_engine.TestResult.uncovered_modules', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unused_expectations', full_name='recipe_engine.TestResult.unused_expectations', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTRESULT_COVERAGEFAILURE, _TESTRESULT_COVERAGEFAILURESENTRY, _TESTRESULT_DIFFFAILURE, _TESTRESULT_CHECKFAILURE, _TESTRESULT_CRASHFAILURE, _TESTRESULT_INTERNALFAILURE, _TESTRESULT_TESTFAILURE, _TESTRESULT_TESTFAILURES, _TESTRESULT_TESTFAILURESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=1141,
)

_TESTRESULT_COVERAGEFAILURE.containing_type = _TESTRESULT
_TESTRESULT_COVERAGEFAILURESENTRY.fields_by_name['value'].message_type = _TESTRESULT_COVERAGEFAILURE
_TESTRESULT_COVERAGEFAILURESENTRY.containing_type = _TESTRESULT
_TESTRESULT_DIFFFAILURE.containing_type = _TESTRESULT
_TESTRESULT_CHECKFAILURE_KWARGSENTRY.containing_type = _TESTRESULT_CHECKFAILURE
_TESTRESULT_CHECKFAILURE.fields_by_name['kwargs'].message_type = _TESTRESULT_CHECKFAILURE_KWARGSENTRY
_TESTRESULT_CHECKFAILURE.containing_type = _TESTRESULT
_TESTRESULT_CRASHFAILURE.containing_type = _TESTRESULT
_TESTRESULT_INTERNALFAILURE.containing_type = _TESTRESULT
_TESTRESULT_TESTFAILURE.fields_by_name['diff_failure'].message_type = _TESTRESULT_DIFFFAILURE
_TESTRESULT_TESTFAILURE.fields_by_name['check_failure'].message_type = _TESTRESULT_CHECKFAILURE
_TESTRESULT_TESTFAILURE.fields_by_name['internal_failure'].message_type = _TESTRESULT_INTERNALFAILURE
_TESTRESULT_TESTFAILURE.fields_by_name['crash_failure'].message_type = _TESTRESULT_CRASHFAILURE
_TESTRESULT_TESTFAILURE.containing_type = _TESTRESULT
_TESTRESULT_TESTFAILURE.oneofs_by_name['failures'].fields.append(
  _TESTRESULT_TESTFAILURE.fields_by_name['diff_failure'])
_TESTRESULT_TESTFAILURE.fields_by_name['diff_failure'].containing_oneof = _TESTRESULT_TESTFAILURE.oneofs_by_name['failures']
_TESTRESULT_TESTFAILURE.oneofs_by_name['failures'].fields.append(
  _TESTRESULT_TESTFAILURE.fields_by_name['check_failure'])
_TESTRESULT_TESTFAILURE.fields_by_name['check_failure'].containing_oneof = _TESTRESULT_TESTFAILURE.oneofs_by_name['failures']
_TESTRESULT_TESTFAILURE.oneofs_by_name['failures'].fields.append(
  _TESTRESULT_TESTFAILURE.fields_by_name['internal_failure'])
_TESTRESULT_TESTFAILURE.fields_by_name['internal_failure'].containing_oneof = _TESTRESULT_TESTFAILURE.oneofs_by_name['failures']
_TESTRESULT_TESTFAILURE.oneofs_by_name['failures'].fields.append(
  _TESTRESULT_TESTFAILURE.fields_by_name['crash_failure'])
_TESTRESULT_TESTFAILURE.fields_by_name['crash_failure'].containing_oneof = _TESTRESULT_TESTFAILURE.oneofs_by_name['failures']
_TESTRESULT_TESTFAILURES.fields_by_name['failures'].message_type = _TESTRESULT_TESTFAILURE
_TESTRESULT_TESTFAILURES.containing_type = _TESTRESULT
_TESTRESULT_TESTFAILURESENTRY.fields_by_name['value'].message_type = _TESTRESULT_TESTFAILURES
_TESTRESULT_TESTFAILURESENTRY.containing_type = _TESTRESULT
_TESTRESULT.fields_by_name['coverage_failures'].message_type = _TESTRESULT_COVERAGEFAILURESENTRY
_TESTRESULT.fields_by_name['test_failures'].message_type = _TESTRESULT_TESTFAILURESENTRY
DESCRIPTOR.message_types_by_name['TestResult'] = _TESTRESULT

TestResult = _reflection.GeneratedProtocolMessageType('TestResult', (_message.Message,), dict(

  CoverageFailure = _reflection.GeneratedProtocolMessageType('CoverageFailure', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_COVERAGEFAILURE,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.CoverageFailure)
    ))
  ,

  CoverageFailuresEntry = _reflection.GeneratedProtocolMessageType('CoverageFailuresEntry', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_COVERAGEFAILURESENTRY,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.CoverageFailuresEntry)
    ))
  ,

  DiffFailure = _reflection.GeneratedProtocolMessageType('DiffFailure', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_DIFFFAILURE,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.DiffFailure)
    ))
  ,

  CheckFailure = _reflection.GeneratedProtocolMessageType('CheckFailure', (_message.Message,), dict(

    KwargsEntry = _reflection.GeneratedProtocolMessageType('KwargsEntry', (_message.Message,), dict(
      DESCRIPTOR = _TESTRESULT_CHECKFAILURE_KWARGSENTRY,
      __module__ = 'test_result_pb2'
      # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.CheckFailure.KwargsEntry)
      ))
    ,
    DESCRIPTOR = _TESTRESULT_CHECKFAILURE,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.CheckFailure)
    ))
  ,

  CrashFailure = _reflection.GeneratedProtocolMessageType('CrashFailure', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_CRASHFAILURE,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.CrashFailure)
    ))
  ,

  InternalFailure = _reflection.GeneratedProtocolMessageType('InternalFailure', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_INTERNALFAILURE,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.InternalFailure)
    ))
  ,

  TestFailure = _reflection.GeneratedProtocolMessageType('TestFailure', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_TESTFAILURE,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.TestFailure)
    ))
  ,

  TestFailures = _reflection.GeneratedProtocolMessageType('TestFailures', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_TESTFAILURES,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.TestFailures)
    ))
  ,

  TestFailuresEntry = _reflection.GeneratedProtocolMessageType('TestFailuresEntry', (_message.Message,), dict(
    DESCRIPTOR = _TESTRESULT_TESTFAILURESENTRY,
    __module__ = 'test_result_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.TestResult.TestFailuresEntry)
    ))
  ,
  DESCRIPTOR = _TESTRESULT,
  __module__ = 'test_result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.TestResult)
  ))
_sym_db.RegisterMessage(TestResult)
_sym_db.RegisterMessage(TestResult.CoverageFailure)
_sym_db.RegisterMessage(TestResult.CoverageFailuresEntry)
_sym_db.RegisterMessage(TestResult.DiffFailure)
_sym_db.RegisterMessage(TestResult.CheckFailure)
_sym_db.RegisterMessage(TestResult.CheckFailure.KwargsEntry)
_sym_db.RegisterMessage(TestResult.CrashFailure)
_sym_db.RegisterMessage(TestResult.InternalFailure)
_sym_db.RegisterMessage(TestResult.TestFailure)
_sym_db.RegisterMessage(TestResult.TestFailures)
_sym_db.RegisterMessage(TestResult.TestFailuresEntry)


_TESTRESULT_COVERAGEFAILURESENTRY.has_options = True
_TESTRESULT_COVERAGEFAILURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_TESTRESULT_CHECKFAILURE_KWARGSENTRY.has_options = True
_TESTRESULT_CHECKFAILURE_KWARGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_TESTRESULT_TESTFAILURESENTRY.has_options = True
_TESTRESULT_TESTFAILURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
