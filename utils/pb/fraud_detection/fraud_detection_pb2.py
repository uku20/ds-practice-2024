# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fraud_detection.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66raud_detection.proto\x12\x05hello\x1a\x1bgoogle/protobuf/empty.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t\"Z\n\x0c\x46raudRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x02 \x01(\t\x12\x0e\n\x06street\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\"!\n\rFraudResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"(\n\x10\x43learDataRequest\x12\x14\n\x0cvector_clock\x18\x01 \x03(\x05\x32\x45\n\x0cHelloService\x12\x35\n\x08SayHello\x12\x13.hello.HelloRequest\x1a\x14.hello.HelloResponse2J\n\x0e\x46raudDetection\x12\x38\n\x0b\x44\x65tectFraud\x12\x13.hello.FraudRequest\x1a\x14.hello.FraudResponse2M\n\x0bYourService\x12>\n\tClearData\x12\x17.hello.ClearDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fraud_detection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=61
  _globals['_HELLOREQUEST']._serialized_end=89
  _globals['_HELLORESPONSE']._serialized_start=91
  _globals['_HELLORESPONSE']._serialized_end=124
  _globals['_FRAUDREQUEST']._serialized_start=126
  _globals['_FRAUDREQUEST']._serialized_end=216
  _globals['_FRAUDRESPONSE']._serialized_start=218
  _globals['_FRAUDRESPONSE']._serialized_end=251
  _globals['_CLEARDATAREQUEST']._serialized_start=253
  _globals['_CLEARDATAREQUEST']._serialized_end=293
  _globals['_HELLOSERVICE']._serialized_start=295
  _globals['_HELLOSERVICE']._serialized_end=364
  _globals['_FRAUDDETECTION']._serialized_start=366
  _globals['_FRAUDDETECTION']._serialized_end=440
  _globals['_YOURSERVICE']._serialized_start=442
  _globals['_YOURSERVICE']._serialized_end=519
# @@protoc_insertion_point(module_scope)
