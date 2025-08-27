import datetime

from ..core import WesternCalendar

class Latvia(WesternCalendar):
    """Latvia"""
    def get_independence_days(self, year: int) -> list[tuple[datetime.date, str]]:
        """returns a possibly empty list of (date, holiday_name) tuples"""
        ...
    def get_republic_days(self, year: int) -> list[tuple[datetime.date, str]]:
        """returns a possibly empty list of (date, holiday_name) tuples"""
        ...
