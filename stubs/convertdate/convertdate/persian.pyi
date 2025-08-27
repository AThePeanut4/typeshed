"""
The modern Persian calendar, or the Solar Hijri calendar, was adopted in 1911.
It consists of twelve months of 30 or 31 days. The new year always falls on the
March equinox.
"""

from typing import Final, Literal

EPOCH: Final = 1948320.5
WEEKDAYS: Final[tuple[str, ...]]
MONTHS: Final[list[str]]
HAS_31_DAYS: Final = (1, 2, 3, 4, 5, 6)
HAS_30_DAYS: Final = (7, 8, 9, 10, 11)

def leap(year: int) -> bool:
    """Is a given year a leap year in the Persian calendar ?"""
    ...
def equinox_jd(gyear: int) -> int:
    """
    Calculate Julian day during which the March equinox, reckoned from the
    Tehran meridian, occurred for a given Gregorian year.
    """
    ...
def last_equinox_jd(jd: float) -> int:
    """
    Return the Julian date of spring equinox immediately preceeding the
    given Julian date.
    """
    ...
def jd_to_pyear(jd: float) -> tuple[int, int]:
    """
    Determine the year in the Persian astronomical calendar in which a given
    Julian day falls.

    Returns:
        tuple - (Persian year, Julian day number containing equinox for this year)
    """
    ...
def to_jd(year: int, month: int, day: int) -> float:
    """Determine Julian day from Persian date"""
    ...
def from_jd(jd: float) -> tuple[int, int, int]:
    """Calculate Persian date from Julian day"""
    ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def to_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def month_length(year: int, month: int) -> Literal[29, 30, 31]: ...
def monthcalendar(year: int, month: int) -> list[list[int | None]]: ...
def format(year: int, month: int, day: int) -> str:
    """Convert a Persian date into a string with the format DD MONTH YYYY."""
    ...
