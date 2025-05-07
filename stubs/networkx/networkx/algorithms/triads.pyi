"""Functions for analyzing triads of a graph."""

from _typeshed import Incomplete
from collections.abc import Collection, Generator

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def triadic_census(G: DiGraph[_Node], nodelist: Collection[_Node] | None = None): ...
@_dispatchable
def is_triad(G: Graph[_Node]):
    """
    Returns True if the graph G is a triad, else False.

    Parameters
    ----------
    G : graph
       A NetworkX Graph

    Returns
    -------
    istriad : boolean
       Whether G is a valid triad

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
    >>> nx.is_triad(G)
    True
    >>> G.add_edge(0, 1)
    >>> nx.is_triad(G)
    False
    """
    ...
@_dispatchable
def all_triplets(G: DiGraph[_Node]):
    """
    Returns a generator of all possible sets of 3 nodes in a DiGraph.

    .. deprecated:: 3.3

       all_triplets is deprecated and will be removed in NetworkX version 3.5.
       Use `itertools.combinations` instead::

          all_triplets = itertools.combinations(G, 3)

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph

    Returns
    -------
    triplets : generator of 3-tuples
       Generator of tuples of 3 nodes

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 4)])
    >>> list(nx.all_triplets(G))
    [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    """
    ...
@_dispatchable
def all_triads(G: DiGraph[_Node]) -> Generator[Incomplete, None, None]:
    """
    A generator of all possible triads in G.

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph

    Returns
    -------
    all_triads : generator of DiGraphs
       Generator of triads (order-3 DiGraphs)

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1), (4, 2)])
    >>> for triad in nx.all_triads(G):
    ...     print(triad.edges)
    [(1, 2), (2, 3), (3, 1)]
    [(1, 2), (4, 1), (4, 2)]
    [(3, 1), (3, 4), (4, 1)]
    [(2, 3), (3, 4), (4, 2)]
    """
    ...
@_dispatchable
def triads_by_type(G: DiGraph[_Node]):
    """
    Returns a list of all triads for each triad type in a directed graph.
    There are exactly 16 different types of triads possible. Suppose 1, 2, 3 are three
    nodes, they will be classified as a particular triad type if their connections
    are as follows:

    - 003: 1, 2, 3
    - 012: 1 -> 2, 3
    - 102: 1 <-> 2, 3
    - 021D: 1 <- 2 -> 3
    - 021U: 1 -> 2 <- 3
    - 021C: 1 -> 2 -> 3
    - 111D: 1 <-> 2 <- 3
    - 111U: 1 <-> 2 -> 3
    - 030T: 1 -> 2 -> 3, 1 -> 3
    - 030C: 1 <- 2 <- 3, 1 -> 3
    - 201: 1 <-> 2 <-> 3
    - 120D: 1 <- 2 -> 3, 1 <-> 3
    - 120U: 1 -> 2 <- 3, 1 <-> 3
    - 120C: 1 -> 2 -> 3, 1 <-> 3
    - 210: 1 -> 2 <-> 3, 1 <-> 3
    - 300: 1 <-> 2 <-> 3, 1 <-> 3

    Refer to the :doc:`example gallery </auto_examples/graph/plot_triad_types>`
    for visual examples of the triad types.

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph

    Returns
    -------
    tri_by_type : dict
       Dictionary with triad types as keys and lists of triads as values.

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (1, 3), (2, 3), (3, 1), (5, 6), (5, 4), (6, 7)])
    >>> dict = nx.triads_by_type(G)
    >>> dict["120C"][0].edges()
    OutEdgeView([(1, 2), (1, 3), (2, 3), (3, 1)])
    >>> dict["012"][0].edges()
    OutEdgeView([(1, 2)])

    References
    ----------
    .. [1] Snijders, T. (2012). "Transitivity and triads." University of
        Oxford.
        https://web.archive.org/web/20170830032057/http://www.stats.ox.ac.uk/~snijders/Trans_Triads_ha.pdf
    """
    ...
@_dispatchable
def triad_type(G: DiGraph[_Node]):
    """
    Returns the sociological triad type for a triad.

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph with 3 nodes

    Returns
    -------
    triad_type : str
       A string identifying the triad type

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
    >>> nx.triad_type(G)
    '030C'
    >>> G.add_edge(1, 3)
    >>> nx.triad_type(G)
    '120C'

    Notes
    -----
    There can be 6 unique edges in a triad (order-3 DiGraph) (so 2^^6=64 unique
    triads given 3 nodes). These 64 triads each display exactly 1 of 16
    topologies of triads (topologies can be permuted). These topologies are
    identified by the following notation:

    {m}{a}{n}{type} (for example: 111D, 210, 102)

    Here:

    {m}     = number of mutual ties (takes 0, 1, 2, 3); a mutual tie is (0,1)
              AND (1,0)
    {a}     = number of asymmetric ties (takes 0, 1, 2, 3); an asymmetric tie
              is (0,1) BUT NOT (1,0) or vice versa
    {n}     = number of null ties (takes 0, 1, 2, 3); a null tie is NEITHER
              (0,1) NOR (1,0)
    {type}  = a letter (takes U, D, C, T) corresponding to up, down, cyclical
              and transitive. This is only used for topologies that can have
              more than one form (eg: 021D and 021U).

    References
    ----------
    .. [1] Snijders, T. (2012). "Transitivity and triads." University of
        Oxford.
        https://web.archive.org/web/20170830032057/http://www.stats.ox.ac.uk/~snijders/Trans_Triads_ha.pdf
    """
    ...
@_dispatchable
def random_triad(G: DiGraph[_Node], seed: int | RandomState | None = None):
    """
    Returns a random triad from a directed graph.

    .. deprecated:: 3.3

       random_triad is deprecated and will be removed in version 3.5.
       Use random sampling directly instead::

          G.subgraph(random.sample(list(G), 3))

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    G2 : subgraph
       A randomly selected triad (order-3 NetworkX DiGraph)

    Raises
    ------
    NetworkXError
        If the input Graph has less than 3 nodes.

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (1, 3), (2, 3), (3, 1), (5, 6), (5, 4), (6, 7)])
    >>> triad = nx.random_triad(G, seed=1)
    >>> triad.edges
    OutEdgeView([(1, 2)])
    """
    ...
