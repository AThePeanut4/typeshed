"""Collect and async write time series data to InfluxDB Cloud or InfluxDB OSS."""

from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import TypeAlias

from influxdb_client.client._base import _BaseWriteApi
from influxdb_client.client.write.point import Point
from influxdb_client.client.write_api import PointSettings
from influxdb_client.domain.write_precision import _WritePrecision

_DataClass: TypeAlias = Any  # any dataclass
_NamedTuple: TypeAlias = tuple[Any, ...]  # any NamedTuple

logger: Incomplete

class WriteApiAsync(_BaseWriteApi):
    """
    Implementation for '/api/v2/write' endpoint.

    Example:
        .. code-block:: python

            from influxdb_client_async import InfluxDBClientAsync


            # Initialize async/await instance of Write API
            async with InfluxDBClientAsync(url="http://localhost:8086", token="my-token", org="my-org") as client:
                write_api = client.write_api()
    """
    def __init__(self, influxdb_client, point_settings: PointSettings = ...) -> None:
        """
        Initialize defaults.

        :param influxdb_client: with default settings (organization)
        :param point_settings: settings to store default tags.
        """
        ...
    async def write(
        self,
        bucket: str,
        org: str | None = None,
        record: (
            str
            | Iterable[str]
            | Point
            | Iterable[Point]
            | dict[Incomplete, Incomplete]
            | Iterable[dict[Incomplete, Incomplete]]
            | bytes
            | Iterable[bytes]
            | _NamedTuple
            | Iterable[_NamedTuple]
            | _DataClass
            | Iterable[_DataClass]
        ) = None,
        write_precision: _WritePrecision = "ns",
        **kwargs,
    ) -> bool:
        """
        Write time-series data into InfluxDB.

        :param str bucket: specifies the destination bucket for writes (required)
        :param str, Organization org: specifies the destination organization for writes;
                                      take the ID, Name or Organization.
                                      If not specified the default value from ``InfluxDBClientAsync.org`` is used.
        :param WritePrecision write_precision: specifies the precision for the unix timestamps within
                                               the body line-protocol. The precision specified on a Point has precedes
                                               and is use for write.
        :param record: Point, Line Protocol, Dictionary, NamedTuple, Data Classes, Pandas DataFrame
        :key data_frame_measurement_name: name of measurement for writing Pandas DataFrame - ``DataFrame``
        :key data_frame_tag_columns: list of DataFrame columns which are tags,
                                     rest columns will be fields - ``DataFrame``
        :key data_frame_timestamp_column: name of DataFrame column which contains a timestamp. The column can be defined as a :class:`~str` value
                                          formatted as `2018-10-26`, `2018-10-26 12:00`, `2018-10-26 12:00:00-05:00`
                                          or other formats and types supported by `pandas.to_datetime <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime>`_ - ``DataFrame``
        :key data_frame_timestamp_timezone: name of the timezone which is used for timestamp column - ``DataFrame``
        :key record_measurement_key: key of record with specified measurement -
                                     ``dictionary``, ``NamedTuple``, ``dataclass``
        :key record_measurement_name: static measurement name - ``dictionary``, ``NamedTuple``, ``dataclass``
        :key record_time_key: key of record with specified timestamp - ``dictionary``, ``NamedTuple``, ``dataclass``
        :key record_tag_keys: list of record keys to use as a tag - ``dictionary``, ``NamedTuple``, ``dataclass``
        :key record_field_keys: list of record keys to use as a field  - ``dictionary``, ``NamedTuple``, ``dataclass``
        :return: ``True`` for successfully accepted data, otherwise raise an exception

        Example:
            .. code-block:: python

                # Record as Line Protocol
                await write_api.write("my-bucket", "my-org", "h2o_feet,location=us-west level=125i 1")

                # Record as Dictionary
                dictionary = {
                    "measurement": "h2o_feet",
                    "tags": {"location": "us-west"},
                    "fields": {"level": 125},
                    "time": 1
                }
                await write_api.write("my-bucket", "my-org", dictionary)

                # Record as Point
                from influxdb_client import Point
                point = Point("h2o_feet").tag("location", "us-west").field("level", 125).time(1)
                await write_api.write("my-bucket", "my-org", point)

        DataFrame:
            If the ``data_frame_timestamp_column`` is not specified the index of `Pandas DataFrame <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`_
            is used as a ``timestamp`` for written data. The index can be `PeriodIndex <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex>`_
            or its must be transformable to ``datetime`` by
            `pandas.to_datetime <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime>`_.

            If you would like to transform a column to ``PeriodIndex``, you can use something like:

            .. code-block:: python

                import pandas as pd

                # DataFrame
                data_frame = ...
                # Set column as Index
                data_frame.set_index('column_name', inplace=True)
                # Transform index to PeriodIndex
                data_frame.index = pd.to_datetime(data_frame.index, unit='s')
        """
        ...
