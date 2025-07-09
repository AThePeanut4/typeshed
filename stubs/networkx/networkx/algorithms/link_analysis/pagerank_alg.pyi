"""PageRank analysis of graph structure."""

from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Collection

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["pagerank", "google_matrix"]

@_dispatchable
def pagerank(
    G: Graph[_Node],
    alpha: float | None = 0.85,
    personalization: SupportsGetItem[Incomplete, Incomplete] | None = None,
    max_iter: int | None = 100,
    tol: float | None = 1e-06,
    nstart: SupportsGetItem[Incomplete, Incomplete] | None = None,
    weight: str | None = "weight",
    dangling: SupportsGetItem[Incomplete, Incomplete] | None = None,
) -> dict[Incomplete, float]: ...
@_dispatchable
def google_matrix(
    G: Graph[_Node],
    alpha: float = 0.85,
    personalization: SupportsGetItem[Incomplete, Incomplete] | None = None,
    nodelist: Collection[_Node] | None = None,
    weight: str | None = "weight",
    dangling: SupportsGetItem[Incomplete, Incomplete] | None = None,
):
    """
    Returns the Google matrix of the graph.

    Parameters
    ----------
    G : graph
      A NetworkX graph.  Undirected graphs will be converted to a directed
      graph with two directed edges for each undirected edge.

    alpha : float
      The damping factor.

    personalization: dict, optional
      The "personalization vector" consisting of a dictionary with a
      key some subset of graph nodes and personalization value each of those.
      At least one personalization value must be non-zero.
      If not specified, a nodes personalization value will be zero.
      By default, a uniform distribution is used.

    nodelist : list, optional
      The rows and columns are ordered according to the nodes in nodelist.
      If nodelist is None, then the ordering is produced by G.nodes().

    weight : key, optional
      Edge data key to use as weight.  If None weights are set to 1.

    dangling: dict, optional
      The outedges to be assigned to any "dangling" nodes, i.e., nodes without
      any outedges. The dict key is the node the outedge points to and the dict
      value is the weight of that outedge. By default, dangling nodes are given
      outedges according to the personalization vector (uniform if not
      specified) This must be selected to result in an irreducible transition
      matrix (see notes below). It may be common to have the dangling dict to
      be the same as the personalization dict.

    Returns
    -------
    A : 2D NumPy ndarray
       Google matrix of the graph

    Notes
    -----
    The array returned represents the transition matrix that describes the
    Markov chain used in PageRank. For PageRank to converge to a unique
    solution (i.e., a unique stationary distribution in a Markov chain), the
    transition matrix must be irreducible. In other words, it must be that
    there exists a path between every pair of nodes in the graph, or else there
    is the potential of "rank sinks."

    This implementation works with Multi(Di)Graphs. For multigraphs the
    weight between two nodes is set to be the sum of all edge weights
    between those nodes.

    See Also
    --------
    pagerank
    """
    ...
