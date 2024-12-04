from typing import Any

from dateparser.parser import _parser

class CalendarBase:
    """
    Base setup class for non-Gregorian calendar system.

    :param source:
        Date string passed to calendar parser.
    :type source: str
    """
    parser: Any
    source: Any
    def __init__(self, source) -> None: ...
    def get_date(self): ...

class non_gregorian_parser(_parser):
    calendar_converter: Any
    default_year: Any
    default_month: Any
    default_day: Any
    non_gregorian_date_cls: Any
    @classmethod
    def to_latin(cls, source): ...
    @classmethod
    def parse(cls, datestring, settings): ...
