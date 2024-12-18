"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class ShardManifest:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, id: Incomplete | None = None, shard_owners: Incomplete | None = None) -> None:
        """ShardManifest - a model defined in OpenAPI."""
        ...
    @property
    def id(self):
        """
        Get the id of this ShardManifest.

        :return: The id of this ShardManifest.
        :rtype: int
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this ShardManifest.

        :return: The id of this ShardManifest.
        :rtype: int
        """
        ...
    @property
    def shard_owners(self):
        """
        Get the shard_owners of this ShardManifest.

        :return: The shard_owners of this ShardManifest.
        :rtype: list[ShardOwner]
        """
        ...
    @shard_owners.setter
    def shard_owners(self, shard_owners) -> None:
        """
        Get the shard_owners of this ShardManifest.

        :return: The shard_owners of this ShardManifest.
        :rtype: list[ShardOwner]
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
