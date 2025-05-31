"""
**********
Matplotlib
**********

Draw networks with matplotlib.

Examples
--------
>>> G = nx.complete_graph(5)
>>> nx.draw(G)

See Also
--------
 - :doc:`matplotlib <matplotlib:index>`
 - :func:`matplotlib.pyplot.scatter`
 - :obj:`matplotlib.patches.FancyArrowPatch`
"""

from _typeshed import Incomplete
from collections.abc import Collection, Iterable, Sequence

from networkx.classes.graph import Graph, _Node

__all__ = [
    "display",
    "apply_matplotlib_colors",
    "draw",
    "draw_networkx",
    "draw_networkx_nodes",
    "draw_networkx_edges",
    "draw_networkx_labels",
    "draw_networkx_edge_labels",
    "draw_bipartite",
    "draw_circular",
    "draw_kamada_kawai",
    "draw_random",
    "draw_spectral",
    "draw_spring",
    "draw_planar",
    "draw_shell",
    "draw_forceatlas2",
]

def apply_matplotlib_colors(
    G: Graph[_Node], src_attr: str, dest_attr: str, map, vmin: float | None = None, vmax: float | None = None, nodes: bool = True
) -> None: ...
def display(
    G: Graph[_Node],
    canvas=None,
    *,
    pos=...,
    node_visible: str | bool = ...,
    node_color: str = ...,
    node_size: str | float = ...,
    node_label: str | bool = ...,
    node_shape: str = ...,
    node_alpha: str = ...,
    node_border_width: str = ...,
    node_border_color: str = ...,
    edge_visible: str | bool = ...,
    edge_width: str | int = ...,
    edge_color=...,
    edge_label: str = ...,
    edge_style: str = ...,
    edge_alpha: str | float = ...,
    arrowstyle: str = ...,
    arrowsize: str | int = ...,
    edge_curvature: str = ...,
    edge_source_margin: str | int = ...,
    edge_target_margin: str | int = ...,
    hide_ticks: bool = True,
): ...
def draw(G: Graph[_Node], pos=None, ax=None, **kwds) -> None: ...
def draw_networkx(G: Graph[_Node], pos=None, arrows=None, with_labels: bool = True, **kwds) -> None: ...
def draw_networkx_nodes(
    G: Graph[_Node],
    pos,
    nodelist: Collection[Incomplete] | None = None,
    node_size: Incomplete | int = 300,
    node_color: str | Sequence[str] = "#1f78b4",
    node_shape: str = "o",
    alpha=None,
    cmap=None,
    vmin=None,
    vmax=None,
    ax=None,
    linewidths=None,
    edgecolors=None,
    label=None,
    margins=None,
    hide_ticks: bool = True,
):
    """
    Draw the nodes of the graph G.

    This draws only the nodes of the graph G.

    Parameters
    ----------
    G : graph
        A networkx graph

    pos : dictionary
        A dictionary with nodes as keys and positions as values.
        Positions should be sequences of length 2.

    ax : Matplotlib Axes object, optional
        Draw the graph in the specified Matplotlib axes.

    nodelist : list (default list(G))
        Draw only specified nodes

    node_size : scalar or array (default=300)
        Size of nodes.  If an array it must be the same length as nodelist.

    node_color : color or array of colors (default='#1f78b4')
        Node color. Can be a single color or a sequence of colors with the same
        length as nodelist. Color can be string or rgb (or rgba) tuple of
        floats from 0-1. If numeric values are specified they will be
        mapped to colors using the cmap and vmin,vmax parameters. See
        matplotlib.scatter for more details.

    node_shape :  string (default='o')
        The shape of the node.  Specification is as matplotlib.scatter
        marker, one of 'so^>v<dph8'.

    alpha : float or array of floats (default=None)
        The node transparency.  This can be a single alpha value,
        in which case it will be applied to all the nodes of color. Otherwise,
        if it is an array, the elements of alpha will be applied to the colors
        in order (cycling through alpha multiple times if necessary).

    cmap : Matplotlib colormap (default=None)
        Colormap for mapping intensities of nodes

    vmin,vmax : floats or None (default=None)
        Minimum and maximum for node colormap scaling

    linewidths : [None | scalar | sequence] (default=1.0)
        Line width of symbol border

    edgecolors : [None | scalar | sequence] (default = node_color)
        Colors of node borders. Can be a single color or a sequence of colors with the
        same length as nodelist. Color can be string or rgb (or rgba) tuple of floats
        from 0-1. If numeric values are specified they will be mapped to colors
        using the cmap and vmin,vmax parameters. See `~matplotlib.pyplot.scatter` for more details.

    label : [None | string]
        Label for legend

    margins : float or 2-tuple, optional
        Sets the padding for axis autoscaling. Increase margin to prevent
        clipping for nodes that are near the edges of an image. Values should
        be in the range ``[0, 1]``. See :meth:`matplotlib.axes.Axes.margins`
        for details. The default is `None`, which uses the Matplotlib default.

    hide_ticks : bool, optional
        Hide ticks of axes. When `True` (the default), ticks and ticklabels
        are removed from the axes. To set ticks and tick labels to the pyplot default,
        use ``hide_ticks=False``.

    Returns
    -------
    matplotlib.collections.PathCollection
        `PathCollection` of the nodes.

    Examples
    --------
    >>> G = nx.dodecahedral_graph()
    >>> nodes = nx.draw_networkx_nodes(G, pos=nx.spring_layout(G))

    Also see the NetworkX drawing examples at
    https://networkx.org/documentation/latest/auto_examples/index.html

    See Also
    --------
    draw
    draw_networkx
    draw_networkx_edges
    draw_networkx_labels
    draw_networkx_edge_labels
    """
    ...
def draw_networkx_edges(
    G: Graph[_Node],
    pos,
    edgelist=None,
    width: float = 1.0,
    edge_color: str = "k",
    style: str = "solid",
    alpha=None,
    arrowstyle=None,
    arrowsize: int = 10,
    edge_cmap=None,
    edge_vmin=None,
    edge_vmax=None,
    ax=None,
    arrows=None,
    label=None,
    node_size: Incomplete | int = 300,
    nodelist: list[Incomplete] | None = None,
    node_shape: str = "o",
    connectionstyle: str = "arc3",
    min_source_margin: int = 0,
    min_target_margin: int = 0,
    hide_ticks: bool = True,
):
    r"""
    Draw the edges of the graph G.

    This draws only the edges of the graph G.

    Parameters
    ----------
    G : graph
        A networkx graph

    pos : dictionary
        A dictionary with nodes as keys and positions as values.
        Positions should be sequences of length 2.

    edgelist : collection of edge tuples (default=G.edges())
        Draw only specified edges

    width : float or array of floats (default=1.0)
        Line width of edges

    edge_color : color or array of colors (default='k')
        Edge color. Can be a single color or a sequence of colors with the same
        length as edgelist. Color can be string or rgb (or rgba) tuple of
        floats from 0-1. If numeric values are specified they will be
        mapped to colors using the edge_cmap and edge_vmin,edge_vmax parameters.

    style : string or array of strings (default='solid')
        Edge line style e.g.: '-', '--', '-.', ':'
        or words like 'solid' or 'dashed'.
        Can be a single style or a sequence of styles with the same
        length as the edge list.
        If less styles than edges are given the styles will cycle.
        If more styles than edges are given the styles will be used sequentially
        and not be exhausted.
        Also, `(offset, onoffseq)` tuples can be used as style instead of a strings.
        (See `matplotlib.patches.FancyArrowPatch`: `linestyle`)

    alpha : float or array of floats (default=None)
        The edge transparency.  This can be a single alpha value,
        in which case it will be applied to all specified edges. Otherwise,
        if it is an array, the elements of alpha will be applied to the colors
        in order (cycling through alpha multiple times if necessary).

    edge_cmap : Matplotlib colormap, optional
        Colormap for mapping intensities of edges

    edge_vmin,edge_vmax : floats, optional
        Minimum and maximum for edge colormap scaling

    ax : Matplotlib Axes object, optional
        Draw the graph in the specified Matplotlib axes.

    arrows : bool or None, optional (default=None)
        If `None`, directed graphs draw arrowheads with
        `~matplotlib.patches.FancyArrowPatch`, while undirected graphs draw edges
        via `~matplotlib.collections.LineCollection` for speed.
        If `True`, draw arrowheads with FancyArrowPatches (bendable and stylish).
        If `False`, draw edges using LineCollection (linear and fast).

        Note: Arrowheads will be the same color as edges.

    arrowstyle : str or list of strs (default='-\|>' for directed graphs)
        For directed graphs and `arrows==True` defaults to '-\|>',
        For undirected graphs default to '-'.

        See `matplotlib.patches.ArrowStyle` for more options.

    arrowsize : int or list of ints(default=10)
        For directed graphs, choose the size of the arrow head's length and
        width. See `matplotlib.patches.FancyArrowPatch` for attribute
        `mutation_scale` for more info.

    connectionstyle : string or iterable of strings (default="arc3")
        Pass the connectionstyle parameter to create curved arc of rounding
        radius rad. For example, connectionstyle='arc3,rad=0.2'.
        See `matplotlib.patches.ConnectionStyle` and
        `matplotlib.patches.FancyArrowPatch` for more info.
        If Iterable, index indicates i'th edge key of MultiGraph

    node_size : scalar or array (default=300)
        Size of nodes. Though the nodes are not drawn with this function, the
        node size is used in determining edge positioning.

    nodelist : list, optional (default=G.nodes())
       This provides the node order for the `node_size` array (if it is an array).

    node_shape :  string (default='o')
        The marker used for nodes, used in determining edge positioning.
        Specification is as a `matplotlib.markers` marker, e.g. one of 'so^>v<dph8'.

    label : None or string
        Label for legend

    min_source_margin : int or list of ints (default=0)
        The minimum margin (gap) at the beginning of the edge at the source.

    min_target_margin : int or list of ints (default=0)
        The minimum margin (gap) at the end of the edge at the target.

    hide_ticks : bool, optional
        Hide ticks of axes. When `True` (the default), ticks and ticklabels
        are removed from the axes. To set ticks and tick labels to the pyplot default,
        use ``hide_ticks=False``.

    Returns
    -------
     matplotlib.collections.LineCollection or a list of matplotlib.patches.FancyArrowPatch
        If ``arrows=True``, a list of FancyArrowPatches is returned.
        If ``arrows=False``, a LineCollection is returned.
        If ``arrows=None`` (the default), then a LineCollection is returned if
        `G` is undirected, otherwise returns a list of FancyArrowPatches.

    Notes
    -----
    For directed graphs, arrows are drawn at the head end.  Arrows can be
    turned off with keyword arrows=False or by passing an arrowstyle without
    an arrow on the end.

    Be sure to include `node_size` as a keyword argument; arrows are
    drawn considering the size of nodes.

    Self-loops are always drawn with `~matplotlib.patches.FancyArrowPatch`
    regardless of the value of `arrows` or whether `G` is directed.
    When ``arrows=False`` or ``arrows=None`` and `G` is undirected, the
    FancyArrowPatches corresponding to the self-loops are not explicitly
    returned. They should instead be accessed via the ``Axes.patches``
    attribute (see examples).

    Examples
    --------
    >>> G = nx.dodecahedral_graph()
    >>> edges = nx.draw_networkx_edges(G, pos=nx.spring_layout(G))

    >>> G = nx.DiGraph()
    >>> G.add_edges_from([(1, 2), (1, 3), (2, 3)])
    >>> arcs = nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
    >>> alphas = [0.3, 0.4, 0.5]
    >>> for i, arc in enumerate(arcs):  # change alpha values of arcs
    ...     arc.set_alpha(alphas[i])

    The FancyArrowPatches corresponding to self-loops are not always
    returned, but can always be accessed via the ``patches`` attribute of the
    `matplotlib.Axes` object.

    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> G = nx.Graph([(0, 1), (0, 0)])  # Self-loop at node 0
    >>> edge_collection = nx.draw_networkx_edges(G, pos=nx.circular_layout(G), ax=ax)
    >>> self_loop_fap = ax.patches[0]

    Also see the NetworkX drawing examples at
    https://networkx.org/documentation/latest/auto_examples/index.html

    See Also
    --------
    draw
    draw_networkx
    draw_networkx_nodes
    draw_networkx_labels
    draw_networkx_edge_labels
    """
    ...
def draw_networkx_labels(
    G: Graph[_Node],
    pos,
    labels=None,
    font_size: int = 12,
    font_color: str = "k",
    font_family: str = "sans-serif",
    font_weight: str = "normal",
    alpha=None,
    bbox=None,
    horizontalalignment: str = "center",
    verticalalignment: str = "center",
    ax=None,
    clip_on: bool = True,
    hide_ticks: bool = True,
):
    """
    Draw node labels on the graph G.

    Parameters
    ----------
    G : graph
        A networkx graph

    pos : dictionary
        A dictionary with nodes as keys and positions as values.
        Positions should be sequences of length 2.

    labels : dictionary (default={n: n for n in G})
        Node labels in a dictionary of text labels keyed by node.
        Node-keys in labels should appear as keys in `pos`.
        If needed use: `{n:lab for n,lab in labels.items() if n in pos}`

    font_size : int or dictionary of nodes to ints (default=12)
        Font size for text labels.

    font_color : color or dictionary of nodes to colors (default='k' black)
        Font color string. Color can be string or rgb (or rgba) tuple of
        floats from 0-1.

    font_weight : string or dictionary of nodes to strings (default='normal')
        Font weight.

    font_family : string or dictionary of nodes to strings (default='sans-serif')
        Font family.

    alpha : float or None or dictionary of nodes to floats (default=None)
        The text transparency.

    bbox : Matplotlib bbox, (default is Matplotlib's ax.text default)
        Specify text box properties (e.g. shape, color etc.) for node labels.

    horizontalalignment : string or array of strings (default='center')
        Horizontal alignment {'center', 'right', 'left'}. If an array is
        specified it must be the same length as `nodelist`.

    verticalalignment : string (default='center')
        Vertical alignment {'center', 'top', 'bottom', 'baseline', 'center_baseline'}.
        If an array is specified it must be the same length as `nodelist`.

    ax : Matplotlib Axes object, optional
        Draw the graph in the specified Matplotlib axes.

    clip_on : bool (default=True)
        Turn on clipping of node labels at axis boundaries

    hide_ticks : bool, optional
        Hide ticks of axes. When `True` (the default), ticks and ticklabels
        are removed from the axes. To set ticks and tick labels to the pyplot default,
        use ``hide_ticks=False``.

    Returns
    -------
    dict
        `dict` of labels keyed on the nodes

    Examples
    --------
    >>> G = nx.dodecahedral_graph()
    >>> labels = nx.draw_networkx_labels(G, pos=nx.spring_layout(G))

    Also see the NetworkX drawing examples at
    https://networkx.org/documentation/latest/auto_examples/index.html

    See Also
    --------
    draw
    draw_networkx
    draw_networkx_nodes
    draw_networkx_edges
    draw_networkx_edge_labels
    """
    ...
def draw_networkx_edge_labels(
    G: Graph[_Node],
    pos,
    edge_labels=None,
    label_pos: float = 0.5,
    font_size: int = 10,
    font_color: str = "k",
    font_family: str = "sans-serif",
    font_weight: str = "normal",
    alpha=None,
    bbox=None,
    horizontalalignment: str = "center",
    verticalalignment: str = "center",
    ax=None,
    rotate: bool = True,
    clip_on: bool = True,
    node_size: int = 300,
    nodelist: list[Incomplete] | None = None,
    connectionstyle: str = "arc3",
    hide_ticks: bool = True,
): ...
def draw_bipartite(G: Graph[_Node], **kwargs): ...
def draw_circular(G: Graph[_Node], **kwargs) -> None: ...
def draw_kamada_kawai(G: Graph[_Node], **kwargs) -> None: ...
def draw_random(G: Graph[_Node], **kwargs) -> None: ...
def draw_spectral(G: Graph[_Node], **kwargs) -> None: ...
def draw_spring(G: Graph[_Node], **kwargs) -> None: ...
def draw_shell(G: Graph[_Node], nlist=None, **kwargs) -> None: ...
def draw_planar(G: Graph[_Node], **kwargs) -> None: ...
def draw_forceatlas2(G: Graph[_Node], **kwargs) -> None: ...
def apply_alpha(
    colors, alpha: float | Iterable[float], elem_list, cmap=None, vmin: float | None = None, vmax: float | None = None
):
    """
    Apply an alpha (or list of alphas) to the colors provided.

    Parameters
    ----------

    colors : color string or array of floats (default='r')
        Color of element. Can be a single color format string,
        or a sequence of colors with the same length as nodelist.
        If numeric values are specified they will be mapped to
        colors using the cmap and vmin,vmax parameters.  See
        matplotlib.scatter for more details.

    alpha : float or array of floats
        Alpha values for elements. This can be a single alpha value, in
        which case it will be applied to all the elements of color. Otherwise,
        if it is an array, the elements of alpha will be applied to the colors
        in order (cycling through alpha multiple times if necessary).

    elem_list : array of networkx objects
        The list of elements which are being colored. These could be nodes,
        edges or labels.

    cmap : matplotlib colormap
        Color map for use if colors is a list of floats corresponding to points
        on a color mapping.

    vmin, vmax : float
        Minimum and maximum values for normalizing colors if a colormap is used

    Returns
    -------

    rgba_colors : numpy ndarray
        Array containing RGBA format values for each of the node colours.
    """
    ...
