from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["triangles", "average_clustering", "clustering", "transitivity", "square_clustering", "generalized_degree"]

@_dispatchable
def triangles(G: Graph[_Node], nodes=None) -> int | dict[Incomplete, int]: ...
@_dispatchable
def average_clustering(
    G: Graph[_Node], nodes: Iterable[_Node] | None = None, weight: str | None = None, count_zeros: bool = True
) -> float: ...
@_dispatchable
def clustering(G: Graph[_Node], nodes=None, weight: str | None = None) -> float | int | dict[Incomplete, float | int]: ...
@_dispatchable
def transitivity(G: Graph[_Node]) -> float: ...
@_dispatchable
def square_clustering(G: Graph[_Node], nodes: Iterable[_Node] | None = None) -> float | int | dict[Incomplete, float | int]: ...
@_dispatchable
def generalized_degree(G: Graph[_Node], nodes: Iterable[_Node] | None = None):
    r"""
    Compute the generalized degree for nodes.

    For each node, the generalized degree shows how many edges of given
    triangle multiplicity the node is connected to. The triangle multiplicity
    of an edge is the number of triangles an edge participates in. The
    generalized degree of node :math:`i` can be written as a vector
    :math:`\mathbf{k}_i=(k_i^{(0)}, \dotsc, k_i^{(N-2)})` where
    :math:`k_i^{(j)}` is the number of edges attached to node :math:`i` that
    participate in :math:`j` triangles.

    Parameters
    ----------
    G : graph

    nodes : container of nodes, optional (default=all nodes in G)
       Compute the generalized degree for nodes in this container.

    Returns
    -------
    out : Counter, or dictionary of Counters
       Generalized degree of specified nodes. The Counter is keyed by edge
       triangle multiplicity.

    Examples
    --------
    >>> G = nx.complete_graph(5)
    >>> print(nx.generalized_degree(G, 0))
    Counter({3: 4})
    >>> print(nx.generalized_degree(G))
    {0: Counter({3: 4}), 1: Counter({3: 4}), 2: Counter({3: 4}), 3: Counter({3: 4}), 4: Counter({3: 4})}

    To recover the number of triangles attached to a node:

    >>> k1 = nx.generalized_degree(G, 0)
    >>> sum([k * v for k, v in k1.items()]) / 2 == nx.triangles(G, 0)
    True

    Notes
    -----
    Self loops are ignored.

    In a network of N nodes, the highest triangle multiplicity an edge can have
    is N-2.

    The return value does not include a `zero` entry if no edges of a
    particular triangle multiplicity are present.

    The number of triangles node :math:`i` is attached to can be recovered from
    the generalized degree :math:`\mathbf{k}_i=(k_i^{(0)}, \dotsc,
    k_i^{(N-2)})` by :math:`(k_i^{(1)}+2k_i^{(2)}+\dotsc +(N-2)k_i^{(N-2)})/2`.

    References
    ----------
    .. [1] Networks with arbitrary edge multiplicities by V. Zlatić,
        D. Garlaschelli and G. Caldarelli, EPL (Europhysics Letters),
        Volume 97, Number 2 (2012).
        https://iopscience.iop.org/article/10.1209/0295-5075/97/28005
    """
    ...
