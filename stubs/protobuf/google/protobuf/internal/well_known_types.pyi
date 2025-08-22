"""
Contains well known classes.

This files defines well known classes which need extra maintenance including:
  - Any
  - Duration
  - FieldMask
  - Struct
  - Timestamp
"""

from _typeshed import Incomplete, SupportsItems
from collections.abc import Iterable, Iterator, KeysView, Mapping, Sequence
from datetime import datetime, timedelta, tzinfo
from typing import Any as tAny
from typing_extensions import TypeAlias

from google.protobuf import struct_pb2

class Any:
    __slots__ = ()
    type_url: str
    value: Incomplete
    def Pack(self, msg, type_url_prefix: str = "type.googleapis.com/", deterministic=None) -> None:
        """Packs the specified message into current Any message."""
        ...
    def Unpack(self, msg) -> bool:
        """Unpacks the current Any message into specified message."""
        ...
    def TypeName(self) -> str:
        """Returns the protobuf type name of the inner message."""
        ...
    def Is(self, descriptor) -> bool:
        """Checks if this Any represents the given protobuf type."""
        ...

class Timestamp:
    __slots__ = ()
    def ToJsonString(self) -> str: ...
    seconds: int
    nanos: int
    def FromJsonString(self, value: str) -> None:
        """
        Parse a RFC 3339 date string format to Timestamp.

        Args:
          value: A date string. Any fractional digits (or none) and any offset are
              accepted as long as they fit into nano-seconds precision.
              Example of accepted format: '1972-01-01T10:00:20.021-05:00'

        Raises:
          ValueError: On parsing problems.
        """
        ...
    def GetCurrentTime(self) -> None:
        """Get the current UTC into Timestamp."""
        ...
    def ToNanoseconds(self) -> int:
        """Converts Timestamp to nanoseconds since epoch."""
        ...
    def ToMicroseconds(self) -> int:
        """Converts Timestamp to microseconds since epoch."""
        ...
    def ToMilliseconds(self) -> int:
        """Converts Timestamp to milliseconds since epoch."""
        ...
    def ToSeconds(self) -> int:
        """Converts Timestamp to seconds since epoch."""
        ...
    def FromNanoseconds(self, nanos: int) -> None:
        """Converts nanoseconds since epoch to Timestamp."""
        ...
    def FromMicroseconds(self, micros: int) -> None:
        """Converts microseconds since epoch to Timestamp."""
        ...
    def FromMilliseconds(self, millis: int) -> None:
        """Converts milliseconds since epoch to Timestamp."""
        ...
    def FromSeconds(self, seconds: int) -> None:
        """Converts seconds since epoch to Timestamp."""
        ...
    def ToDatetime(self, tzinfo: tzinfo | None = None) -> datetime:
        """
        Converts Timestamp to a datetime.

        Args:
          tzinfo: A datetime.tzinfo subclass; defaults to None.

        Returns:
          If tzinfo is None, returns a timezone-naive UTC datetime (with no timezone
          information, i.e. not aware that it's UTC).

          Otherwise, returns a timezone-aware datetime in the input timezone.
        """
        ...
    def FromDatetime(self, dt: datetime) -> None:
        """
        Converts datetime to Timestamp.

        Args:
          dt: A datetime. If it's timezone-naive, it's assumed to be in UTC.
        """
        ...

class Duration:
    __slots__ = ()
    def ToJsonString(self) -> str: ...
    seconds: int
    nanos: int
    def FromJsonString(self, value: tAny) -> None:
        """
        Converts a string to Duration.

        Args:
          value: A string to be converted. The string must end with 's'. Any
              fractional digits (or none) are accepted as long as they fit into
              precision. For example: "1s", "1.01s", "1.0000001s", "-3.100s

        Raises:
          ValueError: On parsing problems.
        """
        ...
    def ToNanoseconds(self) -> int:
        """Converts a Duration to nanoseconds."""
        ...
    def ToMicroseconds(self) -> int:
        """Converts a Duration to microseconds."""
        ...
    def ToMilliseconds(self) -> int:
        """Converts a Duration to milliseconds."""
        ...
    def ToSeconds(self) -> int:
        """Converts a Duration to seconds."""
        ...
    def FromNanoseconds(self, nanos: int) -> None:
        """Converts nanoseconds to Duration."""
        ...
    def FromMicroseconds(self, micros: int) -> None:
        """Converts microseconds to Duration."""
        ...
    def FromMilliseconds(self, millis: int) -> None:
        """Converts milliseconds to Duration."""
        ...
    def FromSeconds(self, seconds: int) -> None:
        """Converts seconds to Duration."""
        ...
    def ToTimedelta(self) -> timedelta:
        """Converts Duration to timedelta."""
        ...
    def FromTimedelta(self, td: timedelta) -> None:
        """Converts timedelta to Duration."""
        ...

class FieldMask:
    __slots__ = ()
    def ToJsonString(self) -> str: ...
    def FromJsonString(self, value: tAny) -> None: ...
    def IsValidForDescriptor(self, message_descriptor: tAny): ...
    def AllFieldsFromDescriptor(self, message_descriptor: tAny) -> None: ...
    def CanonicalFormFromMask(self, mask: tAny) -> None: ...
    def Union(self, mask1: tAny, mask2: tAny) -> None: ...
    def Intersect(self, mask1: tAny, mask2: tAny) -> None: ...
    def MergeMessage(
        self, source: tAny, destination: tAny, replace_message_field: bool = False, replace_repeated_field: bool = False
    ) -> None:
        """
        Merges fields specified in FieldMask from source to destination.

        Args:
          source: Source message.
          destination: The destination message to be merged into.
          replace_message_field: Replace message field if True. Merge message
              field if False.
          replace_repeated_field: Replace repeated field if True. Append
              elements of repeated field if False.
        """
        ...

_StructValue: TypeAlias = struct_pb2.Struct | struct_pb2.ListValue | str | float | bool | None
_StructValueArg: TypeAlias = _StructValue | Mapping[str, _StructValueArg] | Sequence[_StructValueArg]

class Struct:
    __slots__: tuple[()] = ()
    def __getitem__(self, key: str) -> _StructValue: ...
    def __setitem__(self, key: str, value: _StructValueArg) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def keys(self) -> KeysView[str]: ...
    def values(self) -> list[_StructValue]: ...
    def items(self) -> list[tuple[str, _StructValue]]: ...
    def get_or_create_list(self, key: str) -> struct_pb2.ListValue:
        """Returns a list for this key, creating if it didn't exist already."""
        ...
    def get_or_create_struct(self, key: str) -> struct_pb2.Struct:
        """Returns a struct for this key, creating if it didn't exist already."""
        ...
    def update(self, dictionary: SupportsItems[str, _StructValueArg]) -> None: ...

class ListValue:
    __slots__: tuple[()] = ()
    def __len__(self) -> int: ...
    def append(self, value: _StructValue) -> None: ...
    def extend(self, elem_seq: Iterable[_StructValue]) -> None: ...
    def __getitem__(self, index: int) -> _StructValue:
        """Retrieves item by the specified index."""
        ...
    def __setitem__(self, index: int, value: _StructValueArg) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    # Doesn't actually exist at runtime; needed so type checkers understand the class is iterable
    def __iter__(self) -> Iterator[_StructValue]: ...
    def items(self) -> Iterator[_StructValue]: ...
    def add_struct(self) -> struct_pb2.Struct:
        """Appends and returns a struct value as the next value in the list."""
        ...
    def add_list(self) -> struct_pb2.ListValue:
        """Appends and returns a list value as the next value in the list."""
        ...

WKTBASES: dict[str, type[tAny]]
