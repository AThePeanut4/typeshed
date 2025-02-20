"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class RetentionPolicyManifest:
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
        name: Incomplete | None = None,
        replica_n: Incomplete | None = None,
        duration: Incomplete | None = None,
        shard_group_duration: Incomplete | None = None,
        shard_groups: Incomplete | None = None,
        subscriptions: Incomplete | None = None,
    ) -> None:
        """RetentionPolicyManifest - a model defined in OpenAPI."""
        ...
    @property
    def name(self):
        """
        Get the name of this RetentionPolicyManifest.

        :return: The name of this RetentionPolicyManifest.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this RetentionPolicyManifest.

        :return: The name of this RetentionPolicyManifest.
        :rtype: str
        """
        ...
    @property
    def replica_n(self):
        """
        Get the replica_n of this RetentionPolicyManifest.

        :return: The replica_n of this RetentionPolicyManifest.
        :rtype: int
        """
        ...
    @replica_n.setter
    def replica_n(self, replica_n) -> None:
        """
        Get the replica_n of this RetentionPolicyManifest.

        :return: The replica_n of this RetentionPolicyManifest.
        :rtype: int
        """
        ...
    @property
    def duration(self):
        """
        Get the duration of this RetentionPolicyManifest.

        :return: The duration of this RetentionPolicyManifest.
        :rtype: int
        """
        ...
    @duration.setter
    def duration(self, duration) -> None:
        """
        Get the duration of this RetentionPolicyManifest.

        :return: The duration of this RetentionPolicyManifest.
        :rtype: int
        """
        ...
    @property
    def shard_group_duration(self):
        """
        Get the shard_group_duration of this RetentionPolicyManifest.

        :return: The shard_group_duration of this RetentionPolicyManifest.
        :rtype: int
        """
        ...
    @shard_group_duration.setter
    def shard_group_duration(self, shard_group_duration) -> None:
        """
        Get the shard_group_duration of this RetentionPolicyManifest.

        :return: The shard_group_duration of this RetentionPolicyManifest.
        :rtype: int
        """
        ...
    @property
    def shard_groups(self):
        """
        Get the shard_groups of this RetentionPolicyManifest.

        :return: The shard_groups of this RetentionPolicyManifest.
        :rtype: list[ShardGroupManifest]
        """
        ...
    @shard_groups.setter
    def shard_groups(self, shard_groups) -> None:
        """
        Get the shard_groups of this RetentionPolicyManifest.

        :return: The shard_groups of this RetentionPolicyManifest.
        :rtype: list[ShardGroupManifest]
        """
        ...
    @property
    def subscriptions(self):
        """
        Get the subscriptions of this RetentionPolicyManifest.

        :return: The subscriptions of this RetentionPolicyManifest.
        :rtype: list[SubscriptionManifest]
        """
        ...
    @subscriptions.setter
    def subscriptions(self, subscriptions) -> None:
        """
        Get the subscriptions of this RetentionPolicyManifest.

        :return: The subscriptions of this RetentionPolicyManifest.
        :rtype: list[SubscriptionManifest]
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
