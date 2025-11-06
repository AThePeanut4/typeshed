"""
Functions for computing treewidth decomposition.

Treewidth of an undirected graph is a number associated with the graph.
It can be defined as the size of the largest vertex set (bag) in a tree
decomposition of the graph minus one.

`Wikipedia: Treewidth <https://en.wikipedia.org/wiki/Treewidth>`_

The notions of treewidth and tree decomposition have gained their
attractiveness partly because many graph and network problems that are
intractable (e.g., NP-hard) on arbitrary graphs become efficiently
solvable (e.g., with a linear time algorithm) when the treewidth of the
input graphs is bounded by a constant [1]_ [2]_.

There are two different functions for computing a tree decomposition:
:func:`treewidth_min_degree` and :func:`treewidth_min_fill_in`.

.. [1] Hans L. Bodlaender and Arie M. C. A. Koster. 2010. "Treewidth
      computations I.Upper bounds". Inf. Comput. 208, 3 (March 2010),259-275.
      http://dx.doi.org/10.1016/j.ic.2009.03.008

.. [2] Hans L. Bodlaender. "Discovering Treewidth". Institute of Information
      and Computing Sciences, Utrecht University.
      Technical Report UU-CS-2005-018.
      http://www.cs.uu.nl

.. [3] K. Wang, Z. Lu, and J. Hicks *Treewidth*.
      https://web.archive.org/web/20210507025929/http://web.eecs.utk.edu/~cphill25/cs594_spring2015_projects/treewidth.pdf
"""

from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from typing import Generic

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["treewidth_min_degree", "treewidth_min_fill_in"]

@_dispatchable
def treewidth_min_degree(G: Graph[_Node]) -> tuple[int, Graph[frozenset[_Node]]]: ...
@_dispatchable
def treewidth_min_fill_in(G: Graph[_Node]) -> tuple[int, Graph[frozenset[_Node]]]: ...

class MinDegreeHeuristic(Generic[_Node]):
    count: Incomplete

    def __init__(self, graph: Graph[_Node]) -> None: ...
    def best_node(self, graph: Mapping[_Node, set[_Node]]) -> _Node | None: ...

def min_fill_in_heuristic(graph_dict: Mapping[_Node, set[_Node]]) -> _Node | None: ...
@_dispatchable
def treewidth_decomp(
    G: Graph[_Node], heuristic: Callable[[dict[_Node, set[_Node]]], _Node | None] = ...
) -> tuple[int, Graph[frozenset[_Node]]]: ...
