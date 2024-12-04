"""
times module

This module provides some Date and Time classes for dealing with MySQL data.

Use Python datetime module to handle date and time columns.
"""

from _typeshed import Unused
from datetime import date, datetime, time, timedelta

from MySQLdb._mysql import string_literal as string_literal

Date = date
Time = time
TimeDelta = timedelta
Timestamp = datetime
DateTimeDeltaType = timedelta
DateTimeType = datetime

def DateFromTicks(ticks: float | None) -> date:
    """Convert UNIX ticks into a date instance."""
    ...
def TimeFromTicks(ticks: float | None) -> time:
    """Convert UNIX ticks into a time instance."""
    ...
def TimestampFromTicks(ticks: float | None) -> datetime:
    """Convert UNIX ticks into a datetime instance."""
    ...

format_TIME = str
format_DATE = str

def format_TIMEDELTA(v: timedelta) -> str: ...
def format_TIMESTAMP(d: datetime) -> str:
    """:type d: datetime.datetime"""
    ...
def DateTime_or_None(s: str) -> datetime | None: ...
def TimeDelta_or_None(s: str) -> timedelta | None: ...
def Time_or_None(s: str) -> time | None: ...
def Date_or_None(s: str) -> date | None: ...
def DateTime2literal(d: datetime, c: Unused) -> str:
    """Format a DateTime object as an ISO timestamp."""
    ...
def DateTimeDelta2literal(d: datetime, c: Unused) -> str:
    """Format a DateTimeDelta object as a time."""
    ...
