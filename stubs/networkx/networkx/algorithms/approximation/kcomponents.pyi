"""Fast approximation for k-component structure"""

from _typeshed import Incomplete
from collections import defaultdict

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["k_components"]

@_dispatchable
def k_components(G: Graph[_Node], min_density: float = 0.95) -> defaultdict[Incomplete, list[Incomplete]]:
    """
    Returns the approximate k-component structure of a graph G.

    A `k`-component is a maximal subgraph of a graph G that has, at least,
    node connectivity `k`: we need to remove at least `k` nodes to break it
    into more components. `k`-components have an inherent hierarchical
    structure because they are nested in terms of connectivity: a connected
    graph can contain several 2-components, each of which can contain
    one or more 3-components, and so forth.

    This implementation is based on the fast heuristics to approximate
    the `k`-component structure of a graph [1]_. Which, in turn, it is based on
    a fast approximation algorithm for finding good lower bounds of the number
    of node independent paths between two nodes [2]_.

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph

    min_density : Float
        Density relaxation threshold. Default value 0.95

    Returns
    -------
    k_components : dict
        Dictionary with connectivity level `k` as key and a list of
        sets of nodes that form a k-component of level `k` as values.

    Raises
    ------
    NetworkXNotImplemented
        If G is directed.

    Examples
    --------
    >>> # Petersen graph has 10 nodes and it is triconnected, thus all
    >>> # nodes are in a single component on all three connectivity levels
    >>> from networkx.algorithms import approximation as apxa
    >>> G = nx.petersen_graph()
    >>> k_components = apxa.k_components(G)

    Notes
    -----
    The logic of the approximation algorithm for computing the `k`-component
    structure [1]_ is based on repeatedly applying simple and fast algorithms
    for `k`-cores and biconnected components in order to narrow down the
    number of pairs of nodes over which we have to compute White and Newman's
    approximation algorithm for finding node independent paths [2]_. More
    formally, this algorithm is based on Whitney's theorem, which states
    an inclusion relation among node connectivity, edge connectivity, and
    minimum degree for any graph G. This theorem implies that every
    `k`-component is nested inside a `k`-edge-component, which in turn,
    is contained in a `k`-core. Thus, this algorithm computes node independent
    paths among pairs of nodes in each biconnected part of each `k`-core,
    and repeats this procedure for each `k` from 3 to the maximal core number
    of a node in the input graph.

    Because, in practice, many nodes of the core of level `k` inside a
    bicomponent actually are part of a component of level k, the auxiliary
    graph needed for the algorithm is likely to be very dense. Thus, we use
    a complement graph data structure (see `AntiGraph`) to save memory.
    AntiGraph only stores information of the edges that are *not* present
    in the actual auxiliary graph. When applying algorithms to this
    complement graph data structure, it behaves as if it were the dense
    version.

    See also
    --------
    k_components

    References
    ----------
    .. [1]  Torrents, J. and F. Ferraro (2015) Structural Cohesion:
            Visualization and Heuristics for Fast Computation.
            https://arxiv.org/pdf/1503.04476v1

    .. [2]  White, Douglas R., and Mark Newman (2001) A Fast Algorithm for
            Node-Independent Paths. Santa Fe Institute Working Paper #01-07-035
            https://www.santafe.edu/research/results/working-papers/fast-approximation-algorithms-for-finding-node-ind

    .. [3]  Moody, J. and D. White (2003). Social cohesion and embeddedness:
            A hierarchical conception of social groups.
            American Sociological Review 68(1), 103--28.
            https://doi.org/10.2307/3088904
    """
    ...
