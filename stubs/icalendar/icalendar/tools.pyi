import datetime
from typing import Final
from typing_extensions import TypeGuard, TypeIs

from pytz.tzinfo import BaseTzInfo

from .prop import vText

__all__ = ["UIDGenerator", "is_date", "is_datetime", "to_datetime", "is_pytz", "is_pytz_dt", "normalize_pytz"]

class UIDGenerator:
    """
    If you are too lazy to create real uid's.

    
    """
    chars: Final[list[str]]
    @staticmethod
    def rnd_string(length: int = 16) -> str:
        """
        Generates a string with random characters of length.
        
        """
        ...
    @staticmethod
    def uid(host_name: str = "example.com", unique: str = "") -> vText:
        """
        Generates a unique id consisting of:
            datetime-uniquevalue@host.
        Like:
            20050105T225746Z-HKtJMqUgdO0jDUwm@example.com
        """
        ...

def is_date(dt: datetime.date) -> bool:
    """Whether this is a date and not a datetime."""
    ...
def is_datetime(dt: datetime.date) -> TypeIs[datetime.datetime]:
    """Whether this is a date and not a datetime."""
    ...
def to_datetime(dt: datetime.date) -> datetime.datetime:
    """Make sure we have a datetime, not a date."""
    ...
def is_pytz(tz: datetime.tzinfo) -> TypeIs[BaseTzInfo]:
    """Whether the timezone requires localize() and normalize()."""
    ...
def is_pytz_dt(dt: datetime.date) -> TypeGuard[datetime.datetime]:
    """Whether the time requires localize() and normalize()."""
    ...
def normalize_pytz(dt: datetime.date) -> datetime.datetime:
    """
    We have to normalize the time after a calculation if we use pytz.

    pytz requires this function to be used in order to correctly calculate the
    timezone's offset after calculations.
    """
    ...
