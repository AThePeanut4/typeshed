"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Bucket:
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
        links: Incomplete | None = None,
        id: str | None = None,
        type: str = "user",
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        org_id: str | None = None,
        rp: Incomplete | None = None,
        schema_type: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        retention_rules: Incomplete | None = None,
        labels: Incomplete | None = None,
    ) -> None:
        """Bucket - a model defined in OpenAPI."""
        ...
    @property
    def links(self):
        """
        Get the links of this Bucket.

        :return: The links of this Bucket.
        :rtype: BucketLinks
        """
        ...
    @links.setter
    def links(self, links) -> None:
        """
        Get the links of this Bucket.

        :return: The links of this Bucket.
        :rtype: BucketLinks
        """
        ...
    @property
    def id(self) -> str | None:
        """
        Get the id of this Bucket.

        :return: The id of this Bucket.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id: str) -> None:
        """
        Get the id of this Bucket.

        :return: The id of this Bucket.
        :rtype: str
        """
        ...
    @property
    def type(self):
        """
        Get the type of this Bucket.

        :return: The type of this Bucket.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this Bucket.

        :return: The type of this Bucket.
        :rtype: str
        """
        ...
    @property
    def name(self):
        """
        Get the name of this Bucket.

        :return: The name of this Bucket.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this Bucket.

        :return: The name of this Bucket.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this Bucket.

        :return: The description of this Bucket.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this Bucket.

        :return: The description of this Bucket.
        :rtype: str
        """
        ...
    @property
    def org_id(self) -> str | None:
        """
        Get the org_id of this Bucket.

        :return: The org_id of this Bucket.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id: str) -> None:
        """
        Get the org_id of this Bucket.

        :return: The org_id of this Bucket.
        :rtype: str
        """
        ...
    @property
    def rp(self):
        """
        Get the rp of this Bucket.

        :return: The rp of this Bucket.
        :rtype: str
        """
        ...
    @rp.setter
    def rp(self, rp) -> None:
        """
        Get the rp of this Bucket.

        :return: The rp of this Bucket.
        :rtype: str
        """
        ...
    @property
    def schema_type(self):
        """
        Get the schema_type of this Bucket.

        :return: The schema_type of this Bucket.
        :rtype: SchemaType
        """
        ...
    @schema_type.setter
    def schema_type(self, schema_type) -> None:
        """
        Get the schema_type of this Bucket.

        :return: The schema_type of this Bucket.
        :rtype: SchemaType
        """
        ...
    @property
    def created_at(self):
        """
        Get the created_at of this Bucket.

        :return: The created_at of this Bucket.
        :rtype: datetime
        """
        ...
    @created_at.setter
    def created_at(self, created_at) -> None:
        """
        Get the created_at of this Bucket.

        :return: The created_at of this Bucket.
        :rtype: datetime
        """
        ...
    @property
    def updated_at(self):
        """
        Get the updated_at of this Bucket.

        :return: The updated_at of this Bucket.
        :rtype: datetime
        """
        ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None:
        """
        Get the updated_at of this Bucket.

        :return: The updated_at of this Bucket.
        :rtype: datetime
        """
        ...
    @property
    def retention_rules(self):
        """
        Get the retention_rules of this Bucket.

        Retention rules to expire or retain data. The InfluxDB `/api/v2` API uses `RetentionRules` to configure the [retention period](https://docs.influxdata.com/influxdb/latest/reference/glossary/#retention-period).  #### InfluxDB Cloud  - `retentionRules` is required.  #### InfluxDB OSS  - `retentionRules` isn't required.

        :return: The retention_rules of this Bucket.
        :rtype: list[BucketRetentionRules]
        """
        ...
    @retention_rules.setter
    def retention_rules(self, retention_rules) -> None:
        """
        Get the retention_rules of this Bucket.

        Retention rules to expire or retain data. The InfluxDB `/api/v2` API uses `RetentionRules` to configure the [retention period](https://docs.influxdata.com/influxdb/latest/reference/glossary/#retention-period).  #### InfluxDB Cloud  - `retentionRules` is required.  #### InfluxDB OSS  - `retentionRules` isn't required.

        :return: The retention_rules of this Bucket.
        :rtype: list[BucketRetentionRules]
        """
        ...
    @property
    def labels(self):
        """
        Get the labels of this Bucket.

        :return: The labels of this Bucket.
        :rtype: list[Label]
        """
        ...
    @labels.setter
    def labels(self, labels) -> None:
        """
        Get the labels of this Bucket.

        :return: The labels of this Bucket.
        :rtype: list[Label]
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
