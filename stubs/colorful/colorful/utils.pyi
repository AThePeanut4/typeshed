"""
colorful
~~~~~~~~

Terminal string styling done right, in Python.

:copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, see LICENSE for more details.
"""

def hex_to_rgb(value: str) -> tuple[int, int, int]:
    """
    Convert the given hex string to a
    valid RGB channel triplet.
    """
    ...
def check_hex(value: str) -> None:
    """
    Check if the given hex value is a valid RGB color

    It should match the format: [0-9a-fA-F]
    and be of length 3 or 6.
    """
    ...
