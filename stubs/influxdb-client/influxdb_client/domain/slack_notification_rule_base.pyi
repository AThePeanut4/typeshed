"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.notification_rule_discriminator import NotificationRuleDiscriminator

class SlackNotificationRuleBase(NotificationRuleDiscriminator):
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
        type: Incomplete | None = None,
        channel: Incomplete | None = None,
        message_template: Incomplete | None = None,
        latest_completed: Incomplete | None = None,
        last_run_status: Incomplete | None = None,
        last_run_error: Incomplete | None = None,
        id: Incomplete | None = None,
        endpoint_id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        task_id: Incomplete | None = None,
        owner_id: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        status: Incomplete | None = None,
        name: Incomplete | None = None,
        sleep_until: Incomplete | None = None,
        every: Incomplete | None = None,
        offset: Incomplete | None = None,
        runbook_link: Incomplete | None = None,
        limit_every: Incomplete | None = None,
        limit: Incomplete | None = None,
        tag_rules: Incomplete | None = None,
        description: Incomplete | None = None,
        status_rules: Incomplete | None = None,
        labels: Incomplete | None = None,
        links: Incomplete | None = None,
    ) -> None:
        """SlackNotificationRuleBase - a model defined in OpenAPI."""
        ...
    @property
    def type(self):
        """
        Get the type of this SlackNotificationRuleBase.

        :return: The type of this SlackNotificationRuleBase.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this SlackNotificationRuleBase.

        :return: The type of this SlackNotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def channel(self):
        """
        Get the channel of this SlackNotificationRuleBase.

        :return: The channel of this SlackNotificationRuleBase.
        :rtype: str
        """
        ...
    @channel.setter
    def channel(self, channel) -> None:
        """
        Get the channel of this SlackNotificationRuleBase.

        :return: The channel of this SlackNotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def message_template(self):
        """
        Get the message_template of this SlackNotificationRuleBase.

        :return: The message_template of this SlackNotificationRuleBase.
        :rtype: str
        """
        ...
    @message_template.setter
    def message_template(self, message_template) -> None:
        """
        Get the message_template of this SlackNotificationRuleBase.

        :return: The message_template of this SlackNotificationRuleBase.
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
