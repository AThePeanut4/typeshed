"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateSummaryDiffBucketsNewOld:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, name: Incomplete | None = None, description: Incomplete | None = None, retention_rules: Incomplete | None = None
    ) -> None:
        """TemplateSummaryDiffBucketsNewOld - a model defined in OpenAPI."""
        ...
    @property
    def name(self):
        """
        Get the name of this TemplateSummaryDiffBucketsNewOld.

        :return: The name of this TemplateSummaryDiffBucketsNewOld.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this TemplateSummaryDiffBucketsNewOld.

        :return: The name of this TemplateSummaryDiffBucketsNewOld.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this TemplateSummaryDiffBucketsNewOld.

        :return: The description of this TemplateSummaryDiffBucketsNewOld.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this TemplateSummaryDiffBucketsNewOld.

        :return: The description of this TemplateSummaryDiffBucketsNewOld.
        :rtype: str
        """
        ...
    @property
    def retention_rules(self):
        """
        Get the retention_rules of this TemplateSummaryDiffBucketsNewOld.

        Retention rules to expire or retain data. The InfluxDB `/api/v2` API uses `RetentionRules` to configure the [retention period](https://docs.influxdata.com/influxdb/latest/reference/glossary/#retention-period).  #### InfluxDB Cloud  - `retentionRules` is required.  #### InfluxDB OSS  - `retentionRules` isn't required.

        :return: The retention_rules of this TemplateSummaryDiffBucketsNewOld.
        :rtype: list[BucketRetentionRules]
        """
        ...
    @retention_rules.setter
    def retention_rules(self, retention_rules) -> None:
        """
        Get the retention_rules of this TemplateSummaryDiffBucketsNewOld.

        Retention rules to expire or retain data. The InfluxDB `/api/v2` API uses `RetentionRules` to configure the [retention period](https://docs.influxdata.com/influxdb/latest/reference/glossary/#retention-period).  #### InfluxDB Cloud  - `retentionRules` is required.  #### InfluxDB OSS  - `retentionRules` isn't required.

        :return: The retention_rules of this TemplateSummaryDiffBucketsNewOld.
        :rtype: list[BucketRetentionRules]
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
