"""
The Indian Civil calendar, also called the Indian national calendar, or the Shalivahana Shaka calendar,
was instituted following independence. It consists of twelve months of 31 or 30 days, with a
leap day every four years.
"""

from typing import Final, Literal

WEEKDAYS: Final = ("Ravivāra", "Somavāra", "Maṅgalavāra", "Budhavāra", "Guruvāra", "Śukravāra", "Śanivāra")
MONTHS: Final[tuple[str, ...]]
HAVE_31_DAYS: Final = (2, 3, 4, 5, 6)
HAVE_30_DAYS: Final = (7, 8, 9, 10, 11, 12)
SAKA_EPOCH: Final = 78

def to_jd(year: int, month: int, day: int) -> float:
    """Obtain Julian day for Indian Civil date"""
    ...
def from_jd(jd: float) -> tuple[int, int, int]:
    """
    Calculate Indian Civil date from Julian day
    Offset in years from Saka era to Gregorian epoch
    """
    ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def to_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def month_length(year: int, month: int) -> Literal[30, 31]: ...
def monthcalendar(year: int, month: int) -> list[list[int | None]]: ...
def format(year: int, month: int, day: int) -> str:
    """Convert a Indian Civil date into a string with the format DD MONTH YYYY."""
    ...
