"""Generate graphs with a given degree sequence or expected degree sequence."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.graph import Graph
from ..classes.multidigraph import MultiDiGraph
from ..classes.multigraph import MultiGraph

__all__ = [
    "configuration_model",
    "directed_configuration_model",
    "expected_degree_graph",
    "havel_hakimi_graph",
    "directed_havel_hakimi_graph",
    "degree_sequence_tree",
    "random_degree_sequence_graph",
]

@_dispatchable
def configuration_model(deg_sequence, create_using=None, seed=None) -> MultiGraph[Incomplete]: ...
@_dispatchable
def directed_configuration_model(
    in_degree_sequence, out_degree_sequence, create_using=None, seed=None
) -> MultiDiGraph[Incomplete]: ...
@_dispatchable
def expected_degree_graph(w, seed=None, selfloops: bool = True) -> Graph[Incomplete]: ...
@_dispatchable
def havel_hakimi_graph(deg_sequence, create_using=None):
    """
    Returns a simple graph with given degree sequence constructed
    using the Havel-Hakimi algorithm.

    Parameters
    ----------
    deg_sequence: list of integers
        Each integer corresponds to the degree of a node (need not be sorted).
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
        Graph type to create. If graph instance, then cleared before populated.
        Directed graphs are not allowed.

    Raises
    ------
    NetworkXException
        For a non-graphical degree sequence (i.e. one
        not realizable by some simple graph).

    Notes
    -----
    The Havel-Hakimi algorithm constructs a simple graph by
    successively connecting the node of highest degree to other nodes
    of highest degree, resorting remaining nodes by degree, and
    repeating the process. The resulting graph has a high
    degree-associativity.  Nodes are labeled 1,.., len(deg_sequence),
    corresponding to their position in deg_sequence.

    The basic algorithm is from Hakimi [1]_ and was generalized by
    Kleitman and Wang [2]_.

    References
    ----------
    .. [1] Hakimi S., On Realizability of a Set of Integers as
       Degrees of the Vertices of a Linear Graph. I,
       Journal of SIAM, 10(3), pp. 496-506 (1962)
    .. [2] Kleitman D.J. and Wang D.L.
       Algorithms for Constructing Graphs and Digraphs with Given Valences
       and Factors  Discrete Mathematics, 6(1), pp. 79-88 (1973)
    """
    ...
@_dispatchable
def directed_havel_hakimi_graph(in_deg_sequence, out_deg_sequence, create_using=None) -> DiGraph[Incomplete]: ...
@_dispatchable
def degree_sequence_tree(deg_sequence, create_using=None):
    """
    Make a tree for the given degree sequence.

    A tree has #nodes-#edges=1 so
    the degree sequence must have
    len(deg_sequence)-sum(deg_sequence)/2=1
    """
    ...
@_dispatchable
def random_degree_sequence_graph(sequence, seed=None, tries: int = 10) -> Graph[Incomplete]: ...

class DegreeSequenceRandomGraph:
    rng: Incomplete
    degree: Incomplete
    m: Incomplete
    dmax: Incomplete
    def __init__(self, degree, rng) -> None: ...
    remaining_degree: Incomplete
    graph: Incomplete
    def generate(self): ...
    def update_remaining(self, u, v, aux_graph=None) -> None: ...
    def p(self, u, v): ...
    def q(self, u, v): ...
    def suitable_edge(self):
        """
        Returns True if and only if an arbitrary remaining node can
        potentially be joined with some other remaining node.
        """
        ...
    def phase1(self) -> None: ...
    def phase2(self) -> None: ...
    def phase3(self) -> None: ...
