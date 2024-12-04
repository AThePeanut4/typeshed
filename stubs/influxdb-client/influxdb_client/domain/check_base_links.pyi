"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class CheckBaseLinks:
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
        _self: Incomplete | None = None,
        labels: Incomplete | None = None,
        members: Incomplete | None = None,
        owners: Incomplete | None = None,
        query: Incomplete | None = None,
    ) -> None:
        """CheckBaseLinks - a model defined in OpenAPI."""
        ...
    @property
    def labels(self):
        """
        Get the labels of this CheckBaseLinks.

        URI of resource.

        :return: The labels of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @labels.setter
    def labels(self, labels) -> None:
        """
        Get the labels of this CheckBaseLinks.

        URI of resource.

        :return: The labels of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @property
    def members(self):
        """
        Get the members of this CheckBaseLinks.

        URI of resource.

        :return: The members of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @members.setter
    def members(self, members) -> None:
        """
        Get the members of this CheckBaseLinks.

        URI of resource.

        :return: The members of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @property
    def owners(self):
        """
        Get the owners of this CheckBaseLinks.

        URI of resource.

        :return: The owners of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @owners.setter
    def owners(self, owners) -> None:
        """
        Get the owners of this CheckBaseLinks.

        URI of resource.

        :return: The owners of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @property
    def query(self):
        """
        Get the query of this CheckBaseLinks.

        URI of resource.

        :return: The query of this CheckBaseLinks.
        :rtype: str
        """
        ...
    @query.setter
    def query(self, query) -> None:
        """
        Get the query of this CheckBaseLinks.

        URI of resource.

        :return: The query of this CheckBaseLinks.
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
