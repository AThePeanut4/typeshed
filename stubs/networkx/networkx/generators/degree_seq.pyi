"""Generate graphs with a given degree sequence or expected degree sequence."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.graph import Graph
from ..classes.multidigraph import MultiDiGraph
from ..classes.multigraph import MultiGraph

__all__ = [
    "configuration_model",
    "directed_configuration_model",
    "expected_degree_graph",
    "havel_hakimi_graph",
    "directed_havel_hakimi_graph",
    "degree_sequence_tree",
    "random_degree_sequence_graph",
]

@_dispatchable
def configuration_model(deg_sequence, create_using=None, seed=None) -> MultiGraph[Incomplete]:
    """
    Returns a random graph with the given degree sequence.

    The configuration model generates a random pseudograph (graph with
    parallel edges and self loops) by randomly assigning edges to
    match the given degree sequence.

    Parameters
    ----------
    deg_sequence :  list of nonnegative integers
        Each list entry corresponds to the degree of a node.
    create_using : NetworkX graph constructor, optional (default MultiGraph)
        Graph type to create. If graph instance, then cleared before populated.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    G : MultiGraph
        A graph with the specified degree sequence.
        Nodes are labeled starting at 0 with an index
        corresponding to the position in deg_sequence.

    Raises
    ------
    NetworkXError
        If the degree sequence does not have an even sum.

    See Also
    --------
    is_graphical

    Notes
    -----
    As described by Newman [1]_.

    A non-graphical degree sequence (not realizable by some simple
    graph) is allowed since this function returns graphs with self
    loops and parallel edges.  An exception is raised if the degree
    sequence does not have an even sum.

    This configuration model construction process can lead to
    duplicate edges and loops.  You can remove the self-loops and
    parallel edges (see below) which will likely result in a graph
    that doesn't have the exact degree sequence specified.

    The density of self-loops and parallel edges tends to decrease as
    the number of nodes increases. However, typically the number of
    self-loops will approach a Poisson distribution with a nonzero mean,
    and similarly for the number of parallel edges.  Consider a node
    with *k* stubs. The probability of being joined to another stub of
    the same node is basically (*k* - *1*) / *N*, where *k* is the
    degree and *N* is the number of nodes. So the probability of a
    self-loop scales like *c* / *N* for some constant *c*. As *N* grows,
    this means we expect *c* self-loops. Similarly for parallel edges.

    References
    ----------
    .. [1] M.E.J. Newman, "The structure and function of complex networks",
       SIAM REVIEW 45-2, pp 167-256, 2003.

    Examples
    --------
    You can create a degree sequence following a particular distribution
    by using the one of the distribution functions in
    :mod:`~networkx.utils.random_sequence` (or one of your own). For
    example, to create an undirected multigraph on one hundred nodes
    with degree sequence chosen from the power law distribution:

    >>> sequence = nx.random_powerlaw_tree_sequence(100, tries=5000)
    >>> G = nx.configuration_model(sequence)
    >>> len(G)
    100
    >>> actual_degrees = [d for v, d in G.degree()]
    >>> actual_degrees == sequence
    True

    The returned graph is a multigraph, which may have parallel
    edges. To remove any parallel edges from the returned graph:

    >>> G = nx.Graph(G)

    Similarly, to remove self-loops:

    >>> G.remove_edges_from(nx.selfloop_edges(G))
    """
    ...
@_dispatchable
def directed_configuration_model(
    in_degree_sequence, out_degree_sequence, create_using=None, seed=None
) -> MultiDiGraph[Incomplete]:
    """
    Returns a directed_random graph with the given degree sequences.

    The configuration model generates a random directed pseudograph
    (graph with parallel edges and self loops) by randomly assigning
    edges to match the given degree sequences.

    Parameters
    ----------
    in_degree_sequence :  list of nonnegative integers
       Each list entry corresponds to the in-degree of a node.
    out_degree_sequence :  list of nonnegative integers
       Each list entry corresponds to the out-degree of a node.
    create_using : NetworkX graph constructor, optional (default MultiDiGraph)
        Graph type to create. If graph instance, then cleared before populated.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    G : MultiDiGraph
        A graph with the specified degree sequences.
        Nodes are labeled starting at 0 with an index
        corresponding to the position in deg_sequence.

    Raises
    ------
    NetworkXError
        If the degree sequences do not have the same sum.

    See Also
    --------
    configuration_model

    Notes
    -----
    Algorithm as described by Newman [1]_.

    A non-graphical degree sequence (not realizable by some simple
    graph) is allowed since this function returns graphs with self
    loops and parallel edges.  An exception is raised if the degree
    sequences does not have the same sum.

    This configuration model construction process can lead to
    duplicate edges and loops.  You can remove the self-loops and
    parallel edges (see below) which will likely result in a graph
    that doesn't have the exact degree sequence specified.  This
    "finite-size effect" decreases as the size of the graph increases.

    References
    ----------
    .. [1] Newman, M. E. J. and Strogatz, S. H. and Watts, D. J.
       Random graphs with arbitrary degree distributions and their applications
       Phys. Rev. E, 64, 026118 (2001)

    Examples
    --------
    One can modify the in- and out-degree sequences from an existing
    directed graph in order to create a new directed graph. For example,
    here we modify the directed path graph:

    >>> D = nx.DiGraph([(0, 1), (1, 2), (2, 3)])
    >>> din = list(d for n, d in D.in_degree())
    >>> dout = list(d for n, d in D.out_degree())
    >>> din.append(1)
    >>> dout[0] = 2
    >>> # We now expect an edge from node 0 to a new node, node 3.
    ... D = nx.directed_configuration_model(din, dout)

    The returned graph is a directed multigraph, which may have parallel
    edges. To remove any parallel edges from the returned graph:

    >>> D = nx.DiGraph(D)

    Similarly, to remove self-loops:

    >>> D.remove_edges_from(nx.selfloop_edges(D))
    """
    ...
@_dispatchable
def expected_degree_graph(w, seed=None, selfloops: bool = True) -> Graph[Incomplete]:
    r"""
    Returns a random graph with given expected degrees.

    Given a sequence of expected degrees $W=(w_0,w_1,\ldots,w_{n-1})$
    of length $n$ this algorithm assigns an edge between node $u$ and
    node $v$ with probability

    .. math::

       p_{uv} = \frac{w_u w_v}{\sum_k w_k} .

    Parameters
    ----------
    w : list
        The list of expected degrees.
    selfloops: bool (default=True)
        Set to False to remove the possibility of self-loop edges.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    Graph

    Examples
    --------
    >>> z = [10 for i in range(100)]
    >>> G = nx.expected_degree_graph(z)

    Notes
    -----
    The nodes have integer labels corresponding to index of expected degrees
    input sequence.

    The complexity of this algorithm is $\mathcal{O}(n+m)$ where $n$ is the
    number of nodes and $m$ is the expected number of edges.

    The model in [1]_ includes the possibility of self-loop edges.
    Set selfloops=False to produce a graph without self loops.

    For finite graphs this model doesn't produce exactly the given
    expected degree sequence.  Instead the expected degrees are as
    follows.

    For the case without self loops (selfloops=False),

    .. math::

       E[deg(u)] = \sum_{v \ne u} p_{uv}
                = w_u \left( 1 - \frac{w_u}{\sum_k w_k} \right) .


    NetworkX uses the standard convention that a self-loop edge counts 2
    in the degree of a node, so with self loops (selfloops=True),

    .. math::

       E[deg(u)] =  \sum_{v \ne u} p_{uv}  + 2 p_{uu}
                = w_u \left( 1 + \frac{w_u}{\sum_k w_k} \right) .

    References
    ----------
    .. [1] Fan Chung and L. Lu, Connected components in random graphs with
       given expected degree sequences, Ann. Combinatorics, 6,
       pp. 125-145, 2002.
    .. [2] Joel Miller and Aric Hagberg,
       Efficient generation of networks with given expected degrees,
       in Algorithms and Models for the Web-Graph (WAW 2011),
       Alan Frieze, Paul Horn, and Paweł Prałat (Eds), LNCS 6732,
       pp. 115-126, 2011.
    """
    ...
@_dispatchable
def havel_hakimi_graph(deg_sequence, create_using=None):
    """
    Returns a simple graph with given degree sequence constructed
    using the Havel-Hakimi algorithm.

    Parameters
    ----------
    deg_sequence: list of integers
        Each integer corresponds to the degree of a node (need not be sorted).
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
        Graph type to create. If graph instance, then cleared before populated.
        Directed graphs are not allowed.

    Raises
    ------
    NetworkXException
        For a non-graphical degree sequence (i.e. one
        not realizable by some simple graph).

    Notes
    -----
    The Havel-Hakimi algorithm constructs a simple graph by
    successively connecting the node of highest degree to other nodes
    of highest degree, resorting remaining nodes by degree, and
    repeating the process. The resulting graph has a high
    degree-associativity.  Nodes are labeled 1,.., len(deg_sequence),
    corresponding to their position in deg_sequence.

    The basic algorithm is from Hakimi [1]_ and was generalized by
    Kleitman and Wang [2]_.

    References
    ----------
    .. [1] Hakimi S., On Realizability of a Set of Integers as
       Degrees of the Vertices of a Linear Graph. I,
       Journal of SIAM, 10(3), pp. 496-506 (1962)
    .. [2] Kleitman D.J. and Wang D.L.
       Algorithms for Constructing Graphs and Digraphs with Given Valences
       and Factors  Discrete Mathematics, 6(1), pp. 79-88 (1973)
    """
    ...
@_dispatchable
def directed_havel_hakimi_graph(in_deg_sequence, out_deg_sequence, create_using=None) -> DiGraph[Incomplete]:
    """
    Returns a directed graph with the given degree sequences.

    Parameters
    ----------
    in_deg_sequence :  list of integers
        Each list entry corresponds to the in-degree of a node.
    out_deg_sequence : list of integers
        Each list entry corresponds to the out-degree of a node.
    create_using : NetworkX graph constructor, optional (default DiGraph)
        Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    G : DiGraph
        A graph with the specified degree sequences.
        Nodes are labeled starting at 0 with an index
        corresponding to the position in deg_sequence

    Raises
    ------
    NetworkXError
        If the degree sequences are not digraphical.

    See Also
    --------
    configuration_model

    Notes
    -----
    Algorithm as described by Kleitman and Wang [1]_.

    References
    ----------
    .. [1] D.J. Kleitman and D.L. Wang
       Algorithms for Constructing Graphs and Digraphs with Given Valences
       and Factors Discrete Mathematics, 6(1), pp. 79-88 (1973)
    """
    ...
@_dispatchable
def degree_sequence_tree(deg_sequence, create_using=None):
    """
    Make a tree for the given degree sequence.

    A tree has #nodes-#edges=1 so
    the degree sequence must have
    len(deg_sequence)-sum(deg_sequence)/2=1
    """
    ...
@_dispatchable
def random_degree_sequence_graph(sequence, seed=None, tries: int = 10) -> Graph[Incomplete]:
    """
    Returns a simple random graph with the given degree sequence.

    If the maximum degree $d_m$ in the sequence is $O(m^{1/4})$ then the
    algorithm produces almost uniform random graphs in $O(m d_m)$ time
    where $m$ is the number of edges.

    Parameters
    ----------
    sequence :  list of integers
        Sequence of degrees
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.
    tries : int, optional
        Maximum number of tries to create a graph

    Returns
    -------
    G : Graph
        A graph with the specified degree sequence.
        Nodes are labeled starting at 0 with an index
        corresponding to the position in the sequence.

    Raises
    ------
    NetworkXUnfeasible
        If the degree sequence is not graphical.
    NetworkXError
        If a graph is not produced in specified number of tries

    See Also
    --------
    is_graphical, configuration_model

    Notes
    -----
    The generator algorithm [1]_ is not guaranteed to produce a graph.

    References
    ----------
    .. [1] Moshen Bayati, Jeong Han Kim, and Amin Saberi,
       A sequential algorithm for generating random graphs.
       Algorithmica, Volume 58, Number 4, 860-910,
       DOI: 10.1007/s00453-009-9340-1

    Examples
    --------
    >>> sequence = [1, 2, 2, 3]
    >>> G = nx.random_degree_sequence_graph(sequence, seed=42)
    >>> sorted(d for n, d in G.degree())
    [1, 2, 2, 3]
    """
    ...

class DegreeSequenceRandomGraph:
    rng: Incomplete
    degree: Incomplete
    m: Incomplete
    dmax: Incomplete
    def __init__(self, degree, rng) -> None: ...
    remaining_degree: Incomplete
    graph: Incomplete
    def generate(self): ...
    def update_remaining(self, u, v, aux_graph=None) -> None: ...
    def p(self, u, v): ...
    def q(self, u, v): ...
    def suitable_edge(self):
        """
        Returns True if and only if an arbitrary remaining node can
        potentially be joined with some other remaining node.
        """
        ...
    def phase1(self) -> None: ...
    def phase2(self) -> None: ...
    def phase3(self) -> None: ...
