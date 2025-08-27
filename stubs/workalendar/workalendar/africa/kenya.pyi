from collections.abc import Generator, Iterable
from typing import ClassVar

from ..core import _D, IslamoWesternCalendar

class Kenya(IslamoWesternCalendar):
    """Kenya"""
    shift_sunday_holidays: ClassVar[bool]
    def get_shifted_holidays(self, dates: Iterable[tuple[_D, str]]) -> Generator[tuple[_D, str]]:
        """
        Taking a list of existing holidays, yield a list of 'shifted' days if
        the holiday falls on SUN, excluding the Islamic holidays.
        """
        ...
