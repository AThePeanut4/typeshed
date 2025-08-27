from typing import Final, Literal

EPOCH: Final = 347995.5
HEBREW_YEAR_OFFSET: Final = 3760
NISAN: Final = 1
IYYAR: Final = 2
SIVAN: Final = 3
TAMMUZ: Final = 4
AV: Final = 5
ELUL: Final = 6
TISHRI: Final = 7
HESHVAN: Final = 8
KISLEV: Final = 9
TEVETH: Final = 10
SHEVAT: Final = 11
ADAR: Final = 12
VEADAR: Final = 13
MONTHS: Final[list[str]]
MONTHS_HEB: Final[list[str]]

def leap(year: int) -> bool: ...
def year_months(year: int) -> Literal[12, 13]:
    """How many months are there in a Hebrew year (12 = normal, 13 = leap)"""
    ...
def delay_1(year: int) -> int:
    """
    Test for delay of start of the ecclesiastical new year to
    avoid improper weekdays for holidays.
    """
    ...
def delay_2(year: int) -> Literal[0, 1, 2]:
    """
    Check for delay in start of the ecclesiastical new year due to length
    of adjacent years
    """
    ...
def year_days(year: int) -> float:
    """How many days are in a Hebrew year ?"""
    ...
def month_days(year: int, month: int) -> Literal[29, 30]:
    """How many days are in a given month of a given year"""
    ...
def to_jd(year: int, month: int, day: int) -> float: ...
def from_jd(jd: float) -> tuple[int, int, int]: ...
def to_civil(year: int, month: int, day: int) -> tuple[int, int, int]:
    """
    Convert a date in the ecclestical calendar (year starts in Nisan) to
    the civil calendar (year starts in Tishrei).
    """
    ...
def to_jd_gregorianyear(gregorianyear: int, hebrew_month: int, hebrew_day: int) -> float:
    """Returns the Gregorian date when a given Hebrew month and year within a given Gregorian year."""
    ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def to_gregorian(year: int, month: int, day: int) -> tuple[int, int, int]: ...
def monthcalendar(year: int, month: int) -> list[list[int | None]]: ...
def format(year: int, month: int, day: int, lang: str | None = None) -> str:
    """Convert a Hebrew date into a string with the format DD MONTH YYYY."""
    ...
