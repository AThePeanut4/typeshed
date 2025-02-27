"""
=============================
Breadth First Search on Edges
=============================

Algorithms for a breadth-first traversal of edges in a graph.
"""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def edge_bfs(G: Graph[_Node], source=None, orientation=None) -> Generator[Incomplete, None, Incomplete]: ...
