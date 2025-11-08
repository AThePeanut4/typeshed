"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

from typing import Final

MODIFIERS: Final[dict[str, tuple[int, int]]]
MODIFIER_RESET_OFFSET: Final[int]
FOREGROUND_COLOR_OFFSET: Final[int]
BACKGROUND_COLOR_OFFSET: Final[int]
COLOR_CLOSE_OFFSET: Final[int]
CSI: Final[str]
ANSI_ESCAPE_CODE: Final[str]
NEST_PLACEHOLDER: Final[str]

def round(value: float) -> int: ...
def rgb_to_ansi256(r: int, g: int, b: int) -> int:
    """Convert RGB to ANSI 256 color"""
    ...
def rgb_to_ansi16(r: int, g: int, b: int, use_bright: bool = False) -> int:
    """Convert RGB to ANSI 16 color"""
    ...
