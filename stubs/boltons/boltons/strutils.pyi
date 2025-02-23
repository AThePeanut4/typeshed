from _typeshed import ReadableBuffer
from collections.abc import Callable, Generator, Iterable, Sized
from html.parser import HTMLParser
from re import Pattern
from typing import Literal, overload

def camel2under(camel_string: str) -> str: ...
def under2camel(under_string: str) -> str: ...
@overload
def slugify(text: str, delim: str = "_", lower: bool = True, *, ascii: Literal[True]) -> bytes: ...
@overload
def slugify(text: str, delim: str, lower: bool, ascii: Literal[True]) -> bytes: ...
@overload
def slugify(text: str, delim: str = "_", lower: bool = True, ascii: Literal[False] = False) -> str: ...
def split_punct_ws(text: str) -> list[str]: ...
def unit_len(sized_iterable: Sized, unit_noun: str = "item") -> str: ...
def ordinalize(number: int | str, ext_only: bool = False) -> str: ...
def cardinalize(unit_noun: str, count: int) -> str: ...
def singularize(word: str) -> str: ...
def pluralize(word: str) -> str: ...
def find_hashtags(string: str) -> list[str]: ...
def a10n(string: str) -> str: ...
def strip_ansi(text: str) -> str: ...
def asciify(text: str | bytes | bytearray, ignore: bool = False) -> bytes: ...
def is_ascii(text: str) -> bool: ...

class DeaccenterDict(dict[int, int]):
    def __missing__(self, key: int) -> int: ...

def bytes2human(nbytes: int, ndigits: int = 0) -> str:
    """
    Turns an integer value of *nbytes* into a human readable format. Set
    *ndigits* to control how many digits after the decimal point
    should be shown (default ``0``).

    >>> bytes2human(128991)
    '126K'
    >>> bytes2human(100001221)
    '95M'
    >>> bytes2human(0, 2)
    '0.00B'
    """
    ...

class HTMLTextExtractor(HTMLParser):
    strict: bool
    convert_charrefs: bool
    result: list[str]
    def __init__(self) -> None: ...
    def handle_data(self, d: str) -> None: ...
    def handle_charref(self, number: str) -> None: ...
    def handle_entityref(self, name: str) -> None: ...
    def get_text(self) -> str: ...

def html2text(html: str) -> str: ...
def gunzip_bytes(bytestring: ReadableBuffer) -> bytes: ...
def gzip_bytes(bytestring: ReadableBuffer, level: int = 6) -> int: ...
def iter_splitlines(text: str) -> Generator[str, None, None]: ...
def indent(text: str, margin: str, newline: str = "\n", key: Callable[[str], bool] = ...) -> str: ...
def is_uuid(obj, version: int = 4) -> bool: ...
def escape_shell_args(args: Iterable[str], sep: str = " ", style: Literal["cmd", "sh"] | None = None) -> str: ...
def args2sh(args: Iterable[str], sep: str = " ") -> str: ...
def args2cmd(args: Iterable[str], sep: str = " ") -> str: ...
def parse_int_list(range_string: str, delim: str = ",", range_delim: str = "-") -> list[int]: ...
def format_int_list(int_list: list[int], delim: str = ",", range_delim: str = "-", delim_space: bool = False) -> str: ...
def complement_int_list(
    range_string: str, range_start: int = 0, range_end: int | None = None, delim: str = ",", range_delim: str = "-"
) -> str:
    """
    Returns range string that is the complement of the one provided as
    *range_string* parameter.

    These range strings are of the kind produce by :func:`format_int_list`, and
    parseable by :func:`parse_int_list`.

    Args:
        range_string (str): String of comma separated positive integers or
           ranges (e.g. '1,2,4-6,8'). Typical of a custom page range string
           used in printer dialogs.
        range_start (int): A positive integer from which to start the resulting
           range. Value is inclusive. Defaults to ``0``.
        range_end (int): A positive integer from which the produced range is
           stopped. Value is exclusive. Defaults to the maximum value found in
           the provided ``range_string``.
        delim (char): Defaults to ','. Separates integers and contiguous ranges
           of integers.
        range_delim (char): Defaults to '-'. Indicates a contiguous range of
           integers.

    >>> complement_int_list('1,3,5-8,10-11,15')
    '0,2,4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_start=0)
    '0,2,4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_start=1)
    '2,4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_start=2)
    '2,4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_start=3)
    '4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_end=15)
    '0,2,4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_end=14)
    '0,2,4,9,12-13'

    >>> complement_int_list('1,3,5-8,10-11,15', range_end=13)
    '0,2,4,9,12'

    >>> complement_int_list('1,3,5-8,10-11,15', range_end=20)
    '0,2,4,9,12-14,16-19'

    >>> complement_int_list('1,3,5-8,10-11,15', range_end=0)
    ''

    >>> complement_int_list('1,3,5-8,10-11,15', range_start=-1)
    '0,2,4,9,12-14'

    >>> complement_int_list('1,3,5-8,10-11,15', range_end=-1)
    ''

    >>> complement_int_list('1,3,5-8', range_start=1, range_end=1)
    ''

    >>> complement_int_list('1,3,5-8', range_start=2, range_end=2)
    ''

    >>> complement_int_list('1,3,5-8', range_start=2, range_end=3)
    '2'

    >>> complement_int_list('1,3,5-8', range_start=-10, range_end=-5)
    ''

    >>> complement_int_list('1,3,5-8', range_start=20, range_end=10)
    ''

    >>> complement_int_list('')
    ''
    """
    ...
def int_ranges_from_int_list(range_string: str, delim: str = ",", range_delim: str = "-") -> tuple[int, int]:
    """
    Transform a string of ranges (*range_string*) into a tuple of tuples.

    Args:
        range_string (str): String of comma separated positive integers or
           ranges (e.g. '1,2,4-6,8'). Typical of a custom page range string
           used in printer dialogs.
        delim (char): Defaults to ','. Separates integers and contiguous ranges
           of integers.
        range_delim (char): Defaults to '-'. Indicates a contiguous range of
           integers.

    >>> int_ranges_from_int_list('1,3,5-8,10-11,15')
    ((1, 1), (3, 3), (5, 8), (10, 11), (15, 15))

    >>> int_ranges_from_int_list('1')
    ((1, 1),)

    >>> int_ranges_from_int_list('')
    ()
    """
    ...

class MultiReplace:
    """
    MultiReplace is a tool for doing multiple find/replace actions in one pass.

    Given a mapping of values to be replaced it allows for all of the matching
    values to be replaced in a single pass which can save a lot of performance
    on very large strings. In addition to simple replace, it also allows for
    replacing based on regular expressions.

    Keyword Arguments:

    :type regex: bool
    :param regex: Treat search keys as regular expressions [Default: False]
    :type flags: int
    :param flags: flags to pass to the regex engine during compile

    Dictionary Usage::

        from boltons import strutils
        s = strutils.MultiReplace({
            'foo': 'zoo',
            'cat': 'hat',
            'bat': 'kraken'
        })
        new = s.sub('The foo bar cat ate a bat')
        new == 'The zoo bar hat ate a kraken'

    Iterable Usage::

        from boltons import strutils
        s = strutils.MultiReplace([
            ('foo', 'zoo'),
            ('cat', 'hat'),
            ('bat', 'kraken)'
        ])
        new = s.sub('The foo bar cat ate a bat')
        new == 'The zoo bar hat ate a kraken'


    The constructor can be passed a dictionary or other mapping as well as
    an iterable of tuples. If given an iterable, the substitution will be run
    in the order the replacement values are specified in the iterable. This is
    also true if it is given an OrderedDict. If given a dictionary then the
    order will be non-deterministic::

        >>> 'foo bar baz'.replace('foo', 'baz').replace('baz', 'bar')
        'bar bar bar'
        >>> m = MultiReplace({'foo': 'baz', 'baz': 'bar'})
        >>> m.sub('foo bar baz')
        'baz bar bar'

    This is because the order of replacement can matter if you're inserting
    something that might be replaced by a later substitution. Pay attention and
    if you need to rely on order then consider using a list of tuples instead
    of a dictionary.
    """
    group_map: dict[str, str]
    combined_pattern: Pattern[str]
    def __init__(self, sub_map: dict[str, str], **kwargs) -> None: ...
    def sub(self, text: str) -> str: ...

def multi_replace(text: str, sub_map: dict[str, str], **kwargs) -> str: ...
def unwrap_text(text: str, ending: str | None = "\n\n") -> str: ...
def removeprefix(text: str, prefix: str) -> str: ...
