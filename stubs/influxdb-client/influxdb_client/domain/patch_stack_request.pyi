"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class PatchStackRequest:
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
        description: Incomplete | None = None,
        template_ur_ls: Incomplete | None = None,
        additional_resources: Incomplete | None = None,
    ) -> None:
        """PatchStackRequest - a model defined in OpenAPI."""
        ...
    @property
    def name(self):
        """
        Get the name of this PatchStackRequest.

        :return: The name of this PatchStackRequest.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this PatchStackRequest.

        :return: The name of this PatchStackRequest.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this PatchStackRequest.

        :return: The description of this PatchStackRequest.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this PatchStackRequest.

        :return: The description of this PatchStackRequest.
        :rtype: str
        """
        ...
    @property
    def template_ur_ls(self):
        """
        Get the template_ur_ls of this PatchStackRequest.

        :return: The template_ur_ls of this PatchStackRequest.
        :rtype: list[str]
        """
        ...
    @template_ur_ls.setter
    def template_ur_ls(self, template_ur_ls) -> None:
        """
        Get the template_ur_ls of this PatchStackRequest.

        :return: The template_ur_ls of this PatchStackRequest.
        :rtype: list[str]
        """
        ...
    @property
    def additional_resources(self):
        """
        Get the additional_resources of this PatchStackRequest.

        :return: The additional_resources of this PatchStackRequest.
        :rtype: list[PatchStackRequestAdditionalResources]
        """
        ...
    @additional_resources.setter
    def additional_resources(self, additional_resources) -> None:
        """
        Get the additional_resources of this PatchStackRequest.

        :return: The additional_resources of this PatchStackRequest.
        :rtype: list[PatchStackRequestAdditionalResources]
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
