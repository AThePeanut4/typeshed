from collections.abc import Iterable, Sequence
from typing import Literal, TypeVar, overload
from typing_extensions import Self, TypeAlias

from matplotlib.colors import Colormap, LinearSegmentedColormap, ListedColormap
from matplotlib.typing import ColorType

__all__ = [
    "color_palette",
    "hls_palette",
    "husl_palette",
    "mpl_palette",
    "dark_palette",
    "light_palette",
    "diverging_palette",
    "blend_palette",
    "xkcd_palette",
    "crayon_palette",
    "cubehelix_palette",
    "set_color_codes",
]

_ColorT = TypeVar("_ColorT", bound=ColorType)

SEABORN_PALETTES: dict[str, list[str]]
MPL_QUAL_PALS: dict[str, int]
QUAL_PALETTE_SIZES: dict[str, int]
QUAL_PALETTES: list[str]

class _ColorPalette(list[_ColorT]):
    """Set the color palette in a with statement, otherwise be a list."""
    def __enter__(self) -> Self:
        """Open the context."""
        ...
    def __exit__(self, *args: object) -> None:
        """Close the context."""
        ...
    def as_hex(self) -> _ColorPalette[str]:
        """Return a color palette with hex codes instead of RGB values."""
        ...

_RGBColorPalette: TypeAlias = _ColorPalette[tuple[float, float, float]]
_SeabornPaletteName: TypeAlias = Literal[
    "deep", "deep6", "muted", "muted6", "pastel", "pastel6", "bright", "bright6", "dark", "dark6", "colorblind", "colorblind6"
]

@overload
def color_palette(  # type: ignore[overload-overlap]
    palette: _SeabornPaletteName | None = None, n_colors: int | None = None, desat: float | None = None, *, as_cmap: Literal[True]
) -> list[str]:
    """
    Return a list of colors or continuous colormap defining a palette.

    Possible ``palette`` values include:
        - Name of a seaborn palette (deep, muted, bright, pastel, dark, colorblind)
        - Name of matplotlib colormap
        - 'husl' or 'hls'
        - 'ch:<cubehelix arguments>'
        - 'light:<color>', 'dark:<color>', 'blend:<color>,<color>',
        - A sequence of colors in any format matplotlib accepts

    Calling this function with ``palette=None`` will return the current
    matplotlib color cycle.

    This function can also be used in a ``with`` statement to temporarily
    set the color cycle for a plot or set of plots.

    See the :ref:`tutorial <palette_tutorial>` for more information.

    Parameters
    ----------
    palette : None, string, or sequence, optional
        Name of palette or None to return current palette. If a sequence, input
        colors are used but possibly cycled and desaturated.
    n_colors : int, optional
        Number of colors in the palette. If ``None``, the default will depend
        on how ``palette`` is specified. Named palettes default to 6 colors,
        but grabbing the current palette or passing in a list of colors will
        not change the number of colors unless this is specified. Asking for
        more colors than exist in the palette will cause it to cycle. Ignored
        when ``as_cmap`` is True.
    desat : float, optional
        Proportion to desaturate each color by.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    set_palette : Set the default color cycle for all plots.
    set_color_codes : Reassign color codes like ``"b"``, ``"g"``, etc. to
                      colors from one of the seaborn palettes.

    Examples
    --------

    .. include:: ../docstrings/color_palette.rst
    """
    ...
@overload
def color_palette(
    palette: str | Sequence[ColorType], n_colors: int | None = None, desat: float | None = None, *, as_cmap: Literal[True]
) -> Colormap:
    """
    Return a list of colors or continuous colormap defining a palette.

    Possible ``palette`` values include:
        - Name of a seaborn palette (deep, muted, bright, pastel, dark, colorblind)
        - Name of matplotlib colormap
        - 'husl' or 'hls'
        - 'ch:<cubehelix arguments>'
        - 'light:<color>', 'dark:<color>', 'blend:<color>,<color>',
        - A sequence of colors in any format matplotlib accepts

    Calling this function with ``palette=None`` will return the current
    matplotlib color cycle.

    This function can also be used in a ``with`` statement to temporarily
    set the color cycle for a plot or set of plots.

    See the :ref:`tutorial <palette_tutorial>` for more information.

    Parameters
    ----------
    palette : None, string, or sequence, optional
        Name of palette or None to return current palette. If a sequence, input
        colors are used but possibly cycled and desaturated.
    n_colors : int, optional
        Number of colors in the palette. If ``None``, the default will depend
        on how ``palette`` is specified. Named palettes default to 6 colors,
        but grabbing the current palette or passing in a list of colors will
        not change the number of colors unless this is specified. Asking for
        more colors than exist in the palette will cause it to cycle. Ignored
        when ``as_cmap`` is True.
    desat : float, optional
        Proportion to desaturate each color by.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    set_palette : Set the default color cycle for all plots.
    set_color_codes : Reassign color codes like ``"b"``, ``"g"``, etc. to
                      colors from one of the seaborn palettes.

    Examples
    --------

    .. include:: ../docstrings/color_palette.rst
    """
    ...
@overload
def color_palette(
    palette: str | Sequence[ColorType] | None = None,
    n_colors: int | None = None,
    desat: float | None = None,
    as_cmap: Literal[False] = False,
) -> _RGBColorPalette:
    """
    Return a list of colors or continuous colormap defining a palette.

    Possible ``palette`` values include:
        - Name of a seaborn palette (deep, muted, bright, pastel, dark, colorblind)
        - Name of matplotlib colormap
        - 'husl' or 'hls'
        - 'ch:<cubehelix arguments>'
        - 'light:<color>', 'dark:<color>', 'blend:<color>,<color>',
        - A sequence of colors in any format matplotlib accepts

    Calling this function with ``palette=None`` will return the current
    matplotlib color cycle.

    This function can also be used in a ``with`` statement to temporarily
    set the color cycle for a plot or set of plots.

    See the :ref:`tutorial <palette_tutorial>` for more information.

    Parameters
    ----------
    palette : None, string, or sequence, optional
        Name of palette or None to return current palette. If a sequence, input
        colors are used but possibly cycled and desaturated.
    n_colors : int, optional
        Number of colors in the palette. If ``None``, the default will depend
        on how ``palette`` is specified. Named palettes default to 6 colors,
        but grabbing the current palette or passing in a list of colors will
        not change the number of colors unless this is specified. Asking for
        more colors than exist in the palette will cause it to cycle. Ignored
        when ``as_cmap`` is True.
    desat : float, optional
        Proportion to desaturate each color by.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    set_palette : Set the default color cycle for all plots.
    set_color_codes : Reassign color codes like ``"b"``, ``"g"``, etc. to
                      colors from one of the seaborn palettes.

    Examples
    --------

    .. include:: ../docstrings/color_palette.rst
    """
    ...
@overload
def hls_palette(
    n_colors: int = 6, h: float = 0.01, l: float = 0.6, s: float = 0.65, *, as_cmap: Literal[True]
) -> ListedColormap:
    """
    Return hues with constant lightness and saturation in the HLS system.

    The hues are evenly sampled along a circular path. The resulting palette will be
    appropriate for categorical or cyclical data.

    The `h`, `l`, and `s` values should be between 0 and 1.

    .. note::
        While the separation of the resulting colors will be mathematically
        constant, the HLS system does not construct a perceptually-uniform space,
        so their apparent intensity will vary.

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    h : float
        The value of the first hue.
    l : float
        The lightness value.
    s : float
        The saturation intensity.
    as_cmap : bool
        If True, return a matplotlib colormap object.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    husl_palette : Make a palette using evenly spaced hues in the HUSL system.

    Examples
    --------
    .. include:: ../docstrings/hls_palette.rst
    """
    ...
@overload
def hls_palette(
    n_colors: int = 6, h: float = 0.01, l: float = 0.6, s: float = 0.65, as_cmap: Literal[False] = False
) -> _RGBColorPalette:
    """
    Return hues with constant lightness and saturation in the HLS system.

    The hues are evenly sampled along a circular path. The resulting palette will be
    appropriate for categorical or cyclical data.

    The `h`, `l`, and `s` values should be between 0 and 1.

    .. note::
        While the separation of the resulting colors will be mathematically
        constant, the HLS system does not construct a perceptually-uniform space,
        so their apparent intensity will vary.

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    h : float
        The value of the first hue.
    l : float
        The lightness value.
    s : float
        The saturation intensity.
    as_cmap : bool
        If True, return a matplotlib colormap object.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    husl_palette : Make a palette using evenly spaced hues in the HUSL system.

    Examples
    --------
    .. include:: ../docstrings/hls_palette.rst
    """
    ...
@overload
def husl_palette(
    n_colors: int = 6, h: float = 0.01, s: float = 0.9, l: float = 0.65, *, as_cmap: Literal[True]
) -> ListedColormap:
    """
    Return hues with constant lightness and saturation in the HUSL system.

    The hues are evenly sampled along a circular path. The resulting palette will be
    appropriate for categorical or cyclical data.

    The `h`, `l`, and `s` values should be between 0 and 1.

    This function is similar to :func:`hls_palette`, but it uses a nonlinear color
    space that is more perceptually uniform.

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    h : float
        The value of the first hue.
    l : float
        The lightness value.
    s : float
        The saturation intensity.
    as_cmap : bool
        If True, return a matplotlib colormap object.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    hls_palette : Make a palette using evenly spaced hues in the HSL system.

    Examples
    --------
    .. include:: ../docstrings/husl_palette.rst
    """
    ...
@overload
def husl_palette(
    n_colors: int = 6, h: float = 0.01, s: float = 0.9, l: float = 0.65, as_cmap: Literal[False] = False
) -> _RGBColorPalette:
    """
    Return hues with constant lightness and saturation in the HUSL system.

    The hues are evenly sampled along a circular path. The resulting palette will be
    appropriate for categorical or cyclical data.

    The `h`, `l`, and `s` values should be between 0 and 1.

    This function is similar to :func:`hls_palette`, but it uses a nonlinear color
    space that is more perceptually uniform.

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    h : float
        The value of the first hue.
    l : float
        The lightness value.
    s : float
        The saturation intensity.
    as_cmap : bool
        If True, return a matplotlib colormap object.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    hls_palette : Make a palette using evenly spaced hues in the HSL system.

    Examples
    --------
    .. include:: ../docstrings/husl_palette.rst
    """
    ...
@overload
def mpl_palette(name: str, n_colors: int = 6, *, as_cmap: Literal[True]) -> LinearSegmentedColormap:
    """
    Return a palette or colormap from the matplotlib registry.

    For continuous palettes, evenly-spaced discrete samples are chosen while
    excluding the minimum and maximum value in the colormap to provide better
    contrast at the extremes.

    For qualitative palettes (e.g. those from colorbrewer), exact values are
    indexed (rather than interpolated), but fewer than `n_colors` can be returned
    if the palette does not define that many.

    Parameters
    ----------
    name : string
        Name of the palette. This should be a named matplotlib colormap.
    n_colors : int
        Number of discrete colors in the palette.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    Examples
    --------
    .. include:: ../docstrings/mpl_palette.rst
    """
    ...
@overload
def mpl_palette(name: str, n_colors: int = 6, as_cmap: Literal[False] = False) -> _RGBColorPalette:
    """
    Return a palette or colormap from the matplotlib registry.

    For continuous palettes, evenly-spaced discrete samples are chosen while
    excluding the minimum and maximum value in the colormap to provide better
    contrast at the extremes.

    For qualitative palettes (e.g. those from colorbrewer), exact values are
    indexed (rather than interpolated), but fewer than `n_colors` can be returned
    if the palette does not define that many.

    Parameters
    ----------
    name : string
        Name of the palette. This should be a named matplotlib colormap.
    n_colors : int
        Number of discrete colors in the palette.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    Examples
    --------
    .. include:: ../docstrings/mpl_palette.rst
    """
    ...
@overload
def dark_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, *, as_cmap: Literal[True], input: str = "rgb"
) -> LinearSegmentedColormap:
    """
    Make a sequential palette that blends from dark to ``color``.

    This kind of palette is good for data that range between relatively
    uninteresting low values and interesting high values.

    The ``color`` parameter can be specified in a number of ways, including
    all options for defining a color in matplotlib and several additional
    color spaces that are handled by seaborn. You can also use the database
    of named colors from the XKCD color survey.

    If you are using the IPython notebook, you can also choose this palette
    interactively with the :func:`choose_dark_palette` function.

    Parameters
    ----------
    color : base color for high values
        hex, rgb-tuple, or html color name
    n_colors : int, optional
        number of colors in the palette
    reverse : bool, optional
        if True, reverse the direction of the blend
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.
    input : {'rgb', 'hls', 'husl', xkcd'}
        Color space to interpret the input color. The first three options
        apply to tuple inputs and the latter applies to string inputs.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    light_palette : Create a sequential palette with bright low values.
    diverging_palette : Create a diverging palette with two colors.

    Examples
    --------
    .. include:: ../docstrings/dark_palette.rst
    """
    ...
@overload
def dark_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, as_cmap: Literal[False] = False, input: str = "rgb"
) -> _RGBColorPalette:
    """
    Make a sequential palette that blends from dark to ``color``.

    This kind of palette is good for data that range between relatively
    uninteresting low values and interesting high values.

    The ``color`` parameter can be specified in a number of ways, including
    all options for defining a color in matplotlib and several additional
    color spaces that are handled by seaborn. You can also use the database
    of named colors from the XKCD color survey.

    If you are using the IPython notebook, you can also choose this palette
    interactively with the :func:`choose_dark_palette` function.

    Parameters
    ----------
    color : base color for high values
        hex, rgb-tuple, or html color name
    n_colors : int, optional
        number of colors in the palette
    reverse : bool, optional
        if True, reverse the direction of the blend
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.
    input : {'rgb', 'hls', 'husl', xkcd'}
        Color space to interpret the input color. The first three options
        apply to tuple inputs and the latter applies to string inputs.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    light_palette : Create a sequential palette with bright low values.
    diverging_palette : Create a diverging palette with two colors.

    Examples
    --------
    .. include:: ../docstrings/dark_palette.rst
    """
    ...
@overload
def light_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, *, as_cmap: Literal[True], input: str = "rgb"
) -> LinearSegmentedColormap:
    """
    Make a sequential palette that blends from light to ``color``.

    The ``color`` parameter can be specified in a number of ways, including
    all options for defining a color in matplotlib and several additional
    color spaces that are handled by seaborn. You can also use the database
    of named colors from the XKCD color survey.

    If you are using a Jupyter notebook, you can also choose this palette
    interactively with the :func:`choose_light_palette` function.

    Parameters
    ----------
    color : base color for high values
        hex code, html color name, or tuple in `input` space.
    n_colors : int, optional
        number of colors in the palette
    reverse : bool, optional
        if True, reverse the direction of the blend
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.
    input : {'rgb', 'hls', 'husl', xkcd'}
        Color space to interpret the input color. The first three options
        apply to tuple inputs and the latter applies to string inputs.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    dark_palette : Create a sequential palette with dark low values.
    diverging_palette : Create a diverging palette with two colors.

    Examples
    --------
    .. include:: ../docstrings/light_palette.rst
    """
    ...
@overload
def light_palette(
    color: ColorType, n_colors: int = 6, reverse: bool = False, as_cmap: Literal[False] = False, input: str = "rgb"
) -> _RGBColorPalette:
    """
    Make a sequential palette that blends from light to ``color``.

    The ``color`` parameter can be specified in a number of ways, including
    all options for defining a color in matplotlib and several additional
    color spaces that are handled by seaborn. You can also use the database
    of named colors from the XKCD color survey.

    If you are using a Jupyter notebook, you can also choose this palette
    interactively with the :func:`choose_light_palette` function.

    Parameters
    ----------
    color : base color for high values
        hex code, html color name, or tuple in `input` space.
    n_colors : int, optional
        number of colors in the palette
    reverse : bool, optional
        if True, reverse the direction of the blend
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.
    input : {'rgb', 'hls', 'husl', xkcd'}
        Color space to interpret the input color. The first three options
        apply to tuple inputs and the latter applies to string inputs.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    dark_palette : Create a sequential palette with dark low values.
    diverging_palette : Create a diverging palette with two colors.

    Examples
    --------
    .. include:: ../docstrings/light_palette.rst
    """
    ...
@overload
def diverging_palette(
    h_neg: float,
    h_pos: float,
    s: float = 75,
    l: float = 50,
    sep: int = 1,
    n: int = 6,
    center: Literal["light", "dark"] = "light",
    *,
    as_cmap: Literal[True],
) -> LinearSegmentedColormap:
    """
    Make a diverging palette between two HUSL colors.

    If you are using the IPython notebook, you can also choose this palette
    interactively with the :func:`choose_diverging_palette` function.

    Parameters
    ----------
    h_neg, h_pos : float in [0, 359]
        Anchor hues for negative and positive extents of the map.
    s : float in [0, 100], optional
        Anchor saturation for both extents of the map.
    l : float in [0, 100], optional
        Anchor lightness for both extents of the map.
    sep : int, optional
        Size of the intermediate region.
    n : int, optional
        Number of colors in the palette (if not returning a cmap)
    center : {"light", "dark"}, optional
        Whether the center of the palette is light or dark
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    dark_palette : Create a sequential palette with dark values.
    light_palette : Create a sequential palette with light values.

    Examples
    --------
    .. include: ../docstrings/diverging_palette.rst
    """
    ...
@overload
def diverging_palette(
    h_neg: float,
    h_pos: float,
    s: float = 75,
    l: float = 50,
    sep: int = 1,
    n: int = 6,
    center: Literal["light", "dark"] = "light",
    as_cmap: Literal[False] = False,
) -> _RGBColorPalette:
    """
    Make a diverging palette between two HUSL colors.

    If you are using the IPython notebook, you can also choose this palette
    interactively with the :func:`choose_diverging_palette` function.

    Parameters
    ----------
    h_neg, h_pos : float in [0, 359]
        Anchor hues for negative and positive extents of the map.
    s : float in [0, 100], optional
        Anchor saturation for both extents of the map.
    l : float in [0, 100], optional
        Anchor lightness for both extents of the map.
    sep : int, optional
        Size of the intermediate region.
    n : int, optional
        Number of colors in the palette (if not returning a cmap)
    center : {"light", "dark"}, optional
        Whether the center of the palette is light or dark
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    dark_palette : Create a sequential palette with dark values.
    light_palette : Create a sequential palette with light values.

    Examples
    --------
    .. include: ../docstrings/diverging_palette.rst
    """
    ...
@overload
def blend_palette(
    colors: Iterable[ColorType], n_colors: int = 6, *, as_cmap: Literal[True], input: str = "rgb"
) -> LinearSegmentedColormap:
    """
    Make a palette that blends between a list of colors.

    Parameters
    ----------
    colors : sequence of colors in various formats interpreted by `input`
        hex code, html color name, or tuple in `input` space.
    n_colors : int, optional
        Number of colors in the palette.
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    Examples
    --------
    .. include: ../docstrings/blend_palette.rst
    """
    ...
@overload
def blend_palette(
    colors: Iterable[ColorType], n_colors: int = 6, as_cmap: Literal[False] = False, input: str = "rgb"
) -> _RGBColorPalette:
    """
    Make a palette that blends between a list of colors.

    Parameters
    ----------
    colors : sequence of colors in various formats interpreted by `input`
        hex code, html color name, or tuple in `input` space.
    n_colors : int, optional
        Number of colors in the palette.
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    Examples
    --------
    .. include: ../docstrings/blend_palette.rst
    """
    ...
def xkcd_palette(colors: Iterable[str]) -> _RGBColorPalette:
    """
    Make a palette with color names from the xkcd color survey.

    See xkcd for the full list of colors: https://xkcd.com/color/rgb/

    This is just a simple wrapper around the `seaborn.xkcd_rgb` dictionary.

    Parameters
    ----------
    colors : list of strings
        List of keys in the `seaborn.xkcd_rgb` dictionary.

    Returns
    -------
    palette
        A list of colors as RGB tuples.

    See Also
    --------
    crayon_palette : Make a palette with Crayola crayon colors.
    """
    ...
def crayon_palette(colors: Iterable[str]) -> _RGBColorPalette:
    """
    Make a palette with color names from Crayola crayons.

    Colors are taken from here:
    https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

    This is just a simple wrapper around the `seaborn.crayons` dictionary.

    Parameters
    ----------
    colors : list of strings
        List of keys in the `seaborn.crayons` dictionary.

    Returns
    -------
    palette
        A list of colors as RGB tuples.

    See Also
    --------
    xkcd_palette : Make a palette with named colors from the XKCD color survey.
    """
    ...
@overload
def cubehelix_palette(
    n_colors: int = 6,
    start: float = 0,
    rot: float = 0.4,
    gamma: float = 1.0,
    hue: float = 0.8,
    light: float = 0.85,
    dark: float = 0.15,
    reverse: bool = False,
    *,
    as_cmap: Literal[True],
) -> ListedColormap:
    """
    Make a sequential palette from the cubehelix system.

    This produces a colormap with linearly-decreasing (or increasing)
    brightness. That means that information will be preserved if printed to
    black and white or viewed by someone who is colorblind.  "cubehelix" is
    also available as a matplotlib-based palette, but this function gives the
    user more control over the look of the palette and has a different set of
    defaults.

    In addition to using this function, it is also possible to generate a
    cubehelix palette generally in seaborn using a string starting with
    `ch:` and containing other parameters (e.g. `"ch:s=.25,r=-.5"`).

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    start : float, 0 <= start <= 3
        The hue value at the start of the helix.
    rot : float
        Rotations around the hue wheel over the range of the palette.
    gamma : float 0 <= gamma
        Nonlinearity to emphasize dark (gamma < 1) or light (gamma > 1) colors.
    hue : float, 0 <= hue <= 1
        Saturation of the colors.
    dark : float 0 <= dark <= 1
        Intensity of the darkest color in the palette.
    light : float 0 <= light <= 1
        Intensity of the lightest color in the palette.
    reverse : bool
        If True, the palette will go from dark to light.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    choose_cubehelix_palette : Launch an interactive widget to select cubehelix
                               palette parameters.
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.

    References
    ----------
    Green, D. A. (2011). "A colour scheme for the display of astronomical
    intensity images". Bulletin of the Astromical Society of India, Vol. 39,
    p. 289-295.

    Examples
    --------
    .. include:: ../docstrings/cubehelix_palette.rst
    """
    ...
@overload
def cubehelix_palette(
    n_colors: int = 6,
    start: float = 0,
    rot: float = 0.4,
    gamma: float = 1.0,
    hue: float = 0.8,
    light: float = 0.85,
    dark: float = 0.15,
    reverse: bool = False,
    as_cmap: Literal[False] = False,
) -> _RGBColorPalette:
    """
    Make a sequential palette from the cubehelix system.

    This produces a colormap with linearly-decreasing (or increasing)
    brightness. That means that information will be preserved if printed to
    black and white or viewed by someone who is colorblind.  "cubehelix" is
    also available as a matplotlib-based palette, but this function gives the
    user more control over the look of the palette and has a different set of
    defaults.

    In addition to using this function, it is also possible to generate a
    cubehelix palette generally in seaborn using a string starting with
    `ch:` and containing other parameters (e.g. `"ch:s=.25,r=-.5"`).

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    start : float, 0 <= start <= 3
        The hue value at the start of the helix.
    rot : float
        Rotations around the hue wheel over the range of the palette.
    gamma : float 0 <= gamma
        Nonlinearity to emphasize dark (gamma < 1) or light (gamma > 1) colors.
    hue : float, 0 <= hue <= 1
        Saturation of the colors.
    dark : float 0 <= dark <= 1
        Intensity of the darkest color in the palette.
    light : float 0 <= light <= 1
        Intensity of the lightest color in the palette.
    reverse : bool
        If True, the palette will go from dark to light.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    choose_cubehelix_palette : Launch an interactive widget to select cubehelix
                               palette parameters.
    dark_palette : Create a sequential palette with dark low values.
    light_palette : Create a sequential palette with bright low values.

    References
    ----------
    Green, D. A. (2011). "A colour scheme for the display of astronomical
    intensity images". Bulletin of the Astromical Society of India, Vol. 39,
    p. 289-295.

    Examples
    --------
    .. include:: ../docstrings/cubehelix_palette.rst
    """
    ...
def set_color_codes(palette: str = "deep") -> None:
    """
    Change how matplotlib color shorthands are interpreted.

    Calling this will change how shorthand codes like "b" or "g"
    are interpreted by matplotlib in subsequent plots.

    Parameters
    ----------
    palette : {deep, muted, pastel, dark, bright, colorblind}
        Named seaborn palette to use as the source of colors.

    See Also
    --------
    set : Color codes can be set through the high-level seaborn style
          manager.
    set_palette : Color codes can also be set through the function that
                  sets the matplotlib color cycle.
    """
    ...
