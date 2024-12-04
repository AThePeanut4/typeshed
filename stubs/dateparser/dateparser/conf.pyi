from _typeshed import Incomplete
from typing import Any
from typing_extensions import Self

class Settings:
    """
    Control and configure default parsing behavior of dateparser.
    Currently, supported settings are:

    * `DATE_ORDER`
    * `PREFER_LOCALE_DATE_ORDER`
    * `TIMEZONE`
    * `TO_TIMEZONE`
    * `RETURN_AS_TIMEZONE_AWARE`
    * `PREFER_MONTH_OF_YEAR`
    * `PREFER_DAY_OF_MONTH`
    * `PREFER_DATES_FROM`
    * `RELATIVE_BASE`
    * `STRICT_PARSING`
    * `REQUIRE_PARTS`
    * `SKIP_TOKENS`
    * `NORMALIZE`
    * `RETURN_TIME_AS_PERIOD`
    * `PARSERS`
    * `DEFAULT_LANGUAGES`
    * `LANGUAGE_DETECTION_CONFIDENCE_THRESHOLD`
    * `CACHE_SIZE_LIMIT`
    """
    def __new__(cls, *args, **kw) -> Self: ...
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    @classmethod
    def get_key(cls, settings: Incomplete | None = None): ...
    def replace(self, mod_settings: Incomplete | None = None, **kwds): ...

settings: Any

def apply_settings(f): ...

class SettingValidationError(ValueError): ...

def check_settings(settings) -> None:
    """
    Check if provided settings are valid, if not it raises `SettingValidationError`.
    Only checks for the modified settings.
    """
    ...
