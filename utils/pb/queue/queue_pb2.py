# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: queue.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bqueue.proto\x12\x05queue\"x\n\x11\x41\x64\x64toQueueRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\t\x12\x16\n\x0e\x65xpirationDate\x18\x04 \x01(\t\x12\x0b\n\x03\x63vv\x18\x05 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x06 \x01(\t\"&\n\x12\x41\x64\x64toQueueResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"&\n\x13GetFromQueueRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\t\"{\n\x14GetFromQueueResponse\x12\x0f\n\x07orderId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\t\x12\x16\n\x0e\x65xpirationDate\x18\x04 \x01(\t\x12\x0b\n\x03\x63vv\x18\x05 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x06 \x01(\t2\x9e\x01\n\x0cQueueService\x12\x41\n\nAddtoQueue\x12\x18.queue.AddtoQueueRequest\x1a\x19.queue.AddtoQueueResponse\x12K\n\x10RequestFromQueue\x12\x1a.queue.GetFromQueueRequest\x1a\x1b.queue.GetFromQueueResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'queue_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADDTOQUEUEREQUEST']._serialized_start=22
  _globals['_ADDTOQUEUEREQUEST']._serialized_end=142
  _globals['_ADDTOQUEUERESPONSE']._serialized_start=144
  _globals['_ADDTOQUEUERESPONSE']._serialized_end=182
  _globals['_GETFROMQUEUEREQUEST']._serialized_start=184
  _globals['_GETFROMQUEUEREQUEST']._serialized_end=222
  _globals['_GETFROMQUEUERESPONSE']._serialized_start=224
  _globals['_GETFROMQUEUERESPONSE']._serialized_end=347
  _globals['_QUEUESERVICE']._serialized_start=350
  _globals['_QUEUESERVICE']._serialized_end=508
# @@protoc_insertion_point(module_scope)