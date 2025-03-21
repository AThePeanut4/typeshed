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
from _typeshed import ConvertibleToFloat, ConvertibleToInt, SupportsKeysAndGetItem, Unused
from collections.abc import Iterable, Iterator
from enum import Enum
from re import Pattern
from typing import Any, ClassVar, Final, Literal, Protocol, SupportsIndex, overload
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
_PeriodTuple: TypeAlias = tuple[datetime.datetime, datetime.datetime | datetime.timedelta]
_AnyTimeType: TypeAlias = datetime.datetime | datetime.date | datetime.timedelta | datetime.time | _PeriodTuple

class _vType(Protocol):
    def to_ical(self) -> bytes | str: ...

DURATION_REGEX: Final[Pattern[str]]
WEEKDAY_RULE: Final[Pattern[str]]

class vBinary:
    obj: str
    params: Parameters
    def __init__(self, obj: str | bytes) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: ICAL_TYPE) -> bytes: ...
    def __eq__(self, other: object) -> bool: ...

class vBoolean(int):
    BOOL_MAP: Final[CaselessDict[bool]]
    params: Parameters
    def __new__(cls, x: ConvertibleToInt = ..., /, *, params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> Literal[b"TRUE", b"FALSE"]: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> bool: ...

class vText(str):
    """
    Simple text.
    
    """
    encoding: str
    params: Parameters
    def __new__(cls, value: ICAL_TYPE, encoding: str = "utf-8", params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
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
    def __new__(cls, value: ICAL_TYPE, encoding="utf-8", params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...
    @property
    def email(self) -> str: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...

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
    def __new__(cls, x: ConvertibleToFloat = ..., /, *, params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

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
    def __new__(cls, x: ConvertibleToInt = ..., /, *, params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class vDDDLists:
    """
    A list of vDDDTypes values.
    
    """
    params: Parameters
    dts: list[vDDDTypes]
    def __init__(self, dt_list: Iterable[_AnyTimeType] | _AnyTimeType) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: str, timezone: str | datetime.timezone | None = None): ...
    def __eq__(self, other: object) -> bool: ...

class vCategory:
    cats: list[vText]
    params: Parameters
    def __init__(self, c_list: Iterable[ICAL_TYPE] | ICAL_TYPE, params: SupportsKeysAndGetItem[str, str] = {}) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: ICAL_TYPE) -> str: ...
    def __eq__(self, other: object) -> bool:
        """self == other"""
        ...

class TimeBase:
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class vDDDTypes(TimeBase):
    """
    A combined Datetime, Date or Duration parser/generator. Their format
    cannot be confused, and often values can be of either types.
    So this is practical.
    """
    params: Parameters
    dt: _AnyTimeType
    def __init__(self, dt: _AnyTimeType) -> None: ...
    def to_ical(self) -> bytes: ...
    @overload
    @classmethod
    def from_ical(cls, ical: Self, timezone: Unused | None = None) -> _AnyTimeType: ...
    # Return type is one of vDuration, vPeriod, vDatetime, vDate, or vTime,
    # depending on the ical string.
    @overload
    @classmethod
    def from_ical(cls, ical: str, timezone: datetime.timezone | str | None = None) -> Any: ...

class vDate(TimeBase):
    dt: datetime.date
    params: Parameters
    def __init__(self, dt: datetime.date) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: ICAL_TYPE) -> datetime.date: ...

class vDatetime(TimeBase):
    dt: datetime.datetime
    params: Parameters
    def __init__(self, dt: datetime.datetime, params: SupportsKeysAndGetItem[str, str] = {}) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: ICAL_TYPE, timezone: datetime.timezone | str | None = None) -> datetime.datetime: ...

class vDuration(TimeBase):
    td: datetime.timedelta
    params: Parameters
    def __init__(self, td: datetime.timedelta, params: SupportsKeysAndGetItem[str, str] = {}) -> None: ...
    def to_ical(self) -> bytes: ...
    @staticmethod
    def from_ical(ical: str) -> datetime.timedelta: ...
    @property
    def dt(self) -> datetime.timedelta: ...

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
    start: datetime.datetime
    end: datetime.datetime
    by_duration: bool
    duration: datetime.timedelta
    def __init__(self, per: _PeriodTuple) -> None: ...
    def overlaps(self, other: vPeriod) -> bool: ...
    def to_ical(self) -> bytes: ...
    # Return type is a tuple of vDuration, vPeriod, vDatetime, vDate, or vTime,
    # depending on the ical string. If the ical string is formed according to
    # the iCalendar specification, this should always return a
    # (datetime, datetime) or a (datetime, timedelta) tuple, but this is not
    # enforced.
    @staticmethod
    def from_ical(ical: str, timezone: datetime.timezone | str | None = None) -> tuple[Any, Any]: ...
    @property
    def dt(self) -> _PeriodTuple: ...

class vWeekday(str):
    week_days: Final[CaselessDict[int]]
    weekday: Literal["SU", "MO", "TU", "WE", "TH", "FR", "SA"] | None
    relative: int | None
    params: Parameters
    def __new__(cls, value: ICAL_TYPE, encoding: str = "utf-8", params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class vFrequency(str):
    frequencies: Final[CaselessDict[str]]
    params: Parameters
    def __new__(cls, value: ICAL_TYPE, encoding: str = "utf-8", params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class vMonth(int):
    params: Parameters
    def __new__(cls, month: vMonth | str | int, params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: vMonth | str | int) -> Self: ...
    @property
    def leap(self) -> bool: ...
    @leap.setter
    def leap(self, value: bool) -> None: ...

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

# The type of the values depend on the key. Each key maps to a v* class, and
# the allowed types are the types that the corresponding v* class can parse.
class vRecur(CaselessDict[Iterable[Any] | Any]):
    params: Parameters
    frequencies: Final[list[str]]
    canonical_order: ClassVar[tuple[str, ...]]
    types: Final[CaselessDict[_PropType]]
    def __init__(
        self, *args, params: SupportsKeysAndGetItem[str, str] = {}, **kwargs: list[Any] | tuple[Any, ...] | Any
    ) -> None: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def parse_type(cls, key: str, values: str) -> list[Any]: ...  # Returns a list of v* objects
    @classmethod
    def from_ical(cls, ical: vRecur | str) -> Self: ...

class vTime(TimeBase):
    dt: datetime.time | datetime.datetime
    params: Parameters
    @overload
    def __init__(self, dt: datetime.time | datetime.datetime, /) -> None: ...
    # args are passed to the datetime.time() constructor
    @overload
    def __init__(
        self,
        hour: SupportsIndex = ...,
        minute: SupportsIndex = ...,
        second: SupportsIndex = ...,
        microsecond: SupportsIndex = ...,
        tzinfo: datetime.tzinfo | None = ...,
        /,
    ) -> None: ...
    def to_ical(self) -> str: ...
    @staticmethod
    def from_ical(ical: ICAL_TYPE) -> datetime.time: ...

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
    def __new__(cls, value: ICAL_TYPE, encoding: str = "utf-8", params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class vGeo:
    latitude: float
    longitude: float
    params: Parameters
    def __init__(self, geo: tuple[float | str, float | str], params: SupportsKeysAndGetItem[str, str] = {}) -> None: ...
    def to_ical(self) -> str: ...
    @staticmethod
    def from_ical(ical: str) -> tuple[float, float]: ...
    def __eq__(self, other: _vType) -> bool: ...  # type: ignore[override]

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
    def __init__(self, td: datetime.timedelta, params: SupportsKeysAndGetItem[str, str] = {}) -> None: ...
    def to_ical(self) -> str: ...
    @classmethod
    def from_ical(cls, ical: Self | ICAL_TYPE) -> datetime.timedelta: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class vInline(str):
    """
    This is an especially dumb class that just holds raw unparsed text and
    has parameters. Conversion of inline values are handled by the Component
    class, so no further processing is needed.
    """
    params: Parameters
    def __new__(cls, value: ICAL_TYPE, encoding: str = "utf-8", params: SupportsKeysAndGetItem[str, str] = {}) -> Self: ...
    def to_ical(self) -> bytes: ...
    @classmethod
    def from_ical(cls, ical: ICAL_TYPE) -> Self: ...

class TypesFactory(CaselessDict[_PropType]):
    """
    All Value types defined in RFC 5545 are registered in this factory
    class.

    The value and parameter names don't overlap. So one factory is enough for
    both kinds.
    """
    all_types: tuple[_PropType, ...]
    types_map: CaselessDict[str]
    def for_property(self, name: str) -> _PropType: ...
    # value is str | bytes, depending on what the v* class supports
    def to_ical(self, name: str, value: Any) -> bytes: ...
    # value and return type depend on what the v* class supports
    def from_ical(self, name: str, value: Any) -> Any: ...
