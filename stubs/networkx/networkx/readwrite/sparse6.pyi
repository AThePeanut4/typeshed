"""
Functions for reading and writing graphs in the *sparse6* format.

The *sparse6* file format is a space-efficient format for large sparse
graphs. For small graphs or large dense graphs, use the *graph6* file
format.

For more information, see the `sparse6`_ homepage.

.. _sparse6: https://users.cecs.anu.edu.au/~bdm/data/formats.html
"""

from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["from_sparse6_bytes", "read_sparse6", "to_sparse6_bytes", "write_sparse6"]

@_dispatchable
def from_sparse6_bytes(string) -> Graph[Incomplete]: ...
def to_sparse6_bytes(G: Graph[_Node], nodes=None, header: bool = True): ...
@_dispatchable
def read_sparse6(path): ...
def write_sparse6(G: Graph[_Node], path, nodes=None, header: bool = True) -> None: ...
