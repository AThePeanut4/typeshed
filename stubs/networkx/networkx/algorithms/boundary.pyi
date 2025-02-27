"""
Routines to find the boundary of a set of nodes.

An edge boundary is a set of edges, each of which has exactly one
endpoint in a given set of nodes (or, in the case of directed graphs,
the set of edges whose source node is in the set).

A node boundary of a set *S* of nodes is the set of (out-)neighbors of
nodes in *S* that are outside *S*.
"""

from _typeshed import Incomplete
from collections.abc import Generator, Iterable
from typing import TypeVar, overload

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

_U = TypeVar("_U")

@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node, dict[str, Incomplete]], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node, dict[str, Incomplete]], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: _U | None = None,
) -> Generator[tuple[_Node, _Node, dict[str, _U]], None, None]:
    """
    Returns the edge boundary of `nbunch1`.

    The *edge boundary* of a set *S* with respect to a set *T* is the
    set of edges (*u*, *v*) such that *u* is in *S* and *v* is in *T*.
    If *T* is not specified, it is assumed to be the set of all nodes
    not in *S*.

    Parameters
    ----------
    G : NetworkX graph

    nbunch1 : iterable
        Iterable of nodes in the graph representing the set of nodes
        whose edge boundary will be returned. (This is the set *S* from
        the definition above.)

    nbunch2 : iterable
        Iterable of nodes representing the target (or "exterior") set of
        nodes. (This is the set *T* from the definition above.) If not
        specified, this is assumed to be the set of all nodes in `G`
        not in `nbunch1`.

    keys : bool
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    data : bool or object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    default : object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    Returns
    -------
    iterator
        An iterator over the edges in the boundary of `nbunch1` with
        respect to `nbunch2`. If `keys`, `data`, or `default`
        are specified and `G` is a multigraph, then edges are returned
        with keys and/or data, as in :meth:`MultiGraph.edges`.

    Examples
    --------
    >>> G = nx.wheel_graph(6)

    When nbunch2=None:

    >>> list(nx.edge_boundary(G, (1, 3)))
    [(1, 0), (1, 2), (1, 5), (3, 0), (3, 2), (3, 4)]

    When nbunch2 is given:

    >>> list(nx.edge_boundary(G, (1, 3), (2, 0)))
    [(1, 0), (1, 2), (3, 0), (3, 2)]

    Notes
    -----
    Any element of `nbunch` that is not in the graph `G` will be
    ignored.

    `nbunch1` and `nbunch2` are usually meant to be disjoint, but in
    the interest of speed and generality, that is not required here.
    """
    ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: _U | None = None,
) -> Generator[tuple[_Node, _Node, dict[str, _U]], None, None]:
    """
    Returns the edge boundary of `nbunch1`.

    The *edge boundary* of a set *S* with respect to a set *T* is the
    set of edges (*u*, *v*) such that *u* is in *S* and *v* is in *T*.
    If *T* is not specified, it is assumed to be the set of all nodes
    not in *S*.

    Parameters
    ----------
    G : NetworkX graph

    nbunch1 : iterable
        Iterable of nodes in the graph representing the set of nodes
        whose edge boundary will be returned. (This is the set *S* from
        the definition above.)

    nbunch2 : iterable
        Iterable of nodes representing the target (or "exterior") set of
        nodes. (This is the set *T* from the definition above.) If not
        specified, this is assumed to be the set of all nodes in `G`
        not in `nbunch1`.

    keys : bool
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    data : bool or object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    default : object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    Returns
    -------
    iterator
        An iterator over the edges in the boundary of `nbunch1` with
        respect to `nbunch2`. If `keys`, `data`, or `default`
        are specified and `G` is a multigraph, then edges are returned
        with keys and/or data, as in :meth:`MultiGraph.edges`.

    Examples
    --------
    >>> G = nx.wheel_graph(6)

    When nbunch2=None:

    >>> list(nx.edge_boundary(G, (1, 3)))
    [(1, 0), (1, 2), (1, 5), (3, 0), (3, 2), (3, 4)]

    When nbunch2 is given:

    >>> list(nx.edge_boundary(G, (1, 3), (2, 0)))
    [(1, 0), (1, 2), (3, 0), (3, 2)]

    Notes
    -----
    Any element of `nbunch` that is not in the graph `G` will be
    ignored.

    `nbunch1` and `nbunch2` are usually meant to be disjoint, but in
    the interest of speed and generality, that is not required here.
    """
    ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node, int], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node, int], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node, int, dict[str, Incomplete]], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: Incomplete | None = None,
) -> Generator[tuple[_Node, _Node, int, dict[str, Incomplete]], None, None]: ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: _U | None = None,
) -> Generator[tuple[_Node, _Node, int, dict[str, _U]], None, None]:
    """
    Returns the edge boundary of `nbunch1`.

    The *edge boundary* of a set *S* with respect to a set *T* is the
    set of edges (*u*, *v*) such that *u* is in *S* and *v* is in *T*.
    If *T* is not specified, it is assumed to be the set of all nodes
    not in *S*.

    Parameters
    ----------
    G : NetworkX graph

    nbunch1 : iterable
        Iterable of nodes in the graph representing the set of nodes
        whose edge boundary will be returned. (This is the set *S* from
        the definition above.)

    nbunch2 : iterable
        Iterable of nodes representing the target (or "exterior") set of
        nodes. (This is the set *T* from the definition above.) If not
        specified, this is assumed to be the set of all nodes in `G`
        not in `nbunch1`.

    keys : bool
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    data : bool or object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    default : object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    Returns
    -------
    iterator
        An iterator over the edges in the boundary of `nbunch1` with
        respect to `nbunch2`. If `keys`, `data`, or `default`
        are specified and `G` is a multigraph, then edges are returned
        with keys and/or data, as in :meth:`MultiGraph.edges`.

    Examples
    --------
    >>> G = nx.wheel_graph(6)

    When nbunch2=None:

    >>> list(nx.edge_boundary(G, (1, 3)))
    [(1, 0), (1, 2), (1, 5), (3, 0), (3, 2), (3, 4)]

    When nbunch2 is given:

    >>> list(nx.edge_boundary(G, (1, 3), (2, 0)))
    [(1, 0), (1, 2), (3, 0), (3, 2)]

    Notes
    -----
    Any element of `nbunch` that is not in the graph `G` will be
    ignored.

    `nbunch1` and `nbunch2` are usually meant to be disjoint, but in
    the interest of speed and generality, that is not required here.
    """
    ...
@overload
def edge_boundary(
    G: Graph[_Node],
    nbunch1: Iterable[Incomplete],
    nbunch2: Iterable[Incomplete] | None = None,
    data=False,
    keys: bool = False,
    default: _U | None = None,
) -> Generator[tuple[_Node, _Node, int, dict[str, _U]], None, None]:
    """
    Returns the edge boundary of `nbunch1`.

    The *edge boundary* of a set *S* with respect to a set *T* is the
    set of edges (*u*, *v*) such that *u* is in *S* and *v* is in *T*.
    If *T* is not specified, it is assumed to be the set of all nodes
    not in *S*.

    Parameters
    ----------
    G : NetworkX graph

    nbunch1 : iterable
        Iterable of nodes in the graph representing the set of nodes
        whose edge boundary will be returned. (This is the set *S* from
        the definition above.)

    nbunch2 : iterable
        Iterable of nodes representing the target (or "exterior") set of
        nodes. (This is the set *T* from the definition above.) If not
        specified, this is assumed to be the set of all nodes in `G`
        not in `nbunch1`.

    keys : bool
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    data : bool or object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    default : object
        This parameter has the same meaning as in
        :meth:`MultiGraph.edges`.

    Returns
    -------
    iterator
        An iterator over the edges in the boundary of `nbunch1` with
        respect to `nbunch2`. If `keys`, `data`, or `default`
        are specified and `G` is a multigraph, then edges are returned
        with keys and/or data, as in :meth:`MultiGraph.edges`.

    Examples
    --------
    >>> G = nx.wheel_graph(6)

    When nbunch2=None:

    >>> list(nx.edge_boundary(G, (1, 3)))
    [(1, 0), (1, 2), (1, 5), (3, 0), (3, 2), (3, 4)]

    When nbunch2 is given:

    >>> list(nx.edge_boundary(G, (1, 3), (2, 0)))
    [(1, 0), (1, 2), (3, 0), (3, 2)]

    Notes
    -----
    Any element of `nbunch` that is not in the graph `G` will be
    ignored.

    `nbunch1` and `nbunch2` are usually meant to be disjoint, but in
    the interest of speed and generality, that is not required here.
    """
    ...
@_dispatchable
def node_boundary(G: Graph[_Node], nbunch1: Iterable[Incomplete], nbunch2: Iterable[Incomplete] | None = None) -> set[_Node]: ...
