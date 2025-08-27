import datetime
from typing import Final

from ..core import WesternCalendar

QUEENS_BIRTHDAY_EXCEPTIONS: Final[dict[int, datetime.date]]

class CaymanIslands(WesternCalendar):
    """Cayman Islands"""
    def get_national_heroes_day(self, year: int) -> datetime.date:
        """National Heroes day: Fourth MON in January"""
        ...
    def get_discovery_day(self, year: int) -> datetime.date:
        """Discovery Day: Third MON in May"""
        ...
    def get_queens_birthday(self, year: int) -> datetime.date:
        """Queen's Birthday: On MON after second SAT in June, with exceptions"""
        ...
    def get_constitution_day(self, year: int) -> datetime.date:
        """Constitution Day: First MON of July."""
        ...
    def get_remembrance_day(self, year: int) -> datetime.date:
        """Remembrance Day: Second MON of November."""
        ...
