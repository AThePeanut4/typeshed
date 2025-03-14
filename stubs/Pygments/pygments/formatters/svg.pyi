"""
pygments.formatters.svg
~~~~~~~~~~~~~~~~~~~~~~~

Formatter for SVG output.

:copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
"""

from typing import Any, TypeVar

from pygments.formatter import Formatter

_T = TypeVar("_T", str, bytes)

class SvgFormatter(Formatter[_T]):
    """
    Format tokens as an SVG graphics file.  This formatter is still experimental.
    Each line of code is a ``<text>`` element with explicit ``x`` and ``y``
    coordinates containing ``<tspan>`` elements with the individual token styles.

    By default, this formatter outputs a full SVG document including doctype
    declaration and the ``<svg>`` root element.

    .. versionadded:: 0.9

    Additional options accepted:

    `nowrap`
        Don't wrap the SVG ``<text>`` elements in ``<svg><g>`` elements and
        don't add a XML declaration and a doctype.  If true, the `fontfamily`
        and `fontsize` options are ignored.  Defaults to ``False``.

    `fontfamily`
        The value to give the wrapping ``<g>`` element's ``font-family``
        attribute, defaults to ``"monospace"``.

    `fontsize`
        The value to give the wrapping ``<g>`` element's ``font-size``
        attribute, defaults to ``"14px"``.

    `linenos`
        If ``True``, add line numbers (default: ``False``).

    `linenostart`
        The line number for the first line (default: ``1``).

    `linenostep`
        If set to a number n > 1, only every nth line number is printed.

    `linenowidth`
        Maximum width devoted to line numbers (default: ``3*ystep``, sufficient
        for up to 4-digit line numbers. Increase width for longer code blocks).

    `xoffset`
        Starting offset in X direction, defaults to ``0``.

    `yoffset`
        Starting offset in Y direction, defaults to the font size if it is given
        in pixels, or ``20`` else.  (This is necessary since text coordinates
        refer to the text baseline, not the top edge.)

    `ystep`
        Offset to add to the Y coordinate for each subsequent line.  This should
        roughly be the text size plus 5.  It defaults to that value if the text
        size is given in pixels, or ``25`` else.

    `spacehack`
        Convert spaces in the source to ``&#160;``, which are non-breaking
        spaces.  SVG provides the ``xml:space`` attribute to control how
        whitespace inside tags is handled, in theory, the ``preserve`` value
        could be used to keep all whitespace as-is.  However, many current SVG
        viewers don't obey that rule, so this option is provided as a workaround
        and defaults to ``True``.
    """
    name: str
    aliases: Any
    filenames: Any
    nowrap: Any
    fontfamily: Any
    fontsize: Any
    xoffset: Any
    yoffset: Any
    ystep: Any
    spacehack: Any
    linenos: Any
    linenostart: Any
    linenostep: Any
    linenowidth: Any
    def format_unencoded(self, tokensource, outfile) -> None:
        """
        Format ``tokensource``, an iterable of ``(tokentype, tokenstring)``
        tuples and write it into ``outfile``.

        For our implementation we put all lines in their own 'line group'.
        """
        ...
