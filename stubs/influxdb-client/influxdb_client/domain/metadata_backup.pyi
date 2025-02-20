"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class MetadataBackup:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, kv: Incomplete | None = None, sql: Incomplete | None = None, buckets: Incomplete | None = None
    ) -> None:
        """MetadataBackup - a model defined in OpenAPI."""
        ...
    @property
    def kv(self):
        """
        Get the kv of this MetadataBackup.

        :return: The kv of this MetadataBackup.
        :rtype: file
        """
        ...
    @kv.setter
    def kv(self, kv) -> None:
        """
        Get the kv of this MetadataBackup.

        :return: The kv of this MetadataBackup.
        :rtype: file
        """
        ...
    @property
    def sql(self):
        """
        Get the sql of this MetadataBackup.

        :return: The sql of this MetadataBackup.
        :rtype: file
        """
        ...
    @sql.setter
    def sql(self, sql) -> None:
        """
        Get the sql of this MetadataBackup.

        :return: The sql of this MetadataBackup.
        :rtype: file
        """
        ...
    @property
    def buckets(self):
        """
        Get the buckets of this MetadataBackup.

        :return: The buckets of this MetadataBackup.
        :rtype: list[BucketMetadataManifest]
        """
        ...
    @buckets.setter
    def buckets(self, buckets) -> None:
        """
        Get the buckets of this MetadataBackup.

        :return: The buckets of this MetadataBackup.
        :rtype: list[BucketMetadataManifest]
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
