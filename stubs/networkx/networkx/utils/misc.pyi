"""
Miscellaneous Helpers for NetworkX.

These are not imported into the base networkx namespace but
can be accessed, for example, as

>>> import networkx as nx
>>> nx.utils.make_list_of_ints({1, 2, 3})
[1, 2, 3]
>>> nx.utils.arbitrary_element({5, 1, 7})  # doctest: +SKIP
1
"""

import random
import sys
from types import ModuleType
from typing_extensions import Self, TypeAlias

import numpy
from networkx.classes.graph import Graph, _Node

__all__ = [
    "flatten",
    "make_list_of_ints",
    "dict_to_numpy_array",
    "arbitrary_element",
    "pairwise",
    "groups",
    "create_random_state",
    "create_py_random_state",
    "PythonRandomInterface",
    "PythonRandomViaNumpyBits",
    "nodes_equal",
    "edges_equal",
    "graphs_equal",
    "_clear_cache",
]

_RandomNumberGenerator: TypeAlias = (
    ModuleType | random.Random | numpy.random.RandomState | numpy.random.Generator | PythonRandomInterface
)
_RandomState: TypeAlias = int | _RandomNumberGenerator | None

def flatten(obj, result=None):
    """Return flattened version of (possibly nested) iterable object."""
    ...
def make_list_of_ints(sequence):
    """
    Return list of ints from sequence of integral numbers.

    All elements of the sequence must satisfy int(element) == element
    or a ValueError is raised. Sequence is iterated through once.

    If sequence is a list, the non-int values are replaced with ints.
    So, no new list is created
    """
    ...
def dict_to_numpy_array(d, mapping=None):
    """
    Convert a dictionary of dictionaries to a numpy array
    with optional mapping.
    """
    ...
def arbitrary_element(iterable):
    """
    Returns an arbitrary element of `iterable` without removing it.

    This is most useful for "peeking" at an arbitrary element of a set,
    but can be used for any list, dictionary, etc., as well.

    Parameters
    ----------
    iterable : `abc.collections.Iterable` instance
        Any object that implements ``__iter__``, e.g. set, dict, list, tuple,
        etc.

    Returns
    -------
    The object that results from ``next(iter(iterable))``

    Raises
    ------
    ValueError
        If `iterable` is an iterator (because the current implementation of
        this function would consume an element from the iterator).

    Examples
    --------
    Arbitrary elements from common Iterable objects:

    >>> nx.utils.arbitrary_element([1, 2, 3])  # list
    1
    >>> nx.utils.arbitrary_element((1, 2, 3))  # tuple
    1
    >>> nx.utils.arbitrary_element({1, 2, 3})  # set
    1
    >>> d = {k: v for k, v in zip([1, 2, 3], [3, 2, 1])}
    >>> nx.utils.arbitrary_element(d)  # dict_keys
    1
    >>> nx.utils.arbitrary_element(d.values())  # dict values
    3

    `str` is also an Iterable:

    >>> nx.utils.arbitrary_element("hello")
    'h'

    :exc:`ValueError` is raised if `iterable` is an iterator:

    >>> iterator = iter([1, 2, 3])  # Iterator, *not* Iterable
    >>> nx.utils.arbitrary_element(iterator)
    Traceback (most recent call last):
        ...
    ValueError: cannot return an arbitrary item from an iterator

    Notes
    -----
    This function does not return a *random* element. If `iterable` is
    ordered, sequential calls will return the same value::

        >>> l = [1, 2, 3]
        >>> nx.utils.arbitrary_element(l)
        1
        >>> nx.utils.arbitrary_element(l)
        1
    """
    ...
def pairwise(iterable, cyclic: bool = False):
    """s -> (s0, s1), (s1, s2), (s2, s3), ..."""
    ...
def groups(many_to_one):
    """
    Converts a many-to-one mapping into a one-to-many mapping.

    `many_to_one` must be a dictionary whose keys and values are all
    :term:`hashable`.

    The return value is a dictionary mapping values from `many_to_one`
    to sets of keys from `many_to_one` that have that value.

    Examples
    --------
    >>> from networkx.utils import groups
    >>> many_to_one = {"a": 1, "b": 1, "c": 2, "d": 3, "e": 3}
    >>> groups(many_to_one)  # doctest: +SKIP
    {1: {'a', 'b'}, 2: {'c'}, 3: {'e', 'd'}}
    """
    ...
def create_random_state(random_state=None):
    """
    Returns a numpy.random.RandomState or numpy.random.Generator instance
    depending on input.

    Parameters
    ----------
    random_state : int or NumPy RandomState or Generator instance, optional (default=None)
        If int, return a numpy.random.RandomState instance set with seed=int.
        if `numpy.random.RandomState` instance, return it.
        if `numpy.random.Generator` instance, return it.
        if None or numpy.random, return the global random number generator used
        by numpy.random.
    """
    ...

class PythonRandomViaNumpyBits(random.Random):
    """
    Provide the random.random algorithms using a numpy.random bit generator

    The intent is to allow people to contribute code that uses Python's random
    library, but still allow users to provide a single easily controlled random
    bit-stream for all work with NetworkX. This implementation is based on helpful
    comments and code from Robert Kern on NumPy's GitHub Issue #24458.

    This implementation supersedes that of `PythonRandomInterface` which rewrote
    methods to account for subtle differences in API between `random` and
    `numpy.random`. Instead this subclasses `random.Random` and overwrites
    the methods `random`, `getrandbits`, `getstate`, `setstate` and `seed`.
    It makes them use the rng values from an input numpy `RandomState` or `Generator`.
    Those few methods allow the rest of the `random.Random` methods to provide
    the API interface of `random.random` while using randomness generated by
    a numpy generator.
    """
    def __init__(self, rng: numpy.random.Generator | None = None) -> None: ...
    if sys.version_info < (3, 10):
        # this is a workaround for pyright correctly flagging an inconsistent inherited constructor, see #14624
        def __new__(cls, rng: numpy.random.Generator | None = None) -> Self: ...

    def getrandbits(self, k: int) -> int:
        """getrandbits(k) -> x.  Generates an int with k random bits."""
        ...

class PythonRandomInterface:
    """
    PythonRandomInterface is included for backward compatibility
    New code should use PythonRandomViaNumpyBits instead.
    """
    def __init__(self, rng=None) -> None: ...
    def random(self): ...
    def uniform(self, a, b): ...
    def randrange(self, a, b=None): ...
    def choice(self, seq): ...
    def gauss(self, mu, sigma): ...
    def shuffle(self, seq): ...
    def sample(self, seq, k): ...
    def randint(self, a, b): ...
    def expovariate(self, scale): ...
    def paretovariate(self, shape): ...

def create_py_random_state(random_state: _RandomState = None): ...
def nodes_equal(nodes1, nodes2) -> bool: ...
def edges_equal(edges1, edges2) -> bool: ...
def graphs_equal(graph1, graph2) -> bool: ...
def _clear_cache(G: Graph[_Node]) -> None: ...
