import datetime

from .core import UnitedStates

class Illinois(UnitedStates):
    """Illinois"""
    ...

class ChicagoIllinois(Illinois):
    """Chicago, Illinois"""
    def get_pulaski_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Return Casimir Pulaski Day.

        Defined on the first MON of March.
        ref: https://en.wikipedia.org/wiki/Casimir_Pulaski_Day
        """
        ...
