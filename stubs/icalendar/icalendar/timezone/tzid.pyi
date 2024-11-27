"""
This module identifies timezones.

Normally, timezones have ids.
This is a way to access the ids if you have a
datetime.tzinfo object.
"""

import datetime

__all__ = ["tzid_from_tzinfo", "tzid_from_dt", "tzids_from_tzinfo"]

def tzids_from_tzinfo(tzinfo: datetime.tzinfo | None) -> tuple[str, ...]:
    """
    Get several timezone ids if we can identify the timezone.

    >>> import zoneinfo
    >>> from icalendar.timezone.tzid import tzids_from_tzinfo
    >>> tzids_from_tzinfo(zoneinfo.ZoneInfo("Africa/Accra"))
    ('Africa/Accra',)
    >>> from dateutil.tz import gettz
    >>> tzids_from_tzinfo(gettz("Europe/Berlin"))
    ('Arctic/Longyearbyen', 'Atlantic/Jan_Mayen', 'Europe/Berlin', 'Europe/Budapest', 'Europe/Copenhagen', 'Europe/Oslo', 'Europe/Stockholm', 'Europe/Vienna')
    """
    ...
def tzid_from_tzinfo(tzinfo: datetime.tzinfo | None) -> str | None:
    """
    Retrieve the timezone id from the tzinfo object.

    Some timezones are equivalent.
    Thus, we might return one ID that is equivelant to others.
    """
    ...
def tzid_from_dt(dt: datetime.datetime) -> str | None:
    """Retrieve the timezone id from the datetime object."""
    ...
def tzinfo2tzids(tzinfo: datetime.tzinfo | None) -> set[str]:
    """
    We return the tzids for a certain tzinfo object.

    With different datetimes, we match
    (tzinfo.utcoffset(dt), tzinfo.tzname(dt))

    If we could identify the timezone, you will receive a tuple
    with at least one tzid. All tzids are equivalent which means
    that they describe the same timezone.

    You should get results with any timezone implementation if it is known.
    This one is especially useful for dateutil.

    In the following example, we can see that the timezone Africa/Accra
    is equivalent to many others.

    >>> import zoneinfo
    >>> from icalendar.timezone.tzid import tzinfo2tzids
    >>> "Europe/Berlin" in tzinfo2tzids(zoneinfo.ZoneInfo("Europe/Berlin"))
    True
    """
    ...
