import datetime

from .core import UnitedStates

class AmericanSamoa(UnitedStates):
    """American Samoa"""
    def get_flag_day(self, year: int) -> tuple[datetime.date, str]:
        """Flag day is on April 17th"""
        ...
