from _typeshed import Incomplete
from collections.abc import Callable, Generator, Iterable

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def descendants(G: Graph[_Node], source) -> set[_Node]: ...
@_dispatchable
def ancestors(G: Graph[_Node], source) -> set[_Node]: ...
@_dispatchable
def is_directed_acyclic_graph(G: Graph[_Node]) -> bool:
    """
    Returns True if the graph `G` is a directed acyclic graph (DAG) or
    False if not.

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    bool
        True if `G` is a DAG, False otherwise

    Examples
    --------
    Undirected graph::

        >>> G = nx.Graph([(1, 2), (2, 3)])
        >>> nx.is_directed_acyclic_graph(G)
        False

    Directed graph with cycle::

        >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
        >>> nx.is_directed_acyclic_graph(G)
        False

    Directed acyclic graph::

        >>> G = nx.DiGraph([(1, 2), (2, 3)])
        >>> nx.is_directed_acyclic_graph(G)
        True

    See also
    --------
    topological_sort
    """
    ...
@_dispatchable
def topological_generations(G: DiGraph[_Node]) -> Generator[list[_Node], None, None]:
    """
    Stratifies a DAG into generations.

    A topological generation is node collection in which ancestors of a node in each
    generation are guaranteed to be in a previous generation, and any descendants of
    a node are guaranteed to be in a following generation. Nodes are guaranteed to
    be in the earliest possible generation that they can belong to.

    Parameters
    ----------
    G : NetworkX digraph
        A directed acyclic graph (DAG)

    Yields
    ------
    sets of nodes
        Yields sets of nodes representing each generation.

    Raises
    ------
    NetworkXError
        Generations are defined for directed graphs only. If the graph
        `G` is undirected, a :exc:`NetworkXError` is raised.

    NetworkXUnfeasible
        If `G` is not a directed acyclic graph (DAG) no topological generations
        exist and a :exc:`NetworkXUnfeasible` exception is raised.  This can also
        be raised if `G` is changed while the returned iterator is being processed

    RuntimeError
        If `G` is changed while the returned iterator is being processed.

    Examples
    --------
    >>> DG = nx.DiGraph([(2, 1), (3, 1)])
    >>> [sorted(generation) for generation in nx.topological_generations(DG)]
    [[2, 3], [1]]

    Notes
    -----
    The generation in which a node resides can also be determined by taking the
    max-path-distance from the node to the farthest leaf node. That value can
    be obtained with this function using `enumerate(topological_generations(G))`.

    See also
    --------
    topological_sort
    """
    ...
@_dispatchable
def topological_sort(G: DiGraph[_Node]) -> Generator[_Node, None, None]:
    """
    Returns a generator of nodes in topologically sorted order.

    A topological sort is a nonunique permutation of the nodes of a
    directed graph such that an edge from u to v implies that u
    appears before v in the topological sort order. This ordering is
    valid only if the graph has no directed cycles.

    Parameters
    ----------
    G : NetworkX digraph
        A directed acyclic graph (DAG)

    Yields
    ------
    nodes
        Yields the nodes in topological sorted order.

    Raises
    ------
    NetworkXError
        Topological sort is defined for directed graphs only. If the graph `G`
        is undirected, a :exc:`NetworkXError` is raised.

    NetworkXUnfeasible
        If `G` is not a directed acyclic graph (DAG) no topological sort exists
        and a :exc:`NetworkXUnfeasible` exception is raised.  This can also be
        raised if `G` is changed while the returned iterator is being processed

    RuntimeError
        If `G` is changed while the returned iterator is being processed.

    Examples
    --------
    To get the reverse order of the topological sort:

    >>> DG = nx.DiGraph([(1, 2), (2, 3)])
    >>> list(reversed(list(nx.topological_sort(DG))))
    [3, 2, 1]

    If your DiGraph naturally has the edges representing tasks/inputs
    and nodes representing people/processes that initiate tasks, then
    topological_sort is not quite what you need. You will have to change
    the tasks to nodes with dependence reflected by edges. The result is
    a kind of topological sort of the edges. This can be done
    with :func:`networkx.line_graph` as follows:

    >>> list(nx.topological_sort(nx.line_graph(DG)))
    [(1, 2), (2, 3)]

    Notes
    -----
    This algorithm is based on a description and proof in
    "Introduction to Algorithms: A Creative Approach" [1]_ .

    See also
    --------
    is_directed_acyclic_graph, lexicographical_topological_sort

    References
    ----------
    .. [1] Manber, U. (1989).
       *Introduction to Algorithms - A Creative Approach.* Addison-Wesley.
    """
    ...
@_dispatchable
def lexicographical_topological_sort(
    G: DiGraph[_Node], key: Callable[..., Incomplete] | None = None
) -> Generator[_Node, None, None]: ...
@_dispatchable
def all_topological_sorts(G: DiGraph[_Node]) -> Generator[list[_Node], None, None]:
    """
    Returns a generator of _all_ topological sorts of the directed graph G.

    A topological sort is a nonunique permutation of the nodes such that an
    edge from u to v implies that u appears before v in the topological sort
    order.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed graph

    Yields
    ------
    topological_sort_order : list
        a list of nodes in `G`, representing one of the topological sort orders

    Raises
    ------
    NetworkXNotImplemented
        If `G` is not directed
    NetworkXUnfeasible
        If `G` is not acyclic

    Examples
    --------
    To enumerate all topological sorts of directed graph:

    >>> DG = nx.DiGraph([(1, 2), (2, 3), (2, 4)])
    >>> list(nx.all_topological_sorts(DG))
    [[1, 2, 4, 3], [1, 2, 3, 4]]

    Notes
    -----
    Implements an iterative version of the algorithm given in [1].

    References
    ----------
    .. [1] Knuth, Donald E., Szwarcfiter, Jayme L. (1974).
       "A Structured Program to Generate All Topological Sorting Arrangements"
       Information Processing Letters, Volume 2, Issue 6, 1974, Pages 153-157,
       ISSN 0020-0190,
       https://doi.org/10.1016/0020-0190(74)90001-5.
       Elsevier (North-Holland), Amsterdam
    """
    ...
@_dispatchable
def is_aperiodic(G: DiGraph[_Node]) -> bool:
    """
    Returns True if `G` is aperiodic.

    A directed graph is aperiodic if there is no integer k > 1 that
    divides the length of every cycle in the graph.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed graph

    Returns
    -------
    bool
        True if the graph is aperiodic False otherwise

    Raises
    ------
    NetworkXError
        If `G` is not directed

    Examples
    --------
    A graph consisting of one cycle, the length of which is 2. Therefore ``k = 2``
    divides the length of every cycle in the graph and thus the graph
    is *not aperiodic*::

        >>> DG = nx.DiGraph([(1, 2), (2, 1)])
        >>> nx.is_aperiodic(DG)
        False

    A graph consisting of two cycles: one of length 2 and the other of length 3.
    The cycle lengths are coprime, so there is no single value of k where ``k > 1``
    that divides each cycle length and therefore the graph is *aperiodic*::

        >>> DG = nx.DiGraph([(1, 2), (2, 3), (3, 1), (1, 4), (4, 1)])
        >>> nx.is_aperiodic(DG)
        True

    A graph consisting of two cycles: one of length 2 and the other of length 4.
    The lengths of the cycles share a common factor ``k = 2``, and therefore
    the graph is *not aperiodic*::

        >>> DG = nx.DiGraph([(1, 2), (2, 1), (3, 4), (4, 5), (5, 6), (6, 3)])
        >>> nx.is_aperiodic(DG)
        False

    An acyclic graph, therefore the graph is *not aperiodic*::

        >>> DG = nx.DiGraph([(1, 2), (2, 3)])
        >>> nx.is_aperiodic(DG)
        False

    Notes
    -----
    This uses the method outlined in [1]_, which runs in $O(m)$ time
    given $m$ edges in `G`. Note that a graph is not aperiodic if it is
    acyclic as every integer trivial divides length 0 cycles.

    References
    ----------
    .. [1] Jarvis, J. P.; Shier, D. R. (1996),
       "Graph-theoretic analysis of finite Markov chains,"
       in Shier, D. R.; Wallenius, K. T., Applied Mathematical Modeling:
       A Multidisciplinary Approach, CRC Press.
    """
    ...
@_dispatchable
def transitive_closure(G: Graph[_Node], reflexive=False) -> Graph[_Node]: ...
@_dispatchable
def transitive_closure_dag(G: DiGraph[_Node], topo_order: Iterable[Incomplete] | None = None) -> DiGraph[_Node]: ...
@_dispatchable
def transitive_reduction(G: DiGraph[_Node]) -> DiGraph[_Node]:
    """
    Returns transitive reduction of a directed graph

    The transitive reduction of G = (V,E) is a graph G- = (V,E-) such that
    for all v,w in V there is an edge (v,w) in E- if and only if (v,w) is
    in E and there is no path from v to w in G with length greater than 1.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed acyclic graph (DAG)

    Returns
    -------
    NetworkX DiGraph
        The transitive reduction of `G`

    Raises
    ------
    NetworkXError
        If `G` is not a directed acyclic graph (DAG) transitive reduction is
        not uniquely defined and a :exc:`NetworkXError` exception is raised.

    Examples
    --------
    To perform transitive reduction on a DiGraph:

    >>> DG = nx.DiGraph([(1, 2), (2, 3), (1, 3)])
    >>> TR = nx.transitive_reduction(DG)
    >>> list(TR.edges)
    [(1, 2), (2, 3)]

    To avoid unnecessary data copies, this implementation does not return a
    DiGraph with node/edge data.
    To perform transitive reduction on a DiGraph and transfer node/edge data:

    >>> DG = nx.DiGraph()
    >>> DG.add_edges_from([(1, 2), (2, 3), (1, 3)], color="red")
    >>> TR = nx.transitive_reduction(DG)
    >>> TR.add_nodes_from(DG.nodes(data=True))
    >>> TR.add_edges_from((u, v, DG.edges[u, v]) for u, v in TR.edges)
    >>> list(TR.edges(data=True))
    [(1, 2, {'color': 'red'}), (2, 3, {'color': 'red'})]

    References
    ----------
    https://en.wikipedia.org/wiki/Transitive_reduction
    """
    ...
@_dispatchable
def antichains(G: DiGraph[_Node], topo_order: Iterable[Incomplete] | None = None) -> Generator[list[_Node], None, None]: ...
@_dispatchable
def dag_longest_path(
    G: DiGraph[_Node],
    weight: str | None = "weight",
    default_weight: int | None = 1,
    topo_order: Iterable[Incomplete] | None = None,
) -> list[_Node]: ...
@_dispatchable
def dag_longest_path_length(G: DiGraph[_Node], weight: str | None = "weight", default_weight: int | None = 1) -> int: ...
@_dispatchable
def dag_to_branching(G: Graph[_Node]) -> Graph[_Node]:
    """
    Returns a branching representing all (overlapping) paths from
    root nodes to leaf nodes in the given directed acyclic graph.

    As described in :mod:`networkx.algorithms.tree.recognition`, a
    *branching* is a directed forest in which each node has at most one
    parent. In other words, a branching is a disjoint union of
    *arborescences*. For this function, each node of in-degree zero in
    `G` becomes a root of one of the arborescences, and there will be
    one leaf node for each distinct path from that root to a leaf node
    in `G`.

    Each node `v` in `G` with *k* parents becomes *k* distinct nodes in
    the returned branching, one for each parent, and the sub-DAG rooted
    at `v` is duplicated for each copy. The algorithm then recurses on
    the children of each copy of `v`.

    Parameters
    ----------
    G : NetworkX graph
        A directed acyclic graph.

    Returns
    -------
    DiGraph
        The branching in which there is a bijection between root-to-leaf
        paths in `G` (in which multiple paths may share the same leaf)
        and root-to-leaf paths in the branching (in which there is a
        unique path from a root to a leaf).

        Each node has an attribute 'source' whose value is the original
        node to which this node corresponds. No other graph, node, or
        edge attributes are copied into this new graph.

    Raises
    ------
    NetworkXNotImplemented
        If `G` is not directed, or if `G` is a multigraph.

    HasACycle
        If `G` is not acyclic.

    Examples
    --------
    To examine which nodes in the returned branching were produced by
    which original node in the directed acyclic graph, we can collect
    the mapping from source node to new nodes into a dictionary. For
    example, consider the directed diamond graph::

        >>> from collections import defaultdict
        >>> from operator import itemgetter
        >>>
        >>> G = nx.DiGraph(nx.utils.pairwise("abd"))
        >>> G.add_edges_from(nx.utils.pairwise("acd"))
        >>> B = nx.dag_to_branching(G)
        >>>
        >>> sources = defaultdict(set)
        >>> for v, source in B.nodes(data="source"):
        ...     sources[source].add(v)
        >>> len(sources["a"])
        1
        >>> len(sources["d"])
        2

    To copy node attributes from the original graph to the new graph,
    you can use a dictionary like the one constructed in the above
    example::

        >>> for source, nodes in sources.items():
        ...     for v in nodes:
        ...         B.nodes[v].update(G.nodes[source])

    Notes
    -----
    This function is not idempotent in the sense that the node labels in
    the returned branching may be uniquely generated each time the
    function is invoked. In fact, the node labels may not be integers;
    in order to relabel the nodes to be more readable, you can use the
    :func:`networkx.convert_node_labels_to_integers` function.

    The current implementation of this function uses
    :func:`networkx.prefix_tree`, so it is subject to the limitations of
    that function.
    """
    ...
