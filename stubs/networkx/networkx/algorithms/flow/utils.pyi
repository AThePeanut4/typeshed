"""Utility classes and functions for network flow algorithms."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

__all__ = ["CurrentEdge", "Level", "GlobalRelabelThreshold", "build_residual_network", "detect_unboundedness", "build_flow_dict"]

class CurrentEdge:
    """
    Mechanism for iterating over out-edges incident to a node in a circular
    manner. StopIteration exception is raised when wraparound occurs.
    """
    def __init__(self, edges) -> None: ...
    def get(self): ...
    def move_to_next(self) -> None: ...

class Level:
    """Active and inactive nodes in a level."""
    active: Incomplete
    inactive: Incomplete

    def __init__(self) -> None: ...

class GlobalRelabelThreshold:
    """
    Measurement of work before the global relabeling heuristic should be
    applied.
    """
    def __init__(self, n, m, freq) -> None: ...
    def add_work(self, work) -> None: ...
    def is_reached(self) -> bool: ...
    def clear_work(self) -> None: ...

@_dispatchable
def build_residual_network(G, capacity):
    """
    Build a residual network and initialize a zero flow.

    The residual network :samp:`R` from an input graph :samp:`G` has the
    same nodes as :samp:`G`. :samp:`R` is a DiGraph that contains a pair
    of edges :samp:`(u, v)` and :samp:`(v, u)` iff :samp:`(u, v)` is not a
    self-loop, and at least one of :samp:`(u, v)` and :samp:`(v, u)` exists
    in :samp:`G`.

    For each edge :samp:`(u, v)` in :samp:`R`, :samp:`R[u][v]['capacity']`
    is equal to the capacity of :samp:`(u, v)` in :samp:`G` if it exists
    in :samp:`G` or zero otherwise. If the capacity is infinite,
    :samp:`R[u][v]['capacity']` will have a high arbitrary finite value
    that does not affect the solution of the problem. This value is stored in
    :samp:`R.graph['inf']`. For each edge :samp:`(u, v)` in :samp:`R`,
    :samp:`R[u][v]['flow']` represents the flow function of :samp:`(u, v)` and
    satisfies :samp:`R[u][v]['flow'] == -R[v][u]['flow']`.

    The flow value, defined as the total flow into :samp:`t`, the sink, is
    stored in :samp:`R.graph['flow_value']`. If :samp:`cutoff` is not
    specified, reachability to :samp:`t` using only edges :samp:`(u, v)` such
    that :samp:`R[u][v]['flow'] < R[u][v]['capacity']` induces a minimum
    :samp:`s`-:samp:`t` cut.
    """
    ...
@_dispatchable
def detect_unboundedness(R, s, t) -> None:
    """Detect an infinite-capacity s-t path in R."""
    ...
@_dispatchable
def build_flow_dict(G, R):
    """Build a flow dictionary from a residual network."""
    ...
