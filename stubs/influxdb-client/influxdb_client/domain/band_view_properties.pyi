"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.view_properties import ViewProperties

class BandViewProperties(ViewProperties):
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
        adaptive_zoom_hide: bool | None = None,
        time_format: Incomplete | None = None,
        type: Incomplete | None = None,
        queries: Incomplete | None = None,
        colors: Incomplete | None = None,
        shape: Incomplete | None = None,
        note: Incomplete | None = None,
        show_note_when_empty: Incomplete | None = None,
        axes: Incomplete | None = None,
        static_legend: Incomplete | None = None,
        x_column: Incomplete | None = None,
        generate_x_axis_ticks: Incomplete | None = None,
        x_total_ticks: Incomplete | None = None,
        x_tick_start: Incomplete | None = None,
        x_tick_step: Incomplete | None = None,
        y_column: Incomplete | None = None,
        generate_y_axis_ticks: Incomplete | None = None,
        y_total_ticks: Incomplete | None = None,
        y_tick_start: Incomplete | None = None,
        y_tick_step: Incomplete | None = None,
        upper_column: Incomplete | None = None,
        main_column: Incomplete | None = None,
        lower_column: Incomplete | None = None,
        hover_dimension: Incomplete | None = None,
        geom: Incomplete | None = None,
        legend_colorize_rows: Incomplete | None = None,
        legend_hide: Incomplete | None = None,
        legend_opacity: Incomplete | None = None,
        legend_orientation_threshold: Incomplete | None = None,
    ) -> None:
        """BandViewProperties - a model defined in OpenAPI."""
        ...
    adaptive_zoom_hide: bool | None
    @property
    def time_format(self):
        """
        Get the time_format of this BandViewProperties.

        :return: The time_format of this BandViewProperties.
        :rtype: str
        """
        ...
    @time_format.setter
    def time_format(self, time_format) -> None:
        """
        Get the time_format of this BandViewProperties.

        :return: The time_format of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def type(self):
        """
        Get the type of this BandViewProperties.

        :return: The type of this BandViewProperties.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this BandViewProperties.

        :return: The type of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def queries(self):
        """
        Get the queries of this BandViewProperties.

        :return: The queries of this BandViewProperties.
        :rtype: list[DashboardQuery]
        """
        ...
    @queries.setter
    def queries(self, queries) -> None:
        """
        Get the queries of this BandViewProperties.

        :return: The queries of this BandViewProperties.
        :rtype: list[DashboardQuery]
        """
        ...
    @property
    def colors(self):
        """
        Get the colors of this BandViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this BandViewProperties.
        :rtype: list[DashboardColor]
        """
        ...
    @colors.setter
    def colors(self, colors) -> None:
        """
        Get the colors of this BandViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this BandViewProperties.
        :rtype: list[DashboardColor]
        """
        ...
    @property
    def shape(self):
        """
        Get the shape of this BandViewProperties.

        :return: The shape of this BandViewProperties.
        :rtype: str
        """
        ...
    @shape.setter
    def shape(self, shape) -> None:
        """
        Get the shape of this BandViewProperties.

        :return: The shape of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def note(self):
        """
        Get the note of this BandViewProperties.

        :return: The note of this BandViewProperties.
        :rtype: str
        """
        ...
    @note.setter
    def note(self, note) -> None:
        """
        Get the note of this BandViewProperties.

        :return: The note of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def show_note_when_empty(self):
        """
        Get the show_note_when_empty of this BandViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this BandViewProperties.
        :rtype: bool
        """
        ...
    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty) -> None:
        """
        Get the show_note_when_empty of this BandViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this BandViewProperties.
        :rtype: bool
        """
        ...
    @property
    def axes(self):
        """
        Get the axes of this BandViewProperties.

        :return: The axes of this BandViewProperties.
        :rtype: Axes
        """
        ...
    @axes.setter
    def axes(self, axes) -> None:
        """
        Get the axes of this BandViewProperties.

        :return: The axes of this BandViewProperties.
        :rtype: Axes
        """
        ...
    @property
    def static_legend(self):
        """
        Get the static_legend of this BandViewProperties.

        :return: The static_legend of this BandViewProperties.
        :rtype: StaticLegend
        """
        ...
    @static_legend.setter
    def static_legend(self, static_legend) -> None:
        """
        Get the static_legend of this BandViewProperties.

        :return: The static_legend of this BandViewProperties.
        :rtype: StaticLegend
        """
        ...
    @property
    def x_column(self):
        """
        Get the x_column of this BandViewProperties.

        :return: The x_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @x_column.setter
    def x_column(self, x_column) -> None:
        """
        Get the x_column of this BandViewProperties.

        :return: The x_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def generate_x_axis_ticks(self):
        """
        Get the generate_x_axis_ticks of this BandViewProperties.

        :return: The generate_x_axis_ticks of this BandViewProperties.
        :rtype: list[str]
        """
        ...
    @generate_x_axis_ticks.setter
    def generate_x_axis_ticks(self, generate_x_axis_ticks) -> None:
        """
        Get the generate_x_axis_ticks of this BandViewProperties.

        :return: The generate_x_axis_ticks of this BandViewProperties.
        :rtype: list[str]
        """
        ...
    @property
    def x_total_ticks(self):
        """
        Get the x_total_ticks of this BandViewProperties.

        :return: The x_total_ticks of this BandViewProperties.
        :rtype: int
        """
        ...
    @x_total_ticks.setter
    def x_total_ticks(self, x_total_ticks) -> None:
        """
        Get the x_total_ticks of this BandViewProperties.

        :return: The x_total_ticks of this BandViewProperties.
        :rtype: int
        """
        ...
    @property
    def x_tick_start(self):
        """
        Get the x_tick_start of this BandViewProperties.

        :return: The x_tick_start of this BandViewProperties.
        :rtype: float
        """
        ...
    @x_tick_start.setter
    def x_tick_start(self, x_tick_start) -> None:
        """
        Get the x_tick_start of this BandViewProperties.

        :return: The x_tick_start of this BandViewProperties.
        :rtype: float
        """
        ...
    @property
    def x_tick_step(self):
        """
        Get the x_tick_step of this BandViewProperties.

        :return: The x_tick_step of this BandViewProperties.
        :rtype: float
        """
        ...
    @x_tick_step.setter
    def x_tick_step(self, x_tick_step) -> None:
        """
        Get the x_tick_step of this BandViewProperties.

        :return: The x_tick_step of this BandViewProperties.
        :rtype: float
        """
        ...
    @property
    def y_column(self):
        """
        Get the y_column of this BandViewProperties.

        :return: The y_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @y_column.setter
    def y_column(self, y_column) -> None:
        """
        Get the y_column of this BandViewProperties.

        :return: The y_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def generate_y_axis_ticks(self):
        """
        Get the generate_y_axis_ticks of this BandViewProperties.

        :return: The generate_y_axis_ticks of this BandViewProperties.
        :rtype: list[str]
        """
        ...
    @generate_y_axis_ticks.setter
    def generate_y_axis_ticks(self, generate_y_axis_ticks) -> None:
        """
        Get the generate_y_axis_ticks of this BandViewProperties.

        :return: The generate_y_axis_ticks of this BandViewProperties.
        :rtype: list[str]
        """
        ...
    @property
    def y_total_ticks(self):
        """
        Get the y_total_ticks of this BandViewProperties.

        :return: The y_total_ticks of this BandViewProperties.
        :rtype: int
        """
        ...
    @y_total_ticks.setter
    def y_total_ticks(self, y_total_ticks) -> None:
        """
        Get the y_total_ticks of this BandViewProperties.

        :return: The y_total_ticks of this BandViewProperties.
        :rtype: int
        """
        ...
    @property
    def y_tick_start(self):
        """
        Get the y_tick_start of this BandViewProperties.

        :return: The y_tick_start of this BandViewProperties.
        :rtype: float
        """
        ...
    @y_tick_start.setter
    def y_tick_start(self, y_tick_start) -> None:
        """
        Get the y_tick_start of this BandViewProperties.

        :return: The y_tick_start of this BandViewProperties.
        :rtype: float
        """
        ...
    @property
    def y_tick_step(self):
        """
        Get the y_tick_step of this BandViewProperties.

        :return: The y_tick_step of this BandViewProperties.
        :rtype: float
        """
        ...
    @y_tick_step.setter
    def y_tick_step(self, y_tick_step) -> None:
        """
        Get the y_tick_step of this BandViewProperties.

        :return: The y_tick_step of this BandViewProperties.
        :rtype: float
        """
        ...
    @property
    def upper_column(self):
        """
        Get the upper_column of this BandViewProperties.

        :return: The upper_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @upper_column.setter
    def upper_column(self, upper_column) -> None:
        """
        Get the upper_column of this BandViewProperties.

        :return: The upper_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def main_column(self):
        """
        Get the main_column of this BandViewProperties.

        :return: The main_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @main_column.setter
    def main_column(self, main_column) -> None:
        """
        Get the main_column of this BandViewProperties.

        :return: The main_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def lower_column(self):
        """
        Get the lower_column of this BandViewProperties.

        :return: The lower_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @lower_column.setter
    def lower_column(self, lower_column) -> None:
        """
        Get the lower_column of this BandViewProperties.

        :return: The lower_column of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def hover_dimension(self):
        """
        Get the hover_dimension of this BandViewProperties.

        :return: The hover_dimension of this BandViewProperties.
        :rtype: str
        """
        ...
    @hover_dimension.setter
    def hover_dimension(self, hover_dimension) -> None:
        """
        Get the hover_dimension of this BandViewProperties.

        :return: The hover_dimension of this BandViewProperties.
        :rtype: str
        """
        ...
    @property
    def geom(self):
        """
        Get the geom of this BandViewProperties.

        :return: The geom of this BandViewProperties.
        :rtype: XYGeom
        """
        ...
    @geom.setter
    def geom(self, geom) -> None:
        """
        Get the geom of this BandViewProperties.

        :return: The geom of this BandViewProperties.
        :rtype: XYGeom
        """
        ...
    @property
    def legend_colorize_rows(self):
        """
        Get the legend_colorize_rows of this BandViewProperties.

        :return: The legend_colorize_rows of this BandViewProperties.
        :rtype: bool
        """
        ...
    @legend_colorize_rows.setter
    def legend_colorize_rows(self, legend_colorize_rows) -> None:
        """
        Get the legend_colorize_rows of this BandViewProperties.

        :return: The legend_colorize_rows of this BandViewProperties.
        :rtype: bool
        """
        ...
    @property
    def legend_hide(self):
        """
        Get the legend_hide of this BandViewProperties.

        :return: The legend_hide of this BandViewProperties.
        :rtype: bool
        """
        ...
    @legend_hide.setter
    def legend_hide(self, legend_hide) -> None:
        """
        Get the legend_hide of this BandViewProperties.

        :return: The legend_hide of this BandViewProperties.
        :rtype: bool
        """
        ...
    @property
    def legend_opacity(self):
        """
        Get the legend_opacity of this BandViewProperties.

        :return: The legend_opacity of this BandViewProperties.
        :rtype: float
        """
        ...
    @legend_opacity.setter
    def legend_opacity(self, legend_opacity) -> None:
        """
        Get the legend_opacity of this BandViewProperties.

        :return: The legend_opacity of this BandViewProperties.
        :rtype: float
        """
        ...
    @property
    def legend_orientation_threshold(self):
        """
        Get the legend_orientation_threshold of this BandViewProperties.

        :return: The legend_orientation_threshold of this BandViewProperties.
        :rtype: int
        """
        ...
    @legend_orientation_threshold.setter
    def legend_orientation_threshold(self, legend_orientation_threshold) -> None:
        """
        Get the legend_orientation_threshold of this BandViewProperties.

        :return: The legend_orientation_threshold of this BandViewProperties.
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
