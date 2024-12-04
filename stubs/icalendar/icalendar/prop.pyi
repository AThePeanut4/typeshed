"""
This module contains the parser/generators (or coders/encoders if you
prefer) for the classes/datatypes that are used in iCalendar:

###########################################################################

# This module defines these property value data types and property parameters

4.2 Defined property parameters are:

.. code-block:: text

     ALTREP, CN, CUTYPE, DELEGATED-FROM, DELEGATED-TO, DIR, ENCODING, FMTTYPE,
     FBTYPE, LANGUAGE, MEMBER, PARTSTAT, RANGE, RELATED, RELTYPE, ROLE, RSVP,
     SENT-BY, TZID, VALUE

4.3 Defined value data types are:

.. code-block:: text

    BINARY, BOOLEAN, CAL-ADDRESS, DATE, DATE-TIME, DURATION, FLOAT, INTEGER,
    PERIOD, RECUR, TEXT, TIME, URI, UTC-OFFSET

###########################################################################

iCalendar properties have values. The values are strongly typed. This module
defines these types, calling val.to_ical() on them will render them as defined
in rfc5545.

If you pass any of these classes a Python primitive, you will have an object
that can render itself as iCalendar formatted date.

Property Value Data Types start with a 'v'. they all have an to_ical() and
from_ical() method. The to_ical() method generates a text string in the
iCalendar format. The from_ical() method can parse this format and return a
primitive Python datatype. So it should always be true that:

.. code-block:: python

    x == vDataType.from_ical(VDataType(x).to_ical())

These types are mainly used for parsing and file generation. But you can set
them directly.
"""

import datetime
from _typeshed import Incomplete, Unused
from collections.abc import Iterator
from enum import Enum
from re import Pattern
from typing import Any, ClassVar, Final, TypeVar, overload
from typing_extensions import Self, TypeAlias

from .caselessdict import CaselessDict
from .parser import Parameters
from .parser_tools import ICAL_TYPE
from .timezone import tzid_from_dt as tzid_from_dt, tzid_from_tzinfo as tzid_from_tzinfo

__all__ = [
    "DURATION_REGEX",
    "TimeBase",
    "TypesFactory",
    "WEEKDAY_RULE",
    "vBinary",
    "vBoolean",
    "vCalAddress",
    "vCategory",
    "vDDDLists",
    "vDDDTypes",
    "vDate",
    "vDatetime",
    "vDuration",
    "vFloat",
    "vFrequency",
    "vGeo",
    "vInline",
    "vInt",
    "vMonth",
    "vPeriod",
    "vRecur",
    "vSkip",
    "vText",
    "vTime",
    "vUTCOffset",
    "vUri",
    "vWeekday",
    "tzid_from_dt",
    "tzid_from_tzinfo",
]

_PropType: TypeAlias = type[Any]  # any of the v* classes in this file
_vRecurT = TypeVar("_vRecurT", bound=vRecur)

DURATION_REGEX: Final[Pattern[str]]
WEEKDAY_RULE: Final[Pattern[str]]

class vBinary:
    """
    Binary property values are base 64 encoded.
    
    """
    obj: Incomplete
    params: Parameters
    def __init__(self, obj) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical): ...
    def __eq__(self, other):
        """self == other"""
        ...

class vBoolean(int):
    """
    Boolean

    Value Name:  BOOLEAN

    Purpose:  This value type is used to identify properties that contain
      either a "TRUE" or "FALSE" Boolean value.

    Format Definition:  This value type is defined by the following
      notation:

    .. code-block:: text

        boolean    = "TRUE" / "FALSE"

    Description:  These values are case-insensitive text.  No additional
      content value encoding is defined for this value type.

    Example:  The following is an example of a hypothetical property that
      has a BOOLEAN value type:

    .. code-block:: python

        TRUE

    .. code-block:: pycon

        >>> from icalendar.prop import vBoolean
        >>> boolean = vBoolean.from_ical('TRUE')
        >>> boolean
        True
        >>> boolean = vBoolean.from_ical('FALSE')
        >>> boolean
        False
        >>> boolean = vBoolean.from_ical('True')
        >>> boolean
        True
    """
    BOOL_MAP: Incomplete
    params: Parameters
    def __new__(cls, *args, **kwargs): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class vText(str):
    """
    Simple text.
    
    """
    encoding: str
    params: Parameters
    def __new__(cls, value: ICAL_TYPE, encoding: str = "utf-8") -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class vCalAddress(str):
    """
    Calendar User Address

    Value Name:
        CAL-ADDRESS

    Purpose:
        This value type is used to identify properties that contain a
        calendar user address.

    Format Definition:
        This value type is defined by the following notation:

    .. code-block:: text

        cal-address        = uri

    Description:
        The value is a URI as defined by [RFC3986] or any other
        IANA-registered form for a URI.  When used to address an Internet
        email transport address for a calendar user, the value MUST be a
        mailto URI, as defined by [RFC2368].

    Example:

    .. code-block:: text

        mailto:jane_doe@example.com
    
    .. code-block:: pycon

        >>> from icalendar.prop import vCalAddress
        >>> cal_address = vCalAddress.from_ical('mailto:jane_doe@example.com')
        >>> cal_address
        vCalAddress('mailto:jane_doe@example.com')

  
    """
    params: Parameters
    def __new__(cls, value, encoding="utf-8"): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class vFloat(float):
    """
    Float

    Value Name:
        FLOAT

    Purpose:
        This value type is used to identify properties that contain
        a real-number value.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            float      = (["+"] / "-") 1*DIGIT ["." 1*DIGIT]

    Description:
        If the property permits, multiple "float" values are
        specified by a COMMA-separated list of values.

        Example:

        .. code-block:: text

            1000000.0000001
            1.333
            -3.14
    
        .. code-block:: pycon

            >>> from icalendar.prop import vFloat
            >>> float = vFloat.from_ical('1000000.0000001')
            >>> float
            1000000.0000001
            >>> float = vFloat.from_ical('1.333')
            >>> float
            1.333
            >>> float = vFloat.from_ical('+1.333')
            >>> float
            1.333
            >>> float = vFloat.from_ical('-3.14')
            >>> float
            -3.14
    """
    params: Parameters
    def __new__(cls, *args, **kwargs): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class vInt(int):
    """
    Integer

    Value Name:
        INTEGER

    Purpose:
        This value type is used to identify properties that contain a
        signed integer value.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            integer    = (["+"] / "-") 1*DIGIT

    Description:
        If the property permits, multiple "integer" values are
        specified by a COMMA-separated list of values.  The valid range
        for "integer" is -2147483648 to 2147483647.  If the sign is not
        specified, then the value is assumed to be positive.

        Example:

        .. code-block:: text

            1234567890
            -1234567890
            +1234567890
            432109876

        .. code-block:: pycon

            >>> from icalendar.prop import vInt
            >>> integer = vInt.from_ical('1234567890')
            >>> integer
            1234567890
            >>> integer = vInt.from_ical('-1234567890')
            >>> integer
            -1234567890
            >>> integer = vInt.from_ical('+1234567890')
            >>> integer
            1234567890
            >>> integer = vInt.from_ical('432109876')
            >>> integer
            432109876
    """
    params: Parameters
    def __new__(cls, *args, **kwargs): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class vDDDLists:
    """
    A list of vDDDTypes values.
    
    """
    params: Parameters
    dts: Incomplete
    def __init__(self, dt_list) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical, timezone: Incomplete | None = None): ...
    def __eq__(self, other): ...

class vCategory:
    cats: Incomplete
    params: Parameters
    def __init__(self, c_list) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: ICAL_TYPE) -> str: ...
    def __eq__(self, other: object) -> bool:
        """self == other"""
        ...

class TimeBase:
    """Make classes with a datetime/date comparable."""
    def __eq__(self, other: object) -> bool:
        """self == other"""
        ...
    def __hash__(self): ...

class vDDDTypes(TimeBase):
    """
    A combined Datetime, Date or Duration parser/generator. Their format
    cannot be confused, and often values can be of either types.
    So this is practical.
    """
    params: Parameters
    dt: Incomplete
    def __init__(self, dt) -> None: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical, timezone: Incomplete | None = None): ...

class vDate(TimeBase):
    """
    Date

    Value Name:
        DATE

    Purpose:
        This value type is used to identify values that contain a
        calendar date.
  
    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            date               = date-value

            date-value         = date-fullyear date-month date-mday
            date-fullyear      = 4DIGIT
            date-month         = 2DIGIT        ;01-12
            date-mday          = 2DIGIT        ;01-28, 01-29, 01-30, 01-31
                                               ;based on month/year

    Description:
        If the property permits, multiple "date" values are
        specified as a COMMA-separated list of values.  The format for the
        value type is based on the [ISO.8601.2004] complete
        representation, basic format for a calendar date.  The textual
        format specifies a four-digit year, two-digit month, and two-digit
        day of the month.  There are no separator characters between the
        year, month, and day component text.

    Example:
        The following represents July 14, 1997:

        .. code-block:: text

            19970714

        .. code-block:: pycon

            >>> from icalendar.prop import vDate
            >>> date = vDate.from_ical('19970714')
            >>> date.year
            1997
            >>> date.month
            7
            >>> date.day
            14
    """
    dt: Incomplete
    params: Parameters
    def __init__(self, dt) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical): ...

class vDatetime(TimeBase):
    """
    Render and generates icalendar datetime format.

    vDatetime is timezone aware and uses a timezone library.
    When a vDatetime object is created from an
    ical string, you can pass a valid timezone identifier. When a
    vDatetime object is created from a python datetime object, it uses the
    tzinfo component, if present. Otherwise a timezone-naive object is
    created. Be aware that there are certain limitations with timezone naive
    DATE-TIME components in the icalendar standard.
    """
    dt: Incomplete
    params: Parameters
    def __init__(self, dt) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical, timezone: datetime.timezone | str | None = None) -> datetime.datetime:
        """
        Create a datetime from the RFC string.

        Format:

        .. code-block:: text

            YYYYMMDDTHHMMSS

        .. code-block:: pycon

            >>> from icalendar import vDatetime
            >>> vDatetime.from_ical("20210302T101500")
            datetime.datetime(2021, 3, 2, 10, 15)

            >>> vDatetime.from_ical("20210302T101500", "America/New_York")
            datetime.datetime(2021, 3, 2, 10, 15, tzinfo=ZoneInfo(key='America/New_York'))

            >>> from zoneinfo import ZoneInfo
            >>> timezone = ZoneInfo("Europe/Berlin")
            >>> vDatetime.from_ical("20210302T101500", timezone)
            datetime.datetime(2021, 3, 2, 10, 15, tzinfo=ZoneInfo(key='Europe/Berlin'))
        """
        ...

class vDuration(TimeBase):
    """
    Duration

    Value Name:
        DURATION

    Purpose:
        This value type is used to identify properties that contain
        a duration of time.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            dur-value  = (["+"] / "-") "P" (dur-date / dur-time / dur-week)

            dur-date   = dur-day [dur-time]
            dur-time   = "T" (dur-hour / dur-minute / dur-second)
            dur-week   = 1*DIGIT "W"
            dur-hour   = 1*DIGIT "H" [dur-minute]
            dur-minute = 1*DIGIT "M" [dur-second]
            dur-second = 1*DIGIT "S"
            dur-day    = 1*DIGIT "D"

    Description:
        If the property permits, multiple "duration" values are
        specified by a COMMA-separated list of values.  The format is
        based on the [ISO.8601.2004] complete representation basic format
        with designators for the duration of time.  The format can
        represent nominal durations (weeks and days) and accurate
        durations (hours, minutes, and seconds).  Note that unlike
        [ISO.8601.2004], this value type doesn't support the "Y" and "M"
        designators to specify durations in terms of years and months.
        The duration of a week or a day depends on its position in the
        calendar.  In the case of discontinuities in the time scale, such
        as the change from standard time to daylight time and back, the
        computation of the exact duration requires the subtraction or
        addition of the change of duration of the discontinuity.  Leap
        seconds MUST NOT be considered when computing an exact duration.
        When computing an exact duration, the greatest order time
        components MUST be added first, that is, the number of days MUST
        be added first, followed by the number of hours, number of
        minutes, and number of seconds.
  
    Example:
        A duration of 15 days, 5 hours, and 20 seconds would be:

        .. code-block:: text

            P15DT5H0M20S

        A duration of 7 weeks would be:

        .. code-block:: text

            P7W
    
        .. code-block:: pycon

            >>> from icalendar.prop import vDuration
            >>> duration = vDuration.from_ical('P15DT5H0M20S')
            >>> duration
            datetime.timedelta(days=15, seconds=18020)
            >>> duration = vDuration.from_ical('P7W')
            >>> duration
            datetime.timedelta(days=49)
    """
    td: Incomplete
    params: Parameters
    def __init__(self, td) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical): ...
    @property
    def dt(self):
        """The time delta for compatibility."""
        ...

class vPeriod(TimeBase):
    """
    Period of Time

    Value Name:
        PERIOD

    Purpose:
        This value type is used to identify values that contain a
        precise period of time.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            period     = period-explicit / period-start

           period-explicit = date-time "/" date-time
           ; [ISO.8601.2004] complete representation basic format for a
           ; period of time consisting of a start and end.  The start MUST
           ; be before the end.

           period-start = date-time "/" dur-value
           ; [ISO.8601.2004] complete representation basic format for a
           ; period of time consisting of a start and positive duration
           ; of time.
   
    Description:
        If the property permits, multiple "period" values are
        specified by a COMMA-separated list of values.  There are two
        forms of a period of time.  First, a period of time is identified
        by its start and its end.  This format is based on the
        [ISO.8601.2004] complete representation, basic format for "DATE-
        TIME" start of the period, followed by a SOLIDUS character
        followed by the "DATE-TIME" of the end of the period.  The start
        of the period MUST be before the end of the period.  Second, a
        period of time can also be defined by a start and a positive
        duration of time.  The format is based on the [ISO.8601.2004]
        complete representation, basic format for the "DATE-TIME" start of
        the period, followed by a SOLIDUS character, followed by the
        [ISO.8601.2004] basic format for "DURATION" of the period.

    Example:
        The period starting at 18:00:00 UTC, on January 1, 1997 and
        ending at 07:00:00 UTC on January 2, 1997 would be:

        .. code-block:: text

            19970101T180000Z/19970102T070000Z

        The period start at 18:00:00 on January 1, 1997 and lasting 5 hours
        and 30 minutes would be:

        .. code-block:: text

            19970101T180000Z/PT5H30M
   
        .. code-block:: pycon

            >>> from icalendar.prop import vPeriod
            >>> period = vPeriod.from_ical('19970101T180000Z/19970102T070000Z')
            >>> period = vPeriod.from_ical('19970101T180000Z/PT5H30M')
    """
    params: Parameters
    start: Incomplete
    end: Incomplete
    by_duration: Incomplete
    duration: Incomplete
    def __init__(self, per) -> None: ...
    def overlaps(self, other): ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical, timezone: Incomplete | None = None): ...
    @property
    def dt(self):
        """Make this cooperate with the other vDDDTypes."""
        ...

class vWeekday(str):
    """
    This returns an unquoted weekday abbrevation.
    
    """
    week_days: Incomplete
    relative: Incomplete
    params: Parameters
    def __new__(cls, value, encoding="utf-8"): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class vFrequency(str):
    """
    A simple class that catches illegal values.
    
    """
    frequencies: Incomplete
    params: Parameters
    def __new__(cls, value, encoding="utf-8"): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class vMonth(int):
    """
    The number of the month for recurrence.

    In :rfc:`5545`, this is just an int.
    In :rfc:`7529`, this can be followed by `L` to indicate a leap month.

    .. code-block:: pycon

        >>> from icalendar import vMonth
        >>> vMonth(1) # first month January
        vMonth('1')
        >>> vMonth("5L") # leap month in Hebrew calendar
        vMonth('5L')
        >>> vMonth(1).leap
        False
        >>> vMonth("5L").leap
        True

    Definition from RFC:

    .. code-block:: text

        type-bymonth = element bymonth {
           xsd:positiveInteger |
           xsd:string
        }
    """
    leap: bool
    params: Parameters
    def __new__(cls, month: vMonth | str | int) -> Self: ...
    def to_ical(self) -> bytes:
        """The ical representation."""
        ...
    @classmethod
    def from_ical(cls, ical: vMonth | str | int) -> Self: ...

class vSkip(vText, Enum):
    """
    Skip values for RRULE.

    These are defined in :rfc:`7529`.

    OMIT  is the default value.
    """
    OMIT = "OMIT"
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"

    def __reduce_ex__(self, proto: Unused) -> tuple[Any, ...]:
        """For pickling."""
        ...

class vRecur(CaselessDict[Incomplete]):
    """
    Recurrence definition.
    
    """
    frequencies: ClassVar[list[str]]
    canonical_order: ClassVar[tuple[str, ...]]
    types: ClassVar[CaselessDict[_PropType]]
    params: Parameters
    def __init__(self, *args, **kwargs) -> None: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def parse_type(cls, key, values): ...
    @classmethod
    @overload
    def from_ical(cls, ical: _vRecurT) -> _vRecurT: ...
    @classmethod
    @overload
    def from_ical(cls, ical: str) -> Self: ...

class vTime(TimeBase):
    """
    Time

    Value Name:
        TIME

    Purpose:
        This value type is used to identify values that contain a
        time of day.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            time         = time-hour time-minute time-second [time-utc]

            time-hour    = 2DIGIT        ;00-23
            time-minute  = 2DIGIT        ;00-59
            time-second  = 2DIGIT        ;00-60
            ;The "60" value is used to account for positive "leap" seconds.

            time-utc     = "Z"

    Description:
        If the property permits, multiple "time" values are
        specified by a COMMA-separated list of values.  No additional
        content value encoding (i.e., BACKSLASH character encoding, see
        vText) is defined for this value type.

        The "TIME" value type is used to identify values that contain a
        time of day.  The format is based on the [ISO.8601.2004] complete
        representation, basic format for a time of day.  The text format
        consists of a two-digit, 24-hour of the day (i.e., values 00-23),
        two-digit minute in the hour (i.e., values 00-59), and two-digit
        seconds in the minute (i.e., values 00-60).  The seconds value of
        60 MUST only be used to account for positive "leap" seconds.
        Fractions of a second are not supported by this format.

        In parallel to the "DATE-TIME" definition above, the "TIME" value
        type expresses time values in three forms:

        The form of time with UTC offset MUST NOT be used.  For example,
        the following is not valid for a time value:

        .. code-block:: text

            230000-0800        ;Invalid time format

        **FORM #1 LOCAL TIME**

        The local time form is simply a time value that does not contain
        the UTC designator nor does it reference a time zone.  For
        example, 11:00 PM:

        .. code-block:: text

            230000

        Time values of this type are said to be "floating" and are not
        bound to any time zone in particular.  They are used to represent
        the same hour, minute, and second value regardless of which time
        zone is currently being observed.  For example, an event can be
        defined that indicates that an individual will be busy from 11:00
        AM to 1:00 PM every day, no matter which time zone the person is
        in.  In these cases, a local time can be specified.  The recipient
        of an iCalendar object with a property value consisting of a local
        time, without any relative time zone information, SHOULD interpret
        the value as being fixed to whatever time zone the "ATTENDEE" is
        in at any given moment.  This means that two "Attendees", may
        participate in the same event at different UTC times; floating
        time SHOULD only be used where that is reasonable behavior.

        In most cases, a fixed time is desired.  To properly communicate a
        fixed time in a property value, either UTC time or local time with
        time zone reference MUST be specified.

        The use of local time in a TIME value without the "TZID" property
        parameter is to be interpreted as floating time, regardless of the
        existence of "VTIMEZONE" calendar components in the iCalendar
        object.

        **FORM #2: UTC TIME**

        UTC time, or absolute time, is identified by a LATIN CAPITAL
        LETTER Z suffix character, the UTC designator, appended to the
        time value.  For example, the following represents 07:00 AM UTC:

        .. code-block:: text

            070000Z

        The "TZID" property parameter MUST NOT be applied to TIME
        properties whose time values are specified in UTC.

        **FORM #3: LOCAL TIME AND TIME ZONE REFERENCE**

        The local time with reference to time zone information form is
        identified by the use the "TZID" property parameter to reference
        the appropriate time zone definition.

        Example:
            The following represents 8:30 AM in New York in winter,
            five hours behind UTC, in each of the three formats:

        .. code-block:: text

            083000
            133000Z
            TZID=America/New_York:083000
    """
    dt: Incomplete
    params: Parameters
    def __init__(self, *args) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical): ...

class vUri(str):
    """
    URI

    Value Name:
        URI

    Purpose:
        This value type is used to identify values that contain a
        uniform resource identifier (URI) type of reference to the
        property value.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            uri = scheme ":" hier-part [ "?" query ] [ "#" fragment ]

    Description:
        This value type might be used to reference binary
        information, for values that are large, or otherwise undesirable
        to include directly in the iCalendar object.

        Property values with this value type MUST follow the generic URI
        syntax defined in [RFC3986].

        When a property parameter value is a URI value type, the URI MUST
        be specified as a quoted-string value.

        Example:
            The following is a URI for a network file:

            .. code-block:: text

                http://example.com/my-report.txt

            .. code-block:: pycon

                >>> from icalendar.prop import vUri
                >>> uri = vUri.from_ical('http://example.com/my-report.txt')
                >>> uri
                'http://example.com/my-report.txt'
    """
    params: Parameters
    def __new__(cls, value, encoding="utf-8"): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class vGeo:
    """
    Geographic Position

    Property Name:
        GEO

    Purpose:
        This property specifies information related to the global
        position for the activity specified by a calendar component.

    Value Type:
        FLOAT.  The value MUST be two SEMICOLON-separated FLOAT values.

    Property Parameters:
        IANA and non-standard property parameters can be specified on
        this property.

    Conformance:
        This property can be specified in "VEVENT" or "VTODO"
        calendar components.

    Description:
        This property value specifies latitude and longitude,
        in that order (i.e., "LAT LON" ordering).  The longitude
        represents the location east or west of the prime meridian as a
        positive or negative real number, respectively.  The longitude and
        latitude values MAY be specified up to six decimal places, which
        will allow for accuracy to within one meter of geographical
        position.  Receiving applications MUST accept values of this
        precision and MAY truncate values of greater precision.

        Example:

        .. code-block:: text

            GEO:37.386013;-122.082932

        .. code-block:: pycon

            >>> from icalendar.prop import vGeo
            >>> geo = vGeo.from_ical('37.386013;-122.082932')
            >>> geo
            (37.386013, -122.082932)
    """
    latitude: Incomplete
    longitude: Incomplete
    params: Parameters
    def __init__(self, geo) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical): ...
    def __eq__(self, other): ...

class vUTCOffset:
    """
    UTC Offset

    Value Name:
        UTC-OFFSET

    Purpose:
        This value type is used to identify properties that contain
        an offset from UTC to local time.

    Format Definition:
        This value type is defined by the following notation:

        .. code-block:: text

            utc-offset = time-numzone

            time-numzone = ("+" / "-") time-hour time-minute [time-second]

    Description:
        The PLUS SIGN character MUST be specified for positive
        UTC offsets (i.e., ahead of UTC).  The HYPHEN-MINUS character MUST
        be specified for negative UTC offsets (i.e., behind of UTC).  The
        value of "-0000" and "-000000" are not allowed.  The time-second,
        if present, MUST NOT be 60; if absent, it defaults to zero.

        Example:
            The following UTC offsets are given for standard time for
            New York (five hours behind UTC) and Geneva (one hour ahead of
            UTC):

        .. code-block:: text

            -0500

            +0100

        .. code-block:: pycon

            >>> from icalendar.prop import vUTCOffset
            >>> utc_offset = vUTCOffset.from_ical('-0500')
            >>> utc_offset
            datetime.timedelta(days=-1, seconds=68400)
            >>> utc_offset = vUTCOffset.from_ical('+0100')
            >>> utc_offset
            datetime.timedelta(seconds=3600)
    """
    ignore_exceptions: bool
    td: datetime.timedelta
    params: Parameters
    def __init__(self, td: datetime.timedelta) -> None: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class vInline(str):
    """
    This is an especially dumb class that just holds raw unparsed text and
    has parameters. Conversion of inline values are handled by the Component
    class, so no further processing is needed.
    """
    params: Parameters
    def __new__(cls, value, encoding="utf-8"): ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical): ...

class TypesFactory(CaselessDict[_PropType]):
    """
    All Value types defined in RFC 5545 are registered in this factory
    class.

    The value and parameter names don't overlap. So one factory is enough for
    both kinds.
    """
    all_types: tuple[_PropType, ...]
    def __init__(self, *args, **kwargs) -> None:
        """Set keys to upper for initial dict"""
        ...
    types_map: CaselessDict[str]
    def for_property(self, name: str) -> _PropType:
        """
        Returns a the default type for a property or parameter
        
        """
        ...
    def to_ical(self, name: str, value) -> bytes:
        """
        Encodes a named value from a primitive python type to an icalendar
        encoded string.
        """
        ...
    def from_ical(self, name: str, value):
        """
        Decodes a named property or parameter value from an icalendar
        encoded string to a primitive python type.
        """
        ...
