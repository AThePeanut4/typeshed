"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Axis:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        bounds: Incomplete | None = None,
        label: Incomplete | None = None,
        prefix: Incomplete | None = None,
        suffix: Incomplete | None = None,
        base: Incomplete | None = None,
        scale: Incomplete | None = None,
    ) -> None:
        """Axis - a model defined in OpenAPI."""
        ...
    @property
    def bounds(self):
        """
        Get the bounds of this Axis.

        The extents of the axis in the form [lower, upper]. Clients determine whether bounds are inclusive or exclusive of their limits.

        :return: The bounds of this Axis.
        :rtype: list[str]
        """
        ...
    @bounds.setter
    def bounds(self, bounds) -> None:
        """
        Get the bounds of this Axis.

        The extents of the axis in the form [lower, upper]. Clients determine whether bounds are inclusive or exclusive of their limits.

        :return: The bounds of this Axis.
        :rtype: list[str]
        """
        ...
    @property
    def label(self):
        """
        Get the label of this Axis.

        Description of the axis.

        :return: The label of this Axis.
        :rtype: str
        """
        ...
    @label.setter
    def label(self, label) -> None:
        """
        Get the label of this Axis.

        Description of the axis.

        :return: The label of this Axis.
        :rtype: str
        """
        ...
    @property
    def prefix(self):
        """
        Get the prefix of this Axis.

        Label prefix for formatting axis values.

        :return: The prefix of this Axis.
        :rtype: str
        """
        ...
    @prefix.setter
    def prefix(self, prefix) -> None:
        """
        Get the prefix of this Axis.

        Label prefix for formatting axis values.

        :return: The prefix of this Axis.
        :rtype: str
        """
        ...
    @property
    def suffix(self):
        """
        Get the suffix of this Axis.

        Label suffix for formatting axis values.

        :return: The suffix of this Axis.
        :rtype: str
        """
        ...
    @suffix.setter
    def suffix(self, suffix) -> None:
        """
        Get the suffix of this Axis.

        Label suffix for formatting axis values.

        :return: The suffix of this Axis.
        :rtype: str
        """
        ...
    @property
    def base(self):
        """
        Get the base of this Axis.

        Radix for formatting axis values.

        :return: The base of this Axis.
        :rtype: str
        """
        ...
    @base.setter
    def base(self, base) -> None:
        """
        Get the base of this Axis.

        Radix for formatting axis values.

        :return: The base of this Axis.
        :rtype: str
        """
        ...
    @property
    def scale(self):
        """
        Get the scale of this Axis.

        :return: The scale of this Axis.
        :rtype: AxisScale
        """
        ...
    @scale.setter
    def scale(self, scale) -> None:
        """
        Get the scale of this Axis.

        :return: The scale of this Axis.
        :rtype: AxisScale
        """
        ...
    def to_dict(self):
        """Return the model properties as a dict."""
        ...
    def to_str(self):
        """Return the string representation of the model."""
        ...
    def __eq__(self, other):
        """Return true if both objects are equal."""
        ...
    def __ne__(self, other):
        """Return true if both objects are not equal."""
        ...
