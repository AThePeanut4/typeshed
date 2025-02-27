"""Functions for analyzing triads of a graph."""

from _typeshed import Incomplete
from collections.abc import Generator, Iterable

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def triadic_census(G: DiGraph[_Node], nodelist: Iterable[Incomplete] | None = None): ...
@_dispatchable
def is_triad(G: Graph[_Node]): ...
@_dispatchable
def all_triplets(G: DiGraph[_Node]): ...
@_dispatchable
def all_triads(G: DiGraph[_Node]) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def triads_by_type(G: DiGraph[_Node]): ...
@_dispatchable
def triad_type(G: DiGraph[_Node]): ...
@_dispatchable
def random_triad(G: DiGraph[_Node], seed: int | RandomState | None = None): ...
