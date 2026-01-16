"""
A Catalog of 115 Bright Stars

Data sources:

Hipparcos Catalog
https://cdsarc.u-strasbg.fr/ftp/cats/I/239/hip_main.dat

IAU Catalog of Star Names (IAU-CSN)
http://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt

Proper motion has been applied to the Hipparcos catalog's 1991.25 epoch
positions to generate the 2000.0 positions that PyEphem needs, using the
high-precision Skyfield astronomy library for Python.  See the script
`bin/rebuild-star-data` in the PyEphem project repository for the
details of how the star positions are generated and formatted.  It also
includes variant names for several stars that you might want to consult:

https://github.com/brandon-rhodes/pyephem/blob/master/bin/rebuild-star-data

The 57 navigational stars are drawn from:

Her Majesty's Nautical Almanac Office Publications ('Almanac'):
    NP314-18 "The Nautical Almanac" (2017).
    DP330 "NavPac and Compact Data" (2015).
    NP303(AP3270) "Rapid Sight Reduction Tables for Navigation" (2012).
"""

from typing import Final, overload

from . import FixedBody, Observer
from ._libastro import _DateInitType

db: Final[str]
stars: dict[str, FixedBody]

@overload
def star(name: str, observer: Observer, /) -> FixedBody: ...
@overload
def star(name: str, when: _DateInitType = ..., epoch: _DateInitType = ...) -> FixedBody: ...

STAR_NUMBER_NAME: Final[dict[int, str]]
STAR_NAME_NUMBER: Final[dict[str, int]]
