"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class RemoteConnections:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, remotes: Incomplete | None = None) -> None:
        """RemoteConnections - a model defined in OpenAPI."""
        ...
    @property
    def remotes(self):
        """
        Get the remotes of this RemoteConnections.

        :return: The remotes of this RemoteConnections.
        :rtype: list[RemoteConnection]
        """
        ...
    @remotes.setter
    def remotes(self, remotes) -> None:
        """
        Get the remotes of this RemoteConnections.

        :return: The remotes of this RemoteConnections.
        :rtype: list[RemoteConnection]
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
