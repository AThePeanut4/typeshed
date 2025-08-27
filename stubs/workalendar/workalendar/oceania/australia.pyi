import datetime
from typing import ClassVar

from ..core import WesternCalendar

class Australia(WesternCalendar):
    """Australia"""
    include_queens_birthday: ClassVar[bool]
    include_labour_day_october: ClassVar[bool]
    shift_anzac_day: ClassVar[bool]
    ANZAC_SHIFT_DAYS: ClassVar[tuple[int, ...]]
    def get_canberra_day(self, year: int) -> tuple[datetime.date, str]: ...
    def get_queens_birthday(self, year: int) -> tuple[datetime.date, str]: ...
    def get_labour_day_october(self, year: int) -> tuple[datetime.date, str]: ...
    def get_anzac_day(self, year: int) -> tuple[datetime.date, str]: ...

class AustralianCapitalTerritory(Australia):
    """Australian Capital Territory"""
    def get_family_community_day(self, year: int) -> tuple[datetime.date, str] | None:
        """
        Return Family & Community Day.

        see: https://en.wikipedia.org/wiki/Family_Day#Australia
        """
        ...
    def get_reconciliation_day(self, year: int) -> tuple[datetime.date, str] | None:
        """
        Return Reconciliaton Day.

        As of 2018, it replaces Family & Community Day.
        """
        ...

class NewSouthWales(Australia):
    """New South Wales"""
    ...

class NorthernTerritory(Australia):
    """Northern Territory"""
    def get_may_day(self, year: int) -> tuple[datetime.date, str]: ...
    def get_picnic_day(self, year: int) -> tuple[datetime.date, str]: ...

class Queensland(Australia):
    """Queensland"""
    def get_labour_day_may(self, year: int) -> tuple[datetime.date, str]: ...

class SouthAustralia(Australia):
    """South Australia"""
    def get_adelaides_cup(self, year: int) -> tuple[datetime.date, str]: ...
    def get_proclamation_day(self, year: int) -> tuple[datetime.date, str]: ...

class Tasmania(Australia):
    """Tasmania"""
    @property
    def has_recreation_day(self) -> bool: ...
    def get_eight_hours_day(self, year: int) -> tuple[datetime.date, str]: ...
    def get_recreation_day(self, year: int) -> tuple[datetime.date, str]: ...

class Hobart(Tasmania):
    """Hobart"""
    def get_hobart(self, year: int) -> tuple[datetime.date, str]: ...

class Victoria(Australia):
    """Victoria"""
    def get_labours_day_in_march(self, year: int) -> tuple[datetime.date, str]: ...
    def get_melbourne_cup(self, year: int) -> tuple[datetime.date, str]: ...

class WesternAustralia(Australia):
    """Western Australia"""
    def get_labours_day_in_march(self, year: int) -> tuple[datetime.date, str]: ...
    def get_western_australia_day(self, year: int) -> tuple[datetime.date, str]: ...
