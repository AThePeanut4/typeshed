"""
Algorithms for directed acyclic graphs (DAGs).

Note that most of these functions are only guaranteed to work for DAGs.
In general, these functions do not check for acyclic-ness, so it is up
to the user to check for that.
"""

from _typeshed import Incomplete
from collections.abc import Callable, Generator, Iterable

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "descendants",
    "ancestors",
    "topological_sort",
    "lexicographical_topological_sort",
    "all_topological_sorts",
    "topological_generations",
    "is_directed_acyclic_graph",
    "is_aperiodic",
    "transitive_closure",
    "transitive_closure_dag",
    "transitive_reduction",
    "antichains",
    "dag_longest_path",
    "dag_longest_path_length",
    "dag_to_branching",
    "compute_v_structures",
]

@_dispatchable
def descendants(G: Graph[_Node], source) -> set[_Node]:
    """
    Returns all nodes reachable from `source` in `G`.

    Parameters
    ----------
    G : NetworkX Graph
    source : node in `G`

    Returns
    -------
    set()
        The descendants of `source` in `G`

    Raises
    ------
    NetworkXError
        If node `source` is not in `G`.

    Examples
    --------
    >>> DG = nx.path_graph(5, create_using=nx.DiGraph)
    >>> sorted(nx.descendants(DG, 2))
    [3, 4]

    The `source` node is not a descendant of itself, but can be included manually:

    >>> sorted(nx.descendants(DG, 2) | {2})
    [2, 3, 4]

    See also
    --------
    ancestors
    """
    ...
@_dispatchable
def ancestors(G: Graph[_Node], source) -> set[_Node]:
    """
    Returns all nodes having a path to `source` in `G`.

    Parameters
    ----------
    G : NetworkX Graph
    source : node in `G`

    Returns
    -------
    set()
        The ancestors of `source` in `G`

    Raises
    ------
    NetworkXError
        If node `source` is not in `G`.

    Examples
    --------
    >>> DG = nx.path_graph(5, create_using=nx.DiGraph)
    >>> sorted(nx.ancestors(DG, 2))
    [0, 1]

    The `source` node is not an ancestor of itself, but can be included manually:

    >>> sorted(nx.ancestors(DG, 2) | {2})
    [0, 1, 2]

    See also
    --------
    descendants
    """
    ...
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
) -> Generator[_Node, None, None]:
    """
    Generate the nodes in the unique lexicographical topological sort order.

    Generates a unique ordering of nodes by first sorting topologically (for which there are often
    multiple valid orderings) and then additionally by sorting lexicographically.

    A topological sort arranges the nodes of a directed graph so that the
    upstream node of each directed edge precedes the downstream node.
    It is always possible to find a solution for directed graphs that have no cycles.
    There may be more than one valid solution.

    Lexicographical sorting is just sorting alphabetically. It is used here to break ties in the
    topological sort and to determine a single, unique ordering.  This can be useful in comparing
    sort results.

    The lexicographical order can be customized by providing a function to the `key=` parameter.
    The definition of the key function is the same as used in python's built-in `sort()`.
    The function takes a single argument and returns a key to use for sorting purposes.

    Lexicographical sorting can fail if the node names are un-sortable. See the example below.
    The solution is to provide a function to the `key=` argument that returns sortable keys.


    Parameters
    ----------
    G : NetworkX digraph
        A directed acyclic graph (DAG)

    key : function, optional
        A function of one argument that converts a node name to a comparison key.
        It defines and resolves ambiguities in the sort order.  Defaults to the identity function.

    Yields
    ------
    nodes
        Yields the nodes of G in lexicographical topological sort order.

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

    TypeError
        Results from un-sortable node names.
        Consider using `key=` parameter to resolve ambiguities in the sort order.

    Examples
    --------
    >>> DG = nx.DiGraph([(2, 1), (2, 5), (1, 3), (1, 4), (5, 4)])
    >>> list(nx.lexicographical_topological_sort(DG))
    [2, 1, 3, 5, 4]
    >>> list(nx.lexicographical_topological_sort(DG, key=lambda x: -x))
    [2, 5, 1, 4, 3]

    The sort will fail for any graph with integer and string nodes. Comparison of integer to strings
    is not defined in python.  Is 3 greater or less than 'red'?

    >>> DG = nx.DiGraph([(1, "red"), (3, "red"), (1, "green"), (2, "blue")])
    >>> list(nx.lexicographical_topological_sort(DG))
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    ...

    Incomparable nodes can be resolved using a `key` function. This example function
    allows comparison of integers and strings by returning a tuple where the first
    element is True for `str`, False otherwise. The second element is the node name.
    This groups the strings and integers separately so they can be compared only among themselves.

    >>> key = lambda node: (isinstance(node, str), node)
    >>> list(nx.lexicographical_topological_sort(DG, key=key))
    [1, 2, 3, 'blue', 'green', 'red']

    Notes
    -----
    This algorithm is based on a description and proof in
    "Introduction to Algorithms: A Creative Approach" [1]_ .

    See also
    --------
    topological_sort

    References
    ----------
    .. [1] Manber, U. (1989).
       *Introduction to Algorithms - A Creative Approach.* Addison-Wesley.
    """
    ...
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
def transitive_closure(G: Graph[_Node], reflexive=False) -> Graph[_Node]:
    """
    Returns transitive closure of a graph

    The transitive closure of G = (V,E) is a graph G+ = (V,E+) such that
    for all v, w in V there is an edge (v, w) in E+ if and only if there
    is a path from v to w in G.

    Handling of paths from v to v has some flexibility within this definition.
    A reflexive transitive closure creates a self-loop for the path
    from v to v of length 0. The usual transitive closure creates a
    self-loop only if a cycle exists (a path from v to v with length > 0).
    We also allow an option for no self-loops.

    Parameters
    ----------
    G : NetworkX Graph
        A directed/undirected graph/multigraph.
    reflexive : Bool or None, optional (default: False)
        Determines when cycles create self-loops in the Transitive Closure.
        If True, trivial cycles (length 0) create self-loops. The result
        is a reflexive transitive closure of G.
        If False (the default) non-trivial cycles create self-loops.
        If None, self-loops are not created.

    Returns
    -------
    NetworkX graph
        The transitive closure of `G`

    Raises
    ------
    NetworkXError
        If `reflexive` not in `{None, True, False}`

    Examples
    --------
    The treatment of trivial (i.e. length 0) cycles is controlled by the
    `reflexive` parameter.

    Trivial (i.e. length 0) cycles do not create self-loops when
    ``reflexive=False`` (the default)::

        >>> DG = nx.DiGraph([(1, 2), (2, 3)])
        >>> TC = nx.transitive_closure(DG, reflexive=False)
        >>> TC.edges()
        OutEdgeView([(1, 2), (1, 3), (2, 3)])

    However, nontrivial (i.e. length greater than 0) cycles create self-loops
    when ``reflexive=False`` (the default)::

        >>> DG = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
        >>> TC = nx.transitive_closure(DG, reflexive=False)
        >>> TC.edges()
        OutEdgeView([(1, 2), (1, 3), (1, 1), (2, 3), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3)])

    Trivial cycles (length 0) create self-loops when ``reflexive=True``::

        >>> DG = nx.DiGraph([(1, 2), (2, 3)])
        >>> TC = nx.transitive_closure(DG, reflexive=True)
        >>> TC.edges()
        OutEdgeView([(1, 2), (1, 1), (1, 3), (2, 3), (2, 2), (3, 3)])

    And the third option is not to create self-loops at all when ``reflexive=None``::

        >>> DG = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
        >>> TC = nx.transitive_closure(DG, reflexive=None)
        >>> TC.edges()
        OutEdgeView([(1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (3, 2)])

    References
    ----------
    .. [1] https://www.ics.uci.edu/~eppstein/PADS/PartialOrder.py
    """
    ...
@_dispatchable
def transitive_closure_dag(G: DiGraph[_Node], topo_order: Iterable[Incomplete] | None = None) -> DiGraph[_Node]:
    """
    Returns the transitive closure of a directed acyclic graph.

    This function is faster than the function `transitive_closure`, but fails
    if the graph has a cycle.

    The transitive closure of G = (V,E) is a graph G+ = (V,E+) such that
    for all v, w in V there is an edge (v, w) in E+ if and only if there
    is a non-null path from v to w in G.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed acyclic graph (DAG)

    topo_order: list or tuple, optional
        A topological order for G (if None, the function will compute one)

    Returns
    -------
    NetworkX DiGraph
        The transitive closure of `G`

    Raises
    ------
    NetworkXNotImplemented
        If `G` is not directed
    NetworkXUnfeasible
        If `G` has a cycle

    Examples
    --------
    >>> DG = nx.DiGraph([(1, 2), (2, 3)])
    >>> TC = nx.transitive_closure_dag(DG)
    >>> TC.edges()
    OutEdgeView([(1, 2), (1, 3), (2, 3)])

    Notes
    -----
    This algorithm is probably simple enough to be well-known but I didn't find
    a mention in the literature.
    """
    ...
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
def antichains(G: DiGraph[_Node], topo_order: Iterable[Incomplete] | None = None) -> Generator[list[_Node], None, None]:
    """
    Generates antichains from a directed acyclic graph (DAG).

    An antichain is a subset of a partially ordered set such that any
    two elements in the subset are incomparable.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed acyclic graph (DAG)

    topo_order: list or tuple, optional
        A topological order for G (if None, the function will compute one)

    Yields
    ------
    antichain : list
        a list of nodes in `G` representing an antichain

    Raises
    ------
    NetworkXNotImplemented
        If `G` is not directed

    NetworkXUnfeasible
        If `G` contains a cycle

    Examples
    --------
    >>> DG = nx.DiGraph([(1, 2), (1, 3)])
    >>> list(nx.antichains(DG))
    [[], [3], [2], [2, 3], [1]]

    Notes
    -----
    This function was originally developed by Peter Jipsen and Franco Saliola
    for the SAGE project. It's included in NetworkX with permission from the
    authors. Original SAGE code at:

    https://github.com/sagemath/sage/blob/master/src/sage/combinat/posets/hasse_diagram.py

    References
    ----------
    .. [1] Free Lattices, by R. Freese, J. Jezek and J. B. Nation,
       AMS, Vol 42, 1995, p. 226.
    """
    ...
@_dispatchable
def dag_longest_path(
    G: DiGraph[_Node],
    weight: str | None = "weight",
    default_weight: int | None = 1,
    topo_order: Iterable[Incomplete] | None = None,
) -> list[_Node]:
    """
    Returns the longest path in a directed acyclic graph (DAG).

    If `G` has edges with `weight` attribute the edge data are used as
    weight values.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed acyclic graph (DAG)

    weight : str, optional
        Edge data key to use for weight

    default_weight : int, optional
        The weight of edges that do not have a weight attribute

    topo_order: list or tuple, optional
        A topological order for `G` (if None, the function will compute one)

    Returns
    -------
    list
        Longest path

    Raises
    ------
    NetworkXNotImplemented
        If `G` is not directed

    Examples
    --------
    >>> DG = nx.DiGraph(
    ...     [(0, 1, {"cost": 1}), (1, 2, {"cost": 1}), (0, 2, {"cost": 42})]
    ... )
    >>> list(nx.all_simple_paths(DG, 0, 2))
    [[0, 1, 2], [0, 2]]
    >>> nx.dag_longest_path(DG)
    [0, 1, 2]
    >>> nx.dag_longest_path(DG, weight="cost")
    [0, 2]

    In the case where multiple valid topological orderings exist, `topo_order`
    can be used to specify a specific ordering:

    >>> DG = nx.DiGraph([(0, 1), (0, 2)])
    >>> sorted(nx.all_topological_sorts(DG))  # Valid topological orderings
    [[0, 1, 2], [0, 2, 1]]
    >>> nx.dag_longest_path(DG, topo_order=[0, 1, 2])
    [0, 1]
    >>> nx.dag_longest_path(DG, topo_order=[0, 2, 1])
    [0, 2]

    See also
    --------
    dag_longest_path_length
    """
    ...
@_dispatchable
def dag_longest_path_length(G: DiGraph[_Node], weight: str | None = "weight", default_weight: int | None = 1) -> int:
    """
    Returns the longest path length in a DAG

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed acyclic graph (DAG)

    weight : string, optional
        Edge data key to use for weight

    default_weight : int, optional
        The weight of edges that do not have a weight attribute

    Returns
    -------
    int
        Longest path length

    Raises
    ------
    NetworkXNotImplemented
        If `G` is not directed

    Examples
    --------
    >>> DG = nx.DiGraph(
    ...     [(0, 1, {"cost": 1}), (1, 2, {"cost": 1}), (0, 2, {"cost": 42})]
    ... )
    >>> list(nx.all_simple_paths(DG, 0, 2))
    [[0, 1, 2], [0, 2]]
    >>> nx.dag_longest_path_length(DG)
    2
    >>> nx.dag_longest_path_length(DG, weight="cost")
    42

    See also
    --------
    dag_longest_path
    """
    ...
@_dispatchable
def dag_to_branching(G: Graph[_Node]) -> Graph[_Node]: ...
@_dispatchable
def compute_v_structures(G) -> Generator[tuple[Incomplete, Incomplete, Incomplete]]: ...
