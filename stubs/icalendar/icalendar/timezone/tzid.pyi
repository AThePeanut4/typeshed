"""
This module identifies timezones.

Normally, timezones have ids.
This is a way to access the ids if you have a
datetime.tzinfo object.
"""

import datetime

__all__ = ["tzid_from_tzinfo", "tzid_from_dt", "tzids_from_tzinfo"]

def tzids_from_tzinfo(tzinfo: datetime.tzinfo | None) -> tuple[str, ...]: ...
def tzid_from_tzinfo(tzinfo: datetime.tzinfo | None) -> str | None: ...
def tzid_from_dt(dt: datetime.datetime) -> str | None: ...
