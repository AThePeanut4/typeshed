"""Provides explicit constructions of expander graphs."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

__all__ = [
    "margulis_gabber_galil_graph",
    "chordal_cycle_graph",
    "paley_graph",
    "maybe_regular_expander",
    "is_regular_expander",
    "random_regular_expander_graph",
]

@_dispatchable
def margulis_gabber_galil_graph(n, create_using: Incomplete | None = None):
    r"""
    Returns the Margulis-Gabber-Galil undirected MultiGraph on `n^2` nodes.

    The undirected MultiGraph is regular with degree `8`. Nodes are integer
    pairs. The second-largest eigenvalue of the adjacency matrix of the graph
    is at most `5 \sqrt{2}`, regardless of `n`.

    Parameters
    ----------
    n : int
        Determines the number of nodes in the graph: `n^2`.
    create_using : NetworkX graph constructor, optional (default MultiGraph)
       Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    G : graph
        The constructed undirected multigraph.

    Raises
    ------
    NetworkXError
        If the graph is directed or not a multigraph.
    """
    ...
@_dispatchable
def chordal_cycle_graph(p, create_using: Incomplete | None = None):
    """
    Returns the chordal cycle graph on `p` nodes.

    The returned graph is a cycle graph on `p` nodes with chords joining each
    vertex `x` to its inverse modulo `p`. This graph is a (mildly explicit)
    3-regular expander [1]_.

    `p` *must* be a prime number.

    Parameters
    ----------
    p : a prime number

        The number of vertices in the graph. This also indicates where the
        chordal edges in the cycle will be created.

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    G : graph
        The constructed undirected multigraph.

    Raises
    ------
    NetworkXError

        If `create_using` indicates directed or not a multigraph.

    References
    ----------

    .. [1] Theorem 4.4.2 in A. Lubotzky. "Discrete groups, expanding graphs and
           invariant measures", volume 125 of Progress in Mathematics.
           Birkhäuser Verlag, Basel, 1994.
    """
    ...
@_dispatchable
def paley_graph(p, create_using: Incomplete | None = None): ...
@_dispatchable
def maybe_regular_expander(n, d, *, create_using=None, max_tries=100, seed=None): ...
@_dispatchable
def is_regular_expander(G, *, epsilon=0) -> bool: ...
@_dispatchable
def random_regular_expander_graph(n, d, *, epsilon=0, create_using=None, max_tries=100, seed=None): ...
