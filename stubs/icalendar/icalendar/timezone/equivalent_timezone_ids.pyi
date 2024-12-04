"""
This module helps identifying the timezone ids and where they differ.

The algorithm: We use the tzname and the utcoffset for each hour from
1970 - 2030.
We make a big map.
If they are equivalent, they are equivalent within the time that is mostly used.

You can regenerate the information from this module.

See also:
- https://stackoverflow.com/questions/79185519/which-timezones-are-equivalent
"""

import datetime
from collections.abc import Callable
from typing import Final

__all__ = ["main"]

def check(dt: datetime.datetime, tz: datetime.tzinfo) -> tuple[datetime.datetime, datetime.timedelta]: ...
def checks(tz: datetime.tzinfo) -> list[tuple[datetime.datetime, datetime.timedelta]]: ...

START: Final[datetime.datetime]
END: Final[datetime.datetime]

DTS: Final[list[datetime.datetime]]

def main(create_timezones: list[Callable[[str], datetime.tzinfo]], name: str, pool_size: int = ...) -> None:
    """
    Generate a lookup table for timezone information if unknown timezones.

    We cannot create one lookup for all because they seem to be all equivalent
    if we mix timezone implementations.
    """
    ...
