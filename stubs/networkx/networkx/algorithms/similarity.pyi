from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Callable, Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def graph_edit_distance(
    G1: Graph[_Node],
    G2: Graph[_Node],
    node_match: Callable[..., Incomplete] | None = None,
    edge_match: Callable[..., Incomplete] | None = None,
    node_subst_cost: Callable[..., Incomplete] | None = None,
    node_del_cost: Callable[..., Incomplete] | None = None,
    node_ins_cost: Callable[..., Incomplete] | None = None,
    edge_subst_cost: Callable[..., Incomplete] | None = None,
    edge_del_cost: Callable[..., Incomplete] | None = None,
    edge_ins_cost: Callable[..., Incomplete] | None = None,
    roots=None,
    upper_bound: float | None = None,
    timeout: float | None = None,
): ...
@_dispatchable
def optimal_edit_paths(
    G1: Graph[_Node],
    G2: Graph[_Node],
    node_match: Callable[..., Incomplete] | None = None,
    edge_match: Callable[..., Incomplete] | None = None,
    node_subst_cost: Callable[..., Incomplete] | None = None,
    node_del_cost: Callable[..., Incomplete] | None = None,
    node_ins_cost: Callable[..., Incomplete] | None = None,
    edge_subst_cost: Callable[..., Incomplete] | None = None,
    edge_del_cost: Callable[..., Incomplete] | None = None,
    edge_ins_cost: Callable[..., Incomplete] | None = None,
    upper_bound: float | None = None,
): ...
@_dispatchable
def optimize_graph_edit_distance(
    G1: Graph[_Node],
    G2: Graph[_Node],
    node_match: Callable[..., Incomplete] | None = None,
    edge_match: Callable[..., Incomplete] | None = None,
    node_subst_cost: Callable[..., Incomplete] | None = None,
    node_del_cost: Callable[..., Incomplete] | None = None,
    node_ins_cost: Callable[..., Incomplete] | None = None,
    edge_subst_cost: Callable[..., Incomplete] | None = None,
    edge_del_cost: Callable[..., Incomplete] | None = None,
    edge_ins_cost: Callable[..., Incomplete] | None = None,
    upper_bound: float | None = None,
) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def optimize_edit_paths(
    G1: Graph[_Node],
    G2: Graph[_Node],
    node_match: Callable[..., Incomplete] | None = None,
    edge_match: Callable[..., Incomplete] | None = None,
    node_subst_cost: Callable[..., Incomplete] | None = None,
    node_del_cost: Callable[..., Incomplete] | None = None,
    node_ins_cost: Callable[..., Incomplete] | None = None,
    edge_subst_cost: Callable[..., Incomplete] | None = None,
    edge_del_cost: Callable[..., Incomplete] | None = None,
    edge_ins_cost: Callable[..., Incomplete] | None = None,
    upper_bound: float | None = None,
    strictly_decreasing: bool = True,
    roots=None,
    timeout: float | None = None,
) -> Generator[Incomplete, None, Incomplete]: ...
@_dispatchable
def simrank_similarity(
    G: Graph[_Node],
    source: _Node | None = None,
    target: _Node | None = None,
    importance_factor: float = 0.9,
    max_iterations: int = 1000,
    tolerance: float = 0.0001,
):
    """
    Returns the SimRank similarity of nodes in the graph ``G``.

    SimRank is a similarity metric that says "two objects are considered
    to be similar if they are referenced by similar objects." [1]_.

    The pseudo-code definition from the paper is::

        def simrank(G, u, v):
            in_neighbors_u = G.predecessors(u)
            in_neighbors_v = G.predecessors(v)
            scale = C / (len(in_neighbors_u) * len(in_neighbors_v))
            return scale * sum(
                simrank(G, w, x) for w, x in product(in_neighbors_u, in_neighbors_v)
            )

    where ``G`` is the graph, ``u`` is the source, ``v`` is the target,
    and ``C`` is a float decay or importance factor between 0 and 1.

    The SimRank algorithm for determining node similarity is defined in
    [2]_.

    Parameters
    ----------
    G : NetworkX graph
        A NetworkX graph

    source : node
        If this is specified, the returned dictionary maps each node
        ``v`` in the graph to the similarity between ``source`` and
        ``v``.

    target : node
        If both ``source`` and ``target`` are specified, the similarity
        value between ``source`` and ``target`` is returned. If
        ``target`` is specified but ``source`` is not, this argument is
        ignored.

    importance_factor : float
        The relative importance of indirect neighbors with respect to
        direct neighbors.

    max_iterations : integer
        Maximum number of iterations.

    tolerance : float
        Error tolerance used to check convergence. When an iteration of
        the algorithm finds that no similarity value changes more than
        this amount, the algorithm halts.

    Returns
    -------
    similarity : dictionary or float
        If ``source`` and ``target`` are both ``None``, this returns a
        dictionary of dictionaries, where keys are node pairs and value
        are similarity of the pair of nodes.

        If ``source`` is not ``None`` but ``target`` is, this returns a
        dictionary mapping node to the similarity of ``source`` and that
        node.

        If neither ``source`` nor ``target`` is ``None``, this returns
        the similarity value for the given pair of nodes.

    Raises
    ------
    ExceededMaxIterations
        If the algorithm does not converge within ``max_iterations``.

    NodeNotFound
        If either ``source`` or ``target`` is not in `G`.

    Examples
    --------
    >>> G = nx.cycle_graph(2)
    >>> nx.simrank_similarity(G)
    {0: {0: 1.0, 1: 0.0}, 1: {0: 0.0, 1: 1.0}}
    >>> nx.simrank_similarity(G, source=0)
    {0: 1.0, 1: 0.0}
    >>> nx.simrank_similarity(G, source=0, target=0)
    1.0

    The result of this function can be converted to a numpy array
    representing the SimRank matrix by using the node order of the
    graph to determine which row and column represent each node.
    Other ordering of nodes is also possible.

    >>> import numpy as np
    >>> sim = nx.simrank_similarity(G)
    >>> np.array([[sim[u][v] for v in G] for u in G])
    array([[1., 0.],
           [0., 1.]])
    >>> sim_1d = nx.simrank_similarity(G, source=0)
    >>> np.array([sim[0][v] for v in G])
    array([1., 0.])

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/SimRank
    .. [2] G. Jeh and J. Widom.
           "SimRank: a measure of structural-context similarity",
           In KDD'02: Proceedings of the Eighth ACM SIGKDD
           International Conference on Knowledge Discovery and Data Mining,
           pp. 538--543. ACM Press, 2002.
    """
    ...
@_dispatchable
def panther_similarity(
    G: Graph[_Node],
    source: _Node,
    k: int = 5,
    path_length: int = 5,
    c: float = 0.5,
    delta: float = 0.1,
    eps=None,
    weight: str | None = "weight",
): ...
@_dispatchable
def generate_random_paths(
    G: Graph[_Node],
    sample_size: int,
    path_length: int = 5,
    index_map: SupportsGetItem[Incomplete, Incomplete] | None = None,
    weight: str | None = "weight",
    seed: int | RandomState | None = None,
) -> Generator[Incomplete, None, None]: ...
