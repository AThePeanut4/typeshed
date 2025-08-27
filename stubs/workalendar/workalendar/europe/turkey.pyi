import datetime

from ..core import IslamicCalendar

class Turkey(IslamicCalendar):
    """Turkey"""
    def get_delta_islamic_holidays(self, year: int) -> datetime.timedelta:
        """Turkey Islamic holidays are shifted by one day every year."""
        ...
