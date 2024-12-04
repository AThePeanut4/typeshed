"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateSummaryDiffTasksNewOld:
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
        cron: Incomplete | None = None,
        description: Incomplete | None = None,
        every: Incomplete | None = None,
        offset: Incomplete | None = None,
        query: Incomplete | None = None,
        status: Incomplete | None = None,
    ) -> None:
        """TemplateSummaryDiffTasksNewOld - a model defined in OpenAPI."""
        ...
    @property
    def name(self):
        """
        Get the name of this TemplateSummaryDiffTasksNewOld.

        :return: The name of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this TemplateSummaryDiffTasksNewOld.

        :return: The name of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @property
    def cron(self):
        """
        Get the cron of this TemplateSummaryDiffTasksNewOld.

        :return: The cron of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @cron.setter
    def cron(self, cron) -> None:
        """
        Get the cron of this TemplateSummaryDiffTasksNewOld.

        :return: The cron of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this TemplateSummaryDiffTasksNewOld.

        :return: The description of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this TemplateSummaryDiffTasksNewOld.

        :return: The description of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @property
    def every(self):
        """
        Get the every of this TemplateSummaryDiffTasksNewOld.

        :return: The every of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @every.setter
    def every(self, every) -> None:
        """
        Get the every of this TemplateSummaryDiffTasksNewOld.

        :return: The every of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @property
    def offset(self):
        """
        Get the offset of this TemplateSummaryDiffTasksNewOld.

        :return: The offset of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @offset.setter
    def offset(self, offset) -> None:
        """
        Get the offset of this TemplateSummaryDiffTasksNewOld.

        :return: The offset of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @property
    def query(self):
        """
        Get the query of this TemplateSummaryDiffTasksNewOld.

        :return: The query of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @query.setter
    def query(self, query) -> None:
        """
        Get the query of this TemplateSummaryDiffTasksNewOld.

        :return: The query of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @property
    def status(self):
        """
        Get the status of this TemplateSummaryDiffTasksNewOld.

        :return: The status of this TemplateSummaryDiffTasksNewOld.
        :rtype: str
        """
        ...
    @status.setter
    def status(self, status) -> None:
        """
        Get the status of this TemplateSummaryDiffTasksNewOld.

        :return: The status of this TemplateSummaryDiffTasksNewOld.
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
