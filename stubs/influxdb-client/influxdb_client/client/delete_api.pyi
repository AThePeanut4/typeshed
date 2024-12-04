"""Delete time series data from InfluxDB."""

from datetime import datetime

from influxdb_client import Organization
from influxdb_client.client._base import _BaseDeleteApi

class DeleteApi(_BaseDeleteApi):
    """Implementation for '/api/v2/delete' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def delete(
        self, start: str | datetime, stop: str | datetime, predicate: str, bucket: str, org: str | Organization | None = None
    ) -> None:
        """
        Delete Time series data from InfluxDB.

        :param str, datetime.datetime start: start time
        :param str, datetime.datetime stop: stop time
        :param str predicate: predicate
        :param str bucket: bucket id or name from which data will be deleted
        :param str, Organization org: specifies the organization to delete data from.
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :return:
        """
        ...
