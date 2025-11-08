"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

from typing import Final, Protocol, overload, type_check_only

@type_check_only
class _SupportsGet(Protocol):
    @overload
    def get(self, name: str, /) -> str | None: ...
    @overload
    def get(self, name: str, default: str, /) -> str: ...

NO_COLORS: Final[int]
ANSI_8_COLORS: Final[int]
ANSI_16_COLORS: Final[int]
ANSI_256_COLORS: Final[int]
TRUE_COLORS: Final[int]

def detect_color_support(env: _SupportsGet) -> int:
    """
    Detect what color palettes are supported.
    It'll return a valid color mode to use
    with colorful.

    :param dict env: the environment dict like returned by ``os.envion``
    """
    ...
