"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateExportByNameResources:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, kind: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """TemplateExportByNameResources - a model defined in OpenAPI."""
        ...
    @property
    def kind(self):
        """
        Get the kind of this TemplateExportByNameResources.

        :return: The kind of this TemplateExportByNameResources.
        :rtype: TemplateKind
        """
        ...
    @kind.setter
    def kind(self, kind) -> None:
        """
        Get the kind of this TemplateExportByNameResources.

        :return: The kind of this TemplateExportByNameResources.
        :rtype: TemplateKind
        """
        ...
    @property
    def name(self):
        """
        Get the name of this TemplateExportByNameResources.

        :return: The name of this TemplateExportByNameResources.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this TemplateExportByNameResources.

        :return: The name of this TemplateExportByNameResources.
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
