"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class NotificationEndpointBase:
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
        user_id: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        description: Incomplete | None = None,
        name: Incomplete | None = None,
        status: str = "active",
        labels: Incomplete | None = None,
        links: Incomplete | None = None,
        type: Incomplete | None = None,
    ) -> None:
        """NotificationEndpointBase - a model defined in OpenAPI."""
        ...
    @property
    def id(self):
        """
        Get the id of this NotificationEndpointBase.

        :return: The id of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this NotificationEndpointBase.

        :return: The id of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @property
    def org_id(self):
        """
        Get the org_id of this NotificationEndpointBase.

        :return: The org_id of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id) -> None:
        """
        Get the org_id of this NotificationEndpointBase.

        :return: The org_id of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @property
    def user_id(self):
        """
        Get the user_id of this NotificationEndpointBase.

        :return: The user_id of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @user_id.setter
    def user_id(self, user_id) -> None:
        """
        Get the user_id of this NotificationEndpointBase.

        :return: The user_id of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @property
    def created_at(self):
        """
        Get the created_at of this NotificationEndpointBase.

        :return: The created_at of this NotificationEndpointBase.
        :rtype: datetime
        """
        ...
    @created_at.setter
    def created_at(self, created_at) -> None:
        """
        Get the created_at of this NotificationEndpointBase.

        :return: The created_at of this NotificationEndpointBase.
        :rtype: datetime
        """
        ...
    @property
    def updated_at(self):
        """
        Get the updated_at of this NotificationEndpointBase.

        :return: The updated_at of this NotificationEndpointBase.
        :rtype: datetime
        """
        ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None:
        """
        Get the updated_at of this NotificationEndpointBase.

        :return: The updated_at of this NotificationEndpointBase.
        :rtype: datetime
        """
        ...
    @property
    def description(self):
        """
        Get the description of this NotificationEndpointBase.

        An optional description of the notification endpoint.

        :return: The description of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this NotificationEndpointBase.

        An optional description of the notification endpoint.

        :return: The description of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @property
    def name(self):
        """
        Get the name of this NotificationEndpointBase.

        :return: The name of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this NotificationEndpointBase.

        :return: The name of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @property
    def status(self):
        """
        Get the status of this NotificationEndpointBase.

        The status of the endpoint.

        :return: The status of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @status.setter
    def status(self, status) -> None:
        """
        Get the status of this NotificationEndpointBase.

        The status of the endpoint.

        :return: The status of this NotificationEndpointBase.
        :rtype: str
        """
        ...
    @property
    def labels(self):
        """
        Get the labels of this NotificationEndpointBase.

        :return: The labels of this NotificationEndpointBase.
        :rtype: list[Label]
        """
        ...
    @labels.setter
    def labels(self, labels) -> None:
        """
        Get the labels of this NotificationEndpointBase.

        :return: The labels of this NotificationEndpointBase.
        :rtype: list[Label]
        """
        ...
    @property
    def links(self):
        """
        Get the links of this NotificationEndpointBase.

        :return: The links of this NotificationEndpointBase.
        :rtype: NotificationEndpointBaseLinks
        """
        ...
    @links.setter
    def links(self, links) -> None:
        """
        Get the links of this NotificationEndpointBase.

        :return: The links of this NotificationEndpointBase.
        :rtype: NotificationEndpointBaseLinks
        """
        ...
    @property
    def type(self):
        """
        Get the type of this NotificationEndpointBase.

        :return: The type of this NotificationEndpointBase.
        :rtype: NotificationEndpointType
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this NotificationEndpointBase.

        :return: The type of this NotificationEndpointBase.
        :rtype: NotificationEndpointType
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
