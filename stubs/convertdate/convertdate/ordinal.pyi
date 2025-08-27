"""
The `ordinal date <https://en.wikipedia.org/wiki/Ordinal_date>` specifies the day
of year as a number between 1 and 366.

Ordinal dates are represented by a tuple: ``(year, dayofyear)``
"""

def to_jd(year: int, dayofyear: int) -> float:
    """Return Julian day count of given ordinal date."""
    ...
def from_jd(jd: float) -> tuple[int, int]:
    """Convert a Julian day count to an ordinal date."""
    ...
def from_gregorian(year: int, month: int, day: int) -> tuple[int, int]:
    """Convert a Gregorian date to an ordinal date."""
    ...
def to_gregorian(year: int, dayofyear: int) -> tuple[int, int, int]:
    """Convert an ordinal date to a Gregorian date."""
    ...
