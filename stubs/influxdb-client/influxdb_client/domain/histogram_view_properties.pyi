"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.view_properties import ViewProperties

class HistogramViewProperties(ViewProperties):
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
        queries: Incomplete | None = None,
        colors: Incomplete | None = None,
        shape: Incomplete | None = None,
        note: Incomplete | None = None,
        show_note_when_empty: Incomplete | None = None,
        x_column: Incomplete | None = None,
        fill_columns: Incomplete | None = None,
        x_domain: Incomplete | None = None,
        x_axis_label: Incomplete | None = None,
        position: Incomplete | None = None,
        bin_count: Incomplete | None = None,
        legend_colorize_rows: Incomplete | None = None,
        legend_hide: Incomplete | None = None,
        legend_opacity: Incomplete | None = None,
        legend_orientation_threshold: Incomplete | None = None,
    ) -> None:
        """HistogramViewProperties - a model defined in OpenAPI."""
        ...
    @property
    def type(self):
        """
        Get the type of this HistogramViewProperties.

        :return: The type of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this HistogramViewProperties.

        :return: The type of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @property
    def queries(self):
        """
        Get the queries of this HistogramViewProperties.

        :return: The queries of this HistogramViewProperties.
        :rtype: list[DashboardQuery]
        """
        ...
    @queries.setter
    def queries(self, queries) -> None:
        """
        Get the queries of this HistogramViewProperties.

        :return: The queries of this HistogramViewProperties.
        :rtype: list[DashboardQuery]
        """
        ...
    @property
    def colors(self):
        """
        Get the colors of this HistogramViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this HistogramViewProperties.
        :rtype: list[DashboardColor]
        """
        ...
    @colors.setter
    def colors(self, colors) -> None:
        """
        Get the colors of this HistogramViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this HistogramViewProperties.
        :rtype: list[DashboardColor]
        """
        ...
    @property
    def shape(self):
        """
        Get the shape of this HistogramViewProperties.

        :return: The shape of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @shape.setter
    def shape(self, shape) -> None:
        """
        Get the shape of this HistogramViewProperties.

        :return: The shape of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @property
    def note(self):
        """
        Get the note of this HistogramViewProperties.

        :return: The note of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @note.setter
    def note(self, note) -> None:
        """
        Get the note of this HistogramViewProperties.

        :return: The note of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @property
    def show_note_when_empty(self):
        """
        Get the show_note_when_empty of this HistogramViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this HistogramViewProperties.
        :rtype: bool
        """
        ...
    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty) -> None:
        """
        Get the show_note_when_empty of this HistogramViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this HistogramViewProperties.
        :rtype: bool
        """
        ...
    @property
    def x_column(self):
        """
        Get the x_column of this HistogramViewProperties.

        :return: The x_column of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @x_column.setter
    def x_column(self, x_column) -> None:
        """
        Get the x_column of this HistogramViewProperties.

        :return: The x_column of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @property
    def fill_columns(self):
        """
        Get the fill_columns of this HistogramViewProperties.

        :return: The fill_columns of this HistogramViewProperties.
        :rtype: list[str]
        """
        ...
    @fill_columns.setter
    def fill_columns(self, fill_columns) -> None:
        """
        Get the fill_columns of this HistogramViewProperties.

        :return: The fill_columns of this HistogramViewProperties.
        :rtype: list[str]
        """
        ...
    @property
    def x_domain(self):
        """
        Get the x_domain of this HistogramViewProperties.

        :return: The x_domain of this HistogramViewProperties.
        :rtype: list[float]
        """
        ...
    @x_domain.setter
    def x_domain(self, x_domain) -> None:
        """
        Get the x_domain of this HistogramViewProperties.

        :return: The x_domain of this HistogramViewProperties.
        :rtype: list[float]
        """
        ...
    @property
    def x_axis_label(self):
        """
        Get the x_axis_label of this HistogramViewProperties.

        :return: The x_axis_label of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @x_axis_label.setter
    def x_axis_label(self, x_axis_label) -> None:
        """
        Get the x_axis_label of this HistogramViewProperties.

        :return: The x_axis_label of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @property
    def position(self):
        """
        Get the position of this HistogramViewProperties.

        :return: The position of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @position.setter
    def position(self, position) -> None:
        """
        Get the position of this HistogramViewProperties.

        :return: The position of this HistogramViewProperties.
        :rtype: str
        """
        ...
    @property
    def bin_count(self):
        """
        Get the bin_count of this HistogramViewProperties.

        :return: The bin_count of this HistogramViewProperties.
        :rtype: int
        """
        ...
    @bin_count.setter
    def bin_count(self, bin_count) -> None:
        """
        Get the bin_count of this HistogramViewProperties.

        :return: The bin_count of this HistogramViewProperties.
        :rtype: int
        """
        ...
    @property
    def legend_colorize_rows(self):
        """
        Get the legend_colorize_rows of this HistogramViewProperties.

        :return: The legend_colorize_rows of this HistogramViewProperties.
        :rtype: bool
        """
        ...
    @legend_colorize_rows.setter
    def legend_colorize_rows(self, legend_colorize_rows) -> None:
        """
        Get the legend_colorize_rows of this HistogramViewProperties.

        :return: The legend_colorize_rows of this HistogramViewProperties.
        :rtype: bool
        """
        ...
    @property
    def legend_hide(self):
        """
        Get the legend_hide of this HistogramViewProperties.

        :return: The legend_hide of this HistogramViewProperties.
        :rtype: bool
        """
        ...
    @legend_hide.setter
    def legend_hide(self, legend_hide) -> None:
        """
        Get the legend_hide of this HistogramViewProperties.

        :return: The legend_hide of this HistogramViewProperties.
        :rtype: bool
        """
        ...
    @property
    def legend_opacity(self):
        """
        Get the legend_opacity of this HistogramViewProperties.

        :return: The legend_opacity of this HistogramViewProperties.
        :rtype: float
        """
        ...
    @legend_opacity.setter
    def legend_opacity(self, legend_opacity) -> None:
        """
        Get the legend_opacity of this HistogramViewProperties.

        :return: The legend_opacity of this HistogramViewProperties.
        :rtype: float
        """
        ...
    @property
    def legend_orientation_threshold(self):
        """
        Get the legend_orientation_threshold of this HistogramViewProperties.

        :return: The legend_orientation_threshold of this HistogramViewProperties.
        :rtype: int
        """
        ...
    @legend_orientation_threshold.setter
    def legend_orientation_threshold(self, legend_orientation_threshold) -> None:
        """
        Get the legend_orientation_threshold of this HistogramViewProperties.

        :return: The legend_orientation_threshold of this HistogramViewProperties.
        :rtype: int
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
