from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["greedy_modularity_communities", "naive_greedy_modularity_communities"]

@_dispatchable
def greedy_modularity_communities(
    G: Graph[_Node], weight: str | None = None, resolution: float | None = 1, cutoff: int | None = 1, best_n: int | None = None
) -> list[set[Incomplete]] | list[frozenset[Incomplete]]: ...
@_dispatchable
def naive_greedy_modularity_communities(G: Graph[_Node], resolution: float = 1, weight: str | None = None):
    r"""
    Find communities in G using greedy modularity maximization.

    This implementation is O(n^4), much slower than alternatives, but it is
    provided as an easy-to-understand reference implementation.

    Greedy modularity maximization begins with each node in its own community
    and joins the pair of communities that most increases modularity until no
    such pair exists.

    This function maximizes the generalized modularity, where `resolution`
    is the resolution parameter, often expressed as $\gamma$.
    See :func:`~networkx.algorithms.community.quality.modularity`.

    Parameters
    ----------
    G : NetworkX graph
        Graph must be simple and undirected.

    resolution : float (default=1)
        If resolution is less than 1, modularity favors larger communities.
        Greater than 1 favors smaller communities.

    weight : string or None, optional (default=None)
        The name of an edge attribute that holds the numerical value used
        as a weight.  If None, then each edge has weight 1.
        The degree is the sum of the edge weights adjacent to the node.

    Returns
    -------
    list
        A list of sets of nodes, one for each community.
        Sorted by length with largest communities first.

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> c = nx.community.naive_greedy_modularity_communities(G)
    >>> sorted(c[0])
    [8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    See Also
    --------
    greedy_modularity_communities
    modularity
    """
    ...
