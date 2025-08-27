import datetime

from ..core import OrthodoxCalendar

class Romania(OrthodoxCalendar):
    """Romania"""
    def get_childrens_day(self, year: int) -> list[tuple[datetime.date, str]]:
        """returns a possibly empty list of (date, holiday_name) tuples"""
        ...
    def get_liberation_day(self, year: int) -> list[tuple[datetime.date, str]]:
        """returns a possibly empty list of (date, holiday_name) tuples"""
        ...
