"""
`PEP 3101`_ introduced the :meth:`str.format` method, and what
would later be called "new-style" string formatting. For the sake of
explicit correctness, it is probably best to refer to Python's dual
string formatting capabilities as *bracket-style* and
*percent-style*. There is overlap, but one does not replace the
other.

  * Bracket-style is more pluggable, slower, and uses a method.
  * Percent-style is simpler, faster, and uses an operator.

Bracket-style formatting brought with it a much more powerful toolbox,
but it was far from a full one. :meth:`str.format` uses `more powerful
syntax`_, but `the tools and idioms`_ for working with
that syntax are not well-developed nor well-advertised.

``formatutils`` adds several functions for working with bracket-style
format strings:

  * :class:`DeferredValue`: Defer fetching or calculating a value
    until format time.
  * :func:`get_format_args`: Parse the positional and keyword
    arguments out of a format string.
  * :func:`tokenize_format_str`: Tokenize a format string into
    literals and :class:`BaseFormatField` objects.
  * :func:`construct_format_field_str`: Assists in programmatic
    construction of format strings.
  * :func:`infer_positional_format_args`: Converts anonymous
    references in 2.7+ format strings to explicit positional arguments
    suitable for usage with Python 2.6.

.. _more powerful syntax: https://docs.python.org/2/library/string.html#format-string-syntax
.. _the tools and idioms: https://docs.python.org/2/library/string.html#string-formatting
.. _PEP 3101: https://www.python.org/dev/peps/pep-3101/
"""

from collections.abc import Callable
from typing import Generic, TypeVar

_T = TypeVar("_T")

def construct_format_field_str(fname: str | None, fspec: str | None, conv: str | None) -> str: ...
def infer_positional_format_args(fstr: str) -> str: ...
def get_format_args(fstr: str) -> tuple[list[tuple[int, type]], list[tuple[str, type]]]: ...
def tokenize_format_str(fstr: str, resolve_pos: bool = True) -> list[str | BaseFormatField]: ...

class BaseFormatField:
    """
    A class representing a reference to an argument inside of a
    bracket-style format string. For instance, in ``"{greeting},
    world!"``, there is a field named "greeting".

    These fields can have many options applied to them. See the
    Python docs on `Format String Syntax`_ for the full details.

    .. _Format String Syntax: https://docs.python.org/2/library/string.html#string-formatting
    """
    def __init__(self, fname: str, fspec: str = "", conv: str | None = None) -> None: ...
    base_name: str
    fname: str
    subpath: str
    is_positional: bool
    def set_fname(self, fname: str) -> None:
        """Set the field name."""
        ...
    subfields: list[str]
    fspec: str
    type_char: str
    type_func: str
    def set_fspec(self, fspec) -> None: ...
    conv: str | None
    conv_func: str | None
    def set_conv(self, conv: str | None) -> None: ...
    @property
    def fstr(self) -> str:
        """The current state of the field in string format."""
        ...

class DeferredValue(Generic[_T]):
    func: Callable[[], _T]
    cache_value: bool
    def __init__(self, func: Callable[[], _T], cache_value: bool = True) -> None: ...
    def get_value(self) -> _T: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __unicode__(self) -> str: ...
    def __format__(self, fmt: str) -> str: ...
