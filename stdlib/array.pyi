"""
This module defines an object type which can efficiently represent
an array of basic values: characters, integers, floating-point
numbers.  Arrays are sequence types and behave very much like lists,
except that the type of objects stored in them is constrained.
"""

import sys
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from collections.abc import Iterable, MutableSequence
from types import GenericAlias
from typing import Any, ClassVar, Literal, SupportsIndex, TypeVar, overload
from typing_extensions import Self, TypeAlias

_IntTypeCode: TypeAlias = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode: TypeAlias = Literal["f", "d"]
_UnicodeTypeCode: TypeAlias = Literal["u"]
_TypeCode: TypeAlias = _IntTypeCode | _FloatTypeCode | _UnicodeTypeCode

_T = TypeVar("_T", int, float, str)

typecodes: str

class array(MutableSequence[_T]):
    """
    array(typecode [, initializer]) -> array

    Return a new array whose items are restricted by typecode, and
    initialized from the optional initializer value, which must be a list,
    string or iterable over elements of the appropriate type.

    Arrays represent basic values and behave very much like lists, except
    the type of objects stored in them is constrained. The type is specified
    at object creation time by using a type code, which is a single character.
    The following type codes are defined:

        Type code   C Type             Minimum size in bytes
        'b'         signed integer     1
        'B'         unsigned integer   1
        'u'         Unicode character  2 (see note)
        'h'         signed integer     2
        'H'         unsigned integer   2
        'i'         signed integer     2
        'I'         unsigned integer   2
        'l'         signed integer     4
        'L'         unsigned integer   4
        'q'         signed integer     8 (see note)
        'Q'         unsigned integer   8 (see note)
        'f'         floating-point     4
        'd'         floating-point     8

    NOTE: The 'u' typecode corresponds to Python's unicode character. On
    narrow builds this is 2-bytes on wide builds this is 4-bytes.

    NOTE: The 'q' and 'Q' type codes are only available if the platform
    C compiler used to build Python supports 'long long', or, on Windows,
    '__int64'.

    Methods:

    append() -- append a new item to the end of the array
    buffer_info() -- return information giving the current memory info
    byteswap() -- byteswap all the items of the array
    count() -- return number of occurrences of an object
    extend() -- extend array by appending multiple elements from an iterable
    fromfile() -- read items from a file object
    fromlist() -- append items from the list
    frombytes() -- append items from the string
    index() -- return index of first occurrence of an object
    insert() -- insert a new item into the array at a provided position
    pop() -- remove and return item (default last)
    remove() -- remove first occurrence of an object
    reverse() -- reverse the order of the items in the array
    tofile() -- write all items to a file object
    tolist() -- return the array converted to an ordinary list
    tobytes() -- return the array converted to a string

    Attributes:

    typecode -- the typecode character used to create the array
    itemsize -- the length in bytes of one array item
    """
    @property
    def typecode(self) -> _TypeCode:
        """the typecode character used to create the array"""
        ...
    @property
    def itemsize(self) -> int:
        """the size, in bytes, of one array item"""
        ...
    @overload
    def __new__(
        cls: type[array[int]], typecode: _IntTypeCode, initializer: bytes | bytearray | Iterable[int] = ..., /
    ) -> array[int]: ...
    @overload
    def __new__(
        cls: type[array[float]], typecode: _FloatTypeCode, initializer: bytes | bytearray | Iterable[float] = ..., /
    ) -> array[float]: ...
    @overload
    def __new__(
        cls: type[array[str]], typecode: _UnicodeTypeCode, initializer: bytes | bytearray | Iterable[str] = ..., /
    ) -> array[str]: ...
    @overload
    def __new__(cls, typecode: str, initializer: Iterable[_T], /) -> Self: ...
    @overload
    def __new__(cls, typecode: str, initializer: bytes | bytearray = ..., /) -> Self: ...
    def append(self, v: _T, /) -> None:
        """Append new value v to the end of the array."""
        ...
    def buffer_info(self) -> tuple[int, int]:
        """
        Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.

    def insert(self, i: int, v: _T, /) -> None: ...
    def pop(self, i: int = -1, /) -> _T: ...
    def remove(self, v: _T, /) -> None: ...
    def tobytes(self) -> bytes: ...
    def tofile(self, f: SupportsWrite[bytes], /) -> None: ...
    def tolist(self) -> list[_T]: ...
    def tounicode(self) -> str: ...

    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __len__(self) -> int:
        """Return len(self)."""
        ...
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> _T:
        """Return self[key]."""
        ...
    @overload
    def __getitem__(self, key: slice, /) -> array[_T]:
        """Return self[key]."""
        ...
    @overload  # type: ignore[override]
    def __setitem__(self, key: SupportsIndex, value: _T, /) -> None:
        """Set self[key] to value."""
        ...
    @overload
    def __setitem__(self, key: slice, value: array[_T], /) -> None:
        """Set self[key] to value."""
        ...
    def __delitem__(self, key: SupportsIndex | slice, /) -> None:
        """Delete self[key]."""
        ...
    def __add__(self, value: array[_T], /) -> array[_T]:
        """Return self+value."""
        ...
    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def __ge__(self, value: array[_T], /) -> bool:
        """Return self>=value."""
        ...
    def __gt__(self, value: array[_T], /) -> bool:
        """Return self>value."""
        ...
    def __iadd__(self, value: array[_T], /) -> Self:
        """Implement self+=value."""
        ...
    def __imul__(self, value: int, /) -> Self:
        """Implement self*=value."""
        ...
    def __le__(self, value: array[_T], /) -> bool:
        """Return self<=value."""
        ...
    def __lt__(self, value: array[_T], /) -> bool:
        """Return self<value."""
        ...
    def __mul__(self, value: int, /) -> array[_T]:
        """Return self*value."""
        ...
    def __rmul__(self, value: int, /) -> array[_T]:
        """Return value*self."""
        ...
    def __copy__(self) -> array[_T]:
        """Return a copy of the array."""
        ...
    def __deepcopy__(self, unused: Any, /) -> array[_T]:
        """Return a copy of the array."""
        ...
    def __buffer__(self, flags: int, /) -> memoryview:
        """Return a buffer object that exposes the underlying memory of the object."""
        ...
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
        ...
    if sys.version_info >= (3, 12):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias:
            """See PEP 585"""
            ...

ArrayType = array
