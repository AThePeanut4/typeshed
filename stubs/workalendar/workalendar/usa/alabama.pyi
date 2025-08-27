import datetime

from .core import UnitedStates

class Alabama(UnitedStates):
    """Alabama"""
    ...
class AlabamaBaldwinCounty(Alabama):
    """Baldwin County, Alabama"""
    ...
class AlabamaMobileCounty(Alabama):
    """Mobile County, Alabama"""
    ...

class AlabamaPerryCounty(Alabama):
    """Mobile Perry, Alabama"""
    def get_obama_day(self, year: int) -> tuple[datetime.date, str]:
        """Obama Day happens on the 2nd MON of November."""
        ...
