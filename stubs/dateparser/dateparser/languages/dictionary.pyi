import re
from _typeshed import Incomplete
from typing import Any, Final, overload

PARSER_HARDCODED_TOKENS: Final[list[str]]
PARSER_KNOWN_TOKENS: Final[list[str]]
ALWAYS_KEEP_TOKENS: Final[list[str]]
KNOWN_WORD_TOKENS: Final[list[str]]
PARENTHESES_PATTERN: Final[re.Pattern[str]]
NUMERAL_PATTERN: Final[re.Pattern[str]]
KEEP_TOKEN_PATTERN: Final[re.Pattern[str]]

class UnknownTokenError(Exception): ...

class Dictionary:
    """
    Class that modifies and stores translations and handles splitting of date string.

    :param locale_info:
        Locale info (translation data) of the locale.
    :type language_info: dict

    :param settings:
        Configure customized behavior using settings defined in :mod:`dateparser.conf.Settings`.
    :type settings: dict

    :return: a Dictionary instance.
    """
    info: Any
    def __init__(self, locale_info: dict[str, Incomplete], settings: Incomplete | None = None) -> None: ...
    def __contains__(self, key): ...
    def __getitem__(self, key): ...
    def __iter__(self) -> Any: ...
    def are_tokens_valid(self, tokens: list[str]) -> bool: ...
    @overload
    def split(self, string: None, keep_formatting: bool = False) -> None: ...
    @overload
    def split(self, string: str, keep_formatting: bool = False) -> list[str]: ...

class NormalizedDictionary(Dictionary):
    def __init__(self, locale_info: dict[str, Incomplete], settings: Incomplete | None = None) -> None: ...
