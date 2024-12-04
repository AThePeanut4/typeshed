"""Provides multi-point element-wise operations such as ``contains``."""

from typing import overload

import numpy as np
from numpy.typing import NDArray

from .._typing import ArrayLike, ArrayLikeSeq
from ..lib import Geometry
from ..prepared import PreparedGeometry

@overload
def contains(geometry: Geometry | PreparedGeometry[Geometry], x: float, y: float) -> bool:
    """
    Vectorized (element-wise) version of `contains` which checks whether
    multiple points are contained by a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points contained by the given `geometry`.
    """
    ...
@overload
def contains(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLikeSeq[float], y: ArrayLike[float]
) -> NDArray[np.bool_]:
    """
    Vectorized (element-wise) version of `contains` which checks whether
    multiple points are contained by a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points contained by the given `geometry`.
    """
    ...
@overload
def contains(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[float], y: ArrayLikeSeq[float]
) -> NDArray[np.bool_]:
    """
    Vectorized (element-wise) version of `contains` which checks whether
    multiple points are contained by a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points contained by the given `geometry`.
    """
    ...
@overload
def contains(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[float], y: ArrayLike[float]
) -> bool | NDArray[np.bool_]:
    """
    Vectorized (element-wise) version of `contains` which checks whether
    multiple points are contained by a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points contained by the given `geometry`.
    """
    ...
@overload
def touches(geometry: Geometry | PreparedGeometry[Geometry], x: float, y: float) -> bool:
    """
    Vectorized (element-wise) version of `touches` which checks whether
    multiple points touch the exterior of a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points which touch the exterior of the given `geometry`.
    """
    ...
@overload
def touches(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLikeSeq[float], y: ArrayLike[float]
) -> NDArray[np.bool_]:
    """
    Vectorized (element-wise) version of `touches` which checks whether
    multiple points touch the exterior of a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points which touch the exterior of the given `geometry`.
    """
    ...
@overload
def touches(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[float], y: ArrayLikeSeq[float]
) -> NDArray[np.bool_]:
    """
    Vectorized (element-wise) version of `touches` which checks whether
    multiple points touch the exterior of a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points which touch the exterior of the given `geometry`.
    """
    ...
@overload
def touches(
    geometry: Geometry | PreparedGeometry[Geometry], x: ArrayLike[float], y: ArrayLike[float]
) -> bool | NDArray[np.bool_]:
    """
    Vectorized (element-wise) version of `touches` which checks whether
    multiple points touch the exterior of a single geometry.

    Parameters
    ----------
    geometry : PreparedGeometry or subclass of BaseGeometry
        The geometry which is to be checked to see whether each point is
        contained within. The geometry will be "prepared" if it is not already
        a PreparedGeometry instance.
    x : array
        The x coordinates of the points to check.
    y : array
        The y coordinates of the points to check.

    Returns
    -------
    Mask of points which touch the exterior of the given `geometry`.
    """
    ...
