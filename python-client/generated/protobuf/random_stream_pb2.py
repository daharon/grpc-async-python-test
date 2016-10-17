# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: random_stream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='random_stream.proto',
  package='us.aharon.randomstream',
  syntax='proto3',
  serialized_pb=_b('\n\x13random_stream.proto\x12\x16us.aharon.randomstream\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"K\n\x0bRandomValue\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x06\x32W\n\x0cRandomStream\x12G\n\x04Read\x12\x16.google.protobuf.Empty\x1a#.us.aharon.randomstream.RandomValue\"\x00\x30\x01\x42-\n\x16us.aharon.randomstreamB\x11RandomStreamProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RANDOMVALUE = _descriptor.Descriptor(
  name='RandomValue',
  full_name='us.aharon.randomstream.RandomValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='us.aharon.randomstream.RandomValue.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='us.aharon.randomstream.RandomValue.value', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=109,
  serialized_end=184,
)

_RANDOMVALUE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['RandomValue'] = _RANDOMVALUE

RandomValue = _reflection.GeneratedProtocolMessageType('RandomValue', (_message.Message,), dict(
  DESCRIPTOR = _RANDOMVALUE,
  __module__ = 'random_stream_pb2'
  # @@protoc_insertion_point(class_scope:us.aharon.randomstream.RandomValue)
  ))
_sym_db.RegisterMessage(RandomValue)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026us.aharon.randomstreamB\021RandomStreamProtoP\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class RandomStreamStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Read = channel.unary_stream(
        '/us.aharon.randomstream.RandomStream/Read',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=RandomValue.FromString,
        )


class RandomStreamServicer(object):

  def Read(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RandomStreamServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Read': grpc.unary_stream_rpc_method_handler(
          servicer.Read,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=RandomValue.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'us.aharon.randomstream.RandomStream', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaRandomStreamServicer(object):
  def Read(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaRandomStreamStub(object):
  def Read(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_RandomStream_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('us.aharon.randomstream.RandomStream', 'Read'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
  }
  response_serializers = {
    ('us.aharon.randomstream.RandomStream', 'Read'): RandomValue.SerializeToString,
  }
  method_implementations = {
    ('us.aharon.randomstream.RandomStream', 'Read'): face_utilities.unary_stream_inline(servicer.Read),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_RandomStream_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('us.aharon.randomstream.RandomStream', 'Read'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
  }
  response_deserializers = {
    ('us.aharon.randomstream.RandomStream', 'Read'): RandomValue.FromString,
  }
  cardinalities = {
    'Read': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'us.aharon.randomstream.RandomStream', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
