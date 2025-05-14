from networkx.utils.backends import _dispatchable

__all__ = ["grid_2d_graph", "grid_graph", "hypercube_graph", "triangular_lattice_graph", "hexagonal_lattice_graph"]

@_dispatchable
def grid_2d_graph(m, n, periodic: bool = False, create_using=None): ...
@_dispatchable
def grid_graph(dim, periodic: bool = False):
    """
    Returns the *n*-dimensional grid graph.

    The dimension *n* is the length of the list `dim` and the size in
    each dimension is the value of the corresponding list element.

    Parameters
    ----------
    dim : list or tuple of numbers or iterables of nodes
        'dim' is a tuple or list with, for each dimension, either a number
        that is the size of that dimension or an iterable of nodes for
        that dimension. The dimension of the grid_graph is the length
        of `dim`.

    periodic : bool or iterable
        If `periodic` is True, all dimensions are periodic. If False all
        dimensions are not periodic. If `periodic` is iterable, it should
        yield `dim` bool values each of which indicates whether the
        corresponding axis is periodic.

    Returns
    -------
    NetworkX graph
        The (possibly periodic) grid graph of the specified dimensions.

    Examples
    --------
    To produce a 2 by 3 by 4 grid graph, a graph on 24 nodes:

    >>> from networkx import grid_graph
    >>> G = grid_graph(dim=(2, 3, 4))
    >>> len(G)
    24
    >>> G = grid_graph(dim=(range(7, 9), range(3, 6)))
    >>> len(G)
    6
    """
    ...
@_dispatchable
def hypercube_graph(n):
    """
    Returns the *n*-dimensional hypercube graph.

    The nodes are the integers between 0 and ``2 ** n - 1``, inclusive.

    For more information on the hypercube graph, see the Wikipedia
    article `Hypercube graph`_.

    .. _Hypercube graph: https://en.wikipedia.org/wiki/Hypercube_graph

    Parameters
    ----------
    n : int
        The dimension of the hypercube.
        The number of nodes in the graph will be ``2 ** n``.

    Returns
    -------
    NetworkX graph
        The hypercube graph of dimension *n*.
    """
    ...
@_dispatchable
def triangular_lattice_graph(m, n, periodic: bool = False, with_positions: bool = True, create_using=None): ...
@_dispatchable
def hexagonal_lattice_graph(m, n, periodic: bool = False, with_positions: bool = True, create_using=None): ...
