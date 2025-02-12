"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.create_dashboard_request import CreateDashboardRequest

class DashboardWithViewProperties(CreateDashboardRequest):
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
        links: Incomplete | None = None,
        id: Incomplete | None = None,
        meta: Incomplete | None = None,
        cells: Incomplete | None = None,
        labels: Incomplete | None = None,
        org_id: Incomplete | None = None,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
    ) -> None:
        """DashboardWithViewProperties - a model defined in OpenAPI."""
        ...
    @property
    def links(self):
        """
        Get the links of this DashboardWithViewProperties.

        :return: The links of this DashboardWithViewProperties.
        :rtype: object
        """
        ...
    @links.setter
    def links(self, links) -> None:
        """
        Get the links of this DashboardWithViewProperties.

        :return: The links of this DashboardWithViewProperties.
        :rtype: object
        """
        ...
    @property
    def id(self):
        """
        Get the id of this DashboardWithViewProperties.

        :return: The id of this DashboardWithViewProperties.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this DashboardWithViewProperties.

        :return: The id of this DashboardWithViewProperties.
        :rtype: str
        """
        ...
    @property
    def meta(self):
        """
        Get the meta of this DashboardWithViewProperties.

        :return: The meta of this DashboardWithViewProperties.
        :rtype: object
        """
        ...
    @meta.setter
    def meta(self, meta) -> None:
        """
        Get the meta of this DashboardWithViewProperties.

        :return: The meta of this DashboardWithViewProperties.
        :rtype: object
        """
        ...
    @property
    def cells(self):
        """
        Get the cells of this DashboardWithViewProperties.

        :return: The cells of this DashboardWithViewProperties.
        :rtype: list[CellWithViewProperties]
        """
        ...
    @cells.setter
    def cells(self, cells) -> None:
        """
        Get the cells of this DashboardWithViewProperties.

        :return: The cells of this DashboardWithViewProperties.
        :rtype: list[CellWithViewProperties]
        """
        ...
    @property
    def labels(self):
        """
        Get the labels of this DashboardWithViewProperties.

        :return: The labels of this DashboardWithViewProperties.
        :rtype: list[Label]
        """
        ...
    @labels.setter
    def labels(self, labels) -> None:
        """
        Get the labels of this DashboardWithViewProperties.

        :return: The labels of this DashboardWithViewProperties.
        :rtype: list[Label]
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
