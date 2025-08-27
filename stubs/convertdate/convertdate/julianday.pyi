"""
The `Julian day <https://en.wikipedia.org/wiki/Julian_day>`__
is a continuous count of days since the beginning of the Julian era on January 1, 4713 BC.
"""

import datetime

def to_datetime(jdc: float) -> datetime.datetime:
    """Return a datetime for the input floating point julian day count"""
    ...
def from_datetime(dt: datetime.datetime) -> float:
    """Convert from ``datetime`` to julian day count."""
    ...
def to_gregorian(jdc: float) -> tuple[int, int, int]:
    """Convert from julian day count to Gregorian date."""
    ...
def from_gregorian(year: int, month: int, day: int) -> float:
    """Convert from Gregorian ``year``, ``month`` and ``day`` to julian day count."""
    ...
def to_julian(jdc: float) -> tuple[int, int, int]:
    """Convert from julian day count to Julian date."""
    ...
def from_julian(year: int, month: int, day: int) -> float:
    """Convert from Julian ``year``, ``month`` and ``day`` to julian day count."""
    ...
