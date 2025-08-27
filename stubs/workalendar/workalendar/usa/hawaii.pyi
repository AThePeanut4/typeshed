import datetime

from .core import UnitedStates

class Hawaii(UnitedStates):
    """Hawaii"""
    def get_statehood_day(self, year: int) -> tuple[datetime.date, str]:
        """Statehood Day: 3rd Friday in August."""
        ...
