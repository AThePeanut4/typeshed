"""
This module defines a few common page sizes in points (1/72 inch).
To be expanded to include things like label sizes, envelope windows
etc.
"""

from typing import Final

__version__: Final[str]
A0: Final[tuple[float, float]]
A1: Final[tuple[float, float]]
A2: Final[tuple[float, float]]
A3: Final[tuple[float, float]]
A4: Final[tuple[float, float]]
A5: Final[tuple[float, float]]
A6: Final[tuple[float, float]]
A7: Final[tuple[float, float]]
A8: Final[tuple[float, float]]
A9: Final[tuple[float, float]]
A10: Final[tuple[float, float]]
B0: Final[tuple[float, float]]
B1: Final[tuple[float, float]]
B2: Final[tuple[float, float]]
B3: Final[tuple[float, float]]
B4: Final[tuple[float, float]]
B5: Final[tuple[float, float]]
B6: Final[tuple[float, float]]
B7: Final[tuple[float, float]]
B8: Final[tuple[float, float]]
B9: Final[tuple[float, float]]
B10: Final[tuple[float, float]]
C0: Final[tuple[float, float]]
C1: Final[tuple[float, float]]
C2: Final[tuple[float, float]]
C3: Final[tuple[float, float]]
C4: Final[tuple[float, float]]
C5: Final[tuple[float, float]]
C6: Final[tuple[float, float]]
C7: Final[tuple[float, float]]
C8: Final[tuple[float, float]]
C9: Final[tuple[float, float]]
C10: Final[tuple[float, float]]
LETTER: Final[tuple[float, float]]
LEGAL: Final[tuple[float, float]]
ELEVENSEVENTEEN: Final[tuple[float, float]]
JUNIOR_LEGAL: Final[tuple[float, float]]
HALF_LETTER: Final[tuple[float, float]]
GOV_LETTER: Final[tuple[float, float]]
GOV_LEGAL: Final[tuple[float, float]]
TABLOID: Final[tuple[float, float]]
LEDGER: Final[tuple[float, float]]
letter: Final[tuple[float, float]]
legal: Final[tuple[float, float]]
elevenSeventeen: Final[tuple[float, float]]

def landscape(pagesize: tuple[float, float]) -> tuple[float, float]:
    """Use this to get page orientation right"""
    ...
def portrait(pagesize: tuple[float, float]) -> tuple[float, float]:
    """Use this to get page orientation right"""
    ...
