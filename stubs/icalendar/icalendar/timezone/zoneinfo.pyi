"""Use zoneinfo timezones"""

import datetime
import sys
from typing import Final, Literal

from dateutil.rrule import rrule, rruleset

if sys.version_info >= (3, 9):
    from zoneinfo import ZoneInfo
else:
    from backports.zoneinfo import ZoneInfo

from ..cal import Timezone
from ..prop import vRecur
from .provider import TZProvider

__all__ = ["ZONEINFO"]

class ZONEINFO(TZProvider):
    """Provide icalendar with timezones from zoneinfo."""
    @property
    def name(self) -> Literal["zoneinfo"]: ...
    utc: Final[ZoneInfo]
    def localize(self, dt: datetime.datetime, tz: ZoneInfo) -> datetime.datetime:
        """Localize a datetime to a timezone."""
        ...
    def localize_utc(self, dt: datetime.datetime) -> datetime.datetime:
        """Return the datetime in UTC."""
        ...
    def timezone(self, name: str) -> datetime.tzinfo | None:
        """Return a timezone with a name or None if we cannot find it."""
        ...
    def knows_timezone_id(self, id: str) -> bool:
        """Whether the timezone is already cached by the implementation."""
        ...
    def fix_rrule_until(self, rrule: rrule, ical_rrule: vRecur) -> None:
        """Make sure the until value works for the rrule generated from the ical_rrule."""
        ...
    def create_timezone(self, tz: Timezone) -> datetime.tzinfo:
        """Create a timezone from the given information."""
        ...
    def uses_pytz(self) -> Literal[False]:
        """Whether we use pytz."""
        ...
    def uses_zoneinfo(self) -> Literal[True]:
        """Whether we use zoneinfo."""
        ...

def pickle_tzicalvtz(tzicalvtz):
    """Because we use dateutil.tzical, we need to make it pickle-able."""
    ...
def pickle_rruleset_with_cache(rs: rruleset):
    """Pickle an rruleset."""
    ...
def unpickle_rruleset_with_cache(rrule, rdate, exrule, exdate, cache):
    """unpickling the rruleset."""
    ...
