from networkx.utils.backends import _dispatchable

__all__ = [
    "LCF_graph",
    "bull_graph",
    "chvatal_graph",
    "cubical_graph",
    "desargues_graph",
    "diamond_graph",
    "dodecahedral_graph",
    "frucht_graph",
    "heawood_graph",
    "hoffman_singleton_graph",
    "house_graph",
    "house_x_graph",
    "icosahedral_graph",
    "krackhardt_kite_graph",
    "moebius_kantor_graph",
    "octahedral_graph",
    "pappus_graph",
    "petersen_graph",
    "sedgewick_maze_graph",
    "tetrahedral_graph",
    "truncated_cube_graph",
    "truncated_tetrahedron_graph",
    "tutte_graph",
]

@_dispatchable
def LCF_graph(n, shift_list, repeats, create_using=None): ...
@_dispatchable
def bull_graph(create_using=None): ...
@_dispatchable
def chvatal_graph(create_using=None): ...
@_dispatchable
def cubical_graph(create_using=None): ...
@_dispatchable
def desargues_graph(create_using=None): ...
@_dispatchable
def diamond_graph(create_using=None): ...
@_dispatchable
def dodecahedral_graph(create_using=None): ...
@_dispatchable
def frucht_graph(create_using=None): ...
@_dispatchable
def heawood_graph(create_using=None): ...
@_dispatchable
def hoffman_singleton_graph():
    """
    Returns the Hoffman-Singleton Graph.

    The Hoffman–Singleton graph is a symmetrical undirected graph
    with 50 nodes and 175 edges.
    All indices lie in ``Z % 5``: that is, the integers mod 5 [1]_.
    It is the only regular graph of vertex degree 7, diameter 2, and girth 5.
    It is the unique (7,5)-cage graph and Moore graph, and contains many
    copies of the Petersen graph [2]_.

    Returns
    -------
    G : networkx Graph
        Hoffman–Singleton Graph with 50 nodes and 175 edges

    Notes
    -----
    Constructed from pentagon and pentagram as follows: Take five pentagons $P_h$
    and five pentagrams $Q_i$ . Join vertex $j$ of $P_h$ to vertex $h·i+j$ of $Q_i$ [3]_.

    References
    ----------
    .. [1] https://blogs.ams.org/visualinsight/2016/02/01/hoffman-singleton-graph/
    .. [2] https://mathworld.wolfram.com/Hoffman-SingletonGraph.html
    .. [3] https://en.wikipedia.org/wiki/Hoffman%E2%80%93Singleton_graph
    """
    ...
@_dispatchable
def house_graph(create_using=None): ...
@_dispatchable
def house_x_graph(create_using=None): ...
@_dispatchable
def icosahedral_graph(create_using=None): ...
@_dispatchable
def krackhardt_kite_graph(create_using=None): ...
@_dispatchable
def moebius_kantor_graph(create_using=None): ...
@_dispatchable
def octahedral_graph(create_using=None): ...
@_dispatchable
def pappus_graph():
    """
    Returns the Pappus graph.

    The Pappus graph is a cubic symmetric distance-regular graph with 18 nodes
    and 27 edges. It is Hamiltonian and can be represented in LCF notation as
    [5,7,-7,7,-7,-5]^3 [1]_.

    Returns
    -------
    G : networkx Graph
        Pappus graph

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Pappus_graph
    """
    ...
@_dispatchable
def petersen_graph(create_using=None): ...
@_dispatchable
def sedgewick_maze_graph(create_using=None): ...
@_dispatchable
def tetrahedral_graph(create_using=None): ...
@_dispatchable
def truncated_cube_graph(create_using=None): ...
@_dispatchable
def truncated_tetrahedron_graph(create_using=None): ...
@_dispatchable
def tutte_graph(create_using=None): ...
