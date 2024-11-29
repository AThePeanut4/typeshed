"""Provides explicit constructions of expander graphs."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

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
def paley_graph(p, create_using: Incomplete | None = None):
    r"""
    Returns the Paley $\frac{(p-1)}{2}$ -regular graph on $p$ nodes.

    The returned graph is a graph on $\mathbb{Z}/p\mathbb{Z}$ with edges between $x$ and $y$
    if and only if $x-y$ is a nonzero square in $\mathbb{Z}/p\mathbb{Z}$.

    If $p \equiv 1  \pmod 4$, $-1$ is a square in $\mathbb{Z}/p\mathbb{Z}$ and therefore $x-y$ is a square if and
    only if $y-x$ is also a square, i.e the edges in the Paley graph are symmetric.

    If $p \equiv 3 \pmod 4$, $-1$ is not a square in $\mathbb{Z}/p\mathbb{Z}$ and therefore either $x-y$ or $y-x$
    is a square in $\mathbb{Z}/p\mathbb{Z}$ but not both.

    Note that a more general definition of Paley graphs extends this construction
    to graphs over $q=p^n$ vertices, by using the finite field $F_q$ instead of $\mathbb{Z}/p\mathbb{Z}$.
    This construction requires to compute squares in general finite fields and is
    not what is implemented here (i.e `paley_graph(25)` does not return the true
    Paley graph associated with $5^2$).

    Parameters
    ----------
    p : int, an odd prime number.

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    G : graph
        The constructed directed graph.

    Raises
    ------
    NetworkXError
        If the graph is a multigraph.

    References
    ----------
    Chapter 13 in B. Bollobas, Random Graphs. Second edition.
    Cambridge Studies in Advanced Mathematics, 73.
    Cambridge University Press, Cambridge (2001).
    """
    ...
