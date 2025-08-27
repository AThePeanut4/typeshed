import datetime

from ..core import WesternCalendar

class Colombia(WesternCalendar):
    """Colombia"""
    def get_epiphany(self, year: int) -> datetime.date:
        """Epiphany is shifted in Colombia"""
        ...
    def get_saint_joseph(self, year: int) -> datetime.date: ...
    def get_ascension(self, year: int) -> datetime.date: ...
    def get_sacred_heart(self, year: int) -> datetime.date: ...
    def get_saint_peter_and_saint_paul(self, year: int) -> datetime.date: ...
    def get_assumption(self, year: int) -> datetime.date: ...
    def get_day_of_the_races(self, year: int) -> datetime.date:
        """
        Return Day of the Races and Hispanity

        a.k.a. "Día de la Raza"
        Fixed to the next MON after October 12th (Columbus Day)
        """
        ...
    def get_all_saints(self, year: int) -> datetime.date: ...
    def get_cartagena_independence(self, year: int) -> datetime.date:
        """
        Cartagena independance day

        Fixed to the next MON after November 11th.
        """
        ...
