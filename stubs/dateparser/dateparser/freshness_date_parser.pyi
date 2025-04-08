import re
from _typeshed import Incomplete
from typing import Final
from zoneinfo import ZoneInfo

from dateparser.date import DateData

PATTERN: Final[re.Pattern[str]]

class FreshnessDateDataParser:
    """Parses date string like "1 year, 2 months ago" and "3 hours, 50 minutes ago" """
    def get_local_tz(self) -> ZoneInfo: ...
    def parse(self, date_string: str, settings) -> tuple[Incomplete | None, str | None]: ...
    def get_kwargs(self, date_string: str) -> dict[str, float]: ...
    def get_date_data(self, date_string: str, settings: Incomplete | None = None) -> DateData: ...

freshness_date_parser: FreshnessDateDataParser
