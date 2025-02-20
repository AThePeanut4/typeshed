"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class LogEvent:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, time: Incomplete | None = None, message: Incomplete | None = None, run_id: Incomplete | None = None
    ) -> None:
        """LogEvent - a model defined in OpenAPI."""
        ...
    @property
    def time(self):
        """
        Get the time of this LogEvent.

        The time ([RFC3339Nano date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339nano-timestamp)) that the event occurred.

        :return: The time of this LogEvent.
        :rtype: datetime
        """
        ...
    @time.setter
    def time(self, time) -> None:
        """
        Get the time of this LogEvent.

        The time ([RFC3339Nano date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339nano-timestamp)) that the event occurred.

        :return: The time of this LogEvent.
        :rtype: datetime
        """
        ...
    @property
    def message(self):
        """
        Get the message of this LogEvent.

        A description of the event that occurred.

        :return: The message of this LogEvent.
        :rtype: str
        """
        ...
    @message.setter
    def message(self, message) -> None:
        """
        Get the message of this LogEvent.

        A description of the event that occurred.

        :return: The message of this LogEvent.
        :rtype: str
        """
        ...
    @property
    def run_id(self):
        """
        Get the run_id of this LogEvent.

        The ID of the task run that generated the event.

        :return: The run_id of this LogEvent.
        :rtype: str
        """
        ...
    @run_id.setter
    def run_id(self, run_id) -> None:
        """
        Get the run_id of this LogEvent.

        The ID of the task run that generated the event.

        :return: The run_id of this LogEvent.
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
