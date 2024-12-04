"""Convert to and from Roman numerals"""

import re

class RomanError(Exception): ...
class OutOfRangeError(RomanError): ...
class NotIntegerError(RomanError): ...
class InvalidRomanNumeralError(RomanError): ...

romanNumeralMap: tuple[tuple[str, int], ...]

def toRoman(n: int) -> str:
    """convert integer to Roman numeral"""
    ...

romanNumeralPattern: re.Pattern[str]

def fromRoman(s: str) -> int:
    """convert Roman numeral to integer"""
    ...
