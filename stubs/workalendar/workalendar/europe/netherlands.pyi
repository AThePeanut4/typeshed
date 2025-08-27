import datetime
from typing import Final, Literal

from ..core import WesternCalendar

class Netherlands(WesternCalendar):
    """Netherlands"""
    include_carnival: bool
    def __init__(self, include_carnival: bool = False) -> None: ...
    def get_king_queen_day(self, year: int) -> tuple[datetime.date, str]:
        """
        27 April unless this is a Sunday in which case it is the 26th

        Before 2013 it was called Queensday, falling on
        30 April, unless this is a Sunday in which case it is the 29th.
        """
        ...
    def get_carnival_days(self, year: int) -> list[tuple[datetime.date, str]]:
        """Carnival starts 7 weeks before Easter Sunday and lasts 3 days."""
        ...

FALL_HOLIDAYS_EARLY_REGIONS: Final[dict[int, list[str]]]
SPRING_HOLIDAYS_EARLY_REGIONS: Final[dict[int, list[str]]]
SUMMER_HOLIDAYS_EARLY_REGIONS: Final[dict[int, list[str]]]
SUMMER_HOLIDAYS_LATE_REGIONS: Final[dict[int, list[str]]]

class NetherlandsWithSchoolHolidays(Netherlands):
    """
    Netherlands with school holidays (2016 to 2025).

    Data source and regulating body:
    https://www.rijksoverheid.nl/onderwerpen/schoolvakanties/overzicht-schoolvakanties-per-schooljaar
    """
    region: Literal["north", "middle", "south"]
    carnival_instead_of_spring: bool
    def __init__(
        self,
        region: Literal["north", "middle", "south"],
        carnival_instead_of_spring: bool = False,
        *,
        include_carnival: bool = ...,
    ) -> None:
        """
        Set up a calendar incl. school holidays for a specific region

        :param region: either "north", "middle" or "south"
        """
        ...
    def get_fall_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return Fall holidays.

        They start at week 43 or 44 and last for 9 days
        """
        ...
    def get_christmas_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return Christmas holidays

        Christmas holidays run partially in December and partially in January
        (spillover from previous year).
        """
        ...
    def get_spring_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return the Spring holidays

        They start at week 8 or 9 and last for 9 days.
        """
        ...
    def get_carnival_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return Carnival holidays

        Carnival holidays start 7 weeks and 1 day before Easter Sunday
        and last 9 days.
        """
        ...
    def get_may_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return May holidays

        They start at week 18 (or 17) and last for 18 days
        """
        ...
    def get_summer_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """Return the summer holidays as a list"""
        ...
