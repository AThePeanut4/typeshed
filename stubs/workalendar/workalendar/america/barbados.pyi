import datetime

from ..core import WesternCalendar

class Barbados(WesternCalendar):
    """Barbados"""
    non_computable_holiday_dict: dict[int, list[tuple[datetime.date, str]]]
    def get_kadooment_day(self, year: int) -> tuple[datetime.date, str]:
        """First Monday of August."""
        ...
    def get_emancipation_day(self, year: int) -> tuple[datetime.date, str]: ...
    def non_computable_holiday(self, year: int) -> list[tuple[datetime.date, str]] | None: ...
    def get_fixed_holidays(self, year: int) -> list[tuple[datetime.date, str]]:
        """
        Return fixed holidays of the Barbados calendar.

        A shift day is appended if a fixed holiday happens on SUN.
        """
        ...
