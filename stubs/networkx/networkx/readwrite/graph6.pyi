"""
Functions for reading and writing graphs in the *graph6* format.

The *graph6* file format is suitable for small graphs or large dense
graphs. For large sparse graphs, use the *sparse6* format.

For more information, see the `graph6`_ homepage.

.. _graph6: http://users.cecs.anu.edu.au/~bdm/data/formats.html
"""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["from_graph6_bytes", "read_graph6", "to_graph6_bytes", "write_graph6"]

@_dispatchable
def from_graph6_bytes(bytes_in) -> Graph[Incomplete]: ...
def to_graph6_bytes(G: Graph[_Node], nodes=None, header: bool = True): ...
@_dispatchable
def read_graph6(path): ...
def write_graph6(G: Graph[_Node], path, nodes=None, header: bool = True): ...
def write_graph6_file(G: Graph[_Node], f, nodes: Iterable[Incomplete] | None = None, header: bool = True): ...
def data_to_n(data): ...
def n_to_data(n): ...
