from _typeshed import Incomplete
from collections.abc import Iterable, Mapping

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "is_matching",
    "is_maximal_matching",
    "is_perfect_matching",
    "max_weight_matching",
    "min_weight_matching",
    "maximal_matching",
]

@_dispatchable
def maximal_matching(G: Graph[_Node]): ...
def matching_dict_to_set(matching: Mapping[Incomplete, Incomplete]) -> set[Incomplete]: ...
@_dispatchable
def is_matching(G: Graph[_Node], matching: dict[Incomplete, Incomplete] | Iterable[Iterable[Incomplete]]) -> bool: ...
@_dispatchable
def is_maximal_matching(G: Graph[_Node], matching: dict[Incomplete, Incomplete] | Iterable[Iterable[Incomplete]]) -> bool: ...
@_dispatchable
def is_perfect_matching(G: Graph[_Node], matching: dict[Incomplete, Incomplete] | Iterable[Iterable[Incomplete]]) -> bool: ...
@_dispatchable
def min_weight_matching(G: Graph[_Node], weight: str | None = "weight"):
    """
    Computing a minimum-weight maximal matching of G.

    Use the maximum-weight algorithm with edge weights subtracted
    from the maximum weight of all edges.

    A matching is a subset of edges in which no node occurs more than once.
    The weight of a matching is the sum of the weights of its edges.
    A maximal matching cannot add more edges and still be a matching.
    The cardinality of a matching is the number of matched edges.

    This method replaces the edge weights with 1 plus the maximum edge weight
    minus the original edge weight.

    new_weight = (max_weight + 1) - edge_weight

    then runs :func:`max_weight_matching` with the new weights.
    The max weight matching with these new weights corresponds
    to the min weight matching using the original weights.
    Adding 1 to the max edge weight keeps all edge weights positive
    and as integers if they started as integers.

    You might worry that adding 1 to each weight would make the algorithm
    favor matchings with more edges. But we use the parameter
    `maxcardinality=True` in `max_weight_matching` to ensure that the
    number of edges in the competing matchings are the same and thus
    the optimum does not change due to changes in the number of edges.

    Read the documentation of `max_weight_matching` for more information.

    Parameters
    ----------
    G : NetworkX graph
      Undirected graph

    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight.
       If key not found, uses 1 as weight.

    Returns
    -------
    matching : set
        A minimal weight matching of the graph.

    See Also
    --------
    max_weight_matching
    """
    ...
@_dispatchable
def max_weight_matching(G: Graph[_Node], maxcardinality: bool | None = False, weight: str | None = "weight"):
    """
    Compute a maximum-weighted matching of G.

    A matching is a subset of edges in which no node occurs more than once.
    The weight of a matching is the sum of the weights of its edges.
    A maximal matching cannot add more edges and still be a matching.
    The cardinality of a matching is the number of matched edges.

    Parameters
    ----------
    G : NetworkX graph
      Undirected graph

    maxcardinality: bool, optional (default=False)
       If maxcardinality is True, compute the maximum-cardinality matching
       with maximum weight among all maximum-cardinality matchings.

    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight.
       If key not found, uses 1 as weight.


    Returns
    -------
    matching : set
        A maximal matching of the graph.

     Examples
    --------
    >>> G = nx.Graph()
    >>> edges = [(1, 2, 6), (1, 3, 2), (2, 3, 1), (2, 4, 7), (3, 5, 9), (4, 5, 3)]
    >>> G.add_weighted_edges_from(edges)
    >>> sorted(nx.max_weight_matching(G))
    [(2, 4), (5, 3)]

    Notes
    -----
    If G has edges with weight attributes the edge data are used as
    weight values else the weights are assumed to be 1.

    This function takes time O(number_of_nodes ** 3).

    If all edge weights are integers, the algorithm uses only integer
    computations.  If floating point weights are used, the algorithm
    could return a slightly suboptimal matching due to numeric
    precision errors.

    This method is based on the "blossom" method for finding augmenting
    paths and the "primal-dual" method for finding a matching of maximum
    weight, both methods invented by Jack Edmonds [1]_.

    Bipartite graphs can also be matched using the functions present in
    :mod:`networkx.algorithms.bipartite.matching`.

    References
    ----------
    .. [1] "Efficient Algorithms for Finding Maximum Matching in Graphs",
       Zvi Galil, ACM Computing Surveys, 1986.
    """
    ...
