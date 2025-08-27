import datetime
from typing import ClassVar

from ..core import WesternCalendar

class UnitedStates(WesternCalendar):
    """United States of America"""
    include_veterans_day: ClassVar[bool]
    veterans_day_label: ClassVar[str]
    martin_luther_king_label: ClassVar[str]
    include_thanksgiving_friday: ClassVar[bool]
    thanksgiving_friday_label: ClassVar[str]
    include_federal_presidents_day: ClassVar[bool]
    presidents_day_label: ClassVar[str]
    include_lincoln_birthday: ClassVar[bool]
    include_columbus_day: ClassVar[bool]
    columbus_day_label: ClassVar[str]
    include_confederation_day: ClassVar[bool]
    include_jefferson_davis_birthday: ClassVar[bool]
    include_cesar_chavez_day: ClassVar[bool]
    include_patriots_day: ClassVar[bool]
    include_election_day_every_year: ClassVar[bool]
    include_election_day_even: ClassVar[bool]
    election_day_label: ClassVar[str]
    include_inauguration_day: ClassVar[bool]
    national_memorial_day_label: ClassVar[str]
    fat_tuesday_label: ClassVar[str]
    include_juneteenth: ClassVar[bool]
    shift_exceptions: ClassVar[tuple[tuple[int, int], ...] | list[tuple[int, int]]]
    def shift(self, holidays: list[tuple[datetime.date, str]], year: int) -> list[tuple[datetime.date, str]]:
        """Shift all holidays of the year, according to the shifting rules."""
        ...
    @staticmethod
    def is_presidential_year(year: int) -> bool: ...
    def get_election_date(self, year: int) -> datetime.date:
        """
        Return the Election Day *Date*

        Definition: on an election year, "the Tuesday next after the first
        Monday in the month of November".
        """
        ...
    def get_election_day(self, year: int) -> tuple[datetime.date, str]:
        """Return the Election Day"""
        ...
    def get_thanksgiving_friday(self, year: int) -> tuple[datetime.date, str]:
        """Thanksgiving friday is on the day following Thanksgiving Day"""
        ...
    def get_confederate_day(self, year: int) -> tuple[datetime.date, str]:
        """Confederate memorial day is on the 4th MON of April."""
        ...
    def get_jefferson_davis_birthday(self, year: int) -> tuple[datetime.date, str]:
        """The first MON of June is Jefferson Davis Birthday"""
        ...
    def get_martin_luther_king_date(self, year: int) -> datetime.date:
        """Martin Luther King is on 3rd MON of January, starting of 1985."""
        ...
    def get_martin_luther_king_day(self, year: int) -> tuple[datetime.date, str]:
        """Return holiday record for Martin Luther King Jr. Day."""
        ...
    def get_presidents_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Presidents Day is on the 3rd MON of February

        May be called Washington's or Lincoln's birthday
        """
        ...
    def get_cesar_chavez_days(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Cesar Chavez day is on 31st of March

        Will return a list of days, because in some states (California),
        it can float to MON if it happens on SUN.
        """
        ...
    def get_patriots_day(self, year: int) -> tuple[datetime.date, str]:
        """3rd Monday of April"""
        ...
    def get_columbus_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Columbus day is on the 2nd MON of October.

        Only half of the states recognize it.
        """
        ...
    def get_lincoln_birthday(self, year: int) -> tuple[datetime.date, str]:
        """
        February the 2nd is Lincoln's birthday in the following States:

        * Connecticut,
        * Illinois,
        * Missouri,
        * New York
        """
        ...
    def get_inauguration_date(self, year: int) -> datetime.date:
        """
        If the year is an Inauguration Year, will return the Inauguration Day
        date.

        If this day falls on SUN, it's replaced by the next MON.
        If the year is not a Inauguration Year, it raises a ValueError.
        """
        ...
    def get_national_memorial_day(self, year: int) -> tuple[datetime.date, str]:
        """Return National Memorial Day"""
        ...
    def get_juneteenth_day(self, year: int) -> tuple[datetime.date, str]:
        """Return Juneteenth Day"""
        ...
    def get_veterans_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Return Veterans Day (November 11th).

        Placed here because some States are renaming it.
        """
        ...

class FederalReserveSystem(UnitedStates):
    """Board of Governors of the Federal Reserve System of the USA"""
    ...
