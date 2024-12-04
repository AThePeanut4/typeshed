"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class LabelsResponse:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, labels: Incomplete | None = None, links: Incomplete | None = None) -> None:
        """LabelsResponse - a model defined in OpenAPI."""
        ...
    @property
    def labels(self):
        """
        Get the labels of this LabelsResponse.

        :return: The labels of this LabelsResponse.
        :rtype: list[Label]
        """
        ...
    @labels.setter
    def labels(self, labels) -> None:
        """
        Get the labels of this LabelsResponse.

        :return: The labels of this LabelsResponse.
        :rtype: list[Label]
        """
        ...
    @property
    def links(self):
        """
        Get the links of this LabelsResponse.

        :return: The links of this LabelsResponse.
        :rtype: Links
        """
        ...
    @links.setter
    def links(self, links) -> None:
        """
        Get the links of this LabelsResponse.

        :return: The links of this LabelsResponse.
        :rtype: Links
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
