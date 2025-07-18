"""Functions for computing the harmonic centrality of a graph."""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["harmonic_centrality"]

@_dispatchable
def harmonic_centrality(
    G: Graph[_Node], nbunch: Iterable[Incomplete] | None = None, distance=None, sources: Iterable[Incomplete] | None = None
) -> dict[Incomplete, int]:
    r"""
    Compute harmonic centrality for nodes.

    Harmonic centrality [1]_ of a node `u` is the sum of the reciprocal
    of the shortest path distances from all other nodes to `u`

    .. math::

        C(u) = \sum_{v \neq u} \frac{1}{d(v, u)}

    where `d(v, u)` is the shortest-path distance between `v` and `u`.

    If `sources` is given as an argument, the returned harmonic centrality
    values are calculated as the sum of the reciprocals of the shortest
    path distances from the nodes specified in `sources` to `u` instead
    of from all nodes to `u`.

    Notice that higher values indicate higher centrality.

    Parameters
    ----------
    G : graph
      A NetworkX graph

    nbunch : container (default: all nodes in G)
      Container of nodes for which harmonic centrality values are calculated.

    sources : container (default: all nodes in G)
      Container of nodes `v` over which reciprocal distances are computed.
      Nodes not in `G` are silently ignored.

    distance : edge attribute key, optional (default=None)
      Use the specified edge attribute as the edge distance in shortest
      path calculations.  If `None`, then each edge will have distance equal to 1.

    Returns
    -------
    nodes : dictionary
      Dictionary of nodes with harmonic centrality as the value.

    See Also
    --------
    betweenness_centrality, load_centrality, eigenvector_centrality,
    degree_centrality, closeness_centrality

    Notes
    -----
    If the 'distance' keyword is set to an edge attribute key then the
    shortest-path length will be computed using Dijkstra's algorithm with
    that edge attribute as the edge weight.

    References
    ----------
    .. [1] Boldi, Paolo, and Sebastiano Vigna. "Axioms for centrality."
           Internet Mathematics 10.3-4 (2014): 222-262.
    """
    ...
