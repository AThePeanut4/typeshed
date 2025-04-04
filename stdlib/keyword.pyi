"""
Keywords (from "Grammar/python.gram")

This file is automatically generated; please don't muck it up!

To update the symbols in this file, 'cd' to the top directory of
the python source tree and run:

    PYTHONPATH=Tools/peg_generator python3 -m pegen.keywordgen         Grammar/python.gram         Grammar/Tokens         Lib/keyword.py

Alternatively, you can run 'make regen-keyword'.
"""

from collections.abc import Sequence
from typing import Final

__all__ = ["iskeyword", "issoftkeyword", "kwlist", "softkwlist"]

def iskeyword(s: str, /) -> bool:
    """x.__contains__(y) <==> y in x."""
    ...

# a list at runtime, but you're not meant to mutate it;
# type it as a sequence
kwlist: Final[Sequence[str]]

def issoftkeyword(s: str, /) -> bool:
    """x.__contains__(y) <==> y in x."""
    ...

# a list at runtime, but you're not meant to mutate it;
# type it as a sequence
softkwlist: Final[Sequence[str]]
