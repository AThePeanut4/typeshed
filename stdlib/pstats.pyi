"""Class for printing reports on profiled python code."""

import sys
from _typeshed import StrOrBytesPath
from collections.abc import Iterable
from cProfile import Profile as _cProfile
from dataclasses import dataclass
from profile import Profile
from typing import IO, Any, Literal, overload
from typing_extensions import Self, TypeAlias

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from enum import Enum

__all__ = ["Stats", "SortKey", "FunctionProfile", "StatsProfile"]

_Selector: TypeAlias = str | float | int

if sys.version_info >= (3, 11):
    class SortKey(StrEnum):
        """An enumeration."""
        CALLS = "calls"
        CUMULATIVE = "cumulative"
        FILENAME = "filename"
        LINE = "line"
        NAME = "name"
        NFL = "nfl"
        PCALLS = "pcalls"
        STDNAME = "stdname"
        TIME = "time"

else:
    class SortKey(str, Enum):
        """An enumeration."""
        CALLS = "calls"
        CUMULATIVE = "cumulative"
        FILENAME = "filename"
        LINE = "line"
        NAME = "name"
        NFL = "nfl"
        PCALLS = "pcalls"
        STDNAME = "stdname"
        TIME = "time"

@dataclass(unsafe_hash=True)
class FunctionProfile:
    """FunctionProfile(ncalls: str, tottime: float, percall_tottime: float, cumtime: float, percall_cumtime: float, file_name: str, line_number: int)"""
    ncalls: str
    tottime: float
    percall_tottime: float
    cumtime: float
    percall_cumtime: float
    file_name: str
    line_number: int

@dataclass(unsafe_hash=True)
class StatsProfile:
    """Class for keeping track of an item in inventory."""
    total_tt: float
    func_profiles: dict[str, FunctionProfile]

_SortArgDict: TypeAlias = dict[str, tuple[tuple[tuple[int, int], ...], str]]

class Stats:
    """
    This class is used for creating reports from data generated by the
    Profile class.  It is a "friend" of that class, and imports data either
    by direct access to members of Profile class, or by reading in a dictionary
    that was emitted (via marshal) from the Profile class.

    The big change from the previous Profiler (in terms of raw functionality)
    is that an "add()" method has been provided to combine Stats from
    several distinct profile runs.  Both the constructor and the add()
    method now take arbitrarily many file names as arguments.

    All the print methods now take an argument that indicates how many lines
    to print.  If the arg is a floating-point number between 0 and 1.0, then
    it is taken as a decimal percentage of the available lines to be printed
    (e.g., .1 means print 10% of all available lines).  If it is an integer,
    it is taken to mean the number of lines of data that you wish to have
    printed.

    The sort_stats() method now processes some additional options (i.e., in
    addition to the old -1, 0, 1, or 2 that are respectively interpreted as
    'stdname', 'calls', 'time', and 'cumulative').  It takes either an
    arbitrary number of quoted strings or SortKey enum to select the sort
    order.

    For example sort_stats('time', 'name') or sort_stats(SortKey.TIME,
    SortKey.NAME) sorts on the major key of 'internal function time', and on
    the minor key of 'the name of the function'.  Look at the two tables in
    sort_stats() and get_sort_arg_defs(self) for more examples.

    All methods return self, so you can string together commands like:
        Stats('foo', 'goo').strip_dirs().sort_stats('calls').                            print_stats(5).print_callers(5)
    """
    sort_arg_dict_default: _SortArgDict
    def __init__(
        self,
        arg: None | str | Profile | _cProfile = ...,
        /,
        *args: None | str | Profile | _cProfile | Self,
        stream: IO[Any] | None = None,
    ) -> None: ...
    def init(self, arg: None | str | Profile | _cProfile) -> None: ...
    def load_stats(self, arg: None | str | Profile | _cProfile) -> None: ...
    def get_top_level_stats(self) -> None: ...
    def add(self, *arg_list: None | str | Profile | _cProfile | Self) -> Self: ...
    def dump_stats(self, filename: StrOrBytesPath) -> None:
        """Write the profile data to a file we know how to load back."""
        ...
    def get_sort_arg_defs(self) -> _SortArgDict:
        """Expand all abbreviations that are unique."""
        ...
    @overload
    def sort_stats(self, field: Literal[-1, 0, 1, 2]) -> Self: ...
    @overload
    def sort_stats(self, *field: str) -> Self: ...
    def reverse_order(self) -> Self: ...
    def strip_dirs(self) -> Self: ...
    def calc_callees(self) -> None: ...
    def eval_print_amount(self, sel: _Selector, list: list[str], msg: str) -> tuple[list[str], str]: ...
    def get_stats_profile(self) -> StatsProfile:
        """
        This method returns an instance of StatsProfile, which contains a mapping
        of function names to instances of FunctionProfile. Each FunctionProfile
        instance holds information related to the function's profile such as how
        long the function took to run, how many times it was called, etc...
        """
        ...
    def get_print_list(self, sel_list: Iterable[_Selector]) -> tuple[int, list[str]]: ...
    def print_stats(self, *amount: _Selector) -> Self: ...
    def print_callees(self, *amount: _Selector) -> Self: ...
    def print_callers(self, *amount: _Selector) -> Self: ...
    def print_call_heading(self, name_size: int, column_title: str) -> None: ...
    def print_call_line(self, name_size: int, source: str, call_dict: dict[str, Any], arrow: str = "->") -> None: ...
    def print_title(self) -> None: ...
    def print_line(self, func: str) -> None: ...
