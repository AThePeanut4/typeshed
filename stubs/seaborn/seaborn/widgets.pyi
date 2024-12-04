from typing import Literal, overload

from matplotlib.colors import LinearSegmentedColormap

__all__ = [
    "choose_colorbrewer_palette",
    "choose_cubehelix_palette",
    "choose_dark_palette",
    "choose_light_palette",
    "choose_diverging_palette",
]

@overload
def choose_colorbrewer_palette(
    data_type: Literal["sequential", "diverging", "qualitative"], as_cmap: Literal[True]
) -> LinearSegmentedColormap:
    """
    Select a palette from the ColorBrewer set.

    These palettes are built into matplotlib and can be used by name in
    many seaborn functions, or by passing the object returned by this function.

    Parameters
    ----------
    data_type : {'sequential', 'diverging', 'qualitative'}
        This describes the kind of data you want to visualize. See the seaborn
        color palette docs for more information about how to choose this value.
        Note that you can pass substrings (e.g. 'q' for 'qualitative.

    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.
    diverging_palette : Create a diverging palette from selected colors.
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_colorbrewer_palette(
    data_type: Literal["sequential", "diverging", "qualitative"], as_cmap: Literal[False] = False
) -> list[tuple[float, float, float]]:
    """
    Select a palette from the ColorBrewer set.

    These palettes are built into matplotlib and can be used by name in
    many seaborn functions, or by passing the object returned by this function.

    Parameters
    ----------
    data_type : {'sequential', 'diverging', 'qualitative'}
        This describes the kind of data you want to visualize. See the seaborn
        color palette docs for more information about how to choose this value.
        Note that you can pass substrings (e.g. 'q' for 'qualitative.

    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.
    diverging_palette : Create a diverging palette from selected colors.
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_dark_palette(input: str = "husl", *, as_cmap: Literal[True]) -> LinearSegmentedColormap:
    """
    Launch an interactive widget to create a dark sequential palette.

    This corresponds with the :func:`dark_palette` function. This kind
    of palette is good for data that range between relatively uninteresting
    low values and interesting high values.

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    input : {'husl', 'hls', 'rgb'}
        Color space for defining the seed value. Note that the default is
        different than the default input for :func:`dark_palette`.
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_dark_palette(input: str = "husl", as_cmap: Literal[False] = False) -> list[tuple[float, float, float]]:
    """
    Launch an interactive widget to create a dark sequential palette.

    This corresponds with the :func:`dark_palette` function. This kind
    of palette is good for data that range between relatively uninteresting
    low values and interesting high values.

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    input : {'husl', 'hls', 'rgb'}
        Color space for defining the seed value. Note that the default is
        different than the default input for :func:`dark_palette`.
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_light_palette(input: str = "husl", *, as_cmap: Literal[True]) -> LinearSegmentedColormap:
    """
    Launch an interactive widget to create a light sequential palette.

    This corresponds with the :func:`light_palette` function. This kind
    of palette is good for data that range between relatively uninteresting
    low values and interesting high values.

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    input : {'husl', 'hls', 'rgb'}
        Color space for defining the seed value. Note that the default is
        different than the default input for :func:`light_palette`.
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    light_palette : Create a sequential palette with bright low values.
    dark_palette : Create a sequential palette with dark low values.
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_light_palette(input: str = "husl", as_cmap: Literal[False] = False) -> list[tuple[float, float, float]]:
    """
    Launch an interactive widget to create a light sequential palette.

    This corresponds with the :func:`light_palette` function. This kind
    of palette is good for data that range between relatively uninteresting
    low values and interesting high values.

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    input : {'husl', 'hls', 'rgb'}
        Color space for defining the seed value. Note that the default is
        different than the default input for :func:`light_palette`.
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    light_palette : Create a sequential palette with bright low values.
    dark_palette : Create a sequential palette with dark low values.
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_diverging_palette(as_cmap: Literal[True]) -> LinearSegmentedColormap:
    """
    Launch an interactive widget to choose a diverging color palette.

    This corresponds with the :func:`diverging_palette` function. This kind
    of palette is good for data that range between interesting low values
    and interesting high values with a meaningful midpoint. (For example,
    change scores relative to some baseline value).

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    diverging_palette : Create a diverging color palette or colormap.
    choose_colorbrewer_palette : Interactively choose palettes from the
                                 colorbrewer set, including diverging palettes.
    """
    ...
@overload
def choose_diverging_palette(as_cmap: Literal[False] = False) -> list[tuple[float, float, float]]:
    """
    Launch an interactive widget to choose a diverging color palette.

    This corresponds with the :func:`diverging_palette` function. This kind
    of palette is good for data that range between interesting low values
    and interesting high values with a meaningful midpoint. (For example,
    change scores relative to some baseline value).

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    diverging_palette : Create a diverging color palette or colormap.
    choose_colorbrewer_palette : Interactively choose palettes from the
                                 colorbrewer set, including diverging palettes.
    """
    ...
@overload
def choose_cubehelix_palette(as_cmap: Literal[True]) -> LinearSegmentedColormap:
    """
    Launch an interactive widget to create a sequential cubehelix palette.

    This corresponds with the :func:`cubehelix_palette` function. This kind
    of palette is good for data that range between relatively uninteresting
    low values and interesting high values. The cubehelix system allows the
    palette to have more hue variance across the range, which can be helpful
    for distinguishing a wider range of values.

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
@overload
def choose_cubehelix_palette(as_cmap: Literal[False] = False) -> list[tuple[float, float, float]]:
    """
    Launch an interactive widget to create a sequential cubehelix palette.

    This corresponds with the :func:`cubehelix_palette` function. This kind
    of palette is good for data that range between relatively uninteresting
    low values and interesting high values. The cubehelix system allows the
    palette to have more hue variance across the range, which can be helpful
    for distinguishing a wider range of values.

    Requires IPython 2+ and must be used in the notebook.

    Parameters
    ----------
    as_cmap : bool
        If True, the return value is a matplotlib colormap rather than a
        list of discrete colors.

    Returns
    -------
    pal or cmap : list of colors or matplotlib colormap
        Object that can be passed to plotting functions.

    See Also
    --------
    cubehelix_palette : Create a sequential palette or colormap using the
                        cubehelix system.
    """
    ...
