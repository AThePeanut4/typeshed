from ..errors import TopologicalError as TopologicalError
from ..geometry import Point, Polygon

class Cell:
    """
    A `Cell`'s centroid property is a potential solution to finding the pole
    of inaccessibility for a given polygon. Rich comparison operators are used
    for sorting `Cell` objects in a priority queue based on the potential
    maximum distance of any theoretical point within a cell to a given
    polygon's exterior boundary.
    """
    x: float
    y: float
    h: float
    centroid: Point
    distance: float
    max_distance: float
    def __init__(self, x: float, y: float, h: float, polygon: Polygon) -> None: ...
    def __lt__(self, other: Cell) -> bool: ...
    def __le__(self, other: Cell) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Cell) -> bool: ...
    def __ge__(self, other: Cell) -> bool: ...

def polylabel(polygon: Polygon, tolerance: float = 1.0) -> Point:
    """
    Finds pole of inaccessibility for a given polygon. Based on
    Vladimir Agafonkin's https://github.com/mapbox/polylabel

    Parameters
    ----------
    polygon : shapely.geometry.Polygon
    tolerance : int or float, optional
                `tolerance` represents the highest resolution in units of the
                input geometry that will be considered for a solution. (default
                value is 1.0).

    Returns
    -------
    shapely.geometry.Point
        A point representing the pole of inaccessibility for the given input
        polygon.

    Raises
    ------
    shapely.errors.TopologicalError
        If the input polygon is not a valid geometry.

    Example
    -------
    >>> from shapely import LineString
    >>> polygon = LineString([(0, 0), (50, 200), (100, 100), (20, 50),
    ... (-100, -20), (-150, -200)]).buffer(100)
    >>> polylabel(polygon, tolerance=10).wkt
    'POINT (59.35615556364569 121.83919629746435)'
    """
    ...
