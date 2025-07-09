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

from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

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

def random_layout(
    G, center=None, dim: int = 2, seed: int | RandomState | None = None, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def circular_layout(
    G, scale: float = 1, center=None, dim: int = 2, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def shell_layout(
    G, nlist=None, rotate=None, scale: float = 1, center=None, dim: int = 2, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def bipartite_layout(
    G,
    nodes=None,
    align: str = "vertical",
    scale: float = 1,
    center=None,
    aspect_ratio: float = ...,
    store_pos_as: str | None = None,
) -> dict[Incomplete, Incomplete]: ...
def spring_layout(
    G,
    k=None,
    pos=None,
    fixed=None,
    iterations: int = 50,
    threshold: float = 0.0001,
    weight: str = "weight",
    scale: float = 1,
    center=None,
    dim: int = 2,
    seed: int | RandomState | None = None,
    store_pos_as: str | None = None,
    *,
    method: str = "auto",
    gravity: float = 1.0,
) -> dict[Incomplete, Incomplete]: ...

fruchterman_reingold_layout = spring_layout

def kamada_kawai_layout(
    G, dist=None, pos=None, weight: str = "weight", scale: float = 1, center=None, dim: int = 2, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def spectral_layout(
    G, weight: str = "weight", scale: float = 1, center=None, dim: int = 2, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def planar_layout(
    G, scale: float = 1, center=None, dim: int = 2, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def spiral_layout(
    G,
    scale: float = 1,
    center=None,
    dim: int = 2,
    resolution: float = 0.35,
    equidistant: bool = False,
    store_pos_as: str | None = None,
) -> dict[Incomplete, Incomplete]: ...
def multipartite_layout(
    G, subset_key: str = "subset", align: str = "vertical", scale: float = 1, center=None, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]: ...
def arf_layout(
    G,
    pos=None,
    scaling: float = 1,
    a: float = 1.1,
    etol: float = 1e-06,
    dt: float = 0.001,
    max_iter: int = 1000,
    *,
    seed: int | RandomState | None = None,
    store_pos_as: str | None = None,
):
    """
    Arf layout for networkx

    The attractive and repulsive forces (arf) layout [1] improves the spring
    layout in three ways. First, it prevents congestion of highly connected nodes
    due to strong forcing between nodes. Second, it utilizes the layout space
    more effectively by preventing large gaps that spring layout tends to create.
    Lastly, the arf layout represents symmetries in the layout better than the
    default spring layout.

    Parameters
    ----------
    G : nx.Graph or nx.DiGraph
        Networkx graph.
    pos : dict
        Initial  position of  the nodes.  If set  to None  a
        random layout will be used.
    scaling : float
        Scales the radius of the circular layout space.
    a : float
        Strength of springs between connected nodes. Should be larger than 1.
        The greater a, the clearer the separation of unconnected sub clusters.
    etol : float
        Gradient sum of spring forces must be larger than `etol` before successful
        termination.
    dt : float
        Time step for force differential equation simulations.
    max_iter : int
        Max iterations before termination of the algorithm.
    seed : int, RandomState instance or None  optional (default=None)
        Set the random state for deterministic node layouts.
        If int, `seed` is the seed used by the random number generator,
        if numpy.random.RandomState instance, `seed` is the random
        number generator,
        if None, the random number generator is the RandomState instance used
        by numpy.random.
    store_pos_as : str, default None
        If non-None, the position of each node will be stored on the graph as
        an attribute with this string as its name, which can be accessed with
        ``G.nodes[...][store_pos_as]``. The function still returns the dictionary.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node.

    Examples
    --------
    >>> G = nx.grid_graph((5, 5))
    >>> pos = nx.arf_layout(G)
    >>> # suppress the returned dict and store on the graph directly
    >>> G = nx.grid_graph((5, 5))
    >>> _ = nx.arf_layout(G, store_pos_as="pos")

    References
    ----------
    .. [1] "Self-Organization Applied to Dynamic Network Layout", M. Geipel,
            International Journal of Modern Physics C, 2007, Vol 18, No 10,
            pp. 1537-1549.
            https://doi.org/10.1142/S0129183107011558 https://arxiv.org/abs/0704.1748
    """
    ...
@_dispatchable
def forceatlas2_layout(
    G,
    pos=None,
    *,
    max_iter=100,
    jitter_tolerance=1.0,
    scaling_ratio=2.0,
    gravity: float = 1.0,
    distributed_action=False,
    strong_gravity=False,
    node_mass=None,
    node_size=None,
    weight=None,
    dissuade_hubs=False,
    linlog=False,
    seed: int | RandomState | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[Incomplete, Incomplete]:
    """
    Position nodes using the ForceAtlas2 force-directed layout algorithm.

    This function applies the ForceAtlas2 layout algorithm [1]_ to a NetworkX graph,
    positioning the nodes in a way that visually represents the structure of the graph.
    The algorithm uses physical simulation to minimize the energy of the system,
    resulting in a more readable layout.

    Parameters
    ----------
    G : nx.Graph
        A NetworkX graph to be laid out.
    pos : dict or None, optional
        Initial positions of the nodes. If None, random initial positions are used.
    max_iter : int (default: 100)
        Number of iterations for the layout optimization.
    jitter_tolerance : float (default: 1.0)
        Controls the tolerance for adjusting the speed of layout generation.
    scaling_ratio : float (default: 2.0)
        Determines the scaling of attraction and repulsion forces.
    gravity : float (default: 1.0)
        Determines the amount of attraction on nodes to the center. Prevents islands
        (i.e. weakly connected or disconnected parts of the graph)
        from drifting away.
    distributed_action : bool (default: False)
        Distributes the attraction force evenly among nodes.
    strong_gravity : bool (default: False)
        Applies a strong gravitational pull towards the center.
    node_mass : dict or None, optional
        Maps nodes to their masses, influencing the attraction to other nodes.
    node_size : dict or None, optional
        Maps nodes to their sizes, preventing crowding by creating a halo effect.
    weight : string or None, optional (default: None)
        The edge attribute that holds the numerical value used for
        the edge weight. If None, then all edge weights are 1.
    dissuade_hubs : bool (default: False)
        Prevents the clustering of hub nodes.
    linlog : bool (default: False)
        Uses logarithmic attraction instead of linear.
    seed : int, RandomState instance or None  optional (default=None)
        Used only for the initial positions in the algorithm.
        Set the random state for deterministic node layouts.
        If int, `seed` is the seed used by the random number generator,
        if numpy.random.RandomState instance, `seed` is the random
        number generator,
        if None, the random number generator is the RandomState instance used
        by numpy.random.
    dim : int (default: 2)
        Sets the dimensions for the layout. Ignored if `pos` is provided.
    store_pos_as : str, default None
        If non-None, the position of each node will be stored on the graph as
        an attribute with this string as its name, which can be accessed with
        ``G.nodes[...][store_pos_as]``. The function still returns the dictionary.

    Examples
    --------
    >>> import networkx as nx
    >>> G = nx.florentine_families_graph()
    >>> pos = nx.forceatlas2_layout(G)
    >>> nx.draw(G, pos=pos)
    >>> # suppress the returned dict and store on the graph directly
    >>> pos = nx.forceatlas2_layout(G, store_pos_as="pos")
    >>> _ = nx.forceatlas2_layout(G, store_pos_as="pos")

    References
    ----------
    .. [1] Jacomy, M., Venturini, T., Heymann, S., & Bastian, M. (2014).
           ForceAtlas2, a continuous graph layout algorithm for handy network
           visualization designed for the Gephi software. PloS one, 9(6), e98679.
           https://doi.org/10.1371/journal.pone.0098679
    """
    ...
def rescale_layout(pos, scale: float = 1):
    """
    Returns scaled position array to (-scale, scale) in all axes.

    The function acts on NumPy arrays which hold position information.
    Each position is one row of the array. The dimension of the space
    equals the number of columns. Each coordinate in one column.

    To rescale, the mean (center) is subtracted from each axis separately.
    Then all values are scaled so that the largest magnitude value
    from all axes equals `scale` (thus, the aspect ratio is preserved).
    The resulting NumPy Array is returned (order of rows unchanged).

    Parameters
    ----------
    pos : numpy array
        positions to be scaled. Each row is a position.

    scale : number (default: 1)
        The size of the resulting extent in all directions.

    attribute : str, default None
        If non-None, the position of each node will be stored on the graph as
        an attribute named `attribute` which can be accessed with
        `G.nodes[...][attribute]`. The function still returns the dictionary.

    Returns
    -------
    pos : numpy array
        scaled positions. Each row is a position.

    See Also
    --------
    rescale_layout_dict
    """
    ...
def rescale_layout_dict(pos, scale: float = 1):
    """
    Return a dictionary of scaled positions keyed by node

    Parameters
    ----------
    pos : A dictionary of positions keyed by node

    scale : number (default: 1)
        The size of the resulting extent in all directions.

    Returns
    -------
    pos : A dictionary of positions keyed by node

    Examples
    --------
    >>> import numpy as np
    >>> pos = {0: np.array((0, 0)), 1: np.array((1, 1)), 2: np.array((0.5, 0.5))}
    >>> nx.rescale_layout_dict(pos)
    {0: array([-1., -1.]), 1: array([1., 1.]), 2: array([0., 0.])}

    >>> pos = {0: np.array((0, 0)), 1: np.array((-1, 1)), 2: np.array((-0.5, 0.5))}
    >>> nx.rescale_layout_dict(pos, scale=2)
    {0: array([ 2., -2.]), 1: array([-2.,  2.]), 2: array([0., 0.])}

    See Also
    --------
    rescale_layout
    """
    ...
def bfs_layout(
    G, start, *, align="vertical", scale=1, center=None, store_pos_as: str | None = None
) -> dict[Incomplete, Incomplete]:
    """
    Position nodes according to breadth-first search algorithm.

    Parameters
    ----------
    G : NetworkX graph
        A position will be assigned to every node in G.

    start : node in `G`
        Starting node for bfs

    center : array-like or None
        Coordinate pair around which to center the layout.

    store_pos_as : str, default None
        If non-None, the position of each node will be stored on the graph as
        an attribute with this string as its name, which can be accessed with
        ``G.nodes[...][store_pos_as]``. The function still returns the dictionary.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node.

    Examples
    --------
    >>> from pprint import pprint
    >>> G = nx.path_graph(4)
    >>> pos = nx.bfs_layout(G, 0)
    >>> # suppress the returned dict and store on the graph directly
    >>> _ = nx.bfs_layout(G, 0, store_pos_as="pos")
    >>> pprint(nx.get_node_attributes(G, "pos"))
    {0: array([-1.,  0.]),
     1: array([-0.33333333,  0.        ]),
     2: array([0.33333333, 0.        ]),
     3: array([1., 0.])}



    Notes
    -----
    This algorithm currently only works in two dimensions and does not
    try to minimize edge crossings.
    """
    ...
