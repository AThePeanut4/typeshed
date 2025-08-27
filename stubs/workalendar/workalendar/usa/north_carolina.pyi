import datetime

from .core import UnitedStates

class NorthCarolina(UnitedStates):
    """North Carolina"""
    def get_christmas_shifts(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return Specific Christmas days extra shifts.
        There must be 3 holidays in a row: Christmas Eve, Christmas Day and
        Boxing Day. If one or the other falls on SUN/SAT, extra days must be
        added.
        """
        ...
