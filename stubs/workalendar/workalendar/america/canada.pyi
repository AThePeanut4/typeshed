import datetime

from ..core import WesternCalendar

class Canada(WesternCalendar):
    """Canada"""
    ...

class LateFamilyDayMixin:
    """3rd Monday of February"""
    def get_family_day(self, year: int, label: str = "Family Day") -> tuple[datetime.date, str]: ...

class VictoriaDayMixin:
    """Monday preceding the 25th of May"""
    def get_victoria_day(self, year: int) -> tuple[datetime.date, str] | None: ...

class AugustCivicHolidayMixin:
    """1st Monday of August; different names depending on location"""
    def get_civic_holiday(self, year: int, label: str = "Civic Holiday") -> tuple[datetime.date, str]: ...

class ThanksgivingMixin:
    """2nd Monday of October"""
    def get_thanksgiving(self, year: int) -> tuple[datetime.date, str]: ...

class BoxingDayMixin:
    """26th of December; shift to next working day"""
    def get_boxing_day(self, year: int) -> list[tuple[datetime.date, str]]: ...

class StJeanBaptisteMixin:
    """24th of June; shift to next working day"""
    def get_st_jean(self, year: int) -> list[tuple[datetime.date, str]]: ...

class RemembranceDayShiftMixin:
    """11th of November; shift to next day"""
    def get_remembrance_day(self, year: int) -> list[tuple[datetime.date, str]]: ...

class Ontario(BoxingDayMixin, ThanksgivingMixin, VictoriaDayMixin, LateFamilyDayMixin, AugustCivicHolidayMixin, Canada):
    """Ontario"""
    ...
class Quebec(VictoriaDayMixin, StJeanBaptisteMixin, ThanksgivingMixin, Canada):
    """Quebec"""
    ...

class BritishColumbia(VictoriaDayMixin, AugustCivicHolidayMixin, ThanksgivingMixin, Canada):
    """British Columbia"""
    def get_family_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Return Family Day for British Columbia.

        From 2013 to 2018, Family Day was on 2nd MON of February
        As of 2019, Family Day happens on 3rd MON of February
        """
        ...

class Alberta(LateFamilyDayMixin, VictoriaDayMixin, ThanksgivingMixin, Canada):
    """Alberta"""
    ...
class Saskatchewan(
    LateFamilyDayMixin, VictoriaDayMixin, RemembranceDayShiftMixin, AugustCivicHolidayMixin, ThanksgivingMixin, Canada
):
    """Saskatchewan"""
    ...
class Manitoba(LateFamilyDayMixin, VictoriaDayMixin, AugustCivicHolidayMixin, ThanksgivingMixin, Canada):
    """Manitoba"""
    ...
class NewBrunswick(AugustCivicHolidayMixin, Canada):
    """New Brunswick"""
    ...
class NovaScotia(RemembranceDayShiftMixin, LateFamilyDayMixin, Canada):
    """Nova Scotia"""
    ...
class PrinceEdwardIsland(LateFamilyDayMixin, RemembranceDayShiftMixin, Canada):
    """Prince Edward Island"""
    ...
class Newfoundland(Canada):
    """Newfoundland and Labrador"""
    ...
class Yukon(VictoriaDayMixin, ThanksgivingMixin, Canada):
    """Yukon"""
    ...
class NorthwestTerritories(RemembranceDayShiftMixin, VictoriaDayMixin, ThanksgivingMixin, Canada):
    """Northwest Territories"""
    ...
class Nunavut(VictoriaDayMixin, ThanksgivingMixin, RemembranceDayShiftMixin, Canada):
    """Nunavut"""
    ...
