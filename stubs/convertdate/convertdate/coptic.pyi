"""
The `Coptic calendar <https://en.wikipedia.org/wiki/Coptic_calendar>`__,
also called the Alexandrian calendar, is a liturgical calendar used by the
Coptic Orthodox Church and some communities in Egypt. It is a reformed version
of the ancient Egyptian calendar.

It consists of twelve months of 30 days, followed by a "little month" of five days
(six in leap years).
"""

from typing import Final, Literal

EPOCH: Final = 1825029.5
MONTHS: Final[list[str]]
WEEKDAYS: Final = ["Tkyriaka", "Pesnau", "Pshoment", "Peftoou", "Ptiou", "Psoou", "Psabbaton"]

def is_leap(year: int) -> bool:
    """Determine whether this is a leap year."""
    ...
def to_jd(year: int, month: int, day: int) -> float:
    """Retrieve the Julian date equivalent for this date"""
    ...
def from_jd(jdc: float) -> tuple[int, int, int]:
    """Create a new date from a Julian date."""
    ...
def to_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def month_length(year: int, month: int) -> Literal[5, 6, 30]: ...
def monthcalendar(year: int, month: int) -> list[list[int | None]]: ...
def format(year: int, month: int, day: int) -> str:
    """Convert a Coptic date into a string with the format DD MONTH YYYY."""
    ...
