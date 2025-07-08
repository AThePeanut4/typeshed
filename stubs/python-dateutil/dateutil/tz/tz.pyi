import sys
from datetime import datetime, timedelta, tzinfo
from typing import ClassVar, Literal, Protocol, TypeVar

from ..relativedelta import relativedelta
from ._common import _tzinfo, enfold as enfold, tzrangebase

if sys.platform == "win32":
    from .win import tzwin as tzwin, tzwinlocal as tzwinlocal
else:
    tzwin: None
    tzwinlocal: None

_DT = TypeVar("_DT", bound=datetime)

ZERO: timedelta
EPOCH: datetime
EPOCHORDINAL: int

class tzutc(tzinfo):
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def tzname(self, dt: datetime | None) -> str: ...
    def is_ambiguous(self, dt: datetime | None) -> bool: ...
    def fromutc(self, dt: _DT) -> _DT: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__

UTC: tzutc

class tzoffset(tzinfo):
    def __init__(self, name, offset) -> None: ...
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def is_ambiguous(self, dt: datetime | None) -> bool: ...
    def tzname(self, dt: datetime | None) -> str: ...
    def fromutc(self, dt: _DT) -> _DT: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__
    @classmethod
    def instance(cls, name, offset) -> tzoffset:
        """Alternate constructor that returns a fresh instance"""
        ...

class tzlocal(_tzinfo):
    """A :class:`tzinfo` subclass built around the ``time`` timezone functions."""
    def __init__(self) -> None: ...
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def tzname(self, dt: datetime | None) -> str: ...
    def is_ambiguous(self, dt: datetime | None) -> bool: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__

class _ttinfo:
    offset: float
    delta: timedelta
    isdst: bool
    abbr: str
    isstd: bool
    isgmt: bool
    dstoffset: timedelta
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...

class _TZFileReader(Protocol):
    # optional attribute:
    # name: str
    def read(self, size: int, /) -> bytes: ...
    def seek(self, target: int, whence: Literal[1], /) -> object: ...

class tzfile(_tzinfo):
    """
    This is a ``tzinfo`` subclass that allows one to use the ``tzfile(5)``
    format timezone files to extract current and historical zone information.

    :param fileobj:
        This can be an opened file stream or a file name that the time zone
        information can be read from.

    :param filename:
        This is an optional parameter specifying the source of the time zone
        information in the event that ``fileobj`` is a file object. If omitted
        and ``fileobj`` is a file stream, this parameter will be set either to
        ``fileobj``'s ``name`` attribute or to ``repr(fileobj)``.

    See `Sources for Time Zone and Daylight Saving Time Data
    <https://data.iana.org/time-zones/tz-link.html>`_ for more information.
    Time zone files can be compiled from the `IANA Time Zone database files
    <https://www.iana.org/time-zones>`_ with the `zic time zone compiler
    <https://www.freebsd.org/cgi/man.cgi?query=zic&sektion=8>`_

    .. note::

        Only construct a ``tzfile`` directly if you have a specific timezone
        file on disk that you want to read into a Python ``tzinfo`` object.
        If you want to get a ``tzfile`` representing a specific IANA zone,
        (e.g. ``'America/New_York'``), you should call
        :func:`dateutil.tz.gettz` with the zone identifier.


    **Examples:**

    Using the US Eastern time zone as an example, we can see that a ``tzfile``
    provides time zone information for the standard Daylight Saving offsets:

    .. testsetup:: tzfile

        from dateutil.tz import gettz
        from datetime import datetime

    .. doctest:: tzfile

        >>> NYC = gettz('America/New_York')
        >>> NYC
        tzfile('/usr/share/zoneinfo/America/New_York')

        >>> print(datetime(2016, 1, 3, tzinfo=NYC))     # EST
        2016-01-03 00:00:00-05:00

        >>> print(datetime(2016, 7, 7, tzinfo=NYC))     # EDT
        2016-07-07 00:00:00-04:00


    The ``tzfile`` structure contains a fully history of the time zone,
    so historical dates will also have the right offsets. For example, before
    the adoption of the UTC standards, New York used local solar  mean time:

    .. doctest:: tzfile

       >>> print(datetime(1901, 4, 12, tzinfo=NYC))    # LMT
       1901-04-12 00:00:00-04:56

    And during World War II, New York was on "Eastern War Time", which was a
    state of permanent daylight saving time:

    .. doctest:: tzfile

        >>> print(datetime(1944, 2, 7, tzinfo=NYC))    # EWT
        1944-02-07 00:00:00-04:00
    """
    def __init__(self, fileobj: str | _TZFileReader, filename: str | None = None) -> None: ...
    def is_ambiguous(self, dt: datetime | None, idx: int | None = None) -> bool: ...
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def tzname(self, dt: datetime | None) -> str: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    def __reduce__(self): ...
    def __reduce_ex__(self, protocol): ...

class tzrange(tzrangebase):
    """
    The ``tzrange`` object is a time zone specified by a set of offsets and
    abbreviations, equivalent to the way the ``TZ`` variable can be specified
    in POSIX-like systems, but using Python delta objects to specify DST
    start, end and offsets.

    :param stdabbr:
        The abbreviation for standard time (e.g. ``'EST'``).

    :param stdoffset:
        An integer or :class:`datetime.timedelta` object or equivalent
        specifying the base offset from UTC.

        If unspecified, +00:00 is used.

    :param dstabbr:
        The abbreviation for DST / "Summer" time (e.g. ``'EDT'``).

        If specified, with no other DST information, DST is assumed to occur
        and the default behavior or ``dstoffset``, ``start`` and ``end`` is
        used. If unspecified and no other DST information is specified, it
        is assumed that this zone has no DST.

        If this is unspecified and other DST information is *is* specified,
        DST occurs in the zone but the time zone abbreviation is left
        unchanged.

    :param dstoffset:
        A an integer or :class:`datetime.timedelta` object or equivalent
        specifying the UTC offset during DST. If unspecified and any other DST
        information is specified, it is assumed to be the STD offset +1 hour.

    :param start:
        A :class:`relativedelta.relativedelta` object or equivalent specifying
        the time and time of year that daylight savings time starts. To
        specify, for example, that DST starts at 2AM on the 2nd Sunday in
        March, pass:

            ``relativedelta(hours=2, month=3, day=1, weekday=SU(+2))``

        If unspecified and any other DST information is specified, the default
        value is 2 AM on the first Sunday in April.

    :param end:
        A :class:`relativedelta.relativedelta` object or equivalent
        representing the time and time of year that daylight savings time
        ends, with the same specification method as in ``start``. One note is
        that this should point to the first time in the *standard* zone, so if
        a transition occurs at 2AM in the DST zone and the clocks are set back
        1 hour to 1AM, set the ``hours`` parameter to +1.


    **Examples:**

    .. testsetup:: tzrange

        from dateutil.tz import tzrange, tzstr

    .. doctest:: tzrange

        >>> tzstr('EST5EDT') == tzrange("EST", -18000, "EDT")
        True

        >>> from dateutil.relativedelta import *
        >>> range1 = tzrange("EST", -18000, "EDT")
        >>> range2 = tzrange("EST", -18000, "EDT", -14400,
        ...                  relativedelta(hours=+2, month=4, day=1,
        ...                                weekday=SU(+1)),
        ...                  relativedelta(hours=+1, month=10, day=31,
        ...                                weekday=SU(-1)))
        >>> tzstr('EST5EDT') == range1 == range2
        True
    """
    hasdst: bool
    def __init__(
        self,
        stdabbr: str,
        stdoffset: int | timedelta | None = None,
        dstabbr: str | None = None,
        dstoffset: int | timedelta | None = None,
        start: relativedelta | None = None,
        end: relativedelta | None = None,
    ) -> None: ...
    def transitions(self, year: int) -> tuple[datetime, datetime]: ...
    def __eq__(self, other): ...

class tzstr(tzrange):
    """
    ``tzstr`` objects are time zone objects specified by a time-zone string as
    it would be passed to a ``TZ`` variable on POSIX-style systems (see
    the `GNU C Library: TZ Variable`_ for more details).

    There is one notable exception, which is that POSIX-style time zones use an
    inverted offset format, so normally ``GMT+3`` would be parsed as an offset
    3 hours *behind* GMT. The ``tzstr`` time zone object will parse this as an
    offset 3 hours *ahead* of GMT. If you would like to maintain the POSIX
    behavior, pass a ``True`` value to ``posix_offset``.

    The :class:`tzrange` object provides the same functionality, but is
    specified using :class:`relativedelta.relativedelta` objects. rather than
    strings.

    :param s:
        A time zone string in ``TZ`` variable format. This can be a
        :class:`bytes` (2.x: :class:`str`), :class:`str` (2.x:
        :class:`unicode`) or a stream emitting unicode characters
        (e.g. :class:`StringIO`).

    :param posix_offset:
        Optional. If set to ``True``, interpret strings such as ``GMT+3`` or
        ``UTC+3`` as being 3 hours *behind* UTC rather than ahead, per the
        POSIX standard.

    .. caution::

        Prior to version 2.7.0, this function also supported time zones
        in the format:

            * ``EST5EDT,4,0,6,7200,10,0,26,7200,3600``
            * ``EST5EDT,4,1,0,7200,10,-1,0,7200,3600``

        This format is non-standard and has been deprecated; this function
        will raise a :class:`DeprecatedTZFormatWarning` until
        support is removed in a future version.

    .. _`GNU C Library: TZ Variable`:
        https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html
    """
    hasdst: bool
    def __init__(self, s: str, posix_offset: bool = False) -> None: ...
    @classmethod
    def instance(cls, name, offset) -> tzoffset:
        """Alternate constructor that returns a fresh instance"""
        ...

class _ICalReader(Protocol):
    # optional attribute:
    # name: str
    def read(self) -> str: ...

class tzical:
    """
    This object is designed to parse an iCalendar-style ``VTIMEZONE`` structure
    as set out in `RFC 5545`_ Section 4.6.5 into one or more `tzinfo` objects.

    :param `fileobj`:
        A file or stream in iCalendar format, which should be UTF-8 encoded
        with CRLF endings.

    .. _`RFC 5545`: https://tools.ietf.org/html/rfc5545
    """
    def __init__(self, fileobj: str | _ICalReader) -> None: ...
    def keys(self):
        """Retrieves the available time zones as a list."""
        ...
    def get(self, tzid=None):
        """
        Retrieve a :py:class:`datetime.tzinfo` object by its ``tzid``.

        :param tzid:
            If there is exactly one time zone available, omitting ``tzid``
            or passing :py:const:`None` value returns it. Otherwise a valid
            key (which can be retrieved from :func:`keys`) is required.

        :raises ValueError:
            Raised if ``tzid`` is not specified but there are either more
            or fewer than 1 zone defined.

        :returns:
            Returns either a :py:class:`datetime.tzinfo` object representing
            the relevant time zone or :py:const:`None` if the ``tzid`` was
            not found.
        """
        ...

TZFILES: list[str]
TZPATHS: list[str]

def datetime_exists(dt: datetime, tz: tzinfo | None = None) -> bool: ...
def datetime_ambiguous(dt: datetime, tz: tzinfo | None = None) -> bool: ...
def resolve_imaginary(dt: datetime) -> datetime: ...

class _GetTZ:
    def __call__(self, name: str | None = ...) -> tzinfo | None: ...
    def nocache(self, name: str | None) -> tzinfo | None: ...

gettz: _GetTZ
