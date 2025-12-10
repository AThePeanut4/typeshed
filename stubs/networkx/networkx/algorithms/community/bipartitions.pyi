"""Functions for splitting a network into two communities (finding a bipartition)."""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.algorithms.shortest_paths.weighted import _WeightFunc
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

__all__ = ["kernighan_lin_bisection", "spectral_modularity_bipartition", "greedy_node_swap_bipartition"]

@_dispatchable
def kernighan_lin_bisection(
    G: Graph[_Node],
    partition: tuple[Iterable[Incomplete], Iterable[Incomplete]] | None = None,
    max_iter: int = 10,
    weight: str | _WeightFunc[_Node] = "weight",
    seed: int | RandomState | None = None,
) -> tuple[set[Incomplete], set[Incomplete]]:
    """
    Partition a graph into two blocks using the Kernighan–Lin algorithm.

    This algorithm partitions a network into two sets by iteratively
    swapping pairs of nodes to reduce the edge cut between the two sets.  The
    pairs are chosen according to a modified form of Kernighan-Lin [1]_, which
    moves nodes individually, alternating between sides to keep the bisection
    balanced.

    Kernighan-Lin is an approximate algorithm for maximal modularity bisection.
    In [2]_ they suggest that fine-tuned improvements can be made using
    greedy node swapping, (see `greedy_node_swap_bipartition`).
    The improvements are typically only a few percent of the modularity value.
    But they claim that can make a difference between a good and excellent method.
    This function does not perform any improvements. But you can do that yourself.

    Parameters
    ----------
    G : NetworkX graph
        Graph must be undirected.

    partition : tuple
        Pair of iterables containing an initial partition. If not
        specified, a random balanced partition is used.

    max_iter : int
        Maximum number of times to attempt swaps to find an
        improvement before giving up.

    weight : string or function (default: "weight")
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number or None to indicate a hidden edge.

    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.
        Only used if partition is None

    Returns
    -------
    partition : tuple
        A pair of sets of nodes representing the bipartition.

    Raises
    ------
    NetworkXError
        If `partition` is not a valid partition of the nodes of the graph.

    References
    ----------
    .. [1] Kernighan, B. W.; Lin, Shen (1970).
       "An efficient heuristic procedure for partitioning graphs."
       *Bell Systems Technical Journal* 49: 291--307.
       Oxford University Press 2011.
    .. [2] M. E. J. Newman,
       "Modularity and community structure in networks",
       PNAS, 103 (23), p. 8577-8582,
       https://doi.org/10.1073/pnas.0601602103
    """
    ...
def spectral_modularity_bipartition(G: Graph[_Node]) -> tuple[set[Incomplete], set[Incomplete]]:
    r"""
    Return a bipartition of the nodes based on the spectrum of the
    modularity matrix of the graph.

    This method calculates the eigenvector associated with the second
    largest eigenvalue of the modularity matrix, where the modularity
    matrix *B* is defined by

    ..math::

        B_{i j} = A_{i j} - \frac{k_i k_j}{2 m},

    where *A* is the adjacency matrix, `k_i` is the degree of node *i*,
    and *m* is the number of edges in the graph. Nodes whose
    corresponding values in the eigenvector are negative are placed in
    one block, nodes whose values are nonnegative are placed in another
    block.

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    C : tuple
        Pair of communities as two sets of nodes of ``G``, partitioned
        according to second largest eigenvalue of the modularity matrix.

    Examples
    --------
    >>> G = nx.karate_club_graph()
    >>> MrHi, Officer = nx.community.spectral_modularity_bipartition(G)
    >>> MrHi, Officer = sorted([sorted(MrHi), sorted(Officer)])
    >>> MrHi
    [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 19, 21]
    >>> Officer
    [8, 9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    References
    ----------
    .. [1] M. E. J. Newman *Networks: An Introduction*, pages 373--378
       Oxford University Press 2011.
    .. [2] M. E. J. Newman,
       "Modularity and community structure in networks",
       PNAS, 103 (23), p. 8577-8582,
       https://doi.org/10.1073/pnas.0601602103
    """
    ...
def greedy_node_swap_bipartition(
    G: Graph[_Node], *, init_split: tuple[set[Incomplete], set[Incomplete]] | None = None, max_iter: int = 10
) -> tuple[set[Incomplete], set[Incomplete]]:
    """
    Split the nodes into two communities based on greedy
    modularity maximization.

    The algorithm works by selecting a node to change communities which
    will maximize the modularity. The swap is made and the community
    structure with the highest modularity is kept.

    Parameters
    ----------
    G : NetworkX graph

    init_split : 2-tuple of sets of nodes
        Pair of sets of nodes in ``G`` providing an initial bipartition
        for the algorithm. If not specified, a random balanced partition
        is used. If this pair of sets is not a partition of the nodes of `G`,
        :exc:`NetworkXException` is raised.

    max_iter : int
      Maximum number of iterations of attempting swaps to find an improvement.

    Returns
    -------
    max_split : 2-tuple of sets of nodes
        Pair of sets of nodes of ``G``, partitioned according to a
        node swap greedy modularity maximization algorithm.

    Raises
    ------
    NetworkXError
      if init_split is not a valid partition of the
      graph into two communities or if G is a MultiGraph

    Examples
    --------
    >>> G = nx.barbell_graph(3, 0)
    >>> left, right = nx.community.greedy_node_swap_bipartition(G)
    >>> # Sort the communities so the nodes appear in increasing order.
    >>> left, right = sorted([sorted(left), sorted(right)])
    >>> sorted(left)
    [0, 1, 2]
    >>> sorted(right)
    [3, 4, 5]

    Notes
    -----
    This function is not implemented for multigraphs.

    References
    ----------
    .. [1] M. E. J. Newman "Networks: An Introduction", pages 373--375.
       Oxford University Press 2011.
    """
    ...
