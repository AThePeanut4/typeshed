"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class BucketShardMapping:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, old_id: Incomplete | None = None, new_id: Incomplete | None = None) -> None:
        """BucketShardMapping - a model defined in OpenAPI."""
        ...
    @property
    def old_id(self):
        """
        Get the old_id of this BucketShardMapping.

        :return: The old_id of this BucketShardMapping.
        :rtype: int
        """
        ...
    @old_id.setter
    def old_id(self, old_id) -> None:
        """
        Get the old_id of this BucketShardMapping.

        :return: The old_id of this BucketShardMapping.
        :rtype: int
        """
        ...
    @property
    def new_id(self):
        """
        Get the new_id of this BucketShardMapping.

        :return: The new_id of this BucketShardMapping.
        :rtype: int
        """
        ...
    @new_id.setter
    def new_id(self, new_id) -> None:
        """
        Get the new_id of this BucketShardMapping.

        :return: The new_id of this BucketShardMapping.
        :rtype: int
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
