from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Iterator
from typing import overload

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def enumerate_all_cliques(G: Graph[_Node]) -> Generator[list[_Node], None, None]:
    """
    Returns all cliques in an undirected graph.

    This function returns an iterator over cliques, each of which is a
    list of nodes. The iteration is ordered by cardinality of the
    cliques: first all cliques of size one, then all cliques of size
    two, etc.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    iterator
        An iterator over cliques, each of which is a list of nodes in
        `G`. The cliques are ordered according to size.

    Notes
    -----
    To obtain a list of all cliques, use
    `list(enumerate_all_cliques(G))`. However, be aware that in the
    worst-case, the length of this list can be exponential in the number
    of nodes in the graph (for example, when the graph is the complete
    graph). This function avoids storing all cliques in memory by only
    keeping current candidate node lists in memory during its search.

    The implementation is adapted from the algorithm by Zhang, et
    al. (2005) [1]_ to output all cliques discovered.

    This algorithm ignores self-loops and parallel edges, since cliques
    are not conventionally defined with such edges.

    References
    ----------
    .. [1] Yun Zhang, Abu-Khzam, F.N., Baldwin, N.E., Chesler, E.J.,
           Langston, M.A., Samatova, N.F.,
           "Genome-Scale Computational Approaches to Memory-Intensive
           Applications in Systems Biology".
           *Supercomputing*, 2005. Proceedings of the ACM/IEEE SC 2005
           Conference, pp. 12, 12--18 Nov. 2005.
           <https://doi.org/10.1109/SC.2005.29>.
    """
    ...
@_dispatchable
def find_cliques(G: Graph[_Node], nodes: Iterable[Incomplete] | None = None) -> Generator[list[_Node], None, None]: ...
@_dispatchable
def find_cliques_recursive(G: Graph[_Node], nodes: Iterable[Incomplete] | None = None) -> Iterator[list[_Node]]: ...
@_dispatchable
def make_max_clique_graph(G: Graph[_Node], create_using: Graph[_Node] | None = None) -> Graph[_Node]: ...
@_dispatchable
def make_clique_bipartite(
    G: Graph[_Node], fpos: bool | None = None, create_using: Graph[_Node] | None = None, name=None
) -> Graph[_Node]: ...
@overload
def node_clique_number(
    G: Graph[_Node], nodes=None, cliques: Iterable[Incomplete] | None = None, separate_nodes=False
) -> dict[_Node, int]: ...
@overload
def node_clique_number(G: Graph[_Node], nodes=None, cliques: Iterable[Incomplete] | None = None, separate_nodes=False) -> int: ...
