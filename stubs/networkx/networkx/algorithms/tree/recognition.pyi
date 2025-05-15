"""
Recognition Tests
=================

A *forest* is an acyclic, undirected graph, and a *tree* is a connected forest.
Depending on the subfield, there are various conventions for generalizing these
definitions to directed graphs.

In one convention, directed variants of forest and tree are defined in an
identical manner, except that the direction of the edges is ignored. In effect,
each directed edge is treated as a single undirected edge. Then, additional
restrictions are imposed to define *branchings* and *arborescences*.

In another convention, directed variants of forest and tree correspond to
the previous convention's branchings and arborescences, respectively. Then two
new terms, *polyforest* and *polytree*, are defined to correspond to the other
convention's forest and tree.

Summarizing::

   +-----------------------------+
   | Convention A | Convention B |
   +=============================+
   | forest       | polyforest   |
   | tree         | polytree     |
   | branching    | forest       |
   | arborescence | tree         |
   +-----------------------------+

Each convention has its reasons. The first convention emphasizes definitional
similarity in that directed forests and trees are only concerned with
acyclicity and do not have an in-degree constraint, just as their undirected
counterparts do not. The second convention emphasizes functional similarity
in the sense that the directed analog of a spanning tree is a spanning
arborescence. That is, take any spanning tree and choose one node as the root.
Then every edge is assigned a direction such there is a directed path from the
root to every other node. The result is a spanning arborescence.

NetworkX follows convention "A". Explicitly, these are:

undirected forest
   An undirected graph with no undirected cycles.

undirected tree
   A connected, undirected forest.

directed forest
   A directed graph with no undirected cycles. Equivalently, the underlying
   graph structure (which ignores edge orientations) is an undirected forest.
   In convention B, this is known as a polyforest.

directed tree
   A weakly connected, directed forest. Equivalently, the underlying graph
   structure (which ignores edge orientations) is an undirected tree. In
   convention B, this is known as a polytree.

branching
   A directed forest with each node having, at most, one parent. So the maximum
   in-degree is equal to 1. In convention B, this is known as a forest.

arborescence
   A directed tree with each node having, at most, one parent. So the maximum
   in-degree is equal to 1. In convention B, this is known as a tree.

For trees and arborescences, the adjective "spanning" may be added to designate
that the graph, when considered as a forest/branching, consists of a single
tree/arborescence that includes all nodes in the graph. It is true, by
definition, that every tree/arborescence is spanning with respect to the nodes
that define the tree/arborescence and so, it might seem redundant to introduce
the notion of "spanning". However, the nodes may represent a subset of
nodes from a larger graph, and it is in this context that the term "spanning"
becomes a useful notion.
"""

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_arborescence", "is_branching", "is_forest", "is_tree"]

@_dispatchable
def is_arborescence(G: Graph[_Node]) -> bool: ...
@_dispatchable
def is_branching(G: DiGraph[_Node]) -> bool: ...
@_dispatchable
def is_forest(G: Graph[_Node]) -> bool: ...
@_dispatchable
def is_tree(G: Graph[_Node]) -> bool: ...
