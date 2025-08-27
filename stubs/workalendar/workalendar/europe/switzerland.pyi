import datetime
from typing import ClassVar

from ..core import WesternCalendar

class Switzerland(WesternCalendar):
    """Switzerland"""
    include_berchtolds_day: ClassVar[bool]
    include_st_josephs_day: ClassVar[bool]
    def has_berchtolds_day(self, year: int) -> bool: ...
    def get_federal_thanksgiving_monday(self, year: int) -> tuple[datetime.date, str]:
        """Monday following the 3rd sunday of September"""
        ...

class Aargau(Switzerland):
    """Aargau"""
    ...
class AppenzellInnerrhoden(Switzerland):
    """Appenzell Innerrhoden"""
    ...
class AppenzellAusserrhoden(Switzerland):
    """Appenzell Ausserrhoden"""
    ...
class Bern(Switzerland):
    """Bern"""
    ...
class BaselLandschaft(Switzerland):
    """Basel-Landschaft"""
    ...
class BaselStadt(Switzerland):
    """Basel-Stadt"""
    ...
class Fribourg(Switzerland):
    """Fribourg"""
    ...

class Geneva(Switzerland):
    """Geneva"""
    def get_genevan_fast(self, year: int) -> tuple[datetime.date, str]:
        """Thursday following the first Sunday of September"""
        ...

class Glarus(Switzerland):
    """Glarus (Glaris)"""
    ...
class Graubunden(Switzerland):
    """Graubünden (Grisons)"""
    ...
class Jura(Switzerland):
    """Jura"""
    ...
class Luzern(Switzerland):
    """Luzern"""
    ...
class Neuchatel(Switzerland):
    """Neuchâtel"""
    ...
class Nidwalden(Switzerland):
    """Nidwalden"""
    ...
class Obwalden(Switzerland):
    """Obwalden"""
    ...
class StGallen(Switzerland):
    """St. Gallen"""
    ...
class Schaffhausen(Switzerland):
    """Schaffhausen"""
    ...
class Solothurn(Switzerland):
    """Solothurn"""
    ...
class Schwyz(Switzerland):
    """Schwyz"""
    ...
class Thurgau(Switzerland):
    """Thurgau"""
    ...
class Ticino(Switzerland):
    """Ticino"""
    ...
class Uri(Switzerland):
    """Uri"""
    ...
class Vaud(Switzerland):
    """Vaud"""
    ...
class Valais(Switzerland):
    """Valais"""
    ...
class Zug(Switzerland):
    """Zug"""
    ...
class Zurich(Switzerland):
    """Zürich"""
    ...
