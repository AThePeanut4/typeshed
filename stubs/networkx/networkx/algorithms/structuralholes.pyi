"""Functions for computing measures of structural holes."""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["constraint", "local_constraint", "effective_size"]

@_dispatchable
def mutual_weight(G: Graph[_Node], u, v, weight=None) -> Incomplete | int: ...
@_dispatchable
def normalized_mutual_weight(G: Graph[_Node], u, v, norm=..., weight=None) -> float: ...
@_dispatchable
def effective_size(G: Graph[_Node], nodes: Iterable[Incomplete] | None = None, weight: str | None = None): ...
@_dispatchable
def constraint(G: Graph[_Node], nodes: Iterable[Incomplete] | None = None, weight: str | None = None):
    r"""
    Returns the constraint on all nodes in the graph ``G``.

    The *constraint* is a measure of the extent to which a node *v* is
    invested in those nodes that are themselves invested in the
    neighbors of *v*. Formally, the *constraint on v*, denoted `c(v)`,
    is defined by

    .. math::

       c(v) = \sum_{w \in N(v) \setminus \{v\}} \ell(v, w)

    where $N(v)$ is the subset of the neighbors of `v` that are either
    predecessors or successors of `v` and $\ell(v, w)$ is the local
    constraint on `v` with respect to `w` [1]_. For the definition of local
    constraint, see :func:`local_constraint`.

    Parameters
    ----------
    G : NetworkX graph
        The graph containing ``v``. This can be either directed or undirected.

    nodes : container, optional
        Container of nodes in the graph ``G`` to compute the constraint. If
        None, the constraint of every node is computed.

    weight : None or string, optional
      If None, all edge weights are considered equal.
      Otherwise holds the name of the edge attribute used as weight.

    Returns
    -------
    dict
        Dictionary with nodes as keys and the constraint on the node as values.

    See also
    --------
    local_constraint

    References
    ----------
    .. [1] Burt, Ronald S.
           "Structural holes and good ideas".
           American Journal of Sociology (110): 349–399.
    """
    ...
@_dispatchable
def local_constraint(G: Graph[_Node], u: _Node, v: _Node, weight: str | None = None):
    r"""
    Returns the local constraint on the node ``u`` with respect to
    the node ``v`` in the graph ``G``.

    Formally, the *local constraint on u with respect to v*, denoted
    $\ell(u, v)$, is defined by

    .. math::

       \ell(u, v) = \left(p_{uv} + \sum_{w \in N(v)} p_{uw} p_{wv}\right)^2,

    where $N(v)$ is the set of neighbors of $v$ and $p_{uv}$ is the
    normalized mutual weight of the (directed or undirected) edges
    joining $u$ and $v$, for each vertex $u$ and $v$ [1]_. The *mutual
    weight* of $u$ and $v$ is the sum of the weights of edges joining
    them (edge weights are assumed to be one if the graph is
    unweighted).

    Parameters
    ----------
    G : NetworkX graph
        The graph containing ``u`` and ``v``. This can be either
        directed or undirected.

    u : node
        A node in the graph ``G``.

    v : node
        A node in the graph ``G``.

    weight : None or string, optional
      If None, all edge weights are considered equal.
      Otherwise holds the name of the edge attribute used as weight.

    Returns
    -------
    float
        The constraint of the node ``v`` in the graph ``G``.

    See also
    --------
    constraint

    References
    ----------
    .. [1] Burt, Ronald S.
           "Structural holes and good ideas".
           American Journal of Sociology (110): 349–399.
    """
    ...
