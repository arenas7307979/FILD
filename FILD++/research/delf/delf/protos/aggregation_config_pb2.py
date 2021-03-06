# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delf/protos/aggregation_config.proto

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
  name='delf/protos/aggregation_config.proto',
  package='delf.protos',
  syntax='proto2',
  serialized_pb=_b('\n$delf/protos/aggregation_config.proto\x12\x0b\x64\x65lf.protos\"\xb1\x03\n\x11\x41ggregationConfig\x12\x1c\n\rcodebook_size\x18\x01 \x01(\x05:\x05\x36\x35\x35\x33\x36\x12#\n\x16\x66\x65\x61ture_dimensionality\x18\x02 \x01(\x05:\x03\x31\x32\x38\x12S\n\x10\x61ggregation_type\x18\x03 \x01(\x0e\x32..delf.protos.AggregationConfig.AggregationType:\tASMK_STAR\x12\"\n\x14use_l2_normalization\x18\x04 \x01(\x08:\x04true\x12\x15\n\rcodebook_path\x18\x05 \x01(\t\x12\x1a\n\x0fnum_assignments\x18\x06 \x01(\x05:\x01\x31\x12\'\n\x18use_regional_aggregation\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x12\x66\x65\x61ture_batch_size\x18\n \x01(\x05:\x03\x31\x30\x30\x12\x10\n\x05\x61lpha\x18\x08 \x01(\x02:\x01\x33\x12\x0e\n\x03tau\x18\t \x01(\x02:\x01\x30\"A\n\x0f\x41ggregationType\x12\x0b\n\x07INVALID\x10\x00\x12\x08\n\x04VLAD\x10\x01\x12\x08\n\x04\x41SMK\x10\x02\x12\r\n\tASMK_STAR\x10\x03')
)



_AGGREGATIONCONFIG_AGGREGATIONTYPE = _descriptor.EnumDescriptor(
  name='AggregationType',
  full_name='delf.protos.AggregationConfig.AggregationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VLAD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASMK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASMK_STAR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=422,
  serialized_end=487,
)
_sym_db.RegisterEnumDescriptor(_AGGREGATIONCONFIG_AGGREGATIONTYPE)


_AGGREGATIONCONFIG = _descriptor.Descriptor(
  name='AggregationConfig',
  full_name='delf.protos.AggregationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codebook_size', full_name='delf.protos.AggregationConfig.codebook_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=65536,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_dimensionality', full_name='delf.protos.AggregationConfig.feature_dimensionality', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=128,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aggregation_type', full_name='delf.protos.AggregationConfig.aggregation_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_l2_normalization', full_name='delf.protos.AggregationConfig.use_l2_normalization', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='codebook_path', full_name='delf.protos.AggregationConfig.codebook_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_assignments', full_name='delf.protos.AggregationConfig.num_assignments', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_regional_aggregation', full_name='delf.protos.AggregationConfig.use_regional_aggregation', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_batch_size', full_name='delf.protos.AggregationConfig.feature_batch_size', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='delf.protos.AggregationConfig.alpha', index=8,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tau', full_name='delf.protos.AggregationConfig.tau', index=9,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AGGREGATIONCONFIG_AGGREGATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=487,
)

_AGGREGATIONCONFIG.fields_by_name['aggregation_type'].enum_type = _AGGREGATIONCONFIG_AGGREGATIONTYPE
_AGGREGATIONCONFIG_AGGREGATIONTYPE.containing_type = _AGGREGATIONCONFIG
DESCRIPTOR.message_types_by_name['AggregationConfig'] = _AGGREGATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AggregationConfig = _reflection.GeneratedProtocolMessageType('AggregationConfig', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATIONCONFIG,
  __module__ = 'delf.protos.aggregation_config_pb2'
  # @@protoc_insertion_point(class_scope:delf.protos.AggregationConfig)
  ))
_sym_db.RegisterMessage(AggregationConfig)


# @@protoc_insertion_point(module_scope)
