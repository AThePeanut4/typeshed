"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class PostOrganizationRequest:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, name: Incomplete | None = None, description: Incomplete | None = None) -> None:
        """PostOrganizationRequest - a model defined in OpenAPI."""
        ...
    @property
    def name(self):
        """
        Get the name of this PostOrganizationRequest.

        The name of the organization.

        :return: The name of this PostOrganizationRequest.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this PostOrganizationRequest.

        The name of the organization.

        :return: The name of this PostOrganizationRequest.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this PostOrganizationRequest.

        The description of the organization.

        :return: The description of this PostOrganizationRequest.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this PostOrganizationRequest.

        The description of the organization.

        :return: The description of this PostOrganizationRequest.
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
