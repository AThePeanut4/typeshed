"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.notification_rule_discriminator import NotificationRuleDiscriminator

class TelegramNotificationRuleBase(NotificationRuleDiscriminator):
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
        message_template: Incomplete | None = None,
        parse_mode: Incomplete | None = None,
        disable_web_page_preview: Incomplete | None = None,
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
        """TelegramNotificationRuleBase - a model defined in OpenAPI."""
        ...
    @property
    def type(self):
        """
        Get the type of this TelegramNotificationRuleBase.

        The discriminator between other types of notification rules is "telegram".

        :return: The type of this TelegramNotificationRuleBase.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this TelegramNotificationRuleBase.

        The discriminator between other types of notification rules is "telegram".

        :return: The type of this TelegramNotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def message_template(self):
        """
        Get the message_template of this TelegramNotificationRuleBase.

        The message template as a flux interpolated string.

        :return: The message_template of this TelegramNotificationRuleBase.
        :rtype: str
        """
        ...
    @message_template.setter
    def message_template(self, message_template) -> None:
        """
        Get the message_template of this TelegramNotificationRuleBase.

        The message template as a flux interpolated string.

        :return: The message_template of this TelegramNotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def parse_mode(self):
        """
        Get the parse_mode of this TelegramNotificationRuleBase.

        Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options. Defaults to "MarkdownV2".

        :return: The parse_mode of this TelegramNotificationRuleBase.
        :rtype: str
        """
        ...
    @parse_mode.setter
    def parse_mode(self, parse_mode) -> None:
        """
        Get the parse_mode of this TelegramNotificationRuleBase.

        Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options. Defaults to "MarkdownV2".

        :return: The parse_mode of this TelegramNotificationRuleBase.
        :rtype: str
        """
        ...
    @property
    def disable_web_page_preview(self):
        """
        Get the disable_web_page_preview of this TelegramNotificationRuleBase.

        Disables preview of web links in the sent messages when "true". Defaults to "false".

        :return: The disable_web_page_preview of this TelegramNotificationRuleBase.
        :rtype: bool
        """
        ...
    @disable_web_page_preview.setter
    def disable_web_page_preview(self, disable_web_page_preview) -> None:
        """
        Get the disable_web_page_preview of this TelegramNotificationRuleBase.

        Disables preview of web links in the sent messages when "true". Defaults to "false".

        :return: The disable_web_page_preview of this TelegramNotificationRuleBase.
        :rtype: bool
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
