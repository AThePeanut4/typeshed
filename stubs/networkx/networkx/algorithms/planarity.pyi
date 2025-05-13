from _typeshed import Incomplete
from collections.abc import Generator, Mapping, MutableSet, Reversible

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["check_planarity", "is_planar", "PlanarEmbedding"]

@_dispatchable
def is_planar(G: Graph[_Node]) -> bool:
    """
    Returns True if and only if `G` is planar.

    A graph is *planar* iff it can be drawn in a plane without
    any edge intersections.

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    bool
       Whether the graph is planar.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2)])
    >>> nx.is_planar(G)
    True
    >>> nx.is_planar(nx.complete_graph(5))
    False

    See Also
    --------
    check_planarity :
        Check if graph is planar *and* return a `PlanarEmbedding` instance if True.
    """
    ...
@_dispatchable
def check_planarity(G: Graph[_Node], counterexample: bool = False):
    """
    Check if a graph is planar and return a counterexample or an embedding.

    A graph is planar iff it can be drawn in a plane without
    any edge intersections.

    Parameters
    ----------
    G : NetworkX graph
    counterexample : bool
        A Kuratowski subgraph (to proof non planarity) is only returned if set
        to true.

    Returns
    -------
    (is_planar, certificate) : (bool, NetworkX graph) tuple
        is_planar is true if the graph is planar.
        If the graph is planar `certificate` is a PlanarEmbedding
        otherwise it is a Kuratowski subgraph.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2)])
    >>> is_planar, P = nx.check_planarity(G)
    >>> print(is_planar)
    True

    When `G` is planar, a `PlanarEmbedding` instance is returned:

    >>> P.get_data()
    {0: [1, 2], 1: [0], 2: [0]}

    Notes
    -----
    A (combinatorial) embedding consists of cyclic orderings of the incident
    edges at each vertex. Given such an embedding there are multiple approaches
    discussed in literature to drawing the graph (subject to various
    constraints, e.g. integer coordinates), see e.g. [2].

    The planarity check algorithm and extraction of the combinatorial embedding
    is based on the Left-Right Planarity Test [1].

    A counterexample is only generated if the corresponding parameter is set,
    because the complexity of the counterexample generation is higher.

    See also
    --------
    is_planar :
        Check for planarity without creating a `PlanarEmbedding` or counterexample.

    References
    ----------
    .. [1] Ulrik Brandes:
        The Left-Right Planarity Test
        2009
        http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.217.9208
    .. [2] Takao Nishizeki, Md Saidur Rahman:
        Planar graph drawing
        Lecture Notes Series on Computing: Volume 12
        2004
    """
    ...

class Interval:
    """
    Represents a set of return edges.

    All return edges in an interval induce a same constraint on the contained
    edges, which means that all edges must either have a left orientation or
    all edges must have a right orientation.
    """
    low: Incomplete
    high: Incomplete

    def __init__(self, low: Incomplete | None = None, high: Incomplete | None = None) -> None: ...
    def empty(self):
        """Check if the interval is empty"""
        ...
    def copy(self):
        """Returns a copy of this interval"""
        ...
    def conflicting(self, b, planarity_state):
        """Returns True if interval I conflicts with edge b"""
        ...

class ConflictPair:
    """
    Represents a different constraint between two intervals.

    The edges in the left interval must have a different orientation than
    the one in the right interval.
    """
    left: Incomplete
    right: Incomplete

    def __init__(self, left=..., right=...) -> None: ...
    def swap(self) -> None:
        """Swap left and right intervals"""
        ...
    def lowest(self, planarity_state):
        """Returns the lowest lowpoint of a conflict pair"""
        ...

class LRPlanarity:
    """A class to maintain the state during planarity check."""
    G: Incomplete
    roots: Incomplete
    height: Incomplete
    lowpt: Incomplete
    lowpt2: Incomplete
    nesting_depth: Incomplete
    parent_edge: Incomplete
    DG: Incomplete
    adjs: Incomplete
    ordered_adjs: Incomplete
    ref: Incomplete
    side: Incomplete
    S: Incomplete
    stack_bottom: Incomplete
    lowpt_edge: Incomplete
    left_ref: Incomplete
    right_ref: Incomplete
    embedding: Incomplete

    def __init__(self, G) -> None: ...
    def lr_planarity(self):
        """
        Execute the LR planarity test.

        Returns
        -------
        embedding : dict
            If the graph is planar an embedding is returned. Otherwise None.
        """
        ...
    def lr_planarity_recursive(self):
        """Recursive version of :meth:`lr_planarity`."""
        ...
    def dfs_orientation(self, v):
        """Orient the graph by DFS, compute lowpoints and nesting order."""
        ...
    def dfs_orientation_recursive(self, v) -> None:
        """Recursive version of :meth:`dfs_orientation`."""
        ...
    def dfs_testing(self, v):
        """Test for LR partition."""
        ...
    def dfs_testing_recursive(self, v):
        """Recursive version of :meth:`dfs_testing`."""
        ...
    def add_constraints(self, ei, e): ...
    def remove_back_edges(self, e) -> None: ...
    def dfs_embedding(self, v):
        """Completes the embedding."""
        ...
    def dfs_embedding_recursive(self, v) -> None:
        """Recursive version of :meth:`dfs_embedding`."""
        ...
    def sign(self, e):
        """Resolve the relative side of an edge to the absolute side."""
        ...
    def sign_recursive(self, e):
        """Recursive version of :meth:`sign`."""
        ...

class PlanarEmbedding(DiGraph[_Node]):
    def get_data(self) -> dict[_Node, list[_Node]]: ...
    def set_data(self, data: Mapping[_Node, Reversible[_Node]]) -> None: ...
    def neighbors_cw_order(self, v: _Node) -> Generator[_Node, None, None]: ...
    def add_half_edge(self, start_node: _Node, end_node: _Node, *, cw: _Node | None = None, ccw: _Node | None = None): ...
    def check_structure(self) -> None: ...
    def add_half_edge_ccw(self, start_node: _Node, end_node: _Node, reference_neighbor: _Node) -> None: ...
    def add_half_edge_cw(self, start_node: _Node, end_node: _Node, reference_neighbor: _Node) -> None: ...
    def connect_components(self, v: _Node, w: _Node) -> None: ...
    def add_half_edge_first(self, start_node: _Node, end_node: _Node) -> None: ...
    def next_face_half_edge(self, v: _Node, w: _Node) -> tuple[_Node, _Node]: ...
    def traverse_face(
        self, v: _Node, w: _Node, mark_half_edges: MutableSet[tuple[_Node, _Node]] | None = None
    ) -> list[_Node]:
        """
        Returns nodes on the face that belong to the half-edge (v, w).

        The face that is traversed lies to the right of the half-edge (in an
        orientation where v is below w).

        Optionally it is possible to pass a set to which all encountered half
        edges are added. Before calling this method, this set must not include
        any half-edges that belong to the face.

        Parameters
        ----------
        v : node
            Start node of half-edge.
        w : node
            End node of half-edge.
        mark_half_edges: set, optional
            Set to which all encountered half-edges are added.

        Returns
        -------
        face : list
            A list of nodes that lie on this face.
        """
        ...
