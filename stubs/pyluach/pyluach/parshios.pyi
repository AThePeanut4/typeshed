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

def getparsha(date: BaseDate, israel: bool = False) -> list[int] | None:
    """
    Return the parsha for a given date.

    Returns the parsha for the Shabbos on or following the given
    date.

    Parameters
    ----------
    date : ~pyluach.dates.BaseDate
      Any subclass of ``BaseDate``. This date does not have to be a Shabbos.

    israel : bool, optional
      ``True`` if you want the parsha according to the Israel schedule
      (with only one day of Yom Tov). Defaults to ``False``.

    Returns
    -------
    list of int or None
      A list of the numbers of the parshios for the Shabbos of the given date,
      beginning with 0 for Beraishis, or ``None`` if the Shabbos doesn't
      have a parsha (i.e. it's on Yom Tov).
    """
    ...
def getparsha_string(date: BaseDate, israel: bool = False, hebrew: bool = False) -> str | None:
    """
    Return the parsha as a string for the given date.

    This function wraps ``getparsha`` returning the parsha name.

    Parameters
    ----------
    date : ~pyluach.dates.BaseDate
      Any subclass of ``BaseDate``. The date does not have to be a Shabbos.

    israel : bool, optional
      ``True`` if you want the parsha according to the Israel schedule
      (with only one day of Yom Tov). Default is ``False``.

    hebrew : bool, optional
      ``True`` if you want the name of the parsha in Hebrew.
      Default is ``False``.

    Returns
    -------
    str or None
      The name of the parsha separated by a comma and space if it is a
      double parsha or ``None`` if there is no parsha that Shabbos
      (ie. it's yom tov).
    """
    ...
def iterparshios(year: int, israel: bool = False) -> Generator[list[int] | None]:
    """
    Generate all the parshios in the year.

    Parameters
    ----------
    year : int
      The Hebrew year to get the parshios for.

    israel : bool, optional
      ``True`` if you want the parsha according to the Israel schedule
      (with only one day of Yom Tov). Defaults to ``False``

    Yields
    ------
    :obj:`list` of :obj:`int` or :obj:`None`
      A list of the numbers of the parshios for the next Shabbos in the
      given year. Yields ``None`` for a Shabbos that doesn't have its
      own parsha (i.e. it occurs on a yom tov).
    """
    ...
def parshatable(year: int, israel: bool = False) -> OrderedDict[HebrewDate, list[int] | None]:
    """
    Return a table of all the Shabbosos in the year

    Parameters
    ----------
    year : int
      The Hebrew year to get the parshios for.

    israel : bool, optional
      ``True`` if you want the parshios according to the Israel
      schedule (with only one day of Yom Tov). Defaults to ``False``.

    Returns
    -------
    ~collections.OrderedDict
      An ordered dictionary with the ``HebrewDate`` of each Shabbos
      as the key mapped to the parsha as a list of ints, or ``None`` for a
      Shabbos with no parsha.
    """
    ...
def four_parshios(date: BaseDate, hebrew: bool = False) -> str:
    """
    Return which of the four parshios is given date's Shabbos.

    Parameters
    ----------
    date : ~pyluach.dates.BaseDate
      Any subclass of ``BaseDate``. This date does not have to be a Shabbos.

    hebrew : bool
      ``True`` if you want the name of the parsha in Hebrew.
      Default is ``False``.

    Returns
    -------
    str
      The name of the one of the four parshios or an empty string
      if that shabbos is not one of them.
    """
    ...
