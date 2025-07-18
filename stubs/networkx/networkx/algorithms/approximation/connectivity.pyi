"""Fast approximation for node connectivity"""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["local_node_connectivity", "node_connectivity", "all_pairs_node_connectivity"]

@_dispatchable
def local_node_connectivity(G: Graph[_Node], source: _Node, target: _Node, cutoff: int | None = None):
    """
    Compute node connectivity between source and target.

    Pairwise or local node connectivity between two distinct and nonadjacent
    nodes is the minimum number of nodes that must be removed (minimum
    separating cutset) to disconnect them. By Menger's theorem, this is equal
    to the number of node independent paths (paths that share no nodes other
    than source and target). Which is what we compute in this function.

    This algorithm is a fast approximation that gives an strict lower
    bound on the actual number of node independent paths between two nodes [1]_.
    It works for both directed and undirected graphs.

    Parameters
    ----------

    G : NetworkX graph

    source : node
        Starting node for node connectivity

    target : node
        Ending node for node connectivity

    cutoff : integer
        Maximum node connectivity to consider. If None, the minimum degree
        of source or target is used as a cutoff. Default value None.

    Returns
    -------
    k: integer
       pairwise node connectivity

    Examples
    --------
    >>> # Platonic octahedral graph has node connectivity 4
    >>> # for each non adjacent node pair
    >>> from networkx.algorithms import approximation as approx
    >>> G = nx.octahedral_graph()
    >>> approx.local_node_connectivity(G, 0, 5)
    4

    Notes
    -----
    This algorithm [1]_ finds node independents paths between two nodes by
    computing their shortest path using BFS, marking the nodes of the path
    found as 'used' and then searching other shortest paths excluding the
    nodes marked as used until no more paths exist. It is not exact because
    a shortest path could use nodes that, if the path were longer, may belong
    to two different node independent paths. Thus it only guarantees an
    strict lower bound on node connectivity.

    Note that the authors propose a further refinement, losing accuracy and
    gaining speed, which is not implemented yet.

    See also
    --------
    all_pairs_node_connectivity
    node_connectivity

    References
    ----------
    .. [1] White, Douglas R., and Mark Newman. 2001 A Fast Algorithm for
        Node-Independent Paths. Santa Fe Institute Working Paper #01-07-035
        http://eclectic.ss.uci.edu/~drwhite/working.pdf
    """
    ...
@_dispatchable
def node_connectivity(G: Graph[_Node], s: _Node | None = None, t: _Node | None = None):
    """
    Returns an approximation for node connectivity for a graph or digraph G.

    Node connectivity is equal to the minimum number of nodes that
    must be removed to disconnect G or render it trivial. By Menger's theorem,
    this is equal to the number of node independent paths (paths that
    share no nodes other than source and target).

    If source and target nodes are provided, this function returns the
    local node connectivity: the minimum number of nodes that must be
    removed to break all paths from source to target in G.

    This algorithm is based on a fast approximation that gives an strict lower
    bound on the actual number of node independent paths between two nodes [1]_.
    It works for both directed and undirected graphs.

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph

    s : node
        Source node. Optional. Default value: None.

    t : node
        Target node. Optional. Default value: None.

    Returns
    -------
    K : integer
        Node connectivity of G, or local node connectivity if source
        and target are provided.

    Examples
    --------
    >>> # Platonic octahedral graph is 4-node-connected
    >>> from networkx.algorithms import approximation as approx
    >>> G = nx.octahedral_graph()
    >>> approx.node_connectivity(G)
    4

    Notes
    -----
    This algorithm [1]_ finds node independents paths between two nodes by
    computing their shortest path using BFS, marking the nodes of the path
    found as 'used' and then searching other shortest paths excluding the
    nodes marked as used until no more paths exist. It is not exact because
    a shortest path could use nodes that, if the path were longer, may belong
    to two different node independent paths. Thus it only guarantees an
    strict lower bound on node connectivity.

    See also
    --------
    all_pairs_node_connectivity
    local_node_connectivity

    References
    ----------
    .. [1] White, Douglas R., and Mark Newman. 2001 A Fast Algorithm for
        Node-Independent Paths. Santa Fe Institute Working Paper #01-07-035
        http://eclectic.ss.uci.edu/~drwhite/working.pdf
    """
    ...
@_dispatchable
def all_pairs_node_connectivity(
    G: Graph[_Node], nbunch: Iterable[Incomplete] | None = None, cutoff: int | None = None
) -> dict[Incomplete, dict[Incomplete, Incomplete]]:
    """
    Compute node connectivity between all pairs of nodes.

    Pairwise or local node connectivity between two distinct and nonadjacent
    nodes is the minimum number of nodes that must be removed (minimum
    separating cutset) to disconnect them. By Menger's theorem, this is equal
    to the number of node independent paths (paths that share no nodes other
    than source and target). Which is what we compute in this function.

    This algorithm is a fast approximation that gives an strict lower
    bound on the actual number of node independent paths between two nodes [1]_.
    It works for both directed and undirected graphs.


    Parameters
    ----------
    G : NetworkX graph

    nbunch: container
        Container of nodes. If provided node connectivity will be computed
        only over pairs of nodes in nbunch.

    cutoff : integer
        Maximum node connectivity to consider. If None, the minimum degree
        of source or target is used as a cutoff in each pair of nodes.
        Default value None.

    Returns
    -------
    K : dictionary
        Dictionary, keyed by source and target, of pairwise node connectivity

    Examples
    --------
    A 3 node cycle with one extra node attached has connectivity 2 between all
    nodes in the cycle and connectivity 1 between the extra node and the rest:

    >>> G = nx.cycle_graph(3)
    >>> G.add_edge(2, 3)
    >>> import pprint  # for nice dictionary formatting
    >>> pprint.pprint(nx.all_pairs_node_connectivity(G))
    {0: {1: 2, 2: 2, 3: 1},
     1: {0: 2, 2: 2, 3: 1},
     2: {0: 2, 1: 2, 3: 1},
     3: {0: 1, 1: 1, 2: 1}}

    See Also
    --------
    local_node_connectivity
    node_connectivity

    References
    ----------
    .. [1] White, Douglas R., and Mark Newman. 2001 A Fast Algorithm for
        Node-Independent Paths. Santa Fe Institute Working Paper #01-07-035
        http://eclectic.ss.uci.edu/~drwhite/working.pdf
    """
    ...
