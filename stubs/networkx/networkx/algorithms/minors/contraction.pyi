"""Provides functions for computing minors of a graph."""

from _typeshed import Incomplete
from collections.abc import Callable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["contracted_edge", "contracted_nodes", "equivalence_classes", "identified_nodes", "quotient_graph"]

@_dispatchable
def equivalence_classes(iterable, relation):
    """
    Returns equivalence classes of `relation` when applied to `iterable`.

    The equivalence classes, or blocks, consist of objects from `iterable`
    which are all equivalent. They are defined to be equivalent if the
    `relation` function returns `True` when passed any two objects from that
    class, and `False` otherwise. To define an equivalence relation the
    function must be reflexive, symmetric and transitive.

    Parameters
    ----------
    iterable : list, tuple, or set
        An iterable of elements/nodes.

    relation : function
        A Boolean-valued function that implements an equivalence relation
        (reflexive, symmetric, transitive binary relation) on the elements
        of `iterable` - it must take two elements and return `True` if
        they are related, or `False` if not.

    Returns
    -------
    set of frozensets
        A set of frozensets representing the partition induced by the equivalence
        relation function `relation` on the elements of `iterable`. Each
        member set in the return set represents an equivalence class, or
        block, of the partition.

        Duplicate elements will be ignored so it makes the most sense for
        `iterable` to be a :class:`set`.

    Notes
    -----
    This function does not check that `relation` represents an equivalence
    relation. You can check that your equivalence classes provide a partition
    using `is_partition`.

    Examples
    --------
    Let `X` be the set of integers from `0` to `9`, and consider an equivalence
    relation `R` on `X` of congruence modulo `3`: this means that two integers
    `x` and `y` in `X` are equivalent under `R` if they leave the same
    remainder when divided by `3`, i.e. `(x - y) mod 3 = 0`.

    The equivalence classes of this relation are `{0, 3, 6, 9}`, `{1, 4, 7}`,
    `{2, 5, 8}`: `0`, `3`, `6`, `9` are all divisible by `3` and leave zero
    remainder; `1`, `4`, `7` leave remainder `1`; while `2`, `5` and `8` leave
    remainder `2`. We can see this by calling `equivalence_classes` with
    `X` and a function implementation of `R`.

    >>> X = set(range(10))
    >>> def mod3(x, y):
    ...     return (x - y) % 3 == 0
    >>> equivalence_classes(X, mod3)  # doctest: +SKIP
    {frozenset({1, 4, 7}), frozenset({8, 2, 5}), frozenset({0, 9, 3, 6})}
    """
    ...
@_dispatchable
def quotient_graph(
    G: Graph[_Node],
    partition,
    edge_relation=None,
    node_data: Callable[..., Incomplete] | None = None,
    edge_data: Callable[..., Incomplete] | None = None,
    weight: str | None = "weight",
    relabel: bool = False,
    create_using: Graph[_Node] | None = None,
):
    """
    Returns the quotient graph of `G` under the specified equivalence
    relation on nodes.

    Parameters
    ----------
    G : NetworkX graph
        The graph for which to return the quotient graph with the
        specified node relation.

    partition : function, or dict or list of lists, tuples or sets
        If a function, this function must represent an equivalence
        relation on the nodes of `G`. It must take two arguments *u*
        and *v* and return True exactly when *u* and *v* are in the
        same equivalence class. The equivalence classes form the nodes
        in the returned graph.

        If a dict of lists/tuples/sets, the keys can be any meaningful
        block labels, but the values must be the block lists/tuples/sets
        (one list/tuple/set per block), and the blocks must form a valid
        partition of the nodes of the graph. That is, each node must be
        in exactly one block of the partition.

        If a list of sets, the list must form a valid partition of
        the nodes of the graph. That is, each node must be in exactly
        one block of the partition.

    edge_relation : Boolean function with two arguments
        This function must represent an edge relation on the *blocks* of
        the `partition` of `G`. It must take two arguments, *B* and *C*,
        each one a set of nodes, and return True exactly when there should be
        an edge joining block *B* to block *C* in the returned graph.

        If `edge_relation` is not specified, it is assumed to be the
        following relation. Block *B* is related to block *C* if and
        only if some node in *B* is adjacent to some node in *C*,
        according to the edge set of `G`.

    node_data : function
        This function takes one argument, *B*, a set of nodes in `G`,
        and must return a dictionary representing the node data
        attributes to set on the node representing *B* in the quotient graph.
        If None, the following node attributes will be set:

        * 'graph', the subgraph of the graph `G` that this block
          represents,
        * 'nnodes', the number of nodes in this block,
        * 'nedges', the number of edges within this block,
        * 'density', the density of the subgraph of `G` that this
          block represents.

    edge_data : function
        This function takes two arguments, *B* and *C*, each one a set
        of nodes, and must return a dictionary representing the edge
        data attributes to set on the edge joining *B* and *C*, should
        there be an edge joining *B* and *C* in the quotient graph (if
        no such edge occurs in the quotient graph as determined by
        `edge_relation`, then the output of this function is ignored).

        If the quotient graph would be a multigraph, this function is
        not applied, since the edge data from each edge in the graph
        `G` appears in the edges of the quotient graph.

    weight : string or None, optional (default="weight")
        The name of an edge attribute that holds the numerical value
        used as a weight. If None then each edge has weight 1.

    relabel : bool
        If True, relabel the nodes of the quotient graph to be
        nonnegative integers. Otherwise, the nodes are identified with
        :class:`frozenset` instances representing the blocks given in
        `partition`.

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    NetworkX graph
        The quotient graph of `G` under the equivalence relation
        specified by `partition`. If the partition were given as a
        list of :class:`set` instances and `relabel` is False,
        each node will be a :class:`frozenset` corresponding to the same
        :class:`set`.

    Raises
    ------
    NetworkXException
        If the given partition is not a valid partition of the nodes of
        `G`.

    Examples
    --------
    The quotient graph of the complete bipartite graph under the "same
    neighbors" equivalence relation is `K_2`. Under this relation, two nodes
    are equivalent if they are not adjacent but have the same neighbor set.

    >>> G = nx.complete_bipartite_graph(2, 3)
    >>> same_neighbors = lambda u, v: (u not in G[v] and v not in G[u] and G[u] == G[v])
    >>> Q = nx.quotient_graph(G, same_neighbors)
    >>> K2 = nx.complete_graph(2)
    >>> nx.is_isomorphic(Q, K2)
    True

    The quotient graph of a directed graph under the "same strongly connected
    component" equivalence relation is the condensation of the graph (see
    :func:`condensation`). This example comes from the Wikipedia article
    *`Strongly connected component`_*.

    >>> G = nx.DiGraph()
    >>> edges = [
    ...     "ab",
    ...     "be",
    ...     "bf",
    ...     "bc",
    ...     "cg",
    ...     "cd",
    ...     "dc",
    ...     "dh",
    ...     "ea",
    ...     "ef",
    ...     "fg",
    ...     "gf",
    ...     "hd",
    ...     "hf",
    ... ]
    >>> G.add_edges_from(tuple(x) for x in edges)
    >>> components = list(nx.strongly_connected_components(G))
    >>> sorted(sorted(component) for component in components)
    [['a', 'b', 'e'], ['c', 'd', 'h'], ['f', 'g']]
    >>>
    >>> C = nx.condensation(G, components)
    >>> component_of = C.graph["mapping"]
    >>> same_component = lambda u, v: component_of[u] == component_of[v]
    >>> Q = nx.quotient_graph(G, same_component)
    >>> nx.is_isomorphic(C, Q)
    True

    Node identification can be represented as the quotient of a graph under the
    equivalence relation that places the two nodes in one block and each other
    node in its own singleton block.

    >>> K24 = nx.complete_bipartite_graph(2, 4)
    >>> K34 = nx.complete_bipartite_graph(3, 4)
    >>> C = nx.contracted_nodes(K34, 1, 2)
    >>> nodes = {1, 2}
    >>> is_contracted = lambda u, v: u in nodes and v in nodes
    >>> Q = nx.quotient_graph(K34, is_contracted)
    >>> nx.is_isomorphic(Q, C)
    True
    >>> nx.is_isomorphic(Q, K24)
    True

    The blockmodeling technique described in [1]_ can be implemented as a
    quotient graph.

    >>> G = nx.path_graph(6)
    >>> partition = [{0, 1}, {2, 3}, {4, 5}]
    >>> M = nx.quotient_graph(G, partition, relabel=True)
    >>> list(M.edges())
    [(0, 1), (1, 2)]

    Here is the sample example but using partition as a dict of block sets.

    >>> G = nx.path_graph(6)
    >>> partition = {0: {0, 1}, 2: {2, 3}, 4: {4, 5}}
    >>> M = nx.quotient_graph(G, partition, relabel=True)
    >>> list(M.edges())
    [(0, 1), (1, 2)]

    Partitions can be represented in various ways:

    0. a list/tuple/set of block lists/tuples/sets
    1. a dict with block labels as keys and blocks lists/tuples/sets as values
    2. a dict with block lists/tuples/sets as keys and block labels as values
    3. a function from nodes in the original iterable to block labels
    4. an equivalence relation function on the target iterable

    As `quotient_graph` is designed to accept partitions represented as (0), (1) or
    (4) only, the `equivalence_classes` function can be used to get the partitions
    in the right form, in order to call `quotient_graph`.

    .. _Strongly connected component: https://en.wikipedia.org/wiki/Strongly_connected_component

    References
    ----------
    .. [1] Patrick Doreian, Vladimir Batagelj, and Anuska Ferligoj.
           *Generalized Blockmodeling*.
           Cambridge University Press, 2004.
    """
    ...
@_dispatchable
def contracted_nodes(
    G: Graph[_Node], u, v, self_loops: bool = True, copy: bool = True, *, store_contraction_as: str | None = "contraction"
): ...

identified_nodes = contracted_nodes

@_dispatchable
def contracted_edge(
    G: Graph[_Node],
    edge: tuple[Incomplete],
    self_loops: bool = True,
    copy: bool = True,
    *,
    store_contraction_as: str | None = "contraction",
): ...
