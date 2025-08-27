"""
The `French Republican calendar <https://en.wikipedia.org/wiki/French_Republican_calendar>`__
was created during the heroic overthrow of the Ancien Regime.

Leap year calculations in the French Republican calendar are a matter of
dispute. By default, `convertdate` calculates leap years using the
autumnal equinox. You can also use one of three more systematic methods
proposed over the years.

-   Romme, a co-creator of the calendar, proposed leap years in years
    divisible by four, except for years divisible by 100.
-   Some concordances were drawn up in the 19th century that gave leap
    years every 4 years, in years that give a remainder of three when
    divided by four (19, 23, 27, etc...).
-   Von Mädler proposed leap years in years divisible by four, except
    for years divisible by 128.

You can specify any of these three methods with the method keyword
argument in `french_republican` conversion functions.

.. code-block:: python

   from convertdate import french_republican

   french_republican.to_gregorian(20, 1, 1), method='romme')
   # (1811, 9, 23)

   french_republican.to_gregorian(20, 1, 1), method='continuous')
   # (1811, 9, 24)

   french_republican.to_gregorian(20, 1, 1), method='madler')
   # (1811, 9, 23)

All the conversion methods correctly assign the leap years implemented
while calendar was in use (3, 7, 11).
"""

from typing import Final, Literal

EPOCH: Final = 2375839.5
YEAR_EPOCH: Final = 1791.0
DAYS_IN_YEAR: Final = 365.0
MOIS: Final[list[str]]
MONTHS: Final[list[str]]
LEAP_CYCLE_DAYS: Final = 1461.0
LEAP_CYCLE_YEARS: Final = 4.0

def leap(year: int, method: Literal[4, 100, 128, "continuous", "madler", "romme", "equinox"] | None = None) -> bool:
    """
    Determine if this is a leap year in the FR calendar using one of three methods: 4, 100, 128
    (every 4th years, every 4th or 400th but not 100th, every 4th but not 128th)

    Methods:
        * 4 (concordance rule): leap every four years: 3, 7, 11, 15, ... etc
        * 100 (Romme's rule): leap every 4th and 400th year, but not 100th:
            20, 24, ... 96, 104, ... 396, 400, 404 ...
        * 128 (von Mädler's rule): leap every 4th but not 128th: 20, 24, ... 124, 132, ...
        * equinox [default]: use calculation of the equinox to determine date, never returns a leap year
    """
    ...
def premier_da_la_annee(jd: float) -> float:
    """
    Returns Julian day number containing fall equinox (first day of the FR year)
    of the current FR year.
    """
    ...
def to_jd(
    year: int, month: int, day: int, method: Literal[4, 100, 128, "continuous", "madler", "romme", "equinox"] | None = None
) -> float:
    """Obtain Julian day from a given French Revolutionary calendar date."""
    ...
def from_jd(
    jd: float, method: Literal[4, 100, 128, "continuous", "madler", "romme", "equinox"] | None = None
) -> tuple[int, int, int]:
    """
    Calculate date in the French Revolutionary
    calendar from Julian day.  The five or six
    "sansculottides" are considered a thirteenth
    month in the results of this function.
    """
    ...
def decade(jour: float) -> int: ...
def day_name(month: int, day: int) -> str: ...
def from_gregorian(
    year: int, month: int, day: int, method: Literal[4, 100, 128, "continuous", "madler", "romme", "equinox"] | None = None
) -> tuple[int, int, int]: ...
def to_gregorian(
    an: int, mois: int, jour: int, method: Literal[4, 100, 128, "continuous", "madler", "romme", "equinox"] | None = None
) -> tuple[int, int, int]: ...
def format(an: int, mois: int, jour: int) -> str:
    """Convert a FR date into a string with the format DD MONTH YYYY."""
    ...
