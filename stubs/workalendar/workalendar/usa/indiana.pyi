import datetime
from typing import ClassVar

from .core import UnitedStates

class Indiana(UnitedStates):
    """Indiana"""
    label_washington_birthday_december: ClassVar[str]
    def get_washington_birthday_december(self, year: int) -> tuple[datetime.date, str]:
        """
        Washington birthday observance
        Similar to Christmas Eve, but with special rules.
        It's only observed in Georgia.
        """
        ...
    def get_primary_election_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Return the Primary Election Day

        FIXME: Wikipedia says it's a floating MON, but other sources say it's
        "the first Tuesday after the first Monday of May and every two years
        thereafter".
        """
        ...
