# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpayment.proto\x12\x07payment\"\x1e\n\x0bVoteRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\" \n\x0cVoteResponse\x12\x10\n\x08response\x18\x01 \x01(\t2E\n\x0ePaymentService\x12\x33\n\x04Vote\x12\x14.payment.VoteRequest\x1a\x15.payment.VoteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VOTEREQUEST']._serialized_start=26
  _globals['_VOTEREQUEST']._serialized_end=56
  _globals['_VOTERESPONSE']._serialized_start=58
  _globals['_VOTERESPONSE']._serialized_end=90
  _globals['_PAYMENTSERVICE']._serialized_start=92
  _globals['_PAYMENTSERVICE']._serialized_end=161
# @@protoc_insertion_point(module_scope)
