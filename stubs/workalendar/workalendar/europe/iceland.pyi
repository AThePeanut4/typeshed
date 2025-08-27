import datetime

from ..core import WesternCalendar

class Iceland(WesternCalendar):
    """Iceland"""
    def get_first_day_of_summer(self, year: int) -> datetime.date:
        """
        It's the first thursday *after* April, 18th.
        If April the 18th is a thursday, then it jumps to the 24th.
        """
        ...
    def get_commerce_day(self, year: int) -> datetime.date: ...
