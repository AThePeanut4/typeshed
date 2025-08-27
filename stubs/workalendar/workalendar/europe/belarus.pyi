import datetime

from ..core import OrthodoxCalendar

class Belarus(OrthodoxCalendar):
    """Belarus"""
    def get_radonitsa(self, year: int) -> datetime.date: ...
