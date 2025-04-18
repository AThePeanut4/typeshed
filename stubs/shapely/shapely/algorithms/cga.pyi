"""Shapely CGA algorithms."""

from ..geometry import LinearRing

def signed_area(ring: LinearRing) -> float:
    """
    Return the signed area enclosed by a ring in linear time.

    Algorithm used: https://web.archive.org/web/20080209143651/http://cgafaq.info:80/wiki/Polygon_Area
    """
    ...
