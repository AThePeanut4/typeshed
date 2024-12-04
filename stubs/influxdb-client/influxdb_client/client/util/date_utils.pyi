"""Utils to get right Date parsing function."""

from datetime import datetime, timedelta, tzinfo
from threading import Lock

date_helper: DateHelper | None
lock_: Lock

class DateHelper:
    """
    DateHelper to groups different implementations of date operations.

    If you would like to serialize the query results to custom timezone, you can use following code:

    .. code-block:: python

        from influxdb_client.client.util import date_utils
        from influxdb_client.client.util.date_utils import DateHelper
        import dateutil.parser
        from dateutil import tz

        def parse_date(date_string: str):
            return dateutil.parser.parse(date_string).astimezone(tz.gettz('ETC/GMT+2'))

        date_utils.date_helper = DateHelper()
        date_utils.date_helper.parse_date = parse_date
    """
    timezone: tzinfo
    def __init__(self, timezone: tzinfo = ...) -> None:
        """
        Initialize defaults.

        :param timezone: Default timezone used for serialization "datetime" without "tzinfo".
                         Default value is "UTC".
        """
        ...
    # This returns None in the implementation, but a datetime-compatible
    # object is monkey-patched in at runtime.
    def parse_date(self, date_string: str) -> datetime:
        """
        Parse string into Date or Timestamp.

        :return: Returns a :class:`datetime.datetime` object or compliant implementation
                 like :class:`class 'pandas._libs.tslibs.timestamps.Timestamp`
        """
        ...
    def to_nanoseconds(self, delta: timedelta) -> int:
        """
        Get number of nanoseconds in timedelta.

        Solution comes from v1 client. Thx.
        https://github.com/influxdata/influxdb-python/pull/811
        """
        ...
    def to_utc(self, value: datetime) -> datetime:
        """
        Convert datetime to UTC timezone.

        :param value: datetime
        :return: datetime in UTC
        """
        ...

def get_date_helper() -> DateHelper:
    """
    Return DateHelper with proper implementation.

    If there is a 'ciso8601' than use 'ciso8601.parse_datetime' else
    use 'datetime.fromisoformat' (Python >= 3.11) or 'dateutil.parse' (Python < 3.11).
    """
    ...
