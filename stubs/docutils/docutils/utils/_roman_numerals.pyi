"""Conversion between integers and roman numerals."""

from typing import Final, final
from typing_extensions import Self

__all__ = ("MAX", "MIN", "InvalidRomanNumeralError", "OutOfRangeError", "RomanNumeral")

MIN: Final = 1
MAX: Final = 4_999

@final
class OutOfRangeError(TypeError):
    """Number out of range (must be between 1 and 4,999)."""
    ...

@final
class InvalidRomanNumeralError(ValueError):
    """Not a valid Roman numeral."""
    def __init__(self, value: str, *args: object) -> None: ...

@final
class RomanNumeral:
    """
    A Roman numeral.

    Only values between 1 and 4,999 are valid.
    Stores the value internally as an ``int``.

    >>> answer = RomanNumeral(42)
    >>> print(answer.to_uppercase())
    XLII
    """
    def __init__(self, value: int, /) -> None: ...
    def __int__(self) -> int:
        """Return the integer value of this numeral."""
        ...
    def __eq__(self, other: object) -> bool:
        """Return self == other."""
        ...
    def __lt__(self, other: object) -> bool:
        """Return self < other."""
        ...
    def __hash__(self) -> int:
        """Return the hashed value of this numeral."""
        ...
    def __setattr__(self, key: str, value: object) -> None:
        """Implement setattr(self, name, value)."""
        ...
    def to_uppercase(self) -> str:
        """
        Convert a ``RomanNumeral`` to an uppercase string.

        >>> answer = RomanNumeral(42)
        >>> assert answer.to_uppercase() == 'XLII'
        """
        ...
    def to_lowercase(self) -> str:
        """
        Convert a ``RomanNumeral`` to a lowercase string.

        >>> answer = RomanNumeral(42)
        >>> assert answer.to_lowercase() == 'xlii'
        """
        ...
    @classmethod
    def from_string(cls, string: str, /) -> Self:
        """
        Create a ``RomanNumeral`` from a well-formed string representation.

        Returns ``RomanNumeral`` or raises ``InvalidRomanNumeralError``.

        >>> answer = RomanNumeral.from_string('XLII')
        >>> assert int(answer) == 42
        """
        ...

_ROMAN_NUMERAL_PREFIXES: Final[list[tuple[int, str, str]]]
