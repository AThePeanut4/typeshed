"""Group centrality measures."""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def group_betweenness_centrality(
    G: Graph[_Node], C, normalized: bool | None = True, weight: str | None = None, endpoints: bool | None = False
): ...
@_dispatchable
def prominent_group(
    G: Graph[_Node],
    k: int,
    weight: str | None = None,
    C: Iterable[Incomplete] | None = None,
    endpoints: bool | None = False,
    normalized: bool | None = True,
    greedy: bool | None = False,
): ...
@_dispatchable
def group_closeness_centrality(G: Graph[_Node], S: Iterable[Incomplete], weight: str | None = None): ...
@_dispatchable
def group_degree_centrality(G: Graph[_Node], S: Iterable[Incomplete]): ...
@_dispatchable
def group_in_degree_centrality(G: Graph[_Node], S: Iterable[Incomplete]): ...
@_dispatchable
def group_out_degree_centrality(G: Graph[_Node], S: Iterable[Incomplete]): ...
