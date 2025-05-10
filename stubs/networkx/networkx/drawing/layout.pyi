"""
******
Layout
******

Node positioning algorithms for graph drawing.

For `random_layout()` the possible resulting shape
is a square of side [0, scale] (default: [0, 1])
Changing `center` shifts the layout by that amount.

For the other layout routines, the extent is
[center - scale, center + scale] (default: [-1, 1]).

Warning: Most layout routines have only been tested in 2-dimensions.
"""

from _typeshed import Incomplete

import numpy

__all__ = [
    "bipartite_layout",
    "circular_layout",
    "forceatlas2_layout",
    "kamada_kawai_layout",
    "random_layout",
    "rescale_layout",
    "rescale_layout_dict",
    "shell_layout",
    "spring_layout",
    "spectral_layout",
    "planar_layout",
    "fruchterman_reingold_layout",
    "spiral_layout",
    "multipartite_layout",
    "bfs_layout",
    "arf_layout",
]

def random_layout(G, center: Incomplete | None = None, dim: int = 2, seed: Incomplete | None = None): ...
def circular_layout(G, scale: float = 1, center: Incomplete | None = None, dim: int = 2): ...
def shell_layout(
    G,
    nlist: Incomplete | None = None,
    rotate: Incomplete | None = None,
    scale: float = 1,
    center: Incomplete | None = None,
    dim: int = 2,
):
    """
    Position nodes in concentric circles.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.

    nlist : list of lists
       List of node lists for each shell.

    rotate : angle in radians (default=pi/len(nlist))
       Angle by which to rotate the starting position of each shell
       relative to the starting position of the previous shell.
       To recreate behavior before v2.5 use rotate=0.

    scale : number (default: 1)
        Scale factor for positions.

    center : array-like or None
        Coordinate pair around which to center the layout.

    dim : int
        Dimension of layout, currently only dim=2 is supported.
        Other dimension values result in a ValueError.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node

    Raises
    ------
    ValueError
        If dim != 2

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> shells = [[0], [1, 2, 3]]
    >>> pos = nx.shell_layout(G, shells)

    Notes
    -----
    This algorithm currently only works in two dimensions and does not
    try to minimize edge crossings.
    """
    ...
def bipartite_layout(
    G, nodes, align: str = "vertical", scale: float = 1, center: Incomplete | None = None, aspect_ratio: float = ...
):
    """
    Position nodes in two straight lines.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.

    nodes : list or container
        Nodes in one node set of the bipartite graph.
        This set will be placed on left or top.

    align : string (default='vertical')
        The alignment of nodes. Vertical or horizontal.

    scale : number (default: 1)
        Scale factor for positions.

    center : array-like or None
        Coordinate pair around which to center the layout.

    aspect_ratio : number (default=4/3):
        The ratio of the width to the height of the layout.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node.

    Examples
    --------
    >>> G = nx.bipartite.gnmk_random_graph(3, 5, 10, seed=123)
    >>> top = nx.bipartite.sets(G)[0]
    >>> pos = nx.bipartite_layout(G, top)

    Notes
    -----
    This algorithm currently only works in two dimensions and does not
    try to minimize edge crossings.
    """
    ...
def spring_layout(
    G,
    k: Incomplete | None = None,
    pos: Incomplete | None = None,
    fixed: Incomplete | None = None,
    iterations: int = 50,
    threshold: float = 0.0001,
    weight: str = "weight",
    scale: float = 1,
    center: Incomplete | None = None,
    dim: int = 2,
    seed: Incomplete | None = None,
):
    """
    Position nodes using Fruchterman-Reingold force-directed algorithm.

    The algorithm simulates a force-directed representation of the network
    treating edges as springs holding nodes close, while treating nodes
    as repelling objects, sometimes called an anti-gravity force.
    Simulation continues until the positions are close to an equilibrium.

    There are some hard-coded values: minimal distance between
    nodes (0.01) and "temperature" of 0.1 to ensure nodes don't fly away.
    During the simulation, `k` helps determine the distance between nodes,
    though `scale` and `center` determine the size and place after
    rescaling occurs at the end of the simulation.

    Fixing some nodes doesn't allow them to move in the simulation.
    It also turns off the rescaling feature at the simulation's end.
    In addition, setting `scale` to `None` turns off rescaling.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.

    k : float (default=None)
        Optimal distance between nodes.  If None the distance is set to
        1/sqrt(n) where n is the number of nodes.  Increase this value
        to move nodes farther apart.

    pos : dict or None  optional (default=None)
        Initial positions for nodes as a dictionary with node as keys
        and values as a coordinate list or tuple.  If None, then use
        random initial positions.

    fixed : list or None  optional (default=None)
        Nodes to keep fixed at initial position.
        Nodes not in ``G.nodes`` are ignored.
        ValueError raised if `fixed` specified and `pos` not.

    iterations : int  optional (default=50)
        Maximum number of iterations taken

    threshold: float optional (default = 1e-4)
        Threshold for relative error in node position changes.
        The iteration stops if the error is below this threshold.

    weight : string or None   optional (default='weight')
        The edge attribute that holds the numerical value used for
        the edge weight.  Larger means a stronger attractive force.
        If None, then all edge weights are 1.

    scale : number or None (default: 1)
        Scale factor for positions. Not used unless `fixed is None`.
        If scale is None, no rescaling is performed.

    center : array-like or None
        Coordinate pair around which to center the layout.
        Not used unless `fixed is None`.

    dim : int
        Dimension of layout.

    seed : int, RandomState instance or None  optional (default=None)
        Used only for the initial positions in the algorithm.
        Set the random state for deterministic node layouts.
        If int, `seed` is the seed used by the random number generator,
        if numpy.random.RandomState instance, `seed` is the random
        number generator,
        if None, the random number generator is the RandomState instance used
        by numpy.random.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> pos = nx.spring_layout(G)

    # The same using longer but equivalent function name
    >>> pos = nx.fruchterman_reingold_layout(G)
    """
    ...

fruchterman_reingold_layout = spring_layout

def kamada_kawai_layout(
    G,
    dist: Incomplete | None = None,
    pos: Incomplete | None = None,
    weight: str = "weight",
    scale: float = 1,
    center: Incomplete | None = None,
    dim: int = 2,
):
    """
    Position nodes using Kamada-Kawai path-length cost-function.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.

    dist : dict (default=None)
        A two-level dictionary of optimal distances between nodes,
        indexed by source and destination node.
        If None, the distance is computed using shortest_path_length().

    pos : dict or None  optional (default=None)
        Initial positions for nodes as a dictionary with node as keys
        and values as a coordinate list or tuple.  If None, then use
        circular_layout() for dim >= 2 and a linear layout for dim == 1.

    weight : string or None   optional (default='weight')
        The edge attribute that holds the numerical value used for
        the edge weight.  If None, then all edge weights are 1.

    scale : number (default: 1)
        Scale factor for positions.

    center : array-like or None
        Coordinate pair around which to center the layout.

    dim : int
        Dimension of layout.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> pos = nx.kamada_kawai_layout(G)
    """
    ...
def spectral_layout(G, weight: str = "weight", scale: float = 1, center: Incomplete | None = None, dim: int = 2):
    """
    Position nodes using the eigenvectors of the graph Laplacian.

    Using the unnormalized Laplacian, the layout shows possible clusters of
    nodes which are an approximation of the ratio cut. If dim is the number of
    dimensions then the positions are the entries of the dim eigenvectors
    corresponding to the ascending eigenvalues starting from the second one.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.

    weight : string or None   optional (default='weight')
        The edge attribute that holds the numerical value used for
        the edge weight.  If None, then all edge weights are 1.

    scale : number (default: 1)
        Scale factor for positions.

    center : array-like or None
        Coordinate pair around which to center the layout.

    dim : int
        Dimension of layout.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> pos = nx.spectral_layout(G)

    Notes
    -----
    Directed graphs will be considered as undirected graphs when
    positioning the nodes.

    For larger graphs (>500 nodes) this will use the SciPy sparse
    eigenvalue solver (ARPACK).
    """
    ...
def planar_layout(G, scale: float = 1, center: Incomplete | None = None, dim: int = 2):
    """
    Position nodes without edge intersections.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G. If G is of type
        nx.PlanarEmbedding, the positions are selected accordingly.

    scale : number (default: 1)
        Scale factor for positions.

    center : array-like or None
        Coordinate pair around which to center the layout.

    dim : int
        Dimension of layout.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node

    Raises
    ------
    NetworkXException
        If G is not planar

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> pos = nx.planar_layout(G)
    """
    ...
def spiral_layout(
    G, scale: float = 1, center: Incomplete | None = None, dim: int = 2, resolution: float = 0.35, equidistant: bool = False
):
    """
    Position nodes in a spiral layout.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    scale : number (default: 1)
        Scale factor for positions.
    center : array-like or None
        Coordinate pair around which to center the layout.
    dim : int, default=2
        Dimension of layout, currently only dim=2 is supported.
        Other dimension values result in a ValueError.
    resolution : float, default=0.35
        The compactness of the spiral layout returned.
        Lower values result in more compressed spiral layouts.
    equidistant : bool, default=False
        If True, nodes will be positioned equidistant from each other
        by decreasing angle further from center.
        If False, nodes will be positioned at equal angles
        from each other by increasing separation further from center.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node

    Raises
    ------
    ValueError
        If dim != 2

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> pos = nx.spiral_layout(G)
    >>> nx.draw(G, pos=pos)

    Notes
    -----
    This algorithm currently only works in two dimensions.
    """
    ...
def multipartite_layout(
    G, subset_key: str = "subset", align: str = "vertical", scale: float = 1, center: Incomplete | None = None
):
    """
    Position nodes in layers of straight lines.

    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.

    subset_key : string or dict (default='subset')
        If a string, the key of node data in G that holds the node subset.
        If a dict, keyed by layer number to the nodes in that layer/subset.

    align : string (default='vertical')
        The alignment of nodes. Vertical or horizontal.

    scale : number (default: 1)
        Scale factor for positions.

    center : array-like or None
        Coordinate pair around which to center the layout.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node.

    Examples
    --------
    >>> G = nx.complete_multipartite_graph(28, 16, 10)
    >>> pos = nx.multipartite_layout(G)

    or use a dict to provide the layers of the layout

    >>> G = nx.Graph([(0, 1), (1, 2), (1, 3), (3, 4)])
    >>> layers = {"a": [0], "b": [1], "c": [2, 3], "d": [4]}
    >>> pos = nx.multipartite_layout(G, subset_key=layers)

    Notes
    -----
    This algorithm currently only works in two dimensions and does not
    try to minimize edge crossings.

    Network does not need to be a complete multipartite graph. As long as nodes
    have subset_key data, they will be placed in the corresponding layers.
    """
    ...
def arf_layout(
    G,
    pos: Incomplete | None = None,
    scaling: float = 1,
    a: float = 1.1,
    etol: float = 1e-06,
    dt: float = 0.001,
    max_iter: int = 1000,
    *,
    seed: int | numpy.random.RandomState | None = None,
): ...
def forceatlas2_layout(
    G,
    pos=None,
    *,
    max_iter=100,
    jitter_tolerance=1.0,
    scaling_ratio=2.0,
    gravity=1.0,
    distributed_action=False,
    strong_gravity=False,
    node_mass=None,
    node_size=None,
    weight=None,
    dissuade_hubs=False,
    linlog=False,
    seed=None,
    dim=2,
) -> dict[Incomplete, Incomplete]: ...
def rescale_layout(pos, scale: float = 1): ...
def rescale_layout_dict(pos, scale: float = 1): ...
def bfs_layout(G, start, *, align="vertical", scale=1, center=None) -> dict[Incomplete, Incomplete]: ...
