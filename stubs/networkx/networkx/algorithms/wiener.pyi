"""
Functions related to the Wiener Index of a graph.

The Wiener Index is a topological measure of a graph
related to the distance between nodes and their degree.
The Schultz Index and Gutman Index are similar measures.
They are used categorize molecules via the network of
atoms connected by chemical bonds. The indices are
correlated with functional aspects of the molecules.

References
----------
.. [1] `Wikipedia: Wiener Index <https://en.wikipedia.org/wiki/Wiener_index>`_
.. [2] M.V. Diudeaa and I. Gutman, Wiener-Type Topological Indices,
       Croatica Chemica Acta, 71 (1998), 21-51.
       https://hrcak.srce.hr/132323
"""

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["wiener_index", "schultz_index", "gutman_index"]

@_dispatchable
def wiener_index(G: Graph[_Node], weight: str | None = None): ...
@_dispatchable
def schultz_index(G, weight=None) -> float: ...
@_dispatchable
def gutman_index(G, weight=None) -> float: ...
