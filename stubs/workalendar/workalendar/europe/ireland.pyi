import datetime

from ..core import WesternCalendar

class Ireland(WesternCalendar):
    """Ireland"""
    def get_june_holiday(self, year: int) -> tuple[datetime.date, str]: ...
    def get_august_holiday(self, year: int) -> tuple[datetime.date, str]: ...
