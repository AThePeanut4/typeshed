"""
tzinfo implementations for psycopg2

This module holds two different tzinfo implementations that can be used as
the 'tzinfo' argument to datetime constructors, directly passed to psycopg
functions or used to set the .tzinfo_factory attribute in cursors.
"""

import datetime
from typing import Any
from typing_extensions import Self

ZERO: datetime.timedelta

class FixedOffsetTimezone(datetime.tzinfo):
    """
    Fixed offset in minutes east from UTC.

    This is exactly the implementation__ found in Python 2.3.x documentation,
    with a small change to the `!__init__()` method to allow for pickling
    and a default name in the form ``sHH:MM`` (``s`` is the sign.).

    The implementation also caches instances. During creation, if a
    FixedOffsetTimezone instance has previously been created with the same
    offset and name that instance will be returned. This saves memory and
    improves comparability.

    .. versionchanged:: 2.9

        The constructor can take either a timedelta or a number of minutes of
        offset. Previously only minutes were supported.

    .. __: https://docs.python.org/library/datetime.html
    """
    def __init__(self, offset: datetime.timedelta | float | None = None, name: str | None = None) -> None: ...
    def __new__(cls, offset: datetime.timedelta | float | None = None, name: str | None = None) -> Self:
        """
        Return a suitable instance created earlier if it exists
        
        """
        ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __getinitargs__(self) -> tuple[Any, ...]: ...
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta: ...
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta: ...

STDOFFSET: datetime.timedelta
DSTOFFSET: datetime.timedelta
DSTDIFF: datetime.timedelta

class LocalTimezone(datetime.tzinfo):
    """
    Platform idea of local timezone.

    This is the exact implementation from the Python 2.3 documentation.
    """
    def utcoffset(self, dt: datetime.datetime) -> datetime.timedelta: ...  # type: ignore[override]
    def dst(self, dt: datetime.datetime) -> datetime.timedelta: ...  # type: ignore[override]
    def tzname(self, dt: datetime.datetime) -> str: ...  # type: ignore[override]

LOCAL: LocalTimezone
