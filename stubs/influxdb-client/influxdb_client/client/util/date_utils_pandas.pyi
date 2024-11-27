"""Pandas date utils."""

from influxdb_client.client.util.date_utils import DateHelper

class PandasDateTimeHelper(DateHelper):
    """DateHelper that use Pandas library with nanosecond precision."""
    def parse_date(self, date_string: str):
        """Parse date string into `class 'pandas._libs.tslibs.timestamps.Timestamp`."""
        ...
    def to_nanoseconds(self, delta):
        """Get number of nanoseconds with nanos precision."""
        ...
