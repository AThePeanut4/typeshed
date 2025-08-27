from typing import ClassVar

from .core import UnitedStates

class California(UnitedStates):
    """California"""
    shift_exceptions: ClassVar[list[tuple[int, int]]]

class CaliforniaEducation(California):
    """
    California Education

    This administration holds its own calendar. In order to respect the goal
    of workalendar (to compute (non)working days), we've decided to only retain
    days when the schools are closed.
    """
    ...
class CaliforniaBerkeley(California):
    """Berkeley, California"""
    ...
class CaliforniaSanFrancisco(California):
    """San Francisco, California"""
    ...
class CaliforniaWestHollywood(California):
    """West Hollywood, California"""
    ...
