"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.notification_endpoint_discriminator import NotificationEndpointDiscriminator

class SlackNotificationEndpoint(NotificationEndpointDiscriminator):
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
        url: Incomplete | None = None,
        token: Incomplete | None = None,
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
        type: str = "slack",
    ) -> None:
        """SlackNotificationEndpoint - a model defined in OpenAPI."""
        ...
    @property
    def url(self):
        """
        Get the url of this SlackNotificationEndpoint.

        Specifies the URL of the Slack endpoint. Specify either `URL` or `Token`.

        :return: The url of this SlackNotificationEndpoint.
        :rtype: str
        """
        ...
    @url.setter
    def url(self, url) -> None:
        """
        Get the url of this SlackNotificationEndpoint.

        Specifies the URL of the Slack endpoint. Specify either `URL` or `Token`.

        :return: The url of this SlackNotificationEndpoint.
        :rtype: str
        """
        ...
    @property
    def token(self):
        """
        Get the token of this SlackNotificationEndpoint.

        Specifies the API token string. Specify either `URL` or `Token`.

        :return: The token of this SlackNotificationEndpoint.
        :rtype: str
        """
        ...
    @token.setter
    def token(self, token) -> None:
        """
        Get the token of this SlackNotificationEndpoint.

        Specifies the API token string. Specify either `URL` or `Token`.

        :return: The token of this SlackNotificationEndpoint.
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
