"""
ISMAGS Algorithm
================

Provides a Python implementation of the ISMAGS algorithm. [1]_

It is capable of finding (subgraph) isomorphisms between two graphs, taking the
symmetry of the subgraph into account. In most cases the VF2 algorithm is
faster (at least on small graphs) than this implementation, but in some cases
there is an exponential number of isomorphisms that are symmetrically
equivalent. In that case, the ISMAGS algorithm will provide only one solution
per symmetry group.

>>> petersen = nx.petersen_graph()
>>> ismags = nx.isomorphism.ISMAGS(petersen, petersen)
>>> isomorphisms = list(ismags.isomorphisms_iter(symmetry=False))
>>> len(isomorphisms)
120
>>> isomorphisms = list(ismags.isomorphisms_iter(symmetry=True))
>>> answer = [{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}]
>>> answer == isomorphisms
True

In addition, this implementation also provides an interface to find the
largest common induced subgraph [2]_ between any two graphs, again taking
symmetry into account. Given `graph` and `subgraph` the algorithm will remove
nodes from the `subgraph` until `subgraph` is isomorphic to a subgraph of
`graph`. Since only the symmetry of `subgraph` is taken into account it is
worth thinking about how you provide your graphs:

>>> graph1 = nx.path_graph(4)
>>> graph2 = nx.star_graph(3)
>>> ismags = nx.isomorphism.ISMAGS(graph1, graph2)
>>> ismags.is_isomorphic()
False
>>> largest_common_subgraph = list(ismags.largest_common_subgraph())
>>> answer = [{1: 0, 0: 1, 2: 2}, {2: 0, 1: 1, 3: 2}]
>>> answer == largest_common_subgraph
True
>>> ismags2 = nx.isomorphism.ISMAGS(graph2, graph1)
>>> largest_common_subgraph = list(ismags2.largest_common_subgraph())
>>> answer = [
...     {1: 0, 0: 1, 2: 2},
...     {1: 0, 0: 1, 3: 2},
...     {2: 0, 0: 1, 1: 2},
...     {2: 0, 0: 1, 3: 2},
...     {3: 0, 0: 1, 1: 2},
...     {3: 0, 0: 1, 2: 2},
... ]
>>> answer == largest_common_subgraph
True

However, when not taking symmetry into account, it doesn't matter:

>>> largest_common_subgraph = list(ismags.largest_common_subgraph(symmetry=False))
>>> answer = [
...     {1: 0, 0: 1, 2: 2},
...     {1: 0, 2: 1, 0: 2},
...     {2: 0, 1: 1, 3: 2},
...     {2: 0, 3: 1, 1: 2},
...     {1: 0, 0: 1, 2: 3},
...     {1: 0, 2: 1, 0: 3},
...     {2: 0, 1: 1, 3: 3},
...     {2: 0, 3: 1, 1: 3},
...     {1: 0, 0: 2, 2: 3},
...     {1: 0, 2: 2, 0: 3},
...     {2: 0, 1: 2, 3: 3},
...     {2: 0, 3: 2, 1: 3},
... ]
>>> answer == largest_common_subgraph
True
>>> largest_common_subgraph = list(ismags2.largest_common_subgraph(symmetry=False))
>>> answer = [
...     {1: 0, 0: 1, 2: 2},
...     {1: 0, 0: 1, 3: 2},
...     {2: 0, 0: 1, 1: 2},
...     {2: 0, 0: 1, 3: 2},
...     {3: 0, 0: 1, 1: 2},
...     {3: 0, 0: 1, 2: 2},
...     {1: 1, 0: 2, 2: 3},
...     {1: 1, 0: 2, 3: 3},
...     {2: 1, 0: 2, 1: 3},
...     {2: 1, 0: 2, 3: 3},
...     {3: 1, 0: 2, 1: 3},
...     {3: 1, 0: 2, 2: 3},
... ]
>>> answer == largest_common_subgraph
True

Notes
-----
- The current implementation works for undirected graphs only. The algorithm
  in general should work for directed graphs as well though.
- Node keys for both provided graphs need to be fully orderable as well as
  hashable.
- Node and edge equality is assumed to be transitive: if A is equal to B, and
  B is equal to C, then A is equal to C.

References
----------
.. [1] M. Houbraken, S. Demeyer, T. Michoel, P. Audenaert, D. Colle,
   M. Pickavet, "The Index-Based Subgraph Matching Algorithm with General
   Symmetries (ISMAGS): Exploiting Symmetry for Faster Subgraph
   Enumeration", PLoS One 9(5): e97896, 2014.
   https://doi.org/10.1371/journal.pone.0097896
.. [2] https://en.wikipedia.org/wiki/Maximum_common_induced_subgraph
"""

from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ["ISMAGS"]

class ISMAGS:
    """
    Implements the ISMAGS subgraph matching algorithm. [1]_ ISMAGS stands for
    "Index-based Subgraph Matching Algorithm with General Symmetries". As the
    name implies, it is symmetry aware and will only generate non-symmetric
    isomorphisms.

    Notes
    -----
    The implementation imposes additional conditions compared to the VF2
    algorithm on the graphs provided and the comparison functions
    (:attr:`node_equality` and :attr:`edge_equality`):

     - Node keys in both graphs must be orderable as well as hashable.
     - Equality must be transitive: if A is equal to B, and B is equal to C,
       then A must be equal to C.

    Attributes
    ----------
    graph: networkx.Graph
    subgraph: networkx.Graph
    node_equality: collections.abc.Callable
        The function called to see if two nodes should be considered equal.
        It's signature looks like this:
        ``f(graph1: networkx.Graph, node1, graph2: networkx.Graph, node2) -> bool``.
        `node1` is a node in `graph1`, and `node2` a node in `graph2`.
        Constructed from the argument `node_match`.
    edge_equality: collections.abc.Callable
        The function called to see if two edges should be considered equal.
        It's signature looks like this:
        ``f(graph1: networkx.Graph, edge1, graph2: networkx.Graph, edge2) -> bool``.
        `edge1` is an edge in `graph1`, and `edge2` an edge in `graph2`.
        Constructed from the argument `edge_match`.

    References
    ----------
    .. [1] M. Houbraken, S. Demeyer, T. Michoel, P. Audenaert, D. Colle,
       M. Pickavet, "The Index-Based Subgraph Matching Algorithm with General
       Symmetries (ISMAGS): Exploiting Symmetry for Faster Subgraph
       Enumeration", PLoS One 9(5): e97896, 2014.
       https://doi.org/10.1371/journal.pone.0097896
    """
    graph: Incomplete
    subgraph: Incomplete
    node_equality: Incomplete
    edge_equality: Incomplete

    def __init__(self, graph, subgraph, node_match=None, edge_match=None, cache=None) -> None:
        """
        Parameters
        ----------
        graph: networkx.Graph
        subgraph: networkx.Graph
        node_match: collections.abc.Callable or None
            Function used to determine whether two nodes are equivalent. Its
            signature should look like ``f(n1: dict, n2: dict) -> bool``, with
            `n1` and `n2` node property dicts. See also
            :func:`~networkx.algorithms.isomorphism.categorical_node_match` and
            friends.
            If `None`, all nodes are considered equal.
        edge_match: collections.abc.Callable or None
            Function used to determine whether two edges are equivalent. Its
            signature should look like ``f(e1: dict, e2: dict) -> bool``, with
            `e1` and `e2` edge property dicts. See also
            :func:`~networkx.algorithms.isomorphism.categorical_edge_match` and
            friends.
            If `None`, all edges are considered equal.
        cache: collections.abc.Mapping
            A cache used for caching graph symmetries.
        """
        ...
    def find_isomorphisms(self, symmetry: bool = True) -> Generator[Incomplete, Incomplete, Incomplete]:
        """
        Find all subgraph isomorphisms between subgraph and graph

        Finds isomorphisms where :attr:`subgraph` <= :attr:`graph`.

        Parameters
        ----------
        symmetry: bool
            Whether symmetry should be taken into account. If False, found
            isomorphisms may be symmetrically equivalent.

        Yields
        ------
        dict
            The found isomorphism mappings of {graph_node: subgraph_node}.
        """
        ...
    def largest_common_subgraph(self, symmetry: bool = True) -> Generator[Incomplete, Incomplete, None]:
        """
        Find the largest common induced subgraphs between :attr:`subgraph` and
        :attr:`graph`.

        Parameters
        ----------
        symmetry: bool
            Whether symmetry should be taken into account. If False, found
            largest common subgraphs may be symmetrically equivalent.

        Yields
        ------
        dict
            The found isomorphism mappings of {graph_node: subgraph_node}.
        """
        ...
    def analyze_symmetry(self, graph, node_partitions, edge_colors):
        """
        Find a minimal set of permutations and corresponding co-sets that
        describe the symmetry of `graph`, given the node and edge equalities
        given by `node_partitions` and `edge_colors`, respectively.

        Parameters
        ----------
        graph : networkx.Graph
            The graph whose symmetry should be analyzed.
        node_partitions : list of sets
            A list of sets containing node keys. Node keys in the same set
            are considered equivalent. Every node key in `graph` should be in
            exactly one of the sets. If all nodes are equivalent, this should
            be ``[set(graph.nodes)]``.
        edge_colors : dict mapping edges to their colors
            A dict mapping every edge in `graph` to its corresponding color.
            Edges with the same color are considered equivalent. If all edges
            are equivalent, this should be ``{e: 0 for e in graph.edges}``.


        Returns
        -------
        set[frozenset]
            The found permutations. This is a set of frozensets of pairs of node
            keys which can be exchanged without changing :attr:`subgraph`.
        dict[collections.abc.Hashable, set[collections.abc.Hashable]]
            The found co-sets. The co-sets is a dictionary of
            ``{node key: set of node keys}``.
            Every key-value pair describes which ``values`` can be interchanged
            without changing nodes less than ``key``.
        """
        ...
    def is_isomorphic(self, symmetry: bool = False) -> bool:
        """
        Returns True if :attr:`graph` is isomorphic to :attr:`subgraph` and
        False otherwise.

        Returns
        -------
        bool
        """
        ...
    def subgraph_is_isomorphic(self, symmetry: bool = False) -> bool:
        """
        Returns True if a subgraph of :attr:`graph` is isomorphic to
        :attr:`subgraph` and False otherwise.

        Returns
        -------
        bool
        """
        ...
    def isomorphisms_iter(self, symmetry: bool = True) -> Generator[Incomplete, Incomplete, None]:
        """
        Does the same as :meth:`find_isomorphisms` if :attr:`graph` and
        :attr:`subgraph` have the same number of nodes.
        """
        ...
    def subgraph_isomorphisms_iter(self, symmetry: bool = True):
        """Alternative name for :meth:`find_isomorphisms`."""
        ...
