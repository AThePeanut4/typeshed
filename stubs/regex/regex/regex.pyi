from _typeshed import ReadableBuffer, Unused
from collections.abc import Callable, Mapping
from types import GenericAlias
from typing import Any, AnyStr, Generic, Literal, TypeVar, final, overload
from typing_extensions import Self

from . import _regex
from ._regex_core import *

_T = TypeVar("_T")

__version__: str

def compile(
    pattern: AnyStr | Pattern[AnyStr],
    flags: int = 0,
    ignore_unused: bool = False,
    cache_pattern: bool | None = None,
    **kwargs: Any,
) -> Pattern[AnyStr]:
    """Compile a regular expression pattern, returning a pattern object."""
    ...
@overload
def search(
    pattern: str | Pattern[str],
    string: str,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> Match[str] | None:
    """
    Search through string looking for a match to the pattern, returning a
    match object, or None if no match was found.
    """
    ...
@overload
def search(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> Match[bytes] | None:
    """
    Search through string looking for a match to the pattern, returning a
    match object, or None if no match was found.
    """
    ...
@overload
def match(
    pattern: str | Pattern[str],
    string: str,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> Match[str] | None:
    """
    Try to apply the pattern at the start of the string, returning a match
    object, or None if no match was found.
    """
    ...
@overload
def match(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> Match[bytes] | None:
    """
    Try to apply the pattern at the start of the string, returning a match
    object, or None if no match was found.
    """
    ...
@overload
def fullmatch(
    pattern: str | Pattern[str],
    string: str,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> Match[str] | None:
    """
    Try to apply the pattern against all of the string, returning a match
    object, or None if no match was found.
    """
    ...
@overload
def fullmatch(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> Match[bytes] | None:
    """
    Try to apply the pattern against all of the string, returning a match
    object, or None if no match was found.
    """
    ...
@overload
def split(
    pattern: str | Pattern[str],
    string: str,
    maxsplit: int = 0,
    flags: int = 0,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> list[str | Any]:
    """
    Split the source string by the occurrences of the pattern, returning a
    list containing the resulting substrings.  If capturing parentheses are used
    in pattern, then the text of all groups in the pattern are also returned as
    part of the resulting list.  If maxsplit is nonzero, at most maxsplit splits
    occur, and the remainder of the string is returned as the final element of
    the list.
    """
    ...
@overload
def split(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    maxsplit: int = 0,
    flags: int = 0,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> list[bytes | Any]:
    """
    Split the source string by the occurrences of the pattern, returning a
    list containing the resulting substrings.  If capturing parentheses are used
    in pattern, then the text of all groups in the pattern are also returned as
    part of the resulting list.  If maxsplit is nonzero, at most maxsplit splits
    occur, and the remainder of the string is returned as the final element of
    the list.
    """
    ...
@overload
def splititer(
    pattern: str | Pattern[str],
    string: str,
    maxsplit: int = 0,
    flags: int = 0,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> _regex.Splitter[str]:
    """Return an iterator yielding the parts of a split string."""
    ...
@overload
def splititer(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    maxsplit: int = 0,
    flags: int = 0,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> _regex.Splitter[bytes]:
    """Return an iterator yielding the parts of a split string."""
    ...
@overload
def findall(
    pattern: str | Pattern[str],
    string: str,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    overlapped: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> list[Any]:
    """
    Return a list of all matches in the string. The matches may be overlapped
    if overlapped is True. If one or more groups are present in the pattern,
    return a list of groups; this will be a list of tuples if the pattern has
    more than one group. Empty matches are included in the result.
    """
    ...
@overload
def findall(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    overlapped: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> list[Any]:
    """
    Return a list of all matches in the string. The matches may be overlapped
    if overlapped is True. If one or more groups are present in the pattern,
    return a list of groups; this will be a list of tuples if the pattern has
    more than one group. Empty matches are included in the result.
    """
    ...
@overload
def finditer(
    pattern: str | Pattern[str],
    string: str,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    overlapped: bool = False,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> _regex.Scanner[str]:
    """
    Return an iterator over all matches in the string. The matches may be
    overlapped if overlapped is True. For each match, the iterator returns a
    match object. Empty matches are included in the result.
    """
    ...
@overload
def finditer(
    pattern: bytes | Pattern[bytes],
    string: ReadableBuffer,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    overlapped: bool = False,
    partial: bool = False,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> _regex.Scanner[bytes]:
    """
    Return an iterator over all matches in the string. The matches may be
    overlapped if overlapped is True. For each match, the iterator returns a
    match object. Empty matches are included in the result.
    """
    ...
@overload
def sub(
    pattern: str | Pattern[str],
    repl: str | Callable[[Match[str]], str],
    string: str,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> str:
    """
    Return the string obtained by replacing the leftmost (or rightmost with a
    reverse pattern) non-overlapping occurrences of the pattern in string by the
    replacement repl. repl can be either a string or a callable; if a string,
    backslash escapes in it are processed; if a callable, it's passed the match
    object and must return a replacement string to be used.
    """
    ...
@overload
def sub(
    pattern: bytes | Pattern[bytes],
    repl: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
    string: ReadableBuffer,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> bytes:
    """
    Return the string obtained by replacing the leftmost (or rightmost with a
    reverse pattern) non-overlapping occurrences of the pattern in string by the
    replacement repl. repl can be either a string or a callable; if a string,
    backslash escapes in it are processed; if a callable, it's passed the match
    object and must return a replacement string to be used.
    """
    ...
@overload
def subf(
    pattern: str | Pattern[str],
    format: str | Callable[[Match[str]], str],
    string: str,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> str:
    """
    Return the string obtained by replacing the leftmost (or rightmost with a
    reverse pattern) non-overlapping occurrences of the pattern in string by the
    replacement format. format can be either a string or a callable; if a string,
    it's treated as a format string; if a callable, it's passed the match object
    and must return a replacement string to be used.
    """
    ...
@overload
def subf(
    pattern: bytes | Pattern[bytes],
    format: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
    string: ReadableBuffer,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> bytes:
    """
    Return the string obtained by replacing the leftmost (or rightmost with a
    reverse pattern) non-overlapping occurrences of the pattern in string by the
    replacement format. format can be either a string or a callable; if a string,
    it's treated as a format string; if a callable, it's passed the match object
    and must return a replacement string to be used.
    """
    ...
@overload
def subn(
    pattern: str | Pattern[str],
    repl: str | Callable[[Match[str]], str],
    string: str,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> tuple[str, int]:
    """
    Return a 2-tuple containing (new_string, number). new_string is the string
    obtained by replacing the leftmost (or rightmost with a reverse pattern)
    non-overlapping occurrences of the pattern in the source string by the
    replacement repl. number is the number of substitutions that were made. repl
    can be either a string or a callable; if a string, backslash escapes in it
    are processed; if a callable, it's passed the match object and must return a
    replacement string to be used.
    """
    ...
@overload
def subn(
    pattern: bytes | Pattern[bytes],
    repl: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
    string: ReadableBuffer,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> tuple[bytes, int]:
    """
    Return a 2-tuple containing (new_string, number). new_string is the string
    obtained by replacing the leftmost (or rightmost with a reverse pattern)
    non-overlapping occurrences of the pattern in the source string by the
    replacement repl. number is the number of substitutions that were made. repl
    can be either a string or a callable; if a string, backslash escapes in it
    are processed; if a callable, it's passed the match object and must return a
    replacement string to be used.
    """
    ...
@overload
def subfn(
    pattern: str | Pattern[str],
    format: str | Callable[[Match[str]], str],
    string: str,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> tuple[str, int]:
    """
    Return a 2-tuple containing (new_string, number). new_string is the string
    obtained by replacing the leftmost (or rightmost with a reverse pattern)
    non-overlapping occurrences of the pattern in the source string by the
    replacement format. number is the number of substitutions that were made. format
    can be either a string or a callable; if a string, it's treated as a format
    string; if a callable, it's passed the match object and must return a
    replacement string to be used.
    """
    ...
@overload
def subfn(
    pattern: bytes | Pattern[bytes],
    format: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
    string: ReadableBuffer,
    count: int = 0,
    flags: int = 0,
    pos: int | None = None,
    endpos: int | None = None,
    concurrent: bool | None = None,
    timeout: float | None = None,
    ignore_unused: bool = False,
    **kwargs: Any,
) -> tuple[bytes, int]:
    """
    Return a 2-tuple containing (new_string, number). new_string is the string
    obtained by replacing the leftmost (or rightmost with a reverse pattern)
    non-overlapping occurrences of the pattern in the source string by the
    replacement format. number is the number of substitutions that were made. format
    can be either a string or a callable; if a string, it's treated as a format
    string; if a callable, it's passed the match object and must return a
    replacement string to be used.
    """
    ...
def purge() -> None:
    """Clear the regular expression cache"""
    ...
@overload
def cache_all(value: bool = True) -> None:
    """
    Sets whether to cache all patterns, even those are compiled explicitly.
    Passing None has no effect, but returns the current setting.
    """
    ...
@overload
def cache_all(value: None) -> bool:
    """
    Sets whether to cache all patterns, even those are compiled explicitly.
    Passing None has no effect, but returns the current setting.
    """
    ...
def escape(pattern: AnyStr, special_only: bool = True, literal_spaces: bool = False) -> AnyStr:
    """
    Escape a string for use as a literal in a pattern. If special_only is
    True, escape only special characters, else escape all non-alphanumeric
    characters. If literal_spaces is True, don't escape spaces.
    """
    ...
def template(pattern: AnyStr | Pattern[AnyStr], flags: int = 0) -> Pattern[AnyStr]:
    """Compile a template pattern, returning a pattern object."""
    ...

Regex = compile

@final
class Pattern(Generic[AnyStr]):
    """Compiled regex object"""
    @property
    def flags(self) -> int:
        """The regex matching flags."""
        ...
    @property
    def groupindex(self) -> Mapping[str, int]:
        """A dictionary mapping group names to group numbers."""
        ...
    @property
    def groups(self) -> int:
        """The number of capturing groups in the pattern."""
        ...
    @property
    def pattern(self) -> AnyStr:
        """The pattern string from which the regex object was compiled."""
        ...
    @property
    def named_lists(self) -> Mapping[str, frozenset[AnyStr]]:
        """The named lists used by the regex."""
        ...
    @overload
    def search(
        self: Pattern[str],
        string: str,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> Match[str] | None:
        """
        search(string, pos=None, endpos=None, concurrent=None, timeout=None) --> MatchObject or None.
        Search through string looking for a match, and return a corresponding
        match object instance.  Return None if no match is found.
        """
        ...
    @overload
    def search(
        self: Pattern[bytes],
        string: ReadableBuffer,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> Match[bytes] | None:
        """
        search(string, pos=None, endpos=None, concurrent=None, timeout=None) --> MatchObject or None.
        Search through string looking for a match, and return a corresponding
        match object instance.  Return None if no match is found.
        """
        ...
    @overload
    def match(
        self: Pattern[str],
        string: str,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> Match[str] | None:
        """
        match(string, pos=None, endpos=None, concurrent=None, timeout=None) --> MatchObject or None.
        Match zero or more characters at the beginning of the string.
        """
        ...
    @overload
    def match(
        self: Pattern[bytes],
        string: ReadableBuffer,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> Match[bytes] | None:
        """
        match(string, pos=None, endpos=None, concurrent=None, timeout=None) --> MatchObject or None.
        Match zero or more characters at the beginning of the string.
        """
        ...
    @overload
    def fullmatch(
        self: Pattern[str],
        string: str,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> Match[str] | None:
        """
        fullmatch(string, pos=None, endpos=None, concurrent=None, timeout=None) --> MatchObject or None.
        Match zero or more characters against all of the string.
        """
        ...
    @overload
    def fullmatch(
        self: Pattern[bytes],
        string: ReadableBuffer,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> Match[bytes] | None:
        """
        fullmatch(string, pos=None, endpos=None, concurrent=None, timeout=None) --> MatchObject or None.
        Match zero or more characters against all of the string.
        """
        ...
    @overload
    def split(
        self: Pattern[str], string: str, maxsplit: int = 0, concurrent: bool | None = None, timeout: float | None = None
    ) -> list[str | Any]:
        """
        split(string, maxsplit=0, concurrent=None, timeout=None) --> list.
        Split string by the occurrences of pattern.
        """
        ...
    @overload
    def split(
        self: Pattern[bytes],
        string: ReadableBuffer,
        maxsplit: int = 0,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> list[bytes | Any]:
        """
        split(string, maxsplit=0, concurrent=None, timeout=None) --> list.
        Split string by the occurrences of pattern.
        """
        ...
    @overload
    def splititer(
        self: Pattern[str], string: str, maxsplit: int = 0, concurrent: bool | None = None, timeout: float | None = None
    ) -> _regex.Splitter[str]:
        """
        splititer(string, maxsplit=0, concurrent=None, timeout=None) --> iterator.
        Return an iterator yielding the parts of a split string.
        """
        ...
    @overload
    def splititer(
        self: Pattern[bytes],
        string: ReadableBuffer,
        maxsplit: int = 0,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> _regex.Splitter[bytes]:
        """
        splititer(string, maxsplit=0, concurrent=None, timeout=None) --> iterator.
        Return an iterator yielding the parts of a split string.
        """
        ...
    @overload
    def findall(
        self: Pattern[str],
        string: str,
        pos: int | None = None,
        endpos: int | None = None,
        overlapped: bool = False,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> list[Any]:
        """
        findall(string, pos=None, endpos=None, overlapped=False, concurrent=None, timeout=None) --> list.
        Return a list of all matches of pattern in string.  The matches may be
        overlapped if overlapped is True.
        """
        ...
    @overload
    def findall(
        self: Pattern[bytes],
        string: ReadableBuffer,
        pos: int | None = None,
        endpos: int | None = None,
        overlapped: bool = False,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> list[Any]:
        """
        findall(string, pos=None, endpos=None, overlapped=False, concurrent=None, timeout=None) --> list.
        Return a list of all matches of pattern in string.  The matches may be
        overlapped if overlapped is True.
        """
        ...
    @overload
    def finditer(
        self: Pattern[str],
        string: str,
        pos: int | None = None,
        endpos: int | None = None,
        overlapped: bool = False,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> _regex.Scanner[str]:
        """
        finditer(string, pos=None, endpos=None, overlapped=False, concurrent=None, timeout=None) --> iterator.
        Return an iterator over all matches for the RE pattern in string.  The
        matches may be overlapped if overlapped is True.  For each match, the
        iterator returns a MatchObject.
        """
        ...
    @overload
    def finditer(
        self: Pattern[bytes],
        string: ReadableBuffer,
        pos: int | None = None,
        endpos: int | None = None,
        overlapped: bool = False,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> _regex.Scanner[bytes]:
        """
        finditer(string, pos=None, endpos=None, overlapped=False, concurrent=None, timeout=None) --> iterator.
        Return an iterator over all matches for the RE pattern in string.  The
        matches may be overlapped if overlapped is True.  For each match, the
        iterator returns a MatchObject.
        """
        ...
    @overload
    def sub(
        self: Pattern[str],
        repl: str | Callable[[Match[str]], str],
        string: str,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> str:
        """
        sub(repl, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> newstring
        Return the string obtained by replacing the leftmost (or rightmost with a
        reverse pattern) non-overlapping occurrences of pattern in string by the
        replacement repl.
        """
        ...
    @overload
    def sub(
        self: Pattern[bytes],
        repl: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
        string: ReadableBuffer,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> bytes:
        """
        sub(repl, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> newstring
        Return the string obtained by replacing the leftmost (or rightmost with a
        reverse pattern) non-overlapping occurrences of pattern in string by the
        replacement repl.
        """
        ...
    @overload
    def subf(
        self: Pattern[str],
        format: str | Callable[[Match[str]], str],
        string: str,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> str:
        """
        subf(format, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> newstring
        Return the string obtained by replacing the leftmost (or rightmost with a
        reverse pattern) non-overlapping occurrences of pattern in string by the
        replacement format.
        """
        ...
    @overload
    def subf(
        self: Pattern[bytes],
        format: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
        string: ReadableBuffer,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> bytes:
        """
        subf(format, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> newstring
        Return the string obtained by replacing the leftmost (or rightmost with a
        reverse pattern) non-overlapping occurrences of pattern in string by the
        replacement format.
        """
        ...
    @overload
    def subn(
        self: Pattern[str],
        repl: str | Callable[[Match[str]], str],
        string: str,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> tuple[str, int]:
        """
        subn(repl, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> (newstring, number of subs)
        Return the tuple (new_string, number_of_subs_made) found by replacing the
        leftmost (or rightmost with a reverse pattern) non-overlapping occurrences
        of pattern with the replacement repl.
        """
        ...
    @overload
    def subn(
        self: Pattern[bytes],
        repl: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
        string: ReadableBuffer,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> tuple[bytes, int]:
        """
        subn(repl, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> (newstring, number of subs)
        Return the tuple (new_string, number_of_subs_made) found by replacing the
        leftmost (or rightmost with a reverse pattern) non-overlapping occurrences
        of pattern with the replacement repl.
        """
        ...
    @overload
    def subfn(
        self: Pattern[str],
        format: str | Callable[[Match[str]], str],
        string: str,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> tuple[str, int]:
        """
        subfn(format, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> (newstring, number of subs)
        Return the tuple (new_string, number_of_subs_made) found by replacing the
        leftmost (or rightmost with a reverse pattern) non-overlapping occurrences
        of pattern with the replacement format.
        """
        ...
    @overload
    def subfn(
        self: Pattern[bytes],
        format: ReadableBuffer | Callable[[Match[bytes]], ReadableBuffer],
        string: ReadableBuffer,
        count: int = 0,
        pos: int | None = None,
        endpos: int | None = None,
        concurrent: bool | None = None,
        timeout: float | None = None,
    ) -> tuple[bytes, int]:
        """
        subfn(format, string, count=0, flags=0, pos=None, endpos=None, concurrent=None, timeout=None) --> (newstring, number of subs)
        Return the tuple (new_string, number_of_subs_made) found by replacing the
        leftmost (or rightmost with a reverse pattern) non-overlapping occurrences
        of pattern with the replacement format.
        """
        ...
    @overload
    def scanner(
        self: Pattern[str],
        string: str,
        pos: int | None = None,
        endpos: int | None = None,
        overlapped: bool = False,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> _regex.Scanner[str]:
        """
        scanner(string, pos=None, endpos=None, overlapped=False, concurrent=None, timeout=None) --> scanner.
        Return an scanner for the RE pattern in string.  The matches may be overlapped
        if overlapped is True.
        """
        ...
    @overload
    def scanner(
        self: Pattern[bytes],
        string: bytes,
        pos: int | None = None,
        endpos: int | None = None,
        overlapped: bool = False,
        concurrent: bool | None = None,
        partial: bool = False,
        timeout: float | None = None,
    ) -> _regex.Scanner[bytes]:
        """
        scanner(string, pos=None, endpos=None, overlapped=False, concurrent=None, timeout=None) --> scanner.
        Return an scanner for the RE pattern in string.  The matches may be overlapped
        if overlapped is True.
        """
        ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: Unused, /) -> Self: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

@final
class Match(Generic[AnyStr]):
    """Match object"""
    @property
    def pos(self) -> int:
        """The position at which the regex engine starting searching."""
        ...
    @property
    def endpos(self) -> int:
        """The final position beyond which the regex engine won't search."""
        ...
    @property
    def lastindex(self) -> int | None:
        """The group number of the last matched capturing group, or None."""
        ...
    @property
    def lastgroup(self) -> str | None:
        """The name of the last matched capturing group, or None."""
        ...
    @property
    def string(self) -> AnyStr:
        """The string that was searched, or None if it has been detached."""
        ...
    @property
    def re(self) -> Pattern[AnyStr]:
        """The regex object that produced this match object."""
        ...
    @property
    def partial(self) -> bool:
        """Whether it's a partial match."""
        ...
    @property
    def regs(self) -> tuple[tuple[int, int], ...]:
        """A tuple of the spans of the capturing groups."""
        ...
    @property
    def fuzzy_counts(self) -> tuple[int, int, int]:
        """A tuple of the number of substitutions, insertions and deletions."""
        ...
    @property
    def fuzzy_changes(self) -> tuple[list[int], list[int], list[int]]:
        """A tuple of the positions of the substitutions, insertions and deletions."""
        ...
    @overload
    def group(self, group: Literal[0] = 0, /) -> AnyStr:
        """
        group([group1, ...]) --> string or tuple of strings.
        Return one or more subgroups of the match.  If there is a single argument,
        the result is a single string, or None if the group did not contribute to
        the match; if there are multiple arguments, the result is a tuple with one
        item per argument; if there are no arguments, the whole match is returned.
        Group 0 is the whole match.
        """
        ...
    @overload
    def group(self, group: int | str = ..., /) -> AnyStr | Any:
        """
        group([group1, ...]) --> string or tuple of strings.
        Return one or more subgroups of the match.  If there is a single argument,
        the result is a single string, or None if the group did not contribute to
        the match; if there are multiple arguments, the result is a tuple with one
        item per argument; if there are no arguments, the whole match is returned.
        Group 0 is the whole match.
        """
        ...
    @overload
    def group(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[AnyStr | Any, ...]:
        """
        group([group1, ...]) --> string or tuple of strings.
        Return one or more subgroups of the match.  If there is a single argument,
        the result is a single string, or None if the group did not contribute to
        the match; if there are multiple arguments, the result is a tuple with one
        item per argument; if there are no arguments, the whole match is returned.
        Group 0 is the whole match.
        """
        ...
    @overload
    def groups(self, default: None = None) -> tuple[AnyStr | Any, ...]:
        """
        groups(default=None) --> tuple of strings.
        Return a tuple containing all the subgroups of the match.  The argument is
        the default for groups that did not participate in the match.
        """
        ...
    @overload
    def groups(self, default: _T) -> tuple[AnyStr | _T, ...]:
        """
        groups(default=None) --> tuple of strings.
        Return a tuple containing all the subgroups of the match.  The argument is
        the default for groups that did not participate in the match.
        """
        ...
    @overload
    def groupdict(self, default: None = None) -> dict[str, AnyStr | Any]:
        """
        groupdict(default=None) --> dict.
        Return a dictionary containing all the named subgroups of the match, keyed
        by the subgroup name.  The argument is the value to be given for groups that
        did not participate in the match.
        """
        ...
    @overload
    def groupdict(self, default: _T) -> dict[str, AnyStr | _T]:
        """
        groupdict(default=None) --> dict.
        Return a dictionary containing all the named subgroups of the match, keyed
        by the subgroup name.  The argument is the value to be given for groups that
        did not participate in the match.
        """
        ...
    @overload
    def span(self, group: int | str = ..., /) -> tuple[int, int]:
        """
        span([group1, ...]) --> 2-tuple of int or tuple of 2-tuple of ints.
        Return the span (a 2-tuple of the indices of the start and end) of one or
        more subgroups of the match.  If there is a single argument, the result is a
        span, or (-1, -1) if the group did not contribute to the match; if there are
        multiple arguments, the result is a tuple with one item per argument; if
        there are no arguments, the span of the whole match is returned.  Group 0 is
        the whole match.
        """
        ...
    @overload
    def span(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[tuple[int, int], ...]:
        """
        span([group1, ...]) --> 2-tuple of int or tuple of 2-tuple of ints.
        Return the span (a 2-tuple of the indices of the start and end) of one or
        more subgroups of the match.  If there is a single argument, the result is a
        span, or (-1, -1) if the group did not contribute to the match; if there are
        multiple arguments, the result is a tuple with one item per argument; if
        there are no arguments, the span of the whole match is returned.  Group 0 is
        the whole match.
        """
        ...
    @overload
    def spans(self, group: int | str = ..., /) -> list[tuple[int, int]]:
        """
        spans([group1, ...]) --> list of 2-tuple of ints or tuple of list of 2-tuple of ints.
        Return the spans (a 2-tuple of the indices of the start and end) of the
        captures of one or more subgroups of the match.  If there is a single
        argument, the result is a list of spans; if there are multiple arguments,
        the result is a tuple of lists with one item per argument; if there are no
        arguments, the spans of the captures of the whole match is returned.  Group
        0 is the whole match.
        """
        ...
    @overload
    def spans(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[list[tuple[int, int]], ...]:
        """
        spans([group1, ...]) --> list of 2-tuple of ints or tuple of list of 2-tuple of ints.
        Return the spans (a 2-tuple of the indices of the start and end) of the
        captures of one or more subgroups of the match.  If there is a single
        argument, the result is a list of spans; if there are multiple arguments,
        the result is a tuple of lists with one item per argument; if there are no
        arguments, the spans of the captures of the whole match is returned.  Group
        0 is the whole match.
        """
        ...
    @overload
    def start(self, group: int | str = ..., /) -> int:
        """
        start([group1, ...]) --> int or tuple of ints.
        Return the index of the start of one or more subgroups of the match.  If
        there is a single argument, the result is an index, or -1 if the group did
        not contribute to the match; if there are multiple arguments, the result is
        a tuple with one item per argument; if there are no arguments, the index of
        the start of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def start(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[int, ...]:
        """
        start([group1, ...]) --> int or tuple of ints.
        Return the index of the start of one or more subgroups of the match.  If
        there is a single argument, the result is an index, or -1 if the group did
        not contribute to the match; if there are multiple arguments, the result is
        a tuple with one item per argument; if there are no arguments, the index of
        the start of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def starts(self, group: int | str = ..., /) -> list[int]:
        """
        starts([group1, ...]) --> list of ints or tuple of list of ints.
        Return the indices of the starts of the captures of one or more subgroups of
        the match.  If there is a single argument, the result is a list of indices;
        if there are multiple arguments, the result is a tuple of lists with one
        item per argument; if there are no arguments, the indices of the starts of
        the captures of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def starts(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[list[int], ...]:
        """
        starts([group1, ...]) --> list of ints or tuple of list of ints.
        Return the indices of the starts of the captures of one or more subgroups of
        the match.  If there is a single argument, the result is a list of indices;
        if there are multiple arguments, the result is a tuple of lists with one
        item per argument; if there are no arguments, the indices of the starts of
        the captures of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def end(self, group: int | str = ..., /) -> int:
        """
        end([group1, ...]) --> int or tuple of ints.
        Return the index of the end of one or more subgroups of the match.  If there
        is a single argument, the result is an index, or -1 if the group did not
        contribute to the match; if there are multiple arguments, the result is a
        tuple with one item per argument; if there are no arguments, the index of
        the end of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def end(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[int, ...]:
        """
        end([group1, ...]) --> int or tuple of ints.
        Return the index of the end of one or more subgroups of the match.  If there
        is a single argument, the result is an index, or -1 if the group did not
        contribute to the match; if there are multiple arguments, the result is a
        tuple with one item per argument; if there are no arguments, the index of
        the end of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def ends(self, group: int | str = ..., /) -> list[int]:
        """
        ends([group1, ...]) --> list of ints or tuple of list of ints.
        Return the indices of the ends of the captures of one or more subgroups of
        the match.  If there is a single argument, the result is a list of indices;
        if there are multiple arguments, the result is a tuple of lists with one
        item per argument; if there are no arguments, the indices of the ends of the
        captures of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    @overload
    def ends(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[list[int], ...]:
        """
        ends([group1, ...]) --> list of ints or tuple of list of ints.
        Return the indices of the ends of the captures of one or more subgroups of
        the match.  If there is a single argument, the result is a list of indices;
        if there are multiple arguments, the result is a tuple of lists with one
        item per argument; if there are no arguments, the indices of the ends of the
        captures of the whole match is returned.  Group 0 is the whole match.
        """
        ...
    def expand(self, template: AnyStr, /) -> AnyStr:
        """
        expand(template) --> string.
        Return the string obtained by doing backslash substitution on the template,
        as done by the sub() method.
        """
        ...
    def expandf(self, format: AnyStr, /) -> AnyStr:
        """
        expandf(format) --> string.
        Return the string obtained by using the format, as done by the subf()
        method.
        """
        ...
    @overload
    def captures(self, group: int | str = ..., /) -> list[AnyStr]:
        """
        captures([group1, ...]) --> list of strings or tuple of list of strings.
        Return the captures of one or more subgroups of the match.  If there is a
        single argument, the result is a list of strings; if there are multiple
        arguments, the result is a tuple of lists with one item per argument; if
        there are no arguments, the captures of the whole match is returned.  Group
        0 is the whole match.
        """
        ...
    @overload
    def captures(self, group1: int | str, group2: int | str, /, *groups: int | str) -> tuple[list[AnyStr], ...]:
        """
        captures([group1, ...]) --> list of strings or tuple of list of strings.
        Return the captures of one or more subgroups of the match.  If there is a
        single argument, the result is a list of strings; if there are multiple
        arguments, the result is a tuple of lists with one item per argument; if
        there are no arguments, the captures of the whole match is returned.  Group
        0 is the whole match.
        """
        ...
    def capturesdict(self) -> dict[str, list[AnyStr]]:
        """
        capturesdict() --> dict.
        Return a dictionary containing the captures of all the named subgroups of the
        match, keyed by the subgroup name.
        """
        ...
    def detach_string(self) -> None:
        """
        detach_string()
        Detaches the target string from the match object. The 'string' attribute
        will become None.
        """
        ...
    def allcaptures(self) -> tuple[list[AnyStr]]:
        """
        allcaptures() --> list of strings or tuple of list of strings.
        Return the captures of all the groups of the match and the whole match.
        """
        ...
    def allspans(self) -> tuple[list[tuple[int, int]]]:
        """
        allspans() --> list of 2-tuple of ints or tuple of list of 2-tuple of ints.
        Return the spans (a 2-tuple of the indices of the start and end) of all the
        captures of all the groups of the match and the whole match.
        """
        ...
    @overload
    def __getitem__(self, key: Literal[0], /) -> AnyStr: ...
    @overload
    def __getitem__(self, key: int | str, /) -> AnyStr | Any: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: Unused, /) -> Self: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
