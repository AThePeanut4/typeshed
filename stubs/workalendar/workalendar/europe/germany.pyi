import datetime
from typing import ClassVar

from ..core import WesternCalendar

class Germany(WesternCalendar):
    """Germany"""
    all_time_include_reformation_day: ClassVar[bool]
    include_reformation_day_2018: ClassVar[bool]
    def include_reformation_day(self, year: int) -> bool:
        """Return True if the Reformation Day is a holiday."""
        ...
    def get_reformation_day(self, year: int) -> tuple[datetime.date, str]:
        """
        Reformation Day is a fixed date.

        It's handled via the variable_days because it can be activated
        depending on the Länder or the year (see #150).
        """
        ...

class BadenWurttemberg(Germany):
    """Baden-Wuerttemberg"""
    ...
class Bavaria(Germany):
    """Bavaria"""
    ...

class Berlin(Germany):
    """Berlin"""
    def get_international_womens_day(self, year: int) -> tuple[datetime.date, str]: ...
    def get_liberation_day(self, year: int) -> tuple[datetime.date, str]: ...

class Brandenburg(Germany):
    """Brandenburg"""
    ...
class Bremen(Germany):
    """Bremen"""
    ...
class Hamburg(Germany):
    """Hamburg"""
    ...
class Hesse(Germany):
    """Hesse"""
    ...
class MecklenburgVorpommern(Germany):
    """Mecklenburg-Western Pomerania"""
    ...
class LowerSaxony(Germany):
    """Lower Saxony"""
    ...
class NorthRhineWestphalia(Germany):
    """North Rhine-Westphalia"""
    ...
class RhinelandPalatinate(Germany):
    """Rhineland-Palatinate"""
    ...
class Saarland(Germany):
    """Saarland"""
    ...

class Saxony(Germany):
    """Saxony"""
    def get_repentance_day(self, year: int) -> tuple[datetime.date, str]:
        """Wednesday before November 23"""
        ...

class SaxonyAnhalt(Germany):
    """Saxony-Anhalt"""
    ...
class SchleswigHolstein(Germany):
    """Schleswig-Holstein"""
    ...
class Thuringia(Germany):
    """Thuringia"""
    ...
