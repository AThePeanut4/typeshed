"""
Python has a very powerful mapping type at its core: the :class:`dict`
type. While versatile and featureful, the :class:`dict` prioritizes
simplicity and performance. As a result, it does not retain the order
of item insertion [1]_, nor does it store multiple values per key. It
is a fast, unordered 1:1 mapping.

The :class:`OrderedMultiDict` contrasts to the built-in :class:`dict`,
as a relatively maximalist, ordered 1:n subtype of
:class:`dict`. Virtually every feature of :class:`dict` has been
retooled to be intuitive in the face of this added
complexity. Additional methods have been added, such as
:class:`collections.Counter`-like functionality.

A prime advantage of the :class:`OrderedMultiDict` (OMD) is its
non-destructive nature. Data can be added to an :class:`OMD` without being
rearranged or overwritten. The property can allow the developer to
work more freely with the data, as well as make more assumptions about
where input data will end up in the output, all without any extra
work.

One great example of this is the :meth:`OMD.inverted()` method, which
returns a new OMD with the values as keys and the keys as values. All
the data and the respective order is still represented in the inverted
form, all from an operation which would be outright wrong and reckless
with a built-in :class:`dict` or :class:`collections.OrderedDict`.

The OMD has been performance tuned to be suitable for a wide range of
usages, including as a basic unordered MultiDict. Special
thanks to `Mark Williams`_ for all his help.

.. [1] As of 2015, `basic dicts on PyPy are ordered
   <http://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html>`_,
   and as of December 2017, `basic dicts in CPython 3 are now ordered
   <https://mail.python.org/pipermail/python-dev/2017-December/151283.html>`_, as
   well.
.. _Mark Williams: https://github.com/markrwilliams
"""

from _typeshed import SupportsKeysAndGetItem
from collections.abc import Generator, ItemsView, Iterable, KeysView, ValuesView
from typing import NoReturn, TypeVar, overload
from typing_extensions import Self, TypeAlias

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

class OrderedMultiDict(dict[_KT, _VT]):
    def add(self, k: _KT, v: _VT) -> None: ...
    def addlist(self, k: _KT, v: Iterable[_VT]) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> Self: ...
    def counts(self) -> Self: ...
    @classmethod
    def fromkeys(cls, keys: _KT, default: _VT | None = None) -> Self: ...  # type: ignore[override]
    @overload  # type: ignore[override]
    def get(self, k: _KT, default: None = None) -> _VT | None: ...
    @overload
    def get(self, k: _KT, default: _VT) -> _VT: ...
    def getlist(self, k: _KT, default: list[_VT] = ...) -> list[_VT]: ...
    def inverted(self) -> Self: ...
    def items(self, multi: bool = False) -> list[tuple[_KT, _VT]]: ...  # type: ignore[override]
    def iteritems(self, multi: bool = False) -> Generator[tuple[_KT, _VT], None, None]: ...
    def iterkeys(self, multi: bool = False) -> Generator[_KT, None, None]: ...
    def itervalues(self, multi: bool = False) -> Generator[_VT, None, None]: ...
    def keys(self, multi: bool = False) -> list[_KT]: ...  # type: ignore[override]
    def pop(self, k: _KT, default: _VT = ...) -> _VT: ...  # type: ignore[override]
    def popall(self, k: _KT, default: _VT = ...) -> list[_VT]: ...
    def poplast(self, k: _KT = ..., default: _VT = ...) -> _VT: ...
    @overload  # type: ignore[override]
    def setdefault(self, k: _KT, default: None = ...) -> _VT | None: ...
    @overload
    def setdefault(self, k: _KT, default: _VT) -> _VT: ...
    def sorted(self, key: _KT | None = None, reverse: bool = False) -> Self: ...
    def sortedvalues(self, key: _KT | None = None, reverse: bool = False) -> Self: ...
    def todict(self, multi: bool = False) -> dict[_KT, _VT]: ...
    def update(self, E: SupportsKeysAndGetItem[_KT, _VT] | Iterable[tuple[_KT, _VT]], **F) -> None: ...  # type: ignore[override]
    def update_extend(self, E: SupportsKeysAndGetItem[_KT, _VT] | Iterable[tuple[_KT, _VT]], **F) -> None: ...
    def values(self, multi: bool = False) -> list[_VT]: ...  # type: ignore[override]
    def viewitems(self) -> ItemsView[_KT, _VT]: ...
    def viewkeys(self) -> KeysView[_KT]: ...
    def viewvalues(self) -> ValuesView[_VT]: ...

OMD: TypeAlias = OrderedMultiDict[_KT, _VT]
MultiDict: TypeAlias = OrderedMultiDict[_KT, _VT]

class FastIterOrderedMultiDict(OrderedMultiDict[_KT, _VT]):  # undocumented
    """
    An OrderedMultiDict backed by a skip list.  Iteration over keys
    is faster and uses constant memory but adding duplicate key-value
    pairs is slower. Brainchild of Mark Williams.
    """
    def iteritems(self, multi: bool = False) -> Generator[tuple[_KT, _VT], None, None]: ...
    def iterkeys(self, multi: bool = False) -> Generator[_KT, None, None]: ...

class OneToOne(dict[_KT, _VT]):
    inv: OneToOne[_VT, _KT]
    def clear(self) -> None: ...
    def copy(self) -> Self: ...
    def pop(self, key: _KT, default: _VT | _T = ...) -> _VT | _T: ...
    def popitem(self) -> tuple[_KT, _VT]: ...
    def setdefault(self, key: _KT, default: _VT | None = None) -> _VT: ...
    @classmethod
    def unique(cls, *a, **kw) -> Self:
        """
        This alternate constructor for OneToOne will raise an exception
        when input values overlap. For instance:

        >>> OneToOne.unique({'a': 1, 'b': 1})
        Traceback (most recent call last):
        ...
        ValueError: expected unique values, got multiple keys for the following values: ...

        This even works across inputs:

        >>> a_dict = {'a': 2}
        >>> OneToOne.unique(a_dict, b=2)
        Traceback (most recent call last):
        ...
        ValueError: expected unique values, got multiple keys for the following values: ...
        """
        ...
    def update(self, dict_or_iterable, **kw) -> None: ...  # type: ignore[override]

class ManyToMany(dict[_KT, frozenset[_VT]]):
    """
    a dict-like entity that represents a many-to-many relationship
    between two groups of objects

    behaves like a dict-of-tuples; also has .inv which is kept
    up to date which is a dict-of-tuples in the other direction

    also, can be used as a directed graph among hashable python objects
    """
    data: dict[_KT, set[_VT]]
    inv: dict[_VT, set[_KT]]
    # def __contains__(self, key: _KT): ...
    def __delitem__(self, key: _KT) -> None: ...
    def __eq__(self, other): ...
    def __getitem__(self, key: _KT): ...
    def __init__(
        self, items: ManyToMany[_KT, _VT] | SupportsKeysAndGetItem[_KT, _VT] | tuple[_KT, _VT] | None = None
    ) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def __setitem__(self, key: _KT, vals: Iterable[_VT]) -> None: ...
    def add(self, key: _KT, val: _VT) -> None: ...
    def get(self, key: _KT, default: frozenset[_VT] = ...) -> frozenset[_VT]: ...  # type: ignore[override]
    def iteritems(self) -> Generator[tuple[_KT, _VT], None, None]: ...
    def keys(self): ...
    def remove(self, key: _KT, val: _VT) -> None: ...
    def replace(self, key: _KT, newkey: _KT) -> None:
        """replace instances of key by newkey"""
        ...
    def update(self, iterable: ManyToMany[_KT, _VT] | SupportsKeysAndGetItem[_KT, _VT] | tuple[_KT, _VT]) -> None:
        """given an iterable of (key, val), add them all"""
        ...

def subdict(d: dict[_KT, _VT], keep: Iterable[_KT] | None = None, drop: Iterable[_KT] | None = None) -> dict[_KT, _VT]:
    """
    Compute the "subdictionary" of a dict, *d*.

    A subdict is to a dict what a subset is a to set. If *A* is a
    subdict of *B*, that means that all keys of *A* are present in
    *B*.

    Returns a new dict with any keys in *drop* removed, and any keys
    in *keep* still present, provided they were in the original
    dict. *keep* defaults to all keys, *drop* defaults to empty, so
    without one of these arguments, calling this function is
    equivalent to calling ``dict()``.

    >>> from pprint import pprint as pp
    >>> pp(subdict({'a': 1, 'b': 2}))
    {'a': 1, 'b': 2}
    >>> subdict({'a': 1, 'b': 2, 'c': 3}, drop=['b', 'c'])
    {'a': 1}
    >>> pp(subdict({'a': 1, 'b': 2, 'c': 3}, keep=['a', 'c']))
    {'a': 1, 'c': 3}
    """
    ...

class FrozenHashError(TypeError): ...  # undocumented

class FrozenDict(dict[_KT, _VT]):
    """
    An immutable dict subtype that is hashable and can itself be used
    as a :class:`dict` key or :class:`set` entry. What
    :class:`frozenset` is to :class:`set`, FrozenDict is to
    :class:`dict`.

    There was once an attempt to introduce such a type to the standard
    library, but it was rejected: `PEP 416 <https://www.python.org/dev/peps/pep-0416/>`_.

    Because FrozenDict is a :class:`dict` subtype, it automatically
    works everywhere a dict would, including JSON serialization.
    """
    def __copy__(self) -> Self: ...
    @classmethod
    def fromkeys(cls, keys: Iterable[_KT], value: _VT | None = None) -> Self: ...  # type: ignore[override]
    def updated(self, *a, **kw) -> Self: ...
    # Can't noqa because of https://github.com/plinss/flake8-noqa/pull/30
    # Signature conflicts with superclass, so let's just omit it
    # def __ior__(self, *a, **kw) -> NoReturn: ...
    def __setitem__(self, *a, **kw) -> NoReturn: ...
    def __delitem__(self, *a, **kw) -> NoReturn: ...
    def update(self, *a, **kw) -> NoReturn: ...
    def pop(self, *a, **kw) -> NoReturn: ...
    def popitem(self, *a, **kw) -> NoReturn: ...
    def setdefault(self, *a, **kw) -> NoReturn: ...
    def clear(self, *a, **kw) -> NoReturn: ...
