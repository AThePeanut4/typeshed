"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateSummarySummaryStatusRules:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, current_level: Incomplete | None = None, previous_level: Incomplete | None = None) -> None:
        """TemplateSummarySummaryStatusRules - a model defined in OpenAPI."""
        ...
    @property
    def current_level(self):
        """
        Get the current_level of this TemplateSummarySummaryStatusRules.

        :return: The current_level of this TemplateSummarySummaryStatusRules.
        :rtype: str
        """
        ...
    @current_level.setter
    def current_level(self, current_level) -> None:
        """
        Get the current_level of this TemplateSummarySummaryStatusRules.

        :return: The current_level of this TemplateSummarySummaryStatusRules.
        :rtype: str
        """
        ...
    @property
    def previous_level(self):
        """
        Get the previous_level of this TemplateSummarySummaryStatusRules.

        :return: The previous_level of this TemplateSummarySummaryStatusRules.
        :rtype: str
        """
        ...
    @previous_level.setter
    def previous_level(self, previous_level) -> None:
        """
        Get the previous_level of this TemplateSummarySummaryStatusRules.

        :return: The previous_level of this TemplateSummarySummaryStatusRules.
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
