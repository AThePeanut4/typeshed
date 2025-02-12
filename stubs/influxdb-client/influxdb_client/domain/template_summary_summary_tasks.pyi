"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateSummarySummaryTasks:
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
        template_meta_name: Incomplete | None = None,
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        cron: Incomplete | None = None,
        description: Incomplete | None = None,
        every: Incomplete | None = None,
        offset: Incomplete | None = None,
        query: Incomplete | None = None,
        status: Incomplete | None = None,
        env_references: Incomplete | None = None,
    ) -> None:
        """TemplateSummarySummaryTasks - a model defined in OpenAPI."""
        ...
    @property
    def kind(self):
        """
        Get the kind of this TemplateSummarySummaryTasks.

        :return: The kind of this TemplateSummarySummaryTasks.
        :rtype: TemplateKind
        """
        ...
    @kind.setter
    def kind(self, kind) -> None:
        """
        Get the kind of this TemplateSummarySummaryTasks.

        :return: The kind of this TemplateSummarySummaryTasks.
        :rtype: TemplateKind
        """
        ...
    @property
    def template_meta_name(self):
        """
        Get the template_meta_name of this TemplateSummarySummaryTasks.

        :return: The template_meta_name of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @template_meta_name.setter
    def template_meta_name(self, template_meta_name) -> None:
        """
        Get the template_meta_name of this TemplateSummarySummaryTasks.

        :return: The template_meta_name of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def id(self):
        """
        Get the id of this TemplateSummarySummaryTasks.

        :return: The id of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this TemplateSummarySummaryTasks.

        :return: The id of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def name(self):
        """
        Get the name of this TemplateSummarySummaryTasks.

        :return: The name of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this TemplateSummarySummaryTasks.

        :return: The name of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def cron(self):
        """
        Get the cron of this TemplateSummarySummaryTasks.

        :return: The cron of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @cron.setter
    def cron(self, cron) -> None:
        """
        Get the cron of this TemplateSummarySummaryTasks.

        :return: The cron of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this TemplateSummarySummaryTasks.

        :return: The description of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this TemplateSummarySummaryTasks.

        :return: The description of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def every(self):
        """
        Get the every of this TemplateSummarySummaryTasks.

        :return: The every of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @every.setter
    def every(self, every) -> None:
        """
        Get the every of this TemplateSummarySummaryTasks.

        :return: The every of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def offset(self):
        """
        Get the offset of this TemplateSummarySummaryTasks.

        :return: The offset of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @offset.setter
    def offset(self, offset) -> None:
        """
        Get the offset of this TemplateSummarySummaryTasks.

        :return: The offset of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def query(self):
        """
        Get the query of this TemplateSummarySummaryTasks.

        :return: The query of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @query.setter
    def query(self, query) -> None:
        """
        Get the query of this TemplateSummarySummaryTasks.

        :return: The query of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def status(self):
        """
        Get the status of this TemplateSummarySummaryTasks.

        :return: The status of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @status.setter
    def status(self, status) -> None:
        """
        Get the status of this TemplateSummarySummaryTasks.

        :return: The status of this TemplateSummarySummaryTasks.
        :rtype: str
        """
        ...
    @property
    def env_references(self):
        """
        Get the env_references of this TemplateSummarySummaryTasks.

        :return: The env_references of this TemplateSummarySummaryTasks.
        :rtype: list[object]
        """
        ...
    @env_references.setter
    def env_references(self, env_references) -> None:
        """
        Get the env_references of this TemplateSummarySummaryTasks.

        :return: The env_references of this TemplateSummarySummaryTasks.
        :rtype: list[object]
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
