"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

from _typeshed import SupportsItems

def parse_colors(path: str) -> SupportsItems[str, str | tuple[int, int, int]]:
    """
    Parse the given color files.

    Supported are:
        * .txt for X11 colors
        * .json for colornames
    """
    ...
def parse_rgb_txt_file(path: str) -> SupportsItems[str, str | tuple[int, int, int]]:
    """
    Parse the given rgb.txt file into a Python dict.

    See https://en.wikipedia.org/wiki/X11_color_names for more information

    :param str path: the path to the X11 rgb.txt file
    """
    ...
def parse_json_color_file(path: str) -> dict[str, str]:
    """
    Parse a JSON color file.

    The JSON has to be in the following format:

    .. code:: json

       [{"name": "COLOR_NAME", "hex": "#HEX"}, ...]

    :param str path: the path to the JSON color file
    """
    ...
def sanitize_color_palette(colorpalette: SupportsItems[str, str | tuple[int, int, int]]) -> dict[str, tuple[int, int, int]]:
    """
    Sanitze the given color palette so it can
    be safely used by Colorful.

    It will convert colors specified in hex RGB to
    a RGB channel triplet.
    """
    ...
