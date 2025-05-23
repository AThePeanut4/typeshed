"""Distance measures approximated metrics."""

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

__all__ = ["diameter"]

@_dispatchable
def diameter(G: Graph[_Node], seed: int | RandomState | None = None):
    """
    Returns a lower bound on the diameter of the graph G.

    The function computes a lower bound on the diameter (i.e., the maximum eccentricity)
    of a directed or undirected graph G. The procedure used varies depending on the graph
    being directed or not.

    If G is an `undirected` graph, then the function uses the `2-sweep` algorithm [1]_.
    The main idea is to pick the farthest node from a random node and return its eccentricity.

    Otherwise, if G is a `directed` graph, the function uses the `2-dSweep` algorithm [2]_,
    The procedure starts by selecting a random source node $s$ from which it performs a
    forward and a backward BFS. Let $a_1$ and $a_2$ be the farthest nodes in the forward and
    backward cases, respectively. Then, it computes the backward eccentricity of $a_1$ using
    a backward BFS and the forward eccentricity of $a_2$ using a forward BFS.
    Finally, it returns the best lower bound between the two.

    In both cases, the time complexity is linear with respect to the size of G.

    Parameters
    ----------
    G : NetworkX graph

    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    d : integer
       Lower Bound on the Diameter of G

    Examples
    --------
    >>> G = nx.path_graph(10)  # undirected graph
    >>> nx.diameter(G)
    9
    >>> G = nx.cycle_graph(3, create_using=nx.DiGraph)  # directed graph
    >>> nx.diameter(G)
    2

    Raises
    ------
    NetworkXError
        If the graph is empty or
        If the graph is undirected and not connected or
        If the graph is directed and not strongly connected.

    See Also
    --------
    networkx.algorithms.distance_measures.diameter

    References
    ----------
    .. [1] Magnien, Clémence, Matthieu Latapy, and Michel Habib.
       *Fast computation of empirically tight bounds for the diameter of massive graphs.*
       Journal of Experimental Algorithmics (JEA), 2009.
       https://arxiv.org/pdf/0904.2728.pdf
    .. [2] Crescenzi, Pierluigi, Roberto Grossi, Leonardo Lanzi, and Andrea Marino.
       *On computing the diameter of real-world directed (weighted) graphs.*
       International Symposium on Experimental Algorithms. Springer, Berlin, Heidelberg, 2012.
       https://courses.cs.ut.ee/MTAT.03.238/2014_fall/uploads/Main/diameter.pdf
    """
    ...
