"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class ShardGroupManifest:
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
        id: Incomplete | None = None,
        start_time: Incomplete | None = None,
        end_time: Incomplete | None = None,
        deleted_at: Incomplete | None = None,
        truncated_at: Incomplete | None = None,
        shards: Incomplete | None = None,
    ) -> None:
        """ShardGroupManifest - a model defined in OpenAPI."""
        ...
    @property
    def id(self):
        """
        Get the id of this ShardGroupManifest.

        :return: The id of this ShardGroupManifest.
        :rtype: int
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this ShardGroupManifest.

        :return: The id of this ShardGroupManifest.
        :rtype: int
        """
        ...
    @property
    def start_time(self):
        """
        Get the start_time of this ShardGroupManifest.

        :return: The start_time of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @start_time.setter
    def start_time(self, start_time) -> None:
        """
        Get the start_time of this ShardGroupManifest.

        :return: The start_time of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @property
    def end_time(self):
        """
        Get the end_time of this ShardGroupManifest.

        :return: The end_time of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @end_time.setter
    def end_time(self, end_time) -> None:
        """
        Get the end_time of this ShardGroupManifest.

        :return: The end_time of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @property
    def deleted_at(self):
        """
        Get the deleted_at of this ShardGroupManifest.

        :return: The deleted_at of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @deleted_at.setter
    def deleted_at(self, deleted_at) -> None:
        """
        Get the deleted_at of this ShardGroupManifest.

        :return: The deleted_at of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @property
    def truncated_at(self):
        """
        Get the truncated_at of this ShardGroupManifest.

        :return: The truncated_at of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @truncated_at.setter
    def truncated_at(self, truncated_at) -> None:
        """
        Get the truncated_at of this ShardGroupManifest.

        :return: The truncated_at of this ShardGroupManifest.
        :rtype: datetime
        """
        ...
    @property
    def shards(self):
        """
        Get the shards of this ShardGroupManifest.

        :return: The shards of this ShardGroupManifest.
        :rtype: list[ShardManifest]
        """
        ...
    @shards.setter
    def shards(self, shards) -> None:
        """
        Get the shards of this ShardGroupManifest.

        :return: The shards of this ShardGroupManifest.
        :rtype: list[ShardManifest]
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
