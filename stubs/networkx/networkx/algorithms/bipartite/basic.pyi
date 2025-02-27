"""
==========================
Bipartite Graph Algorithms
==========================
"""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def color(G: Graph[_Node]): ...
@_dispatchable
def is_bipartite(G: Graph[_Node]): ...
@_dispatchable
def is_bipartite_node_set(G: Graph[_Node], nodes): ...
@_dispatchable
def sets(G: Graph[_Node], top_nodes: Iterable[Incomplete] | None = None): ...
@_dispatchable
def density(B: Graph[_Node], nodes): ...
@_dispatchable
def degrees(B: Graph[_Node], nodes, weight: str | None = None): ...
