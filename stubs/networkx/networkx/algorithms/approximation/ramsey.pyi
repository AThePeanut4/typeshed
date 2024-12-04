"""Ramsey numbers."""

from networkx.utils.backends import _dispatchable

@_dispatchable
def ramsey_R2(G):
    """
    Compute the largest clique and largest independent set in `G`.

    This can be used to estimate bounds for the 2-color
    Ramsey number `R(2;s,t)` for `G`.

    This is a recursive implementation which could run into trouble
    for large recursions. Note that self-loop edges are ignored.

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph

    Returns
    -------
    max_pair : (set, set) tuple
        Maximum clique, Maximum independent set.

    Raises
    ------
    NetworkXNotImplemented
        If the graph is directed or is a multigraph.
    """
    ...
