from _typeshed import Incomplete
from typing import Any

PARSER_HARDCODED_TOKENS: Any
PARSER_KNOWN_TOKENS: Any
ALWAYS_KEEP_TOKENS: list[str]
KNOWN_WORD_TOKENS: Any
PARENTHESES_PATTERN: Any
NUMERAL_PATTERN: Any
KEEP_TOKEN_PATTERN: Any

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
    def __init__(self, locale_info, settings: Incomplete | None = None) -> None: ...
    def __contains__(self, key): ...
    def __getitem__(self, key): ...
    def __iter__(self) -> Any: ...
    def are_tokens_valid(self, tokens):
        """
        Check if tokens are valid tokens for the locale.

        :param tokens:
            a list of string tokens.
        :type tokens: list

        :return: True if tokens are valid, False otherwise.
        """
        ...
    def split(self, string, keep_formatting: bool = False):
        """
        Split the date string using translations in locale info.

        :param string:
            Date string to be splitted.
        :type string:
            str

        :param keep_formatting:
            If True, retain formatting of the date string.
        :type keep_formatting: bool

        :return: A list of string tokens formed after splitting the date string.
        """
        ...

class NormalizedDictionary(Dictionary):
    def __init__(self, locale_info, settings: Incomplete | None = None) -> None: ...
