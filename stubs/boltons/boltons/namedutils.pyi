"""
The ``namedutils`` module defines two lightweight container types:
:class:`namedtuple` and :class:`namedlist`. Both are subtypes of built-in
sequence types, which are very fast and efficient. They simply add
named attribute accessors for specific indexes within themselves.

The :class:`namedtuple` is identical to the built-in
:class:`collections.namedtuple`, with a couple of enhancements,
including a ``__repr__`` more suitable to inheritance.

The :class:`namedlist` is the mutable counterpart to the
:class:`namedtuple`, and is much faster and lighter-weight than
full-blown :class:`object`. Consider this if you're implementing nodes
in a tree, graph, or other mutable data structure. If you want an even
skinnier approach, you'll probably have to look to C.
"""

from collections.abc import Iterable

def namedtuple(typename: str, field_names: str | Iterable[str], verbose: bool = False, rename: bool = False): ...
def namedlist(typename: str, field_names: str | Iterable[str], verbose: bool = False, rename: bool = False): ...

__all__ = ["namedlist", "namedtuple"]
