"""IEEE 64-bit EUI (Extended Unique Identifier) logic."""

from collections.abc import Iterable, Sequence
from re import Pattern
from typing import ClassVar, Literal

width: Literal[64]
version: Literal[64]
max_int: int

class eui64_base:
    """A standard IEEE EUI-64 dialect class."""
    word_size: ClassVar[int]
    num_words: ClassVar[int]
    max_word: ClassVar[int]
    word_sep: ClassVar[str]
    word_fmt: ClassVar[str]
    word_base: ClassVar[int]

class eui64_unix(eui64_base):
    """A UNIX-style MAC address dialect class."""
    ...
class eui64_unix_expanded(eui64_unix):
    """A UNIX-style MAC address dialect class with leading zeroes."""
    ...
class eui64_cisco(eui64_base):
    """A Cisco 'triple hextet' MAC address dialect class."""
    ...
class eui64_bare(eui64_base):
    """A bare (no delimiters) MAC address dialect class."""
    ...

DEFAULT_EUI64_DIALECT: type[eui64_base]
RE_EUI64_FORMATS: list[Pattern[str]]

def valid_str(addr: str) -> bool:
    """
    :param addr: An IEEE EUI-64 identifier in string form.

    :return: ``True`` if EUI-64 identifier is valid, ``False`` otherwise.
    """
    ...
def str_to_int(addr: str) -> int:
    """
    :param addr: An IEEE EUI-64 identifier in string form.

    :return: An unsigned integer that is equivalent to value represented
        by EUI-64 string address formatted according to the dialect
    """
    ...
def int_to_str(int_val: int, dialect: type[eui64_base] | None = None) -> str:
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options

    :return: An IEEE EUI-64 identifier that is equivalent to unsigned integer.
    """
    ...
def int_to_packed(int_val: int) -> bytes:
    """
    :param int_val: the integer to be packed.

    :return: a packed string that is equivalent to value represented by an
    unsigned integer.
    """
    ...
def packed_to_int(packed_int: bytes) -> int:
    """
    :param packed_int: a packed string containing an unsigned integer.
        It is assumed that string is packed in network byte order.

    :return: An unsigned integer equivalent to value of network address
        represented by packed binary string.
    """
    ...
def valid_words(words: Iterable[int], dialect: type[eui64_base] | None = None) -> bool: ...
def int_to_words(int_val: int, dialect: type[eui64_base] | None = None) -> tuple[int, ...]: ...
def words_to_int(words: Sequence[int], dialect: type[eui64_base] | None = None) -> int: ...
def valid_bits(bits: str, dialect: type[eui64_base] | None = None) -> bool: ...
def bits_to_int(bits: str, dialect: type[eui64_base] | None = None) -> int: ...
def int_to_bits(int_val: int, dialect: type[eui64_base] | None = None) -> str: ...
def valid_bin(bin_val: str, dialect: type[eui64_base] | None = None) -> bool: ...
def int_to_bin(int_val: int) -> str: ...
def bin_to_int(bin_val: str) -> int: ...
