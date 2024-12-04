"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateApplyTemplate:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, content_type: Incomplete | None = None, sources: Incomplete | None = None, contents: Incomplete | None = None
    ) -> None:
        """TemplateApplyTemplate - a model defined in OpenAPI."""
        ...
    @property
    def content_type(self):
        """
        Get the content_type of this TemplateApplyTemplate.

        :return: The content_type of this TemplateApplyTemplate.
        :rtype: str
        """
        ...
    @content_type.setter
    def content_type(self, content_type) -> None:
        """
        Get the content_type of this TemplateApplyTemplate.

        :return: The content_type of this TemplateApplyTemplate.
        :rtype: str
        """
        ...
    @property
    def sources(self):
        """
        Get the sources of this TemplateApplyTemplate.

        :return: The sources of this TemplateApplyTemplate.
        :rtype: list[str]
        """
        ...
    @sources.setter
    def sources(self, sources) -> None:
        """
        Get the sources of this TemplateApplyTemplate.

        :return: The sources of this TemplateApplyTemplate.
        :rtype: list[str]
        """
        ...
    @property
    def contents(self):
        """
        Get the contents of this TemplateApplyTemplate.

        :return: The contents of this TemplateApplyTemplate.
        :rtype: list[object]
        """
        ...
    @contents.setter
    def contents(self, contents) -> None:
        """
        Get the contents of this TemplateApplyTemplate.

        :return: The contents of this TemplateApplyTemplate.
        :rtype: list[object]
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
