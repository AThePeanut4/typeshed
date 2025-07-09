"""Functions for computing measures of structural holes."""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["constraint", "local_constraint", "effective_size"]

@_dispatchable
def mutual_weight(G: Graph[_Node], u, v, weight=None) -> Incomplete | int:
    """
    Returns the sum of the weights of the edge from `u` to `v` and
    the edge from `v` to `u` in `G`.

    `weight` is the edge data key that represents the edge weight. If
    the specified key is `None` or is not in the edge data for an edge,
    that edge is assumed to have weight 1.

    Pre-conditions: `u` and `v` must both be in `G`.
    """
    ...
@_dispatchable
def normalized_mutual_weight(G: Graph[_Node], u, v, norm=..., weight=None) -> float:
    """
    Returns normalized mutual weight of the edges from `u` to `v`
    with respect to the mutual weights of the neighbors of `u` in `G`.

    `norm` specifies how the normalization factor is computed. It must
    be a function that takes a single argument and returns a number.
    The argument will be an iterable of mutual weights
    of pairs ``(u, w)``, where ``w`` ranges over each (in- and
    out-)neighbor of ``u``. Commons values for `normalization` are
    ``sum`` and ``max``.

    `weight` can be ``None`` or a string, if None, all edge weights
    are considered equal. Otherwise holds the name of the edge
    attribute used as weight.
    """
    ...
@_dispatchable
def effective_size(
    G: Graph[_Node], nodes: Iterable[Incomplete] | None = None, weight: str | None = None
) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def constraint(
    G: Graph[_Node], nodes: Iterable[Incomplete] | None = None, weight: str | None = None
) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def local_constraint(G: Graph[_Node], u: _Node, v: _Node, weight: str | None = None) -> float: ...
