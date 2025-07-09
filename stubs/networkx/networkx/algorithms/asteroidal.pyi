"""
Algorithms for asteroidal triples and asteroidal numbers in graphs.

An asteroidal triple in a graph G is a set of three non-adjacent vertices
u, v and w such that there exist a path between any two of them that avoids
closed neighborhood of the third. More formally, v_j, v_k belongs to the same
connected component of G - N[v_i], where N[v_i] denotes the closed neighborhood
of v_i. A graph which does not contain any asteroidal triples is called
an AT-free graph. The class of AT-free graphs is a graph class for which
many NP-complete problems are solvable in polynomial time. Amongst them,
independent set and coloring.
"""

from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_at_free", "find_asteroidal_triple"]

@_dispatchable
def find_asteroidal_triple(G: Graph[_Node]) -> list[Incomplete] | None: ...
@_dispatchable
def is_at_free(G: Graph[_Node]) -> bool:
    """
    Check if a graph is AT-free.

    The method uses the `find_asteroidal_triple` method to recognize
    an AT-free graph. If no asteroidal triple is found the graph is
    AT-free and True is returned. If at least one asteroidal triple is
    found the graph is not AT-free and False is returned.

    Parameters
    ----------
    G : NetworkX Graph
        The graph to check whether is AT-free or not.

    Returns
    -------
    bool
        True if G is AT-free and False otherwise.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (4, 5)])
    >>> nx.is_at_free(G)
    True

    >>> G = nx.cycle_graph(6)
    >>> nx.is_at_free(G)
    False
    """
    ...
@_dispatchable
def create_component_structure(G: Graph[_Node]) -> dict[Incomplete, Incomplete]:
    r"""
    Create component structure for G.

    A *component structure* is an `nxn` array, denoted `c`, where `n` is
    the number of vertices,  where each row and column corresponds to a vertex.

    .. math::
        c_{uv} = \begin{cases} 0, if v \in N[u] \\
            k, if v \in component k of G \setminus N[u] \end{cases}

    Where `k` is an arbitrary label for each component. The structure is used
    to simplify the detection of asteroidal triples.

    Parameters
    ----------
    G : NetworkX Graph
        Undirected, simple graph.

    Returns
    -------
    component_structure : dictionary
        A dictionary of dictionaries, keyed by pairs of vertices.
    """
    ...
