import datetime

from ..core import WesternCalendar

class Paraguay(WesternCalendar):
    """Paraguay"""
    def get_heroes_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Heroes Day is a fixed holidays.

        In 2017, it has been moved to February 27th ; otherwise, it happens on
        March 1st.

        ref: https://en.wikipedia.org/wiki/Public_holidays_in_Paraguay
        """
        ...
    def get_founding_of_asuncion(self, year: int) -> tuple[datetime.date, str]:
        """
        Return the Founding of Asunción.

        In 2017, it has been moved to August 14th ; otherwise it happens on
        August 15th.
        """
        ...
    def get_boqueron_battle_victory_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Return Boqueron Battle Victory Day.

        In 2017, it has been moved to October 2nd ; otherwise it happens on
        September 29th.
        """
        ...
