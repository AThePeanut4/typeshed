import datetime
from _typeshed import Incomplete

log: Incomplete

class _SimpleStruct:
    def __init__(self, *args, **kw) -> None: ...
    def field_names(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class SYSTEMTIME(_SimpleStruct): ...
class TIME_ZONE_INFORMATION(_SimpleStruct): ...
class DYNAMIC_TIME_ZONE_INFORMATION(_SimpleStruct): ...

class TimeZoneDefinition(DYNAMIC_TIME_ZONE_INFORMATION):
    """
    A time zone definition class based on the win32
    DYNAMIC_TIME_ZONE_INFORMATION structure.

    Describes a bias against UTC (bias), and two dates at which a separate
    additional bias applies (standard_bias and daylight_bias).
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Try to construct a TimeZoneDefinition from
        a) [DYNAMIC_]TIME_ZONE_INFORMATION args
        b) another TimeZoneDefinition
        c) a byte structure (using _from_bytes)
        """
        ...
    def __getattribute__(self, attr: str): ...
    @classmethod
    def current(cls):
        """Windows Platform SDK GetTimeZoneInformation"""
        ...
    def set(self) -> None: ...
    def copy(self): ...
    def locate_daylight_start(self, year): ...
    def locate_standard_start(self, year): ...

class TimeZoneInfo(datetime.tzinfo):
    """
    Main class for handling Windows time zones.
    Usage:
        TimeZoneInfo(<Time Zone Standard Name>, [<Fix Standard Time>])

    If <Fix Standard Time> evaluates to True, daylight savings time is
    calculated in the same way as standard time.

    >>> tzi = TimeZoneInfo('Pacific Standard Time')
    >>> march31 = datetime.datetime(2000,3,31)

    We know that time zone definitions haven't changed from 2007
    to 2012, so regardless of whether dynamic info is available,
    there should be consistent results for these years.
    >>> subsequent_years = [march31.replace(year=year)
    ...     for year in range(2007, 2013)]
    >>> offsets = set(tzi.utcoffset(year) for year in subsequent_years)
    >>> len(offsets)
    1
    """
    tzRegKey: str
    timeZoneName: Incomplete
    fixedStandardTime: Incomplete
    def __init__(self, param: Incomplete | None = ..., fix_standard_time: bool = ...) -> None: ...
    def tzname(self, dt): ...
    def getWinInfo(self, targetYear):
        """
        Return the most relevant "info" for this time zone
        in the target year.
        """
        ...
    def utcoffset(self, dt):
        """Calculates the utcoffset according to the datetime.tzinfo spec"""
        ...
    def dst(self, dt):
        """
        Calculate the daylight savings offset according to the
        datetime.tzinfo spec.
        """
        ...
    def GetDSTStartTime(self, year):
        """Given a year, determines the time when daylight savings time starts"""
        ...
    def GetDSTEndTime(self, year):
        """Given a year, determines the time when daylight savings ends."""
        ...
    def __le__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @classmethod
    def local(cls):
        """
        Returns the local time zone as defined by the operating system in the
        registry.
        >>> localTZ = TimeZoneInfo.local()
        >>> now_local = datetime.datetime.now(localTZ)
        >>> now_UTC = datetime.datetime.utcnow()
        >>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)
        Traceback (most recent call last):
        ...
        TypeError: can't subtract offset-naive and offset-aware datetimes

        >>> now_UTC = now_UTC.replace(tzinfo = TimeZoneInfo('GMT Standard Time', True))

        Now one can compare the results of the two offset aware values
        >>> (now_UTC - now_local) < datetime.timedelta(seconds = 5)
        True
        """
        ...
    @classmethod
    def utc(cls):
        """
        Returns a time-zone representing UTC.

        Same as TimeZoneInfo('GMT Standard Time', True) but caches the result
        for performance.

        >>> isinstance(TimeZoneInfo.utc(), TimeZoneInfo)
        True
        """
        ...
    @staticmethod
    def get_sorted_time_zone_names():
        """
        Return a list of time zone names that can
        be used to initialize TimeZoneInfo instances.
        """
        ...
    @staticmethod
    def get_all_time_zones(): ...
    @staticmethod
    def get_sorted_time_zones(key: Incomplete | None = ...):
        """
        Return the time zones sorted by some key.
        key must be a function that takes a TimeZoneInfo object and returns
        a value suitable for sorting on.
        The key defaults to the bias (descending), as is done in Windows
        (see http://blogs.msdn.com/michkap/archive/2006/12/22/1350684.aspx)
        """
        ...

def utcnow():
    """
    Return the UTC time now with timezone awareness as enabled
    by this module
    >>> now = utcnow()
    """
    ...
def now():
    """
    Return the local time now with timezone awareness as enabled
    by this module
    >>> now_local = now()
    """
    ...
def GetTZCapabilities():
    """
    Run a few known tests to determine the capabilities of
    the time zone database on this machine.
    Note Dynamic Time Zone support is not available on any
    platform at this time; this
    is a limitation of this library, not the platform.
    """
    ...

class DLLHandleCache:
    def __getitem__(self, filename): ...

DLLCache: Incomplete

def resolveMUITimeZone(spec):
    """
    Resolve a multilingual user interface resource for the time zone name

    spec should be of the format @path,-stringID[;comment]
    see http://msdn2.microsoft.com/en-us/library/ms725481.aspx for details
    """
    ...

class RangeMap(dict[int, str]):
    """
    A dictionary-like object that uses the keys as bounds for a range.
    Inclusion of the value for that range is determined by the
    key_match_comparator, which defaults to less-than-or-equal.
    A value is returned for a key if it is the first key that matches in
    the sorted list of keys.

    One may supply keyword parameters to be passed to the sort function used
    to sort keys (i.e. keys, reverse) as sort_params.

    Let's create a map that maps 1-3 -> 'a', 4-6 -> 'b'
    >>> r = RangeMap({3: 'a', 6: 'b'})  # boy, that was easy
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    Even float values should work so long as the comparison operator
    supports it.
    >>> r[4.5]
    'b'

    But you'll notice that the way rangemap is defined, it must be open-ended on one side.
    >>> r[0]
    'a'
    >>> r[-1]
    'a'

    One can close the open-end of the RangeMap by using undefined_value
    >>> r = RangeMap({0: RangeMap.undefined_value, 3: 'a', 6: 'b'})
    >>> r[0]
    Traceback (most recent call last):
    ...
    KeyError: 0

    One can get the first or last elements in the range by using RangeMap.Item
    >>> last_item = RangeMap.Item(-1)
    >>> r[last_item]
    'b'

    .last_item is a shortcut for Item(-1)
    >>> r[RangeMap.last_item]
    'b'

    Sometimes it's useful to find the bounds for a RangeMap
    >>> r.bounds()
    (0, 6)

    RangeMap supports .get(key, default)
    >>> r.get(0, 'not found')
    'not found'

    >>> r.get(7, 'not found')
    'not found'
    """
    sort_params: Incomplete
    match: Incomplete
    def __init__(self, source, sort_params=..., key_match_comparator=...) -> None: ...
    def __getitem__(self, item): ...
    def get(self, key, default: Incomplete | None = ...):
        """
        Return the value for key if key is in the dictionary, else default.
        If default is not given, it defaults to None, so that this method
        never raises a KeyError.
        """
        ...
    def bounds(self): ...
    undefined_value: Incomplete

    class Item(int): ...
    first_item: Incomplete
    last_item: Incomplete
