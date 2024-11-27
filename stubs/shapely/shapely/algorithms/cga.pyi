from collections.abc import Callable

from ..geometry import LinearRing

def signed_area(ring: LinearRing) -> float:
    """
    Return the signed area enclosed by a ring in linear time using the
    algorithm at: https://web.archive.org/web/20080209143651/http://cgafaq.info:80/wiki/Polygon_Area
    """
    ...
def is_ccw_impl(name: None = None) -> Callable[[LinearRing], bool]:
    """Predicate implementation"""
    ...
