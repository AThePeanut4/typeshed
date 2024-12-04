"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class DeletePredicateRequest:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, start: Incomplete | None = None, stop: Incomplete | None = None, predicate: Incomplete | None = None
    ) -> None:
        """DeletePredicateRequest - a model defined in OpenAPI."""
        ...
    @property
    def start(self):
        """
        Get the start of this DeletePredicateRequest.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)). The earliest time to delete from.

        :return: The start of this DeletePredicateRequest.
        :rtype: datetime
        """
        ...
    @start.setter
    def start(self, start) -> None:
        """
        Get the start of this DeletePredicateRequest.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)). The earliest time to delete from.

        :return: The start of this DeletePredicateRequest.
        :rtype: datetime
        """
        ...
    @property
    def stop(self):
        """
        Get the stop of this DeletePredicateRequest.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)). The latest time to delete from.

        :return: The stop of this DeletePredicateRequest.
        :rtype: datetime
        """
        ...
    @stop.setter
    def stop(self, stop) -> None:
        """
        Get the stop of this DeletePredicateRequest.

        A timestamp ([RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp)). The latest time to delete from.

        :return: The stop of this DeletePredicateRequest.
        :rtype: datetime
        """
        ...
    @property
    def predicate(self):
        """
        Get the predicate of this DeletePredicateRequest.

        An expression in [delete predicate syntax](https://docs.influxdata.com/influxdb/latest/reference/syntax/delete-predicate/).

        :return: The predicate of this DeletePredicateRequest.
        :rtype: str
        """
        ...
    @predicate.setter
    def predicate(self, predicate) -> None:
        """
        Get the predicate of this DeletePredicateRequest.

        An expression in [delete predicate syntax](https://docs.influxdata.com/influxdb/latest/reference/syntax/delete-predicate/).

        :return: The predicate of this DeletePredicateRequest.
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
