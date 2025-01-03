"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol Buffers - Google's data interchange format
Copyright 2008 Google Inc.  All rights reserved.
https://developers.google.com/protocol-buffers/

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution.
    * Neither the name of Google Inc. nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Wrappers for primitive (non-message) types. These types are useful
for embedding primitives in the `google.protobuf.Any` type and for places
where we need to distinguish between the absence of a primitive
typed field and its default value.

These wrappers have no meaningful use within repeated fields as they lack
the ability to detect presence on individual elements.
These wrappers have no meaningful use within a map or a oneof since
individual entries of a map or fields of a oneof can already detect presence.
"""

import builtins
import typing

import google.protobuf.descriptor
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DoubleValue(google.protobuf.message.Message):
    """Wrapper message for `double`.

    The JSON representation for `DoubleValue` is JSON number.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.float
    """The double value."""
    def __init__(
        self,
        *,
        value: builtins.float | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___DoubleValue = DoubleValue

@typing.final
class FloatValue(google.protobuf.message.Message):
    """Wrapper message for `float`.

    The JSON representation for `FloatValue` is JSON number.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.float
    """The float value."""
    def __init__(
        self,
        *,
        value: builtins.float | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___FloatValue = FloatValue

@typing.final
class Int64Value(google.protobuf.message.Message):
    """Wrapper message for `int64`.

    The JSON representation for `Int64Value` is JSON string.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    """The int64 value."""
    def __init__(
        self,
        *,
        value: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___Int64Value = Int64Value

@typing.final
class UInt64Value(google.protobuf.message.Message):
    """Wrapper message for `uint64`.

    The JSON representation for `UInt64Value` is JSON string.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    """The uint64 value."""
    def __init__(
        self,
        *,
        value: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___UInt64Value = UInt64Value

@typing.final
class Int32Value(google.protobuf.message.Message):
    """Wrapper message for `int32`.

    The JSON representation for `Int32Value` is JSON number.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    """The int32 value."""
    def __init__(
        self,
        *,
        value: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___Int32Value = Int32Value

@typing.final
class UInt32Value(google.protobuf.message.Message):
    """Wrapper message for `uint32`.

    The JSON representation for `UInt32Value` is JSON number.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    """The uint32 value."""
    def __init__(
        self,
        *,
        value: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___UInt32Value = UInt32Value

@typing.final
class BoolValue(google.protobuf.message.Message):
    """Wrapper message for `bool`.

    The JSON representation for `BoolValue` is JSON `true` and `false`.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.bool
    """The bool value."""
    def __init__(
        self,
        *,
        value: builtins.bool | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___BoolValue = BoolValue

@typing.final
class StringValue(google.protobuf.message.Message):
    """Wrapper message for `string`.

    The JSON representation for `StringValue` is JSON string.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.str
    """The string value."""
    def __init__(
        self,
        *,
        value: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___StringValue = StringValue

@typing.final
class BytesValue(google.protobuf.message.Message):
    """Wrapper message for `bytes`.

    The JSON representation for `BytesValue` is JSON string.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.bytes
    """The bytes value."""
    def __init__(
        self,
        *,
        value: builtins.bytes | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___BytesValue = BytesValue
