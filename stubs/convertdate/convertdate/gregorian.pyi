"""
The Gregorian calendar was introduced by Pope Gregory XII in October 1582. It reforms
the Julian calendar by adjusting leap year rules to reduce the drift versus solar
year.

The Gregorian calendar, like the Julian, does not include a year 0. However, for dates before 1,
this module uses the astronomical convention of including a year 0 to simplify
mathematical comparisons across epochs. To present a date in the standard convention,
use the :meth:`gregorian.format` function.
"""

from typing import Final, Literal

EPOCH: Final = 1721425.5
INTERCALATION_CYCLE_YEARS: Final = 400
INTERCALATION_CYCLE_DAYS: Final = 146097
LEAP_SUPPRESSION_YEARS: Final = 100
LEAP_SUPPRESSION_DAYS: Final = 36524
LEAP_CYCLE_YEARS: Final = 4
LEAP_CYCLE_DAYS: Final = 1461
YEAR_DAYS: Final = 365
HAVE_30_DAYS: Final = (4, 6, 9, 11)
HAVE_31_DAYS: Final = (1, 3, 5, 7, 8, 10, 12)

def legal_date(year: int, month: int, day: int) -> Literal[True]:
    """Check if this is a legal date in the Gregorian calendar"""
    ...
def to_jd2(year: int, month: int, day: int) -> float:
    """Gregorian to Julian Day Count for years between 1801-2099"""
    ...
def to_jd(year: int, month: int, day: int) -> float:
    """Convert gregorian date to julian day count."""
    ...
def from_jd(jd: float) -> tuple[int, int, int]:
    """Return Gregorian date in a (Y, M, D) tuple"""
    ...
def month_length(year: int, month: int) -> int:
    """Calculate the length of a month in the Gregorian calendar"""
    ...
def monthcalendar(year: int, month: int) -> list[list[int | None]]:
    """
    Return a list of lists that describe the calender for one month. Each inner
    list have 7 items, one for each weekday, starting with Sunday. These items
    are either ``None`` or an integer, counting from 1 to the number of days in
    the month.
    For Gregorian, this is very similiar to the built-in :meth:``calendar.monthcalendar``.
    """
    ...
def format(year: int, month: int, day: int, format_string: str = "%-d %B %y") -> str: ...
