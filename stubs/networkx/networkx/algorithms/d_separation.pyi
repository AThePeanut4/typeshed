from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def d_separated(G, x, y, z):
    """
    Return whether nodes sets ``x`` and ``y`` are d-separated by ``z``.

    .. deprecated:: 3.3

        This function is deprecated and will be removed in NetworkX v3.5.
        Please use `is_d_separator(G, x, y, z)`.
    """
    ...
@_dispatchable
def minimal_d_separator(G, u, v):
    """
    Returns a minimal_d-separating set between `x` and `y` if possible

    .. deprecated:: 3.3

        minimal_d_separator is deprecated and will be removed in NetworkX v3.5.
        Please use `find_minimal_d_separator(G, x, y)`.
    """
    ...
@_dispatchable
def is_minimal_d_separator(G: DiGraph[_Node], x, y, z, *, included=None, restricted=None): ...
