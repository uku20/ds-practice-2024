from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SuggestResponse(_message.Message):
    __slots__ = ("firstSuggestion", "secondSuggestion")
    FIRSTSUGGESTION_FIELD_NUMBER: _ClassVar[int]
    SECONDSUGGESTION_FIELD_NUMBER: _ClassVar[int]
    firstSuggestion: _containers.RepeatedScalarFieldContainer[str]
    secondSuggestion: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, firstSuggestion: _Optional[_Iterable[str]] = ..., secondSuggestion: _Optional[_Iterable[str]] = ...) -> None: ...

class ClearDataRequest(_message.Message):
    __slots__ = ("vector_clock",)
    VECTOR_CLOCK_FIELD_NUMBER: _ClassVar[int]
    vector_clock: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, vector_clock: _Optional[_Iterable[int]] = ...) -> None: ...
