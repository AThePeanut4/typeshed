"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateSummaryDiffNotificationEndpoints:
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
        kind: Incomplete | None = None,
        state_status: Incomplete | None = None,
        id: Incomplete | None = None,
        template_meta_name: Incomplete | None = None,
        new: Incomplete | None = None,
        old: Incomplete | None = None,
    ) -> None:
        """TemplateSummaryDiffNotificationEndpoints - a model defined in OpenAPI."""
        ...
    @property
    def kind(self):
        """
        Get the kind of this TemplateSummaryDiffNotificationEndpoints.

        :return: The kind of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: TemplateKind
        """
        ...
    @kind.setter
    def kind(self, kind) -> None:
        """
        Get the kind of this TemplateSummaryDiffNotificationEndpoints.

        :return: The kind of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: TemplateKind
        """
        ...
    @property
    def state_status(self):
        """
        Get the state_status of this TemplateSummaryDiffNotificationEndpoints.

        :return: The state_status of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: str
        """
        ...
    @state_status.setter
    def state_status(self, state_status) -> None:
        """
        Get the state_status of this TemplateSummaryDiffNotificationEndpoints.

        :return: The state_status of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: str
        """
        ...
    @property
    def id(self):
        """
        Get the id of this TemplateSummaryDiffNotificationEndpoints.

        :return: The id of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this TemplateSummaryDiffNotificationEndpoints.

        :return: The id of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: str
        """
        ...
    @property
    def template_meta_name(self):
        """
        Get the template_meta_name of this TemplateSummaryDiffNotificationEndpoints.

        :return: The template_meta_name of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: str
        """
        ...
    @template_meta_name.setter
    def template_meta_name(self, template_meta_name) -> None:
        """
        Get the template_meta_name of this TemplateSummaryDiffNotificationEndpoints.

        :return: The template_meta_name of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: str
        """
        ...
    @property
    def new(self):
        """
        Get the new of this TemplateSummaryDiffNotificationEndpoints.

        :return: The new of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: NotificationEndpointDiscriminator
        """
        ...
    @new.setter
    def new(self, new) -> None:
        """
        Get the new of this TemplateSummaryDiffNotificationEndpoints.

        :return: The new of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: NotificationEndpointDiscriminator
        """
        ...
    @property
    def old(self):
        """
        Get the old of this TemplateSummaryDiffNotificationEndpoints.

        :return: The old of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: NotificationEndpointDiscriminator
        """
        ...
    @old.setter
    def old(self, old) -> None:
        """
        Get the old of this TemplateSummaryDiffNotificationEndpoints.

        :return: The old of this TemplateSummaryDiffNotificationEndpoints.
        :rtype: NotificationEndpointDiscriminator
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
