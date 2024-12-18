"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Links:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, next: Incomplete | None = None, _self: Incomplete | None = None, prev: Incomplete | None = None
    ) -> None:
        """Links - a model defined in OpenAPI."""
        ...
    @property
    def next(self):
        """
        Get the next of this Links.

        URI of resource.

        :return: The next of this Links.
        :rtype: str
        """
        ...
    @next.setter
    def next(self, next) -> None:
        """
        Get the next of this Links.

        URI of resource.

        :return: The next of this Links.
        :rtype: str
        """
        ...
    @property
    def prev(self):
        """
        Get the prev of this Links.

        URI of resource.

        :return: The prev of this Links.
        :rtype: str
        """
        ...
    @prev.setter
    def prev(self, prev) -> None:
        """
        Get the prev of this Links.

        URI of resource.

        :return: The prev of this Links.
        :rtype: str
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
