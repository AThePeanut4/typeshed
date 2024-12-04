"""Definitions and behavior for iCalendar, also known as vCalendar 2.0"""

from _typeshed import Incomplete
from datetime import timedelta
from typing import Any

from .base import Component
from .behavior import Behavior

DATENAMES: tuple[str, ...]
RULENAMES: tuple[str, ...]
DATESANDRULES: tuple[str, ...]
PRODID: str
WEEKDAYS: tuple[str, ...]
FREQUENCIES: tuple[str, ...]
zeroDelta: timedelta
twoHours: timedelta

def toUnicode(s: str | bytes) -> str:
    """Take a string or unicode, turn it into unicode, decoding as utf-8"""
    ...
def registerTzid(tzid, tzinfo) -> None:
    """Register a tzid -> tzinfo mapping."""
    ...
def getTzid(tzid, smart: bool = True):
    """Return the tzid if it exists, or None."""
    ...

utc: Any  # dateutil.tz.tz.tzutc

class TimezoneComponent(Component):
    """
    A VTIMEZONE object.

    VTIMEZONEs are parsed by tz.tzical, the resulting datetime.tzinfo
    subclass is stored in self.tzinfo, self.tzid stores the TZID associated
    with this timezone.

    @ivar name:
        The uppercased name of the object, in this case always 'VTIMEZONE'.
    @ivar tzinfo:
        A datetime.tzinfo subclass representing this timezone.
    @ivar tzid:
        The string used to refer to this timezone.
    """
    isNative: bool
    behavior: Any
    tzinfo: Any
    name: str
    useBegin: bool
    def __init__(self, tzinfo: Incomplete | None = None, *args, **kwds) -> None:
        """Accept an existing Component or a tzinfo class."""
        ...
    @classmethod
    def registerTzinfo(cls, tzinfo):
        """Register tzinfo if it's not already registered, return its tzid."""
        ...
    def gettzinfo(self): ...
    tzid: Any
    daylight: Any
    standard: Any
    def settzinfo(self, tzinfo, start: int = 2000, end: int = 2030):
        """
        Create appropriate objects in self to represent tzinfo.

        Collapse DST transitions to rrules as much as possible.

        Assumptions:
        - DST <-> Standard transitions occur on the hour
        - never within a month of one another
        - twice or fewer times a year
        - never in the month of December
        - DST always moves offset exactly one hour later
        - tzinfo classes dst method always treats times that could be in either
          offset as being in the later regime
        """
        ...
    normal_attributes: Any
    @staticmethod
    def pickTzid(tzinfo, allowUTC: bool = False):
        """Given a tzinfo class, use known APIs to determine TZID, or use tzname."""
        ...
    def prettyPrint(self, level, tabwidth) -> None: ...  # type: ignore[override]

class RecurringComponent(Component):
    """
    A vCalendar component like VEVENT or VTODO which may recur.

    Any recurring component can have one or multiple RRULE, RDATE,
    EXRULE, or EXDATE lines, and one or zero DTSTART lines.  It can also have a
    variety of children that don't have any recurrence information.

    In the example below, note that dtstart is included in the rruleset.
    This is not the default behavior for dateutil's rrule implementation unless
    dtstart would already have been a member of the recurrence rule, and as a
    result, COUNT is wrong. This can be worked around when getting rruleset by
    adjusting count down by one if an rrule has a count and dtstart isn't in its
    result set, but by default, the rruleset property doesn't do this work
    around, to access it getrruleset must be called with addRDate set True.

    @ivar rruleset:
        A U{rruleset<https://moin.conectiva.com.br/DateUtil>}.
    """
    isNative: bool
    def __init__(self, *args, **kwds) -> None: ...
    def getrruleset(self, addRDate: bool = False):
        """
        Get an rruleset created from self.

        If addRDate is True, add an RDATE for dtstart if it's not included in
        an RRULE or RDATE, and count is decremented if it exists.

        Note that for rules which don't match DTSTART, DTSTART may not appear
        in list(rruleset), although it should.  By default, an RDATE is not
        created in these cases, and count isn't updated, so dateutil may list
        a spurious occurrence.
        """
        ...
    def setrruleset(self, rruleset): ...
    rruleset: Any
    def __setattr__(self, name, value) -> None:
        """For convenience, make self.contents directly accessible."""
        ...

class TextBehavior(Behavior):
    """
    Provide backslash escape encoding/decoding for single valued properties.

    TextBehavior also deals with base64 encoding if the ENCODING parameter is
    explicitly set to BASE64.
    """
    base64string: str
    @classmethod
    def decode(cls, line) -> None:
        """Remove backslash escaping from line.value."""
        ...
    @classmethod
    def encode(cls, line) -> None:
        """Backslash escape line.value."""
        ...

class VCalendarComponentBehavior(Behavior):
    defaultBehavior: Any
    isComponent: bool

class RecurringBehavior(VCalendarComponentBehavior):
    """Parent Behavior for components which should be RecurringComponents."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Turn a recurring Component into a RecurringComponent."""
        ...
    @staticmethod
    def transformFromNative(obj): ...
    @staticmethod
    def generateImplicitParameters(obj) -> None:
        """
        Generate a UID and DTSTAMP if one does not exist.

        This is just a dummy implementation, for now.
        """
        ...

class DateTimeBehavior(Behavior):
    """Parent Behavior for ContentLines containing one DATE-TIME."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """
        Turn obj.value into a datetime.

        RFC2445 allows times without time zone information, "floating times"
        in some properties.  Mostly, this isn't what you want, but when parsing
        a file, real floating times are noted by setting to 'TRUE' the
        X-VOBJ-FLOATINGTIME-ALLOWED parameter.
        """
        ...
    @classmethod
    def transformFromNative(cls, obj):
        """Replace the datetime in obj.value with an ISO 8601 string."""
        ...

class UTCDateTimeBehavior(DateTimeBehavior):
    """A value which must be specified in UTC."""
    forceUTC: bool

class DateOrDateTimeBehavior(Behavior):
    """Parent Behavior for ContentLines containing one DATE or DATE-TIME."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Turn obj.value into a date or datetime."""
        ...
    @staticmethod
    def transformFromNative(obj):
        """Replace the date or datetime in obj.value with an ISO 8601 string."""
        ...

class MultiDateBehavior(Behavior):
    """
    Parent Behavior for ContentLines containing one or more DATE, DATE-TIME, or
    PERIOD.
    """
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """
        Turn obj.value into a list of dates, datetimes, or
        (datetime, timedelta) tuples.
        """
        ...
    @staticmethod
    def transformFromNative(obj):
        """
        Replace the date, datetime or period tuples in obj.value with
        appropriate strings.
        """
        ...

class MultiTextBehavior(Behavior):
    """
    Provide backslash escape encoding/decoding of each of several values.

    After transformation, value is a list of strings.
    """
    listSeparator: str
    @classmethod
    def decode(cls, line) -> None:
        """Remove backslash escaping from line.value, then split on commas."""
        ...
    @classmethod
    def encode(cls, line) -> None:
        """Backslash escape line.value."""
        ...

class SemicolonMultiTextBehavior(MultiTextBehavior):
    listSeparator: str

class VCalendar2_0(VCalendarComponentBehavior):
    """vCalendar 2.0 behavior. With added VAVAILABILITY support."""
    name: str
    description: str
    versionString: str
    sortFirst: Any
    knownChildren: Any
    @classmethod
    def generateImplicitParameters(cls, obj) -> None:
        """
        Create PRODID, VERSION and VTIMEZONEs if needed.

        VTIMEZONEs will need to exist whenever TZID parameters exist or when
        datetimes with tzinfo exist.
        """
        ...
    @classmethod
    def serialize(cls, obj, buf, lineLength, validate: bool = True):
        """
        Set implicit parameters, do encoding, return unicode string.

        If validate is True, raise VObjectError if the line doesn't validate
        after implicit parameters are generated.

        Default is to call base.defaultSerialize.
        """
        ...

class VTimezone(VCalendarComponentBehavior):
    """Timezone behavior."""
    name: str
    hasNative: bool
    description: str
    sortFirst: Any
    knownChildren: Any
    @classmethod
    def validate(cls, obj, raiseException, *args): ...
    @staticmethod
    def transformToNative(obj): ...
    @staticmethod
    def transformFromNative(obj): ...

class TZID(Behavior):
    """
    Don't use TextBehavior for TZID.

    RFC2445 only allows TZID lines to be paramtext, so they shouldn't need any
    encoding or decoding.  Unfortunately, some Microsoft products use commas
    in TZIDs which should NOT be treated as a multi-valued text property, nor
    do we want to escape them.  Leaving them alone works for Microsoft's breakage,
    and doesn't affect compliant iCalendar streams.
    """
    ...

class DaylightOrStandard(VCalendarComponentBehavior):
    hasNative: bool
    knownChildren: Any

class VEvent(RecurringBehavior):
    """Event behavior."""
    name: str
    sortFirst: Any
    description: str
    knownChildren: Any
    @classmethod
    def validate(cls, obj, raiseException, *args): ...

class VTodo(RecurringBehavior):
    """To-do behavior."""
    name: str
    description: str
    knownChildren: Any
    @classmethod
    def validate(cls, obj, raiseException, *args): ...

class VJournal(RecurringBehavior):
    """Journal entry behavior."""
    name: str
    knownChildren: Any

class VFreeBusy(VCalendarComponentBehavior):
    """Free/busy state behavior."""
    name: str
    description: str
    sortFirst: Any
    knownChildren: Any

class VAlarm(VCalendarComponentBehavior):
    """Alarm behavior."""
    name: str
    description: str
    knownChildren: Any
    @staticmethod
    def generateImplicitParameters(obj) -> None:
        """Create default ACTION and TRIGGER if they're not set."""
        ...
    @classmethod
    def validate(cls, obj, raiseException, *args):
        """
        # TODO
        if obj.contents.has_key('dtend') and obj.contents.has_key('duration'):
            if raiseException:
                m = "VEVENT components cannot contain both DTEND and DURATION                     components"
                raise ValidateError(m)
            return False
        else:
            return super(VEvent, cls).validate(obj, raiseException, *args)
        """
        ...

class VAvailability(VCalendarComponentBehavior):
    """
    Availability state behavior.

    Used to represent user's available time slots.
    """
    name: str
    description: str
    sortFirst: Any
    knownChildren: Any
    @classmethod
    def validate(cls, obj, raiseException, *args): ...

class Available(RecurringBehavior):
    """Event behavior."""
    name: str
    sortFirst: Any
    description: str
    knownChildren: Any
    @classmethod
    def validate(cls, obj, raiseException, *args): ...

class Duration(Behavior):
    """Behavior for Duration ContentLines.  Transform to datetime.timedelta."""
    name: str
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Turn obj.value into a datetime.timedelta."""
        ...
    @staticmethod
    def transformFromNative(obj):
        """Replace the datetime.timedelta in obj.value with an RFC2445 string."""
        ...

class Trigger(Behavior):
    """DATE-TIME or DURATION"""
    name: str
    description: str
    hasNative: bool
    forceUTC: bool
    @staticmethod
    def transformToNative(obj):
        """Turn obj.value into a timedelta or datetime."""
        ...
    @staticmethod
    def transformFromNative(obj): ...

class PeriodBehavior(Behavior):
    """A list of (date-time, timedelta) tuples."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Convert comma separated periods into tuples."""
        ...
    @classmethod
    def transformFromNative(cls, obj):
        """Convert the list of tuples in obj.value to strings."""
        ...

class FreeBusy(PeriodBehavior):
    """Free or busy period of time, must be specified in UTC."""
    name: str
    forceUTC: bool

class RRule(Behavior):
    """
    Dummy behavior to avoid having RRULEs being treated as text lines (and thus
    having semi-colons inaccurately escaped).
    """
    ...

utcDateTimeList: Any
dateTimeOrDateList: Any
textList: Any

def numToDigits(num, places):
    """Helper, for converting numbers to textual digits."""
    ...
def timedeltaToString(delta):
    """Convert timedelta to an ical DURATION."""
    ...
def timeToString(dateOrDateTime):
    """
    Wraps dateToString and dateTimeToString, returning the results
    of either based on the type of the argument
    """
    ...
def dateToString(date): ...
def dateTimeToString(dateTime, convertToUTC: bool = False):
    """Ignore tzinfo unless convertToUTC.  Output string."""
    ...
def deltaToOffset(delta): ...
def periodToString(period, convertToUTC: bool = False): ...
def isDuration(s): ...
def stringToDate(s): ...
def stringToDateTime(s, tzinfo: Incomplete | None = None):
    """Returns datetime.datetime object."""
    ...

escapableCharList: str

def stringToTextValues(s, listSeparator: str = ",", charList: Incomplete | None = None, strict: bool = False):
    """Returns list of strings."""
    ...
def stringToDurations(s, strict: bool = False):
    """Returns list of timedelta objects."""
    ...
def parseDtstart(contentline, allowSignatureMismatch: bool = False):
    """
    Convert a contentline's value into a date or date-time.

    A variety of clients don't serialize dates with the appropriate VALUE
    parameter, so rather than failing on these (technically invalid) lines,
    if allowSignatureMismatch is True, try to parse both varieties.
    """
    ...
def stringToPeriod(s, tzinfo: Incomplete | None = None): ...
def getTransition(transitionTo, year, tzinfo):
    """Return the datetime of the transition to/from DST, or None."""
    ...
def tzinfo_eq(tzinfo1, tzinfo2, startYear: int = 2000, endYear: int = 2020):
    """Compare offsets and DST transitions from startYear to endYear."""
    ...
