from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddtoQueueRequest(_message.Message):
    __slots__ = ("orderId", "name", "number", "expirationDate", "cvv", "contact")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    name: str
    number: str
    expirationDate: str
    cvv: str
    contact: str
    def __init__(self, orderId: _Optional[str] = ..., name: _Optional[str] = ..., number: _Optional[str] = ..., expirationDate: _Optional[str] = ..., cvv: _Optional[str] = ..., contact: _Optional[str] = ...) -> None: ...

class AddtoQueueResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: bool
    def __init__(self, response: bool = ...) -> None: ...

class GetFromQueueRequest(_message.Message):
    __slots__ = ("orderId",)
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    def __init__(self, orderId: _Optional[str] = ...) -> None: ...

class GetFromQueueResponse(_message.Message):
    __slots__ = ("orderId", "name", "number", "expirationDate", "cvv", "contact")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    name: str
    number: str
    expirationDate: str
    cvv: str
    contact: str
    def __init__(self, orderId: _Optional[str] = ..., name: _Optional[str] = ..., number: _Optional[str] = ..., expirationDate: _Optional[str] = ..., cvv: _Optional[str] = ..., contact: _Optional[str] = ...) -> None: ...
