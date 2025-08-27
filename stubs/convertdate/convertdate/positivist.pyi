"""
Convert between Gregorian/Julian Day and Comte's Positivist calendar.
The Positivist calendar has 13 months and one or two festival days.
Festival days are given as the fourteenth month.
The Gregorian date 1789-01-01 is Positivist 0001-01-01.
"""

from typing import Final, Literal

EPOCH: Final = 2374479.5
YEAR_EPOCH: Final = 1789
DAYS_IN_YEAR: Final = 365
MONTHS: Final[tuple[str, ...]]

def legal_date(year: int, month: int, day: int) -> Literal[True]:
    """Checks if a given date is a legal positivist date"""
    ...
def to_jd(year: int, month: int, day: int) -> float:
    """Convert a Positivist date to Julian day count."""
    ...
def from_jd(jd: float) -> tuple[int, int, int]:
    """Convert a Julian day count to Positivist date."""
    ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def to_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def dayname(year: int, month: int, day: int) -> tuple[str, str]:
    """
    Give the name of the month and day for a given date.

    Returns:
        tuple month_name, day_name
    """
    ...
def weekday(day: int) -> int:
    """
    Gives the weekday (0=Monday) of a positivist month and day.
    Note that the festival month does not have a day.
    """
    ...
def festival(month: int, day: int) -> str | None:
    """
    Gives the festival day for a month and day.
    Returns None if inapplicable.
    """
    ...
