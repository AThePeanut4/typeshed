"""Minimum cost flow algorithms on directed connected graphs."""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

class _DataEssentialsAndFunctions:
    node_list: Incomplete
    node_indices: Incomplete
    node_demands: Incomplete
    edge_sources: Incomplete
    edge_targets: Incomplete
    edge_keys: Incomplete
    edge_indices: Incomplete
    edge_capacities: Incomplete
    edge_weights: Incomplete
    edge_count: Incomplete
    edge_flow: Incomplete
    node_potentials: Incomplete
    parent: Incomplete
    parent_edge: Incomplete
    subtree_size: Incomplete
    next_node_dft: Incomplete
    prev_node_dft: Incomplete
    last_descendent_dft: Incomplete

    def __init__(self, G, multigraph, demand: str = "demand", capacity: str = "capacity", weight: str = "weight") -> None: ...
    def initialize_spanning_tree(self, n, faux_inf) -> None: ...
    def find_apex(self, p, q):
        """Find the lowest common ancestor of nodes p and q in the spanning tree."""
        ...
    def trace_path(self, p, w):
        """Returns the nodes and edges on the path from node p to its ancestor w."""
        ...
    def find_cycle(self, i, p, q):
        """
        Returns the nodes and edges on the cycle containing edge i == (p, q)
        when the latter is added to the spanning tree.

        The cycle is oriented in the direction from p to q.
        """
        ...
    def augment_flow(self, Wn, We, f) -> None:
        """Augment f units of flow along a cycle represented by Wn and We."""
        ...
    def trace_subtree(self, p) -> Generator[Incomplete, None, None]:
        """Yield the nodes in the subtree rooted at a node p."""
        ...
    def remove_edge(self, s, t) -> None:
        """Remove an edge (s, t) where parent[t] == s from the spanning tree."""
        ...
    def make_root(self, q) -> None:
        """Make a node q the root of its containing subtree."""
        ...
    def add_edge(self, i, p, q) -> None:
        """Add an edge (p, q) to the spanning tree where q is the root of a subtree."""
        ...
    def update_potentials(self, i, p, q) -> None:
        """
        Update the potentials of the nodes in the subtree rooted at a node
        q connected to its parent p by an edge i.
        """
        ...
    def reduced_cost(self, i):
        """Returns the reduced cost of an edge i."""
        ...
    def find_entering_edges(self) -> Generator[Incomplete, None, None]:
        """Yield entering edges until none can be found."""
        ...
    def residual_capacity(self, i, p):
        """
        Returns the residual capacity of an edge i in the direction away
        from its endpoint p.
        """
        ...
    def find_leaving_edge(self, Wn, We):
        """Returns the leaving edge in a cycle represented by Wn and We."""
        ...

@_dispatchable
def network_simplex(G: Graph[_Node], demand: str = "demand", capacity: str = "capacity", weight: str = "weight"): ...
