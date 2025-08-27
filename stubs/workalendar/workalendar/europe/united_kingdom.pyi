import datetime

from ..core import WesternCalendar

class UnitedKingdom(WesternCalendar):
    """United Kingdom"""
    non_computable_holiday_dict: dict[int, list[tuple[datetime.date, str]]]
    def get_early_may_bank_holiday(self, year: int) -> tuple[datetime.date, str]:
        """Return Early May bank holiday"""
        ...
    def get_spring_bank_holiday(self, year: int) -> tuple[datetime.date, str]: ...
    def get_late_summer_bank_holiday(self, year: int) -> tuple[datetime.date, str]: ...
    def non_computable_holiday(self, year: int) -> tuple[datetime.date, str] | None: ...

class UnitedKingdomNorthernIreland(UnitedKingdom):
    """Northern Ireland"""
    ...
