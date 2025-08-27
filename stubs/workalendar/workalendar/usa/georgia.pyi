import datetime
from typing import ClassVar

from .core import UnitedStates

class Georgia(UnitedStates):
    """Georgia"""
    label_washington_birthday_december: ClassVar[str]
    def get_washington_birthday_december(self, year: int) -> tuple[datetime.date, str]:
        """
        Washington birthday observance
        Similar to Christmas Eve, but with special rules.
        It's only observed in Georgia.
        """
        ...
    def get_robert_lee_birthday(self, year: int) -> tuple[datetime.date, str]:
        """
        Robert E. Lee's birthday.

        Happens on the day after Thanksgiving.
        """
        ...
