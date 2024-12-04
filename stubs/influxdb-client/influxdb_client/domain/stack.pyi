"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Stack:
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
        id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        created_at: Incomplete | None = None,
        events: Incomplete | None = None,
    ) -> None:
        """Stack - a model defined in OpenAPI."""
        ...
    @property
    def id(self):
        """
        Get the id of this Stack.

        :return: The id of this Stack.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this Stack.

        :return: The id of this Stack.
        :rtype: str
        """
        ...
    @property
    def org_id(self):
        """
        Get the org_id of this Stack.

        :return: The org_id of this Stack.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id) -> None:
        """
        Get the org_id of this Stack.

        :return: The org_id of this Stack.
        :rtype: str
        """
        ...
    @property
    def created_at(self):
        """
        Get the created_at of this Stack.

        :return: The created_at of this Stack.
        :rtype: datetime
        """
        ...
    @created_at.setter
    def created_at(self, created_at) -> None:
        """
        Get the created_at of this Stack.

        :return: The created_at of this Stack.
        :rtype: datetime
        """
        ...
    @property
    def events(self):
        """
        Get the events of this Stack.

        :return: The events of this Stack.
        :rtype: list[StackEvents]
        """
        ...
    @events.setter
    def events(self, events) -> None:
        """
        Get the events of this Stack.

        :return: The events of this Stack.
        :rtype: list[StackEvents]
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
