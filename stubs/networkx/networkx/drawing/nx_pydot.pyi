from networkx.utils.backends import _dispatchable

__all__ = ["write_dot", "read_dot", "graphviz_layout", "pydot_layout", "to_pydot", "from_pydot"]

def write_dot(G, path) -> None:
    """
    Write NetworkX graph G to Graphviz dot format on path.

    Path can be a string or a file handle.
    """
    ...
@_dispatchable
def read_dot(path):
    """
    Returns a NetworkX :class:`MultiGraph` or :class:`MultiDiGraph` from the
    dot file with the passed path.

    If this file contains multiple graphs, only the first such graph is
    returned. All graphs _except_ the first are silently ignored.

    Parameters
    ----------
    path : str or file
        Filename or file handle.

    Returns
    -------
    G : MultiGraph or MultiDiGraph
        A :class:`MultiGraph` or :class:`MultiDiGraph`.

    Notes
    -----
    Use `G = nx.Graph(nx.nx_pydot.read_dot(path))` to return a :class:`Graph` instead of a
    :class:`MultiGraph`.
    """
    ...
@_dispatchable
def from_pydot(P): ...
def to_pydot(N): ...
def graphviz_layout(G, prog: str = "neato", root=None): ...
def pydot_layout(G, prog: str = "neato", root=None): ...
