# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61udio.proto\"%\n\x13\x44ownloadFileRequest\x12\x0e\n\x06nombre\x18\x01 \x01(\t\"@\n\x11\x44\x61taChunkResponse\x12\x0e\n\x04\x64\x61ta\x18\x01 \x01(\x0cH\x00\x12\x10\n\x06nombre\x18\x02 \x01(\tH\x00\x42\t\n\x07request2\x86\x01\n\x0c\x41udioService\x12;\n\rdownloadAudio\x12\x14.DownloadFileRequest\x1a\x12.DataChunkResponse0\x01\x12\x39\n\x0buploadAudio\x12\x12.DataChunkResponse\x1a\x14.DownloadFileRequest(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=15
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=52
  _globals['_DATACHUNKRESPONSE']._serialized_start=54
  _globals['_DATACHUNKRESPONSE']._serialized_end=118
  _globals['_AUDIOSERVICE']._serialized_start=121
  _globals['_AUDIOSERVICE']._serialized_end=255
# @@protoc_insertion_point(module_scope)
