"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TemplateSummaryDiffLabels:
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
        state_status: Incomplete | None = None,
        kind: Incomplete | None = None,
        id: Incomplete | None = None,
        template_meta_name: Incomplete | None = None,
        new: Incomplete | None = None,
        old: Incomplete | None = None,
    ) -> None:
        """TemplateSummaryDiffLabels - a model defined in OpenAPI."""
        ...
    @property
    def state_status(self):
        """
        Get the state_status of this TemplateSummaryDiffLabels.

        :return: The state_status of this TemplateSummaryDiffLabels.
        :rtype: str
        """
        ...
    @state_status.setter
    def state_status(self, state_status) -> None:
        """
        Get the state_status of this TemplateSummaryDiffLabels.

        :return: The state_status of this TemplateSummaryDiffLabels.
        :rtype: str
        """
        ...
    @property
    def kind(self):
        """
        Get the kind of this TemplateSummaryDiffLabels.

        :return: The kind of this TemplateSummaryDiffLabels.
        :rtype: TemplateKind
        """
        ...
    @kind.setter
    def kind(self, kind) -> None:
        """
        Get the kind of this TemplateSummaryDiffLabels.

        :return: The kind of this TemplateSummaryDiffLabels.
        :rtype: TemplateKind
        """
        ...
    @property
    def id(self):
        """
        Get the id of this TemplateSummaryDiffLabels.

        :return: The id of this TemplateSummaryDiffLabels.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this TemplateSummaryDiffLabels.

        :return: The id of this TemplateSummaryDiffLabels.
        :rtype: str
        """
        ...
    @property
    def template_meta_name(self):
        """
        Get the template_meta_name of this TemplateSummaryDiffLabels.

        :return: The template_meta_name of this TemplateSummaryDiffLabels.
        :rtype: str
        """
        ...
    @template_meta_name.setter
    def template_meta_name(self, template_meta_name) -> None:
        """
        Get the template_meta_name of this TemplateSummaryDiffLabels.

        :return: The template_meta_name of this TemplateSummaryDiffLabels.
        :rtype: str
        """
        ...
    @property
    def new(self):
        """
        Get the new of this TemplateSummaryDiffLabels.

        :return: The new of this TemplateSummaryDiffLabels.
        :rtype: TemplateSummaryDiffLabelsNewOld
        """
        ...
    @new.setter
    def new(self, new) -> None:
        """
        Get the new of this TemplateSummaryDiffLabels.

        :return: The new of this TemplateSummaryDiffLabels.
        :rtype: TemplateSummaryDiffLabelsNewOld
        """
        ...
    @property
    def old(self):
        """
        Get the old of this TemplateSummaryDiffLabels.

        :return: The old of this TemplateSummaryDiffLabels.
        :rtype: TemplateSummaryDiffLabelsNewOld
        """
        ...
    @old.setter
    def old(self, old) -> None:
        """
        Get the old of this TemplateSummaryDiffLabels.

        :return: The old of this TemplateSummaryDiffLabels.
        :rtype: TemplateSummaryDiffLabelsNewOld
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
