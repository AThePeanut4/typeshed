"""Group centrality measures."""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "group_betweenness_centrality",
    "group_closeness_centrality",
    "group_degree_centrality",
    "group_in_degree_centrality",
    "group_out_degree_centrality",
    "prominent_group",
]

@_dispatchable
def group_betweenness_centrality(
    G: Graph[_Node], C, normalized: bool | None = True, weight: str | None = None, endpoints: bool | None = False
):
    r"""
    Compute the group betweenness centrality for a group of nodes.

    Group betweenness centrality of a group of nodes $C$ is the sum of the
    fraction of all-pairs shortest paths that pass through any vertex in $C$

    .. math::

       c_B(v) =\sum_{s,t \in V} \frac{\sigma(s, t|v)}{\sigma(s, t)}

    where $V$ is the set of nodes, $\sigma(s, t)$ is the number of
    shortest $(s, t)$-paths, and $\sigma(s, t|C)$ is the number of
    those paths passing through some node in group $C$. Note that
    $(s, t)$ are not members of the group ($V-C$ is the set of nodes
    in $V$ that are not in $C$).

    Parameters
    ----------
    G : graph
      A NetworkX graph.

    C : list or set or list of lists or list of sets
      A group or a list of groups containing nodes which belong to G, for which group betweenness
      centrality is to be calculated.

    normalized : bool, optional (default=True)
      If True, group betweenness is normalized by `1/((|V|-|C|)(|V|-|C|-1))`
      where `|V|` is the number of nodes in G and `|C|` is the number of nodes in C.

    weight : None or string, optional (default=None)
      If None, all edge weights are considered equal.
      Otherwise holds the name of the edge attribute used as weight.
      The weight of an edge is treated as the length or distance between the two sides.

    endpoints : bool, optional (default=False)
      If True include the endpoints in the shortest path counts.

    Raises
    ------
    NodeNotFound
       If node(s) in C are not present in G.

    Returns
    -------
    betweenness : list of floats or float
       If C is a single group then return a float. If C is a list with
       several groups then return a list of group betweenness centralities.

    See Also
    --------
    betweenness_centrality

    Notes
    -----
    Group betweenness centrality is described in [1]_ and its importance discussed in [3]_.
    The initial implementation of the algorithm is mentioned in [2]_. This function uses
    an improved algorithm presented in [4]_.

    The number of nodes in the group must be a maximum of n - 2 where `n`
    is the total number of nodes in the graph.

    For weighted graphs the edge weights must be greater than zero.
    Zero edge weights can produce an infinite number of equal length
    paths between pairs of nodes.

    The total number of paths between source and target is counted
    differently for directed and undirected graphs. Directed paths
    between "u" and "v" are counted as two possible paths (one each
    direction) while undirected paths between "u" and "v" are counted
    as one path. Said another way, the sum in the expression above is
    over all ``s != t`` for directed graphs and for ``s < t`` for undirected graphs.


    References
    ----------
    .. [1] M G Everett and S P Borgatti:
       The Centrality of Groups and Classes.
       Journal of Mathematical Sociology. 23(3): 181-201. 1999.
       http://www.analytictech.com/borgatti/group_centrality.htm
    .. [2] Ulrik Brandes:
       On Variants of Shortest-Path Betweenness
       Centrality and their Generic Computation.
       Social Networks 30(2):136-145, 2008.
       http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.72.9610&rep=rep1&type=pdf
    .. [3] Sourav Medya et. al.:
       Group Centrality Maximization via Network Design.
       SIAM International Conference on Data Mining, SDM 2018, 126–134.
       https://sites.cs.ucsb.edu/~arlei/pubs/sdm18.pdf
    .. [4] Rami Puzis, Yuval Elovici, and Shlomi Dolev.
       "Fast algorithm for successive computation of group betweenness centrality."
       https://journals.aps.org/pre/pdf/10.1103/PhysRevE.76.056709
    """
    ...
@_dispatchable
def prominent_group(
    G: Graph[_Node],
    k: int,
    weight: str | None = None,
    C: Iterable[Incomplete] | None = None,
    endpoints: bool | None = False,
    normalized: bool | None = True,
    greedy: bool | None = False,
) -> tuple[float, list[Incomplete]]: ...
@_dispatchable
def group_closeness_centrality(G: Graph[_Node], S: Iterable[Incomplete], weight: str | None = None) -> float: ...
@_dispatchable
def group_degree_centrality(G: Graph[_Node], S: Iterable[Incomplete]) -> float: ...
@_dispatchable
def group_in_degree_centrality(G: Graph[_Node], S: Iterable[Incomplete]) -> float: ...
@_dispatchable
def group_out_degree_centrality(G: Graph[_Node], S: Iterable[Incomplete]) -> float: ...
