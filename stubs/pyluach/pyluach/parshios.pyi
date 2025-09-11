"""
The parshios module has functions to find the weekly parasha.

Examples
--------
>>> from pyluach import dates, parshios
>>> date = dates.HebrewDate(5781, 10, 5)
>>> parshios.getparsha(date)
'Vayigash'
>>> parshios.getparsha_string(date, hebrew=True)
'ויגש'
>>> parshios.getparsha_string(dates.GregorianDate(2021, 3, 7), hebrew=True)
'ויקהל, פקודי'

Note
----
The algorithm is based on Dr. Irv Bromberg's, University of Toronto at
http://individual.utoronto.ca/kalendis/hebrew/parshah.htm

All English parsha names are transliterated into the American Ashkenazik
pronunciation.


Attributes
----------
PARSHIOS : list of str
    A list of the parshios transliterated into English.
PARSHIOS_HEBREW : list of str
    A list of the parshios in Hebrew.
"""

from collections import OrderedDict
from collections.abc import Generator
from typing import Final

from .dates import BaseDate, HebrewDate

PARSHIOS: Final[list[str]]
PARSHIOS_HEBREW: Final[list[str]]

def getparsha(date: BaseDate, israel: bool = False) -> list[int] | None: ...
def getparsha_string(date: BaseDate, israel: bool = False, hebrew: bool = False) -> str | None: ...
def iterparshios(year: int, israel: bool = False) -> Generator[list[int] | None]: ...
def parshatable(year: int, israel: bool = False) -> OrderedDict[HebrewDate, list[int] | None]: ...
def four_parshios(date: BaseDate, hebrew: bool = False) -> str: ...
