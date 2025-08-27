"""
The Armenian calendar begins on 11 July 552 (Julian) and has two modes of
reckoning. The first is the invariant-length version consisting of 12 months
of 30 days each and five epagomenal days; the second is the version
established by Yovhannes Sarkawag in 1084, which fixed the first day of the
year with respect to the Julian calendar and added a sixth epagomenal day
every four years.

By default the invariant calendar is used, but the Sarkawag calendar can be
used beginning with the Armenian year 533 (11 August 1084) by passing the
parameter ``method='sarkawag'`` to the relevant functions.
"""

from typing import Final, Literal

EPOCH: Final = 1922501.5
EPOCH_SARKAWAG: Final = 2117210.5
MONTHS: Final[list[str]]
MONTHS_ARM: Final[list[str]]

def leap(year: int) -> bool:
    """Return true if the year was a leap year under the system of Sarkawag"""
    ...
def to_jd(year: int, month: int, day: int, method: Literal["sarkawag", "moveable"] | None = None) -> float:
    """Convert Armenian date to Julian day count. Use the method of Sarkawag if requested."""
    ...
def from_jd(jd: float, method: Literal["sarkawag", "moveable"] | None = None) -> tuple[int, int, int]:
    """Convert a Julian day count to an Armenian date. Use the method of Sarkawag if requested."""
    ...
def to_julian(year: int, month: int, day: int, method: Literal["sarkawag", "moveable"] | None = None) -> tuple[int, int, int]:
    """Convert an Armenian date to a Julian date"""
    ...
def from_julian(
    year: int, month: int, day: int, method: Literal["sarkawag", "moveable"] | None = None
) -> tuple[int, int, int]:
    """Convert a Julian date to an Armenian date"""
    ...
def to_gregorian(
    year: int, month: int, day: int, method: Literal["sarkawag", "moveable"] | None = None
) -> tuple[int, int, int]:
    """Convert an Armenian date to a Gregorian date"""
    ...
def from_gregorian(
    year: int, month: int, day: int, method: Literal["sarkawag", "moveable"] | None = None
) -> tuple[int, int, int]:
    """Convert a Gregorian date to an Armenian date"""
    ...
def month_length(year: int, month: int, method: Literal["sarkawag", "moveable"] | None = None) -> Literal[5, 6, 30]: ...
def monthcalendar(year: int, month: int, method: Literal["sarkawag", "moveable"] | None = None) -> list[list[int | None]]:
    """
    Returns a matrix representing a month’s calendar.
    Each row represents a week; days outside of the month are represented by zeros.
    """
    ...
def format(year: int, month: int, day: int, lang: str | None = None) -> str:
    """Convert an Armenian date into a string with the format DD MONTH YYYY."""
    ...
def tostring(year: int, month: int, day: int, lang: str | None = None) -> str:
    """Kept for backwards compatibility, the format function name will be standard across the library"""
    ...
