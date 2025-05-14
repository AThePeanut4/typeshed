"""
Generators for some classic graphs.

The typical graph builder function is called as follows:

>>> G = nx.complete_graph(100)

returning the complete graph on n nodes labeled 0, .., 99
as a simple graph. Except for `empty_graph`, all the functions
in this module return a Graph class (i.e. a simple, undirected graph).
"""

from _typeshed import Incomplete

from networkx.classes import Graph
from networkx.utils.backends import _dispatchable

__all__ = [
    "balanced_tree",
    "barbell_graph",
    "binomial_tree",
    "complete_graph",
    "complete_multipartite_graph",
    "circular_ladder_graph",
    "circulant_graph",
    "cycle_graph",
    "dorogovtsev_goltsev_mendes_graph",
    "empty_graph",
    "full_rary_tree",
    "kneser_graph",
    "ladder_graph",
    "lollipop_graph",
    "null_graph",
    "path_graph",
    "star_graph",
    "tadpole_graph",
    "trivial_graph",
    "turan_graph",
    "wheel_graph",
]

@_dispatchable
def full_rary_tree(r, n, create_using=None): ...
@_dispatchable
def kneser_graph(n, k) -> Graph[Incomplete]:
    """
    Returns the Kneser Graph with parameters `n` and `k`.

    The Kneser Graph has nodes that are k-tuples (subsets) of the integers
    between 0 and ``n-1``. Nodes are adjacent if their corresponding sets are disjoint.

    Parameters
    ----------
    n: int
        Number of integers from which to make node subsets.
        Subsets are drawn from ``set(range(n))``.
    k: int
        Size of the subsets.

    Returns
    -------
    G : NetworkX Graph

    Examples
    --------
    >>> G = nx.kneser_graph(5, 2)
    >>> G.number_of_nodes()
    10
    >>> G.number_of_edges()
    15
    >>> nx.is_isomorphic(G, nx.petersen_graph())
    True
    """
    ...
@_dispatchable
def balanced_tree(r, h, create_using=None): ...
@_dispatchable
def barbell_graph(m1, m2, create_using=None): ...
@_dispatchable
def binomial_tree(n, create_using=None): ...
@_dispatchable
def complete_graph(n, create_using=None): ...
@_dispatchable
def circular_ladder_graph(n, create_using=None): ...
@_dispatchable
def circulant_graph(n, offsets, create_using=None): ...
@_dispatchable
def cycle_graph(n, create_using=None): ...
@_dispatchable
def dorogovtsev_goltsev_mendes_graph(n, create_using=None): ...
@_dispatchable
def empty_graph(n: Incomplete | int = 0, create_using=None, default=...): ...
@_dispatchable
def ladder_graph(n, create_using=None): ...
@_dispatchable
def lollipop_graph(m, n, create_using=None): ...
@_dispatchable
def null_graph(create_using=None): ...
@_dispatchable
def path_graph(n, create_using=None): ...
@_dispatchable
def star_graph(n, create_using=None): ...
@_dispatchable
def tadpole_graph(m, n, create_using=None) -> Graph[Incomplete] | Incomplete:
    """
    Returns the (m,n)-tadpole graph; ``C_m`` connected to ``P_n``.

    This graph on m+n nodes connects a cycle of size `m` to a path of length `n`.
    It looks like a tadpole. It is also called a kite graph or a dragon graph.

    .. plot::

        >>> nx.draw(nx.tadpole_graph(3, 5))

    Parameters
    ----------
    m, n : int or iterable container of nodes
        If an integer, nodes are from ``range(m)`` and ``range(m,m+n)``.
        If a container of nodes, those nodes appear in the graph.
        Warning: `m` and `n` are not checked for duplicates and if present the
        resulting graph may not be as desired.

        The nodes for `m` appear in the cycle graph $C_m$ and the nodes
        for `n` appear in the path $P_n$.
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    Networkx graph
       A cycle of size `m` connected to a path of length `n`.

    Raises
    ------
    NetworkXError
        If ``m < 2``. The tadpole graph is undefined for ``m<2``.

    Notes
    -----
    The 2 subgraphs are joined via an edge ``(m-1, m)``.
    If ``n=0``, this is a cycle graph.
    `m` and/or `n` can be a container of nodes instead of an integer.
    """
    ...
@_dispatchable
def trivial_graph(create_using=None): ...
@_dispatchable
def turan_graph(n, r):
    r"""
    Return the Turan Graph

    The Turan Graph is a complete multipartite graph on $n$ nodes
    with $r$ disjoint subsets. That is, edges connect each node to
    every node not in its subset.

    Given $n$ and $r$, we create a complete multipartite graph with
    $r-(n \mod r)$ partitions of size $n/r$, rounded down, and
    $n \mod r$ partitions of size $n/r+1$, rounded down.

    .. plot::

        >>> nx.draw(nx.turan_graph(6, 2))

    Parameters
    ----------
    n : int
        The number of nodes.
    r : int
        The number of partitions.
        Must be less than or equal to n.

    Notes
    -----
    Must satisfy $1 <= r <= n$.
    The graph has $(r-1)(n^2)/(2r)$ edges, rounded down.
    """
    ...
@_dispatchable
def wheel_graph(n, create_using=None): ...
@_dispatchable
def complete_multipartite_graph(*subset_sizes):
    """
    Returns the complete multipartite graph with the specified subset sizes.

    .. plot::

        >>> nx.draw(nx.complete_multipartite_graph(1, 2, 3))

    Parameters
    ----------
    subset_sizes : tuple of integers or tuple of node iterables
       The arguments can either all be integer number of nodes or they
       can all be iterables of nodes. If integers, they represent the
       number of nodes in each subset of the multipartite graph.
       If iterables, each is used to create the nodes for that subset.
       The length of subset_sizes is the number of subsets.

    Returns
    -------
    G : NetworkX Graph
       Returns the complete multipartite graph with the specified subsets.

       For each node, the node attribute 'subset' is an integer
       indicating which subset contains the node.

    Examples
    --------
    Creating a complete tripartite graph, with subsets of one, two, and three
    nodes, respectively.

        >>> G = nx.complete_multipartite_graph(1, 2, 3)
        >>> [G.nodes[u]["subset"] for u in G]
        [0, 1, 1, 2, 2, 2]
        >>> list(G.edges(0))
        [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
        >>> list(G.edges(2))
        [(2, 0), (2, 3), (2, 4), (2, 5)]
        >>> list(G.edges(4))
        [(4, 0), (4, 1), (4, 2)]

        >>> G = nx.complete_multipartite_graph("a", "bc", "def")
        >>> [G.nodes[u]["subset"] for u in sorted(G)]
        [0, 1, 1, 2, 2, 2]

    Notes
    -----
    This function generalizes several other graph builder functions.

    - If no subset sizes are given, this returns the null graph.
    - If a single subset size `n` is given, this returns the empty graph on
      `n` nodes.
    - If two subset sizes `m` and `n` are given, this returns the complete
      bipartite graph on `m + n` nodes.
    - If subset sizes `1` and `n` are given, this returns the star graph on
      `n + 1` nodes.

    See also
    --------
    complete_bipartite_graph
    """
    ...
