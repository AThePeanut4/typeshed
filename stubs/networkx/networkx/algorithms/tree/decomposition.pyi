"""Function for computing a junction tree of a graph."""

from _typeshed import Incomplete

from networkx.classes.graph import Graph
from networkx.utils.backends import _dispatchable

__all__ = ["junction_tree"]

@_dispatchable
def junction_tree(G) -> Graph[Incomplete]:
    """
    Returns a junction tree of a given graph.

    A junction tree (or clique tree) is constructed from a (un)directed graph G.
    The tree is constructed based on a moralized and triangulated version of G.
    The tree's nodes consist of maximal cliques and sepsets of the revised graph.
    The sepset of two cliques is the intersection of the nodes of these cliques,
    e.g. the sepset of (A,B,C) and (A,C,E,F) is (A,C). These nodes are often called
    "variables" in this literature. The tree is bipartite with each sepset
    connected to its two cliques.

    Junction Trees are not unique as the order of clique consideration determines
    which sepsets are included.

    The junction tree algorithm consists of five steps [1]_:

    1. Moralize the graph
    2. Triangulate the graph
    3. Find maximal cliques
    4. Build the tree from cliques, connecting cliques with shared
       nodes, set edge-weight to number of shared variables
    5. Find maximum spanning tree


    Parameters
    ----------
    G : networkx.Graph
        Directed or undirected graph.

    Returns
    -------
    junction_tree : networkx.Graph
        The corresponding junction tree of `G`.

    Raises
    ------
    NetworkXNotImplemented
        Raised if `G` is an instance of `MultiGraph` or `MultiDiGraph`.

    References
    ----------
    .. [1] Junction tree algorithm:
       https://en.wikipedia.org/wiki/Junction_tree_algorithm

    .. [2] Finn V. Jensen and Frank Jensen. 1994. Optimal
       junction trees. In Proceedings of the Tenth international
       conference on Uncertainty in artificial intelligence (UAI’94).
       Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 360–366.
    """
    ...
