"""
This module contains functions that can read and write Python values in
a binary format. The format is specific to Python, but independent of
machine architecture issues.

Not all Python object types are supported; in general, only objects
whose value is independent from a particular invocation of Python can be
written and read by this module. The following types are supported:
None, integers, floating-point numbers, strings, bytes, bytearrays,
tuples, lists, sets, dictionaries, and code objects, where it
should be understood that tuples, lists and dictionaries are only
supported as long as the values contained therein are themselves
supported; and recursive lists and dictionaries should not be written
(they will cause infinite loops).

Variables:

version -- indicates the format that the module uses. Version 0 is the
    historical format, version 1 shares interned strings and version 2
    uses a binary format for floating-point numbers.
    Version 3 shares common object references (New in version 3.4).

Functions:

dump() -- write value to a file
load() -- read value from a file
dumps() -- marshal value as a bytes object
loads() -- read value from a bytes-like object
"""

import builtins
import sys
import types
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from typing import Any, Final
from typing_extensions import TypeAlias

version: Final[int]

_Marshallable: TypeAlias = (
    # handled in w_object() in marshal.c
    None
    | type[StopIteration]
    | builtins.ellipsis
    | bool
    # handled in w_complex_object() in marshal.c
    | int
    | float
    | complex
    | bytes
    | str
    | tuple[_Marshallable, ...]
    | list[Any]
    | dict[Any, Any]
    | set[Any]
    | frozenset[_Marshallable]
    | types.CodeType
    | ReadableBuffer
)

if sys.version_info >= (3, 14):
    def dump(value: _Marshallable, file: SupportsWrite[bytes], version: int = 5, /, *, allow_code: bool = True) -> None: ...
    def dumps(value: _Marshallable, version: int = 5, /, *, allow_code: bool = True) -> bytes: ...

elif sys.version_info >= (3, 13):
    def dump(value: _Marshallable, file: SupportsWrite[bytes], version: int = 4, /, *, allow_code: bool = True) -> None: ...
    def dumps(value: _Marshallable, version: int = 4, /, *, allow_code: bool = True) -> bytes: ...

else:
    def dump(value: _Marshallable, file: SupportsWrite[bytes], version: int = 4, /) -> None: ...
    def dumps(value: _Marshallable, version: int = 4, /) -> bytes: ...

if sys.version_info >= (3, 13):
    def load(file: SupportsRead[bytes], /, *, allow_code: bool = True) -> Any: ...
    def loads(bytes: ReadableBuffer, /, *, allow_code: bool = True) -> Any: ...

else:
    def load(file: SupportsRead[bytes], /) -> Any: ...
    def loads(bytes: ReadableBuffer, /) -> Any: ...
