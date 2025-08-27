"""
The Julian calendar was implemented by Julius Caesar in 45 BC as a reformation of
the Roman calendar. It is designed to follow the solar year, with a standard year
of 365 days and a quadrennial leap year with an intercalary day (29 February).

For the first several centuries of its use, the Julian calendar did not have a
single year-numbering system. The Romans initially specific years with the names of political
leaders. Later on, different areas employed different era with various epochs.
Between the sixth and eighth centuries, western Europe adopted the Anno Domini convention.

This numbering system does not include a year 0. However, for dates before 1,
this module uses the astronomical convention of including a year 0 to simplify
mathematical comparisons across epochs. To present a date in the standard
convention, use the :meth:`julian.format` function.
"""

from typing import Final, Literal

J0000: Final = 1721424.5
J1970: Final = 2440587.5
JMJD: Final = 2400000.5
JULIAN_EPOCH: Final = 1721423.5
J2000: Final = 2451545.0
JULIANCENTURY: Final = 36525.0
HAVE_30_DAYS: Final = (4, 6, 9, 11)
HAVE_31_DAYS: Final = (1, 3, 5, 7, 8, 10, 12)

def leap(year: int) -> bool: ...
def month_length(year: int, month: int) -> Literal[28, 29, 30, 31]: ...
def legal_date(year: int, month: int, day: int) -> Literal[True]:
    """Check if this is a legal date in the Julian calendar"""
    ...
def from_jd(jd: float) -> tuple[int, int, int]:
    """Calculate Julian calendar date from Julian day"""
    ...
def to_jd(year: int, month: int, day: int) -> float:
    """Convert to Julian day using astronomical years (0 = 1 BC, -1 = 2 BC)"""
    ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]:
    """Convert a Gregorian date to a Julian date."""
    ...
def to_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]:
    """Convert a Julian date to a Gregorian date."""
    ...
def monthcalendar(year: int, month: int) -> list[list[int | None]]:
    """
    Returns a matrix representing a month’s calendar. Each row represents a week;
    days outside of the month are represented by zeros. Each week begins with Sunday.
    """
    ...
def format(year: int, month: int, day: int, format_string: str = "%-d %B %y") -> str: ...
