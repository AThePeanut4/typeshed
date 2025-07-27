"""Functions to visualize matrices of data."""

from _typeshed import Incomplete
from collections.abc import Hashable, Iterable, Mapping, Sequence
from typing import Literal, TypedDict, type_check_only
from typing_extensions import Self, TypeAlias

import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.colors import Colormap, ListedColormap, Normalize
from matplotlib.gridspec import GridSpec
from matplotlib.typing import ColorType
from numpy._typing import _ArrayLikeInt_co
from numpy.typing import ArrayLike, NDArray

from .axisgrid import Grid

# pandas._typing.ListLikeU is partially Unknown
_ListLikeU: TypeAlias = Sequence[Incomplete] | NDArray[Incomplete] | pd.Series[Incomplete] | pd.Index[Incomplete]
_ConvertibleToDataFrame: TypeAlias = (
    _ListLikeU
    | pd.DataFrame
    | dict[Incomplete, Incomplete]
    | Iterable[_ListLikeU | tuple[Hashable, _ListLikeU] | dict[Incomplete, Incomplete]]
    | None
)
_FlatOrNestedSequenceOfColors: TypeAlias = (
    Sequence[ColorType]
    | Sequence[Iterable[ColorType]]
    | NDArray[Incomplete]
    | pd.Index[Incomplete]
    | pd.Series[Incomplete]
    | pd.DataFrame
)

__all__ = ["heatmap", "clustermap"]

def heatmap(
    data: pd.DataFrame | ArrayLike,
    *,
    vmin: float | None = None,
    vmax: float | None = None,
    cmap: str | list[ColorType] | Colormap | None = None,
    center: float | None = None,
    robust: bool = False,
    annot: bool | ArrayLike | None = None,
    fmt: str = ".2g",
    annot_kws: dict[str, Incomplete] | None = None,
    linewidths: float = 0,
    linecolor: ColorType = "white",
    cbar: bool = True,
    cbar_kws: dict[str, Incomplete] | None = None,
    cbar_ax: Axes | None = None,
    square: bool = False,
    xticklabels: Literal["auto"] | bool | int | Sequence[str] = "auto",
    yticklabels: Literal["auto"] | bool | int | Sequence[str] = "auto",
    mask: NDArray[np.bool_] | pd.DataFrame | None = None,
    ax: Axes | None = None,
    # Kwargs below passed to matplotlib.axes.Axes.pcolormesh
    alpha: float | None = None,
    norm: str | Normalize | None = None,
    shading: Literal["flat", "nearest", "gouraud", "auto"] | None = None,
    antialiased: bool = False,
    **kwargs,
) -> Axes: ...
@type_check_only
class _Dendogram(TypedDict):
    icoord: list[list[float]]
    dcoord: list[list[float]]
    ivl: list[str]
    leaves: list[int]
    color_list: list[str]
    leaves_color_list: list[str]

class _DendrogramPlotter:
    """Object for drawing tree of similarities between data rows/columns"""
    axis: int
    array: NDArray[np.floating]
    data: pd.DataFrame
    shape: tuple[int, int]
    metric: str
    method: str
    label: bool
    rotate: bool
    linkage: NDArray[np.floating]
    dendrogram: _Dendogram
    xticks: list[float] | NDArray[np.floating]
    yticks: list[float] | NDArray[np.floating]
    xticklabels: list[str]
    yticklabels: list[str]
    ylabel: str
    xlabel: str
    dependent_coord: list[list[float]]
    independent_coord: list[list[float]]
    def __init__(
        self,
        data: pd.DataFrame,
        linkage: NDArray[np.floating] | None,
        metric: str,
        method: str,
        axis: int,
        label: bool,
        rotate: bool,
    ) -> None: ...
    @property
    def calculated_linkage(self) -> NDArray[np.float64]: ...
    def calculate_dendrogram(self) -> _Dendogram: ...
    @property
    def reordered_ind(self) -> list[int]:
        """Indices of the matrix, reordered by the dendrogram"""
        ...
    def plot(self, ax: Axes, tree_kws: dict[str, Incomplete]) -> Self:
        """
        Plots a dendrogram of the similarities between data on the axes

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes object upon which the dendrogram is plotted
        """
        ...

def dendrogram(
    data: pd.DataFrame,
    *,
    linkage: NDArray[np.floating] | None = None,
    axis: int = 1,
    label: bool = True,
    metric: str = "euclidean",
    method: str = "average",
    rotate: bool = False,
    tree_kws: dict[str, Incomplete] | None = None,
    ax: Axes | None = None,
) -> _DendrogramPlotter:
    """
    Draw a tree diagram of relationships within a matrix

    Parameters
    ----------
    data : pandas.DataFrame
        Rectangular data
    linkage : numpy.array, optional
        Linkage matrix
    axis : int, optional
        Which axis to use to calculate linkage. 0 is rows, 1 is columns.
    label : bool, optional
        If True, label the dendrogram at leaves with column or row names
    metric : str, optional
        Distance metric. Anything valid for scipy.spatial.distance.pdist
    method : str, optional
        Linkage method to use. Anything valid for
        scipy.cluster.hierarchy.linkage
    rotate : bool, optional
        When plotting the matrix, whether to rotate it 90 degrees
        counter-clockwise, so the leaves face right
    tree_kws : dict, optional
        Keyword arguments for the ``matplotlib.collections.LineCollection``
        that is used for plotting the lines of the dendrogram tree.
    ax : matplotlib axis, optional
        Axis to plot on, otherwise uses current axis

    Returns
    -------
    dendrogramplotter : _DendrogramPlotter
        A Dendrogram plotter object.

    Notes
    -----
    Access the reordered dendrogram indices with
    dendrogramplotter.reordered_ind
    """
    ...

class ClusterGrid(Grid):
    data: pd.DataFrame
    data2d: pd.DataFrame
    mask: pd.DataFrame
    row_colors: list[list[tuple[float, float, float]]] | None
    row_color_labels: list[str] | None
    col_colors: list[list[tuple[float, float, float]]] | None
    col_color_labels: list[str] | None
    gs: GridSpec
    ax_row_dendrogram: Axes
    ax_col_dendrogram: Axes
    ax_row_colors: Axes | None
    ax_col_colors: Axes | None
    ax_heatmap: Axes
    ax_cbar: Axes | None
    cax: Axes | None
    cbar_pos: tuple[float, float, float, float] | None
    dendrogram_row: _DendrogramPlotter | None
    dendrogram_col: _DendrogramPlotter | None
    def __init__(
        self,
        data: _ConvertibleToDataFrame,
        pivot_kws: Mapping[str, Incomplete] | None = None,
        z_score: int | None = None,
        standard_scale: int | None = None,
        figsize: tuple[float, float] | None = None,
        row_colors: _FlatOrNestedSequenceOfColors | None = None,
        col_colors: _FlatOrNestedSequenceOfColors | None = None,
        mask: NDArray[np.bool_] | pd.DataFrame | None = None,
        dendrogram_ratio: float | tuple[float, float] | None = None,
        colors_ratio: float | tuple[float, float] | None = None,
        cbar_pos: tuple[float, float, float, float] | None = None,
    ) -> None:
        """Grid object for organizing clustered heatmap input on to axes"""
        ...
    def format_data(
        self,
        data: pd.DataFrame,
        pivot_kws: Mapping[str, Incomplete] | None,
        z_score: int | None = None,
        standard_scale: int | None = None,
    ) -> pd.DataFrame: ...
    @staticmethod
    def z_score(data2d: pd.DataFrame, axis: int = 1) -> pd.DataFrame: ...
    @staticmethod
    def standard_scale(data2d: pd.DataFrame, axis: int = 1) -> pd.DataFrame: ...
    def dim_ratios(self, colors: ArrayLike | None, dendrogram_ratio: float, colors_ratio: float) -> list[float]: ...
    @staticmethod
    def color_list_to_matrix_and_cmap(
        colors: _FlatOrNestedSequenceOfColors, ind: _ArrayLikeInt_co, axis: int = 0
    ) -> tuple[NDArray[np.int_], ListedColormap]: ...
    def plot_dendrograms(
        self,
        row_cluster: bool,
        col_cluster: bool,
        metric: str,
        method: str,
        row_linkage: NDArray[np.floating] | None,
        col_linkage: NDArray[np.floating] | None,
        tree_kws: dict[str, Incomplete] | None,
    ) -> None: ...
    def plot_colors(self, xind: _ArrayLikeInt_co, yind: _ArrayLikeInt_co, **kws) -> None:
        """
        Plots color labels between the dendrogram and the heatmap

        Parameters
        ----------
        heatmap_kws : dict
            Keyword arguments heatmap
        """
        ...
    def plot_matrix(self, colorbar_kws: dict[str, Incomplete], xind: _ArrayLikeInt_co, yind: _ArrayLikeInt_co, **kws) -> None: ...
    def plot(
        self,
        metric: str,
        method: str,
        colorbar_kws: dict[str, Incomplete] | None,
        row_cluster: bool,
        col_cluster: bool,
        row_linkage: NDArray[np.floating] | None,
        col_linkage: NDArray[np.floating] | None,
        tree_kws: dict[str, Incomplete] | None,
        **kws,
    ) -> Self: ...

def clustermap(
    data: _ConvertibleToDataFrame,
    *,
    pivot_kws: dict[str, Incomplete] | None = None,
    method: str = "average",
    metric: str = "euclidean",
    z_score: int | None = None,
    standard_scale: int | None = None,
    figsize: tuple[float, float] | None = (10, 10),
    cbar_kws: dict[str, Incomplete] | None = None,
    row_cluster: bool = True,
    col_cluster: bool = True,
    row_linkage: NDArray[np.floating] | None = None,
    col_linkage: NDArray[np.floating] | None = None,
    row_colors: _FlatOrNestedSequenceOfColors | None = None,
    col_colors: _FlatOrNestedSequenceOfColors | None = None,
    mask: NDArray[np.bool_] | pd.DataFrame | None = None,
    dendrogram_ratio: float | tuple[float, float] = 0.2,
    colors_ratio: float | tuple[float, float] = 0.03,
    cbar_pos: tuple[float, float, float, float] | None = (0.02, 0.8, 0.05, 0.18),
    tree_kws: dict[str, Incomplete] | None = None,
    **kwargs,
) -> ClusterGrid:
    """
    Plot a matrix dataset as a hierarchically-clustered heatmap.

    This function requires scipy to be available.

    Parameters
    ----------
    data : 2D array-like
        Rectangular data for clustering. Cannot contain NAs.
    pivot_kws : dict, optional
        If `data` is a tidy dataframe, can provide keyword arguments for
        pivot to create a rectangular dataframe.
    method : str, optional
        Linkage method to use for calculating clusters. See
        :func:`scipy.cluster.hierarchy.linkage` documentation for more
        information.
    metric : str, optional
        Distance metric to use for the data. See
        :func:`scipy.spatial.distance.pdist` documentation for more options.
        To use different metrics (or methods) for rows and columns, you may
        construct each linkage matrix yourself and provide them as
        `{row,col}_linkage`.
    z_score : int or None, optional
        Either 0 (rows) or 1 (columns). Whether or not to calculate z-scores
        for the rows or the columns. Z scores are: z = (x - mean)/std, so
        values in each row (column) will get the mean of the row (column)
        subtracted, then divided by the standard deviation of the row (column).
        This ensures that each row (column) has mean of 0 and variance of 1.
    standard_scale : int or None, optional
        Either 0 (rows) or 1 (columns). Whether or not to standardize that
        dimension, meaning for each row or column, subtract the minimum and
        divide each by its maximum.
    figsize : tuple of (width, height), optional
        Overall size of the figure.
    cbar_kws : dict, optional
        Keyword arguments to pass to `cbar_kws` in :func:`heatmap`, e.g. to
        add a label to the colorbar.
    {row,col}_cluster : bool, optional
        If ``True``, cluster the {rows, columns}.
    {row,col}_linkage : :class:`numpy.ndarray`, optional
        Precomputed linkage matrix for the rows or columns. See
        :func:`scipy.cluster.hierarchy.linkage` for specific formats.
    {row,col}_colors : list-like or pandas DataFrame/Series, optional
        List of colors to label for either the rows or columns. Useful to evaluate
        whether samples within a group are clustered together. Can use nested lists or
        DataFrame for multiple color levels of labeling. If given as a
        :class:`pandas.DataFrame` or :class:`pandas.Series`, labels for the colors are
        extracted from the DataFrames column names or from the name of the Series.
        DataFrame/Series colors are also matched to the data by their index, ensuring
        colors are drawn in the correct order.
    mask : bool array or DataFrame, optional
        If passed, data will not be shown in cells where `mask` is True.
        Cells with missing values are automatically masked. Only used for
        visualizing, not for calculating.
    {dendrogram,colors}_ratio : float, or pair of floats, optional
        Proportion of the figure size devoted to the two marginal elements. If
        a pair is given, they correspond to (row, col) ratios.
    cbar_pos : tuple of (left, bottom, width, height), optional
        Position of the colorbar axes in the figure. Setting to ``None`` will
        disable the colorbar.
    tree_kws : dict, optional
        Parameters for the :class:`matplotlib.collections.LineCollection`
        that is used to plot the lines of the dendrogram tree.
    kwargs : other keyword arguments
        All other keyword arguments are passed to :func:`heatmap`.

    Returns
    -------
    :class:`ClusterGrid`
        A :class:`ClusterGrid` instance.

    See Also
    --------
    heatmap : Plot rectangular data as a color-encoded matrix.

    Notes
    -----
    The returned object has a ``savefig`` method that should be used if you
    want to save the figure object without clipping the dendrograms.

    To access the reordered row indices, use:
    ``clustergrid.dendrogram_row.reordered_ind``

    Column indices, use:
    ``clustergrid.dendrogram_col.reordered_ind``

    Examples
    --------

    .. include:: ../docstrings/clustermap.rst
    """
    ...
