from _typeshed import Incomplete
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from ._enum import ParamEnum
from ._ragged_array import from_ragged_array as from_ragged_array, to_ragged_array as to_ragged_array
from ._typing import ArrayLikeSeq, GeoArray, OptGeoArrayLikeSeq
from .geometry.base import BaseGeometry
from .lib import Geometry

__all__ = ["from_geojson", "from_ragged_array", "from_wkb", "from_wkt", "to_geojson", "to_ragged_array", "to_wkb", "to_wkt"]

# Mypy and stubtest aren't happy with the following definition and
# raise is a reserved keyword, so we cannot use the class syntax of enums
# DecodingErrorOptions = ParamEnum("DecodingErrorOptions", {"ignore": 0, "warn": 1, "raise": 2})
DecodingErrorOptions: Incomplete

class WKBFlavorOptions(ParamEnum):
    """An enumeration."""
    extended = 1
    iso = 2

@overload
def to_wkt(
    geometry: None, rounding_precision: int = 6, trim: bool = True, output_dimension: int = 3, old_3d: bool = False, **kwargs
) -> None:
    """
    Converts to the Well-Known Text (WKT) representation of a Geometry.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKT serialization:

    - for GEOS <= 3.8 a multipoint with an empty sub-geometry will raise an exception
    - for GEOS <= 3.8 empty geometries are always serialized to 2D
    - for GEOS >= 3.9 only simple empty geometries can be 3D, collections are still
      always 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    rounding_precision : int, default 6
        The rounding precision when writing the WKT string. Set to a value of
        -1 to indicate the full precision.
    trim : bool, default True
        If True, trim unnecessary decimals (trailing zeros).
    output_dimension : int, default 3
        The output dimension for the WKT string. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKT string.
    old_3d : bool, default False
        Enable old style 3D/4D WKT generation. By default, new style 3D/4D WKT
        (ie. "POINT Z (10 20 30)") is returned, but with ``old_3d=True``
        the WKT will be formatted in the style "POINT (10 20 30)".
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> to_wkt(Point(0, 0))
    'POINT (0 0)'
    >>> to_wkt(Point(0, 0), rounding_precision=3, trim=False)
    'POINT (0.000 0.000)'
    >>> to_wkt(Point(0, 0), rounding_precision=-1, trim=False)
    'POINT (0.0000000000000000 0.0000000000000000)'
    >>> to_wkt(Point(1, 2, 3), trim=True)
    'POINT Z (1 2 3)'
    >>> to_wkt(Point(1, 2, 3), trim=True, output_dimension=2)
    'POINT (1 2)'
    >>> to_wkt(Point(1, 2, 3), trim=True, old_3d=True)
    'POINT (1 2 3)'

    Notes
    -----
    The defaults differ from the default of the GEOS library. To mimic this,
    use::

        to_wkt(geometry, rounding_precision=-1, trim=False, output_dimension=2)
    """
    ...
@overload
def to_wkt(
    geometry: Geometry, rounding_precision: int = 6, trim: bool = True, output_dimension: int = 3, old_3d: bool = False, **kwargs
) -> str:
    """
    Converts to the Well-Known Text (WKT) representation of a Geometry.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKT serialization:

    - for GEOS <= 3.8 a multipoint with an empty sub-geometry will raise an exception
    - for GEOS <= 3.8 empty geometries are always serialized to 2D
    - for GEOS >= 3.9 only simple empty geometries can be 3D, collections are still
      always 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    rounding_precision : int, default 6
        The rounding precision when writing the WKT string. Set to a value of
        -1 to indicate the full precision.
    trim : bool, default True
        If True, trim unnecessary decimals (trailing zeros).
    output_dimension : int, default 3
        The output dimension for the WKT string. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKT string.
    old_3d : bool, default False
        Enable old style 3D/4D WKT generation. By default, new style 3D/4D WKT
        (ie. "POINT Z (10 20 30)") is returned, but with ``old_3d=True``
        the WKT will be formatted in the style "POINT (10 20 30)".
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> to_wkt(Point(0, 0))
    'POINT (0 0)'
    >>> to_wkt(Point(0, 0), rounding_precision=3, trim=False)
    'POINT (0.000 0.000)'
    >>> to_wkt(Point(0, 0), rounding_precision=-1, trim=False)
    'POINT (0.0000000000000000 0.0000000000000000)'
    >>> to_wkt(Point(1, 2, 3), trim=True)
    'POINT Z (1 2 3)'
    >>> to_wkt(Point(1, 2, 3), trim=True, output_dimension=2)
    'POINT (1 2)'
    >>> to_wkt(Point(1, 2, 3), trim=True, old_3d=True)
    'POINT (1 2 3)'

    Notes
    -----
    The defaults differ from the default of the GEOS library. To mimic this,
    use::

        to_wkt(geometry, rounding_precision=-1, trim=False, output_dimension=2)
    """
    ...
@overload
def to_wkt(
    geometry: OptGeoArrayLikeSeq,
    rounding_precision: int = 6,
    trim: bool = True,
    output_dimension: int = 3,
    old_3d: bool = False,
    **kwargs,
) -> NDArray[np.str_]:
    """
    Converts to the Well-Known Text (WKT) representation of a Geometry.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKT serialization:

    - for GEOS <= 3.8 a multipoint with an empty sub-geometry will raise an exception
    - for GEOS <= 3.8 empty geometries are always serialized to 2D
    - for GEOS >= 3.9 only simple empty geometries can be 3D, collections are still
      always 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    rounding_precision : int, default 6
        The rounding precision when writing the WKT string. Set to a value of
        -1 to indicate the full precision.
    trim : bool, default True
        If True, trim unnecessary decimals (trailing zeros).
    output_dimension : int, default 3
        The output dimension for the WKT string. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKT string.
    old_3d : bool, default False
        Enable old style 3D/4D WKT generation. By default, new style 3D/4D WKT
        (ie. "POINT Z (10 20 30)") is returned, but with ``old_3d=True``
        the WKT will be formatted in the style "POINT (10 20 30)".
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> to_wkt(Point(0, 0))
    'POINT (0 0)'
    >>> to_wkt(Point(0, 0), rounding_precision=3, trim=False)
    'POINT (0.000 0.000)'
    >>> to_wkt(Point(0, 0), rounding_precision=-1, trim=False)
    'POINT (0.0000000000000000 0.0000000000000000)'
    >>> to_wkt(Point(1, 2, 3), trim=True)
    'POINT Z (1 2 3)'
    >>> to_wkt(Point(1, 2, 3), trim=True, output_dimension=2)
    'POINT (1 2)'
    >>> to_wkt(Point(1, 2, 3), trim=True, old_3d=True)
    'POINT (1 2 3)'

    Notes
    -----
    The defaults differ from the default of the GEOS library. To mimic this,
    use::

        to_wkt(geometry, rounding_precision=-1, trim=False, output_dimension=2)
    """
    ...
@overload
def to_wkb(
    geometry: None,
    hex: bool = False,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> None:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_wkb(
    geometry: Geometry,
    hex: Literal[False] = False,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> bytes:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_wkb(
    geometry: Geometry,
    hex: Literal[True],
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> str:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_wkb(
    geometry: Geometry,
    hex: bool,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> bytes | str:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_wkb(
    geometry: OptGeoArrayLikeSeq,
    hex: Literal[False] = False,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> NDArray[np.bytes_]:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_wkb(
    geometry: OptGeoArrayLikeSeq,
    hex: Literal[True],
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> NDArray[np.str_]:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_wkb(
    geometry: OptGeoArrayLikeSeq,
    hex: bool,
    output_dimension: int = 3,
    byte_order: int = -1,
    include_srid: bool = False,
    flavor: Literal["iso", "extended"] = "extended",
    **kwargs,
) -> NDArray[np.bytes_] | NDArray[np.str_]:
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexadecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB representation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification). Not allowed when flavor is "iso".
    flavor : {"iso", "extended"}, default "extended"
        Which flavor of WKB will be returned. The flavor determines how
        extra dimensionality is encoded with the type number, and whether
        SRID can be included in the WKB. ISO flavor is "more standard" for
        3D output, and does not support SRID embedding.
        Both flavors are equivalent when ``output_dimension=2`` (or with 2D
        geometries) and ``include_srid=False``.
        The `from_wkb` function can read both flavors.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    ...
@overload
def to_geojson(geometry: None, indent: int | None = None, **kwargs) -> None:
    """
    Converts to the GeoJSON representation of a Geometry.

    The GeoJSON format is defined in the `RFC 7946 <https://geojson.org/>`__.
    NaN (not-a-number) coordinates will be written as 'null'.

    The following are currently unsupported:

    - Geometries of type LINEARRING: these are output as 'null'.
    - Three-dimensional geometries: the third dimension is ignored.

    Parameters
    ----------
    geometry : str, bytes or array_like
    indent : int, optional
        If indent is a non-negative integer, then GeoJSON will be formatted.
        An indent level of 0 will only insert newlines. None (the default)
        selects the most compact representation.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_geojson(point)
    '{"type":"Point","coordinates":[1.0,1.0]}'
    >>> print(to_geojson(point, indent=2))
    {
      "type": "Point",
      "coordinates": [
          1.0,
          1.0
      ]
    }
    """
    ...
@overload
def to_geojson(geometry: Geometry, indent: int | None = None, **kwargs) -> str:
    """
    Converts to the GeoJSON representation of a Geometry.

    The GeoJSON format is defined in the `RFC 7946 <https://geojson.org/>`__.
    NaN (not-a-number) coordinates will be written as 'null'.

    The following are currently unsupported:

    - Geometries of type LINEARRING: these are output as 'null'.
    - Three-dimensional geometries: the third dimension is ignored.

    Parameters
    ----------
    geometry : str, bytes or array_like
    indent : int, optional
        If indent is a non-negative integer, then GeoJSON will be formatted.
        An indent level of 0 will only insert newlines. None (the default)
        selects the most compact representation.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_geojson(point)
    '{"type":"Point","coordinates":[1.0,1.0]}'
    >>> print(to_geojson(point, indent=2))
    {
      "type": "Point",
      "coordinates": [
          1.0,
          1.0
      ]
    }
    """
    ...
@overload
def to_geojson(geometry: OptGeoArrayLikeSeq, indent: int | None = None, **kwargs) -> NDArray[np.str_]:
    """
    Converts to the GeoJSON representation of a Geometry.

    The GeoJSON format is defined in the `RFC 7946 <https://geojson.org/>`__.
    NaN (not-a-number) coordinates will be written as 'null'.

    The following are currently unsupported:

    - Geometries of type LINEARRING: these are output as 'null'.
    - Three-dimensional geometries: the third dimension is ignored.

    Parameters
    ----------
    geometry : str, bytes or array_like
    indent : int, optional
        If indent is a non-negative integer, then GeoJSON will be formatted.
        An indent level of 0 will only insert newlines. None (the default)
        selects the most compact representation.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_geojson(point)
    '{"type":"Point","coordinates":[1.0,1.0]}'
    >>> print(to_geojson(point, indent=2))
    {
      "type": "Point",
      "coordinates": [
          1.0,
          1.0
      ]
    }
    """
    ...
@overload
def from_wkt(geometry: None, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> None:
    """
    Creates geometries from the Well-Known Text (WKT) representation.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    Parameters
    ----------
    geometry : str or array_like
        The WKT string(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if WKT input geometries are invalid.
        - warn: a warning will be raised and invalid WKT geometries will be
          returned as ``None``.
        - ignore: invalid WKT geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from_wkt('POINT (0 0)')
    <POINT (0 0)>
    """
    ...
@overload
def from_wkt(geometry: str, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> BaseGeometry:
    """
    Creates geometries from the Well-Known Text (WKT) representation.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    Parameters
    ----------
    geometry : str or array_like
        The WKT string(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if WKT input geometries are invalid.
        - warn: a warning will be raised and invalid WKT geometries will be
          returned as ``None``.
        - ignore: invalid WKT geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from_wkt('POINT (0 0)')
    <POINT (0 0)>
    """
    ...
@overload
def from_wkt(
    geometry: ArrayLikeSeq[str | None], on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs
) -> GeoArray:
    """
    Creates geometries from the Well-Known Text (WKT) representation.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    Parameters
    ----------
    geometry : str or array_like
        The WKT string(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if WKT input geometries are invalid.
        - warn: a warning will be raised and invalid WKT geometries will be
          returned as ``None``.
        - ignore: invalid WKT geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from_wkt('POINT (0 0)')
    <POINT (0 0)>
    """
    ...
@overload
def from_wkb(geometry: None, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> None:
    r"""
    Creates geometries from the Well-Known Binary (WKB) representation.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.


    Parameters
    ----------
    geometry : str or array_like
        The WKB byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if a WKB input geometry is invalid.
        - warn: a warning will be raised and invalid WKB geometries will be
          returned as ``None``.
        - ignore: invalid WKB geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from_wkb(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?')
    <POINT (1 1)>
    """
    ...
@overload
def from_wkb(geometry: str | bytes, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> BaseGeometry:
    r"""
    Creates geometries from the Well-Known Binary (WKB) representation.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.


    Parameters
    ----------
    geometry : str or array_like
        The WKB byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if a WKB input geometry is invalid.
        - warn: a warning will be raised and invalid WKB geometries will be
          returned as ``None``.
        - ignore: invalid WKB geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from_wkb(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?')
    <POINT (1 1)>
    """
    ...
@overload
def from_wkb(
    geometry: ArrayLikeSeq[str | bytes | None], on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs
) -> GeoArray:
    r"""
    Creates geometries from the Well-Known Binary (WKB) representation.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.


    Parameters
    ----------
    geometry : str or array_like
        The WKB byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if a WKB input geometry is invalid.
        - warn: a warning will be raised and invalid WKB geometries will be
          returned as ``None``.
        - ignore: invalid WKB geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from_wkb(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?')
    <POINT (1 1)>
    """
    ...
@overload
def from_geojson(geometry: None, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> None:
    """
    Creates geometries from GeoJSON representations (strings).

    If a GeoJSON is a FeatureCollection, it is read as a single geometry
    (with type GEOMETRYCOLLECTION). This may be unpacked using the ``pygeos.get_parts``.
    Properties are not read.

    The GeoJSON format is defined in `RFC 7946 <https://geojson.org/>`__.

    The following are currently unsupported:

    - Three-dimensional geometries: the third dimension is ignored.
    - Geometries having 'null' in the coordinates.

    Parameters
    ----------
    geometry : str, bytes or array_like
        The GeoJSON string or byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if an input GeoJSON is invalid.
        - warn: a warning will be raised and invalid input geometries will be
          returned as ``None``.
        - ignore: invalid input geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    get_parts

    Examples
    --------
    >>> from_geojson('{"type": "Point","coordinates": [1, 2]}')
    <POINT (1 2)>
    """
    ...
@overload
def from_geojson(geometry: str | bytes, on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs) -> BaseGeometry:
    """
    Creates geometries from GeoJSON representations (strings).

    If a GeoJSON is a FeatureCollection, it is read as a single geometry
    (with type GEOMETRYCOLLECTION). This may be unpacked using the ``pygeos.get_parts``.
    Properties are not read.

    The GeoJSON format is defined in `RFC 7946 <https://geojson.org/>`__.

    The following are currently unsupported:

    - Three-dimensional geometries: the third dimension is ignored.
    - Geometries having 'null' in the coordinates.

    Parameters
    ----------
    geometry : str, bytes or array_like
        The GeoJSON string or byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if an input GeoJSON is invalid.
        - warn: a warning will be raised and invalid input geometries will be
          returned as ``None``.
        - ignore: invalid input geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    get_parts

    Examples
    --------
    >>> from_geojson('{"type": "Point","coordinates": [1, 2]}')
    <POINT (1 2)>
    """
    ...
@overload
def from_geojson(
    geometry: ArrayLikeSeq[str | bytes | None], on_invalid: Literal["raise", "warn", "ignore"] = "raise", **kwargs
) -> GeoArray:
    """
    Creates geometries from GeoJSON representations (strings).

    If a GeoJSON is a FeatureCollection, it is read as a single geometry
    (with type GEOMETRYCOLLECTION). This may be unpacked using the ``pygeos.get_parts``.
    Properties are not read.

    The GeoJSON format is defined in `RFC 7946 <https://geojson.org/>`__.

    The following are currently unsupported:

    - Three-dimensional geometries: the third dimension is ignored.
    - Geometries having 'null' in the coordinates.

    Parameters
    ----------
    geometry : str, bytes or array_like
        The GeoJSON string or byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if an input GeoJSON is invalid.
        - warn: a warning will be raised and invalid input geometries will be
          returned as ``None``.
        - ignore: invalid input geometries will be returned as ``None`` without a warning.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    get_parts

    Examples
    --------
    >>> from_geojson('{"type": "Point","coordinates": [1, 2]}')
    <POINT (1 2)>
    """
    ...
