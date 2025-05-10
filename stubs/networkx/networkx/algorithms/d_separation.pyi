from _typeshed import Incomplete

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_d_separator", "is_minimal_d_separator", "find_minimal_d_separator", "d_separated", "minimal_d_separator"]

@_dispatchable
def is_d_separator(G, x, y, z) -> bool: ...
@_dispatchable
def find_minimal_d_separator(G, x, y, *, included=None, restricted=None) -> set[Incomplete] | None: ...
@_dispatchable
def d_separated(G, x, y, z):
    """
    Return whether nodes sets ``x`` and ``y`` are d-separated by ``z``.

    .. deprecated:: 3.3

        This function is deprecated and will be removed in NetworkX v3.5.
        Please use `is_d_separator(G, x, y, z)`.
    """
    ...
@_dispatchable
def minimal_d_separator(G, u, v):
    """
    Returns a minimal_d-separating set between `x` and `y` if possible

    .. deprecated:: 3.3

        minimal_d_separator is deprecated and will be removed in NetworkX v3.5.
        Please use `find_minimal_d_separator(G, x, y)`.
    """
    ...
@_dispatchable
def is_minimal_d_separator(G: DiGraph[_Node], x, y, z, *, included=None, restricted=None):
    """
    Determine if `z` is a minimal d-separator for `x` and `y`.

    A d-separator, `z`, in a DAG is a set of nodes that blocks
    all paths from nodes in set `x` to nodes in set `y`.
    A minimal d-separator is a d-separator `z` such that removing
    any subset of nodes makes it no longer a d-separator.

    Note: This function checks whether `z` is a d-separator AND is
    minimal. One can use the function `is_d_separator` to only check if
    `z` is a d-separator. See examples below.

    Parameters
    ----------
    G : nx.DiGraph
        A NetworkX DAG.
    x : node | set
        A node or set of nodes in the graph.
    y : node | set
        A node or set of nodes in the graph.
    z : node | set
        The node or set of nodes to check if it is a minimal d-separating set.
        The function :func:`is_d_separator` is called inside this function
        to verify that `z` is in fact a d-separator.
    included : set | node | None
        A node or set of nodes which must be included in the found separating set,
        default is ``None``, which means the empty set.
    restricted : set | node | None
        Restricted node or set of nodes to consider. Only these nodes can be in
        the found separating set, default is ``None`` meaning all nodes in ``G``.

    Returns
    -------
    bool
        Whether or not the set `z` is a minimal d-separator subject to
        `restricted` nodes and `included` node constraints.

    Examples
    --------
    >>> G = nx.path_graph([0, 1, 2, 3], create_using=nx.DiGraph)
    >>> G.add_node(4)
    >>> nx.is_minimal_d_separator(G, 0, 2, {1})
    True
    >>> # since {1} is the minimal d-separator, {1, 3, 4} is not minimal
    >>> nx.is_minimal_d_separator(G, 0, 2, {1, 3, 4})
    False
    >>> # alternatively, if we only want to check that {1, 3, 4} is a d-separator
    >>> nx.is_d_separator(G, 0, 2, {1, 3, 4})
    True

    Raises
    ------
    NetworkXError
        Raises a :exc:`NetworkXError` if the input graph is not a DAG.

    NodeNotFound
        If any of the input nodes are not found in the graph,
        a :exc:`NodeNotFound` exception is raised.

    References
    ----------
    .. [1] van der Zander, Benito, and Maciej Liśkiewicz. "Finding
        minimal d-separators in linear time and applications." In
        Uncertainty in Artificial Intelligence, pp. 637-647. PMLR, 2020.

    Notes
    -----
    This function works on verifying that a set is minimal and
    d-separating between two nodes. Uses criterion (a), (b), (c) on
    page 4 of [1]_. a) closure(`x`) and `y` are disjoint. b) `z` contains
    all nodes from `included` and is contained in the `restricted`
    nodes and in the union of ancestors of `x`, `y`, and `included`.
    c) the nodes in `z` not in `included` are contained in both
    closure(x) and closure(y). The closure of a set is the set of nodes
    connected to the set by a directed path in G.

    The complexity is :math:`O(m)`, where :math:`m` stands for the
    number of edges in the subgraph of G consisting of only the
    ancestors of `x` and `y`.

    For full details, see [1]_.
    """
    ...
