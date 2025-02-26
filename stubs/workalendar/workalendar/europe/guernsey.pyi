from typing import ClassVar

from ..core import WesternCalendar

class Guernsey(WesternCalendar):
    """Guernsey"""
    include_easter_monday: ClassVar[bool]
    include_boxing_day: ClassVar[bool]
    shift_new_years_day: ClassVar[bool]
    include_good_friday: ClassVar[bool]
    def get_spring_bank_holiday(self, year): ...
    def get_early_may_bank_holiday(self, year):
        """Return Early May bank holiday"""
        ...
    def get_summer_bank_holiday(self, year): ...
    def get_liberation_day(self, year): ...
    def get_variable_days(self, year): ...
