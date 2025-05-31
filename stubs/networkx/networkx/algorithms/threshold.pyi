"""Threshold Graphs - Creation, manipulation and identification."""

from collections.abc import Sequence

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

__all__ = ["is_threshold_graph", "find_threshold_graph"]

@_dispatchable
def is_threshold_graph(G: Graph[_Node]) -> bool:
    """
    Returns `True` if `G` is a threshold graph.

    Parameters
    ----------
    G : NetworkX graph instance
        An instance of `Graph`, `DiGraph`, `MultiGraph` or `MultiDiGraph`

    Returns
    -------
    bool
        `True` if `G` is a threshold graph, `False` otherwise.

    Examples
    --------
    >>> from networkx.algorithms.threshold import is_threshold_graph
    >>> G = nx.path_graph(3)
    >>> is_threshold_graph(G)
    True
    >>> G = nx.barbell_graph(3, 3)
    >>> is_threshold_graph(G)
    False

    References
    ----------
    .. [1] Threshold graphs: https://en.wikipedia.org/wiki/Threshold_graph
    """
    ...
def is_threshold_sequence(degree_sequence: Sequence[list[int]]) -> bool:
    """
    Returns True if the sequence is a threshold degree sequence.

    Uses the property that a threshold graph must be constructed by
    adding either dominating or isolated nodes. Thus, it can be
    deconstructed iteratively by removing a node of degree zero or a
    node that connects to the remaining nodes.  If this deconstruction
    fails then the sequence is not a threshold sequence.
    """
    ...
def creation_sequence(degree_sequence, with_labels=False, compact=False):
    """
    Determines the creation sequence for the given threshold degree sequence.

    The creation sequence is a list of single characters 'd'
    or 'i': 'd' for dominating or 'i' for isolated vertices.
    Dominating vertices are connected to all vertices present when it
    is added.  The first node added is by convention 'd'.
    This list can be converted to a string if desired using "".join(cs)

    If with_labels==True:
    Returns a list of 2-tuples containing the vertex number
    and a character 'd' or 'i' which describes the type of vertex.

    If compact==True:
    Returns the creation sequence in a compact form that is the number
    of 'i's and 'd's alternating.
    Examples:
    [1,2,2,3] represents d,i,i,d,d,i,i,i
    [3,1,2] represents d,d,d,i,d,d

    Notice that the first number is the first vertex to be used for
    construction and so is always 'd'.

    with_labels and compact cannot both be True.

    Returns None if the sequence is not a threshold sequence
    """
    ...
def make_compact(creation_sequence):
    """
    Returns the creation sequence in a compact form
    that is the number of 'i's and 'd's alternating.

    Examples
    --------
    >>> from networkx.algorithms.threshold import make_compact
    >>> make_compact(["d", "i", "i", "d", "d", "i", "i", "i"])
    [1, 2, 2, 3]
    >>> make_compact(["d", "d", "d", "i", "d", "d"])
    [3, 1, 2]

    Notice that the first number is the first vertex
    to be used for construction and so is always 'd'.

    Labeled creation sequences lose their labels in the
    compact representation.

    >>> make_compact([3, 1, 2])
    [3, 1, 2]
    """
    ...
def uncompact(creation_sequence):
    """
    Converts a compact creation sequence for a threshold
    graph to a standard creation sequence (unlabeled).
    If the creation_sequence is already standard, return it.
    See creation_sequence.
    """
    ...
def creation_sequence_to_weights(creation_sequence):
    """
    Returns a list of node weights which create the threshold
    graph designated by the creation sequence.  The weights
    are scaled so that the threshold is 1.0.  The order of the
    nodes is the same as that in the creation sequence.
    """
    ...
def weights_to_creation_sequence(weights, threshold=1, with_labels=False, compact=False):
    """
    Returns a creation sequence for a threshold graph
    determined by the weights and threshold given as input.
    If the sum of two node weights is greater than the
    threshold value, an edge is created between these nodes.

    The creation sequence is a list of single characters 'd'
    or 'i': 'd' for dominating or 'i' for isolated vertices.
    Dominating vertices are connected to all vertices present
    when it is added.  The first node added is by convention 'd'.

    If with_labels==True:
    Returns a list of 2-tuples containing the vertex number
    and a character 'd' or 'i' which describes the type of vertex.

    If compact==True:
    Returns the creation sequence in a compact form that is the number
    of 'i's and 'd's alternating.
    Examples:
    [1,2,2,3] represents d,i,i,d,d,i,i,i
    [3,1,2] represents d,d,d,i,d,d

    Notice that the first number is the first vertex to be used for
    construction and so is always 'd'.

    with_labels and compact cannot both be True.
    """
    ...
@_dispatchable
def threshold_graph(creation_sequence, create_using=None):
    """
    Create a threshold graph from the creation sequence or compact
    creation_sequence.

    The input sequence can be a

    creation sequence (e.g. ['d','i','d','d','d','i'])
    labeled creation sequence (e.g. [(0,'d'),(2,'d'),(1,'i')])
    compact creation sequence (e.g. [2,1,1,2,0])

    Use cs=creation_sequence(degree_sequence,labeled=True)
    to convert a degree sequence to a creation sequence.

    Returns None if the sequence is not valid
    """
    ...
@_dispatchable
def find_alternating_4_cycle(G: Graph[_Node]):
    """
    Returns False if there aren't any alternating 4 cycles.
    Otherwise returns the cycle as [a,b,c,d] where (a,b)
    and (c,d) are edges and (a,c) and (b,d) are not.
    """
    ...
@_dispatchable
def find_threshold_graph(G: Graph[_Node], create_using: Graph[_Node] | None = None):
    """
    Returns a threshold subgraph that is close to largest in `G`.

    The threshold graph will contain the largest degree node in G.

    Parameters
    ----------
    G : NetworkX graph instance
        An instance of `Graph`, or `MultiDiGraph`
    create_using : NetworkX graph class or `None` (default), optional
        Type of graph to use when constructing the threshold graph.
        If `None`, infer the appropriate graph type from the input.

    Returns
    -------
    graph :
        A graph instance representing the threshold graph

    Examples
    --------
    >>> from networkx.algorithms.threshold import find_threshold_graph
    >>> G = nx.barbell_graph(3, 3)
    >>> T = find_threshold_graph(G)
    >>> T.nodes  # may vary
    NodeView((7, 8, 5, 6))

    References
    ----------
    .. [1] Threshold graphs: https://en.wikipedia.org/wiki/Threshold_graph
    """
    ...
@_dispatchable
def find_creation_sequence(G: Graph[_Node]): ...
def triangles(creation_sequence): ...
def triangle_sequence(creation_sequence): ...
def cluster_sequence(creation_sequence): ...
def degree_sequence(creation_sequence): ...
def density(creation_sequence): ...
def degree_correlation(creation_sequence): ...
def shortest_path(creation_sequence, u, v): ...
def shortest_path_length(creation_sequence, i): ...
def betweenness_sequence(creation_sequence, normalized=True): ...
def eigenvectors(creation_sequence): ...
def spectral_projection(u, eigenpairs): ...
def eigenvalues(creation_sequence): ...
def random_threshold_sequence(n, p, seed: int | RandomState | None = None): ...
def right_d_threshold_sequence(n: int, m: int) -> list[str]: ...
def left_d_threshold_sequence(n: int, m: int) -> list[str]: ...
def swap_d(cs, p_split=1.0, p_combine=1.0, seed: int | RandomState | None = None): ...
