"""Collect and write time series data to InfluxDB Cloud or InfluxDB OSS."""

import logging
from _typeshed import Incomplete
from collections.abc import Iterable
from enum import Enum
from types import TracebackType
from typing import Any
from typing_extensions import Self, TypeAlias

from influxdb_client.client._base import _BaseWriteApi
from influxdb_client.client.write.point import Point
from influxdb_client.domain.write_precision import _WritePrecision

_DataClass: TypeAlias = Any  # any dataclass
_NamedTuple: TypeAlias = tuple[Any, ...]  # any NamedTuple
_Observable: TypeAlias = Any  # reactivex.Observable

logger: logging.Logger

class WriteType(Enum):
    """Configuration which type of writes will client use."""
    batching = 1
    asynchronous = 2
    synchronous = 3

class WriteOptions:
    """Write configuration."""
    write_type: WriteType
    batch_size: int
    flush_interval: int
    jitter_interval: int
    retry_interval: int
    max_retries: int
    max_retry_delay: int
    max_retry_time: int
    exponential_base: int
    write_scheduler: Incomplete
    max_close_wait: int
    def __init__(
        self,
        write_type: WriteType = ...,
        batch_size: int = 1_000,
        flush_interval: int = 1_000,
        jitter_interval: int = 0,
        retry_interval: int = 5_000,
        max_retries: int = 5,
        max_retry_delay: int = 125_000,
        max_retry_time: int = 180_000,
        exponential_base: int = 2,
        max_close_wait: int = 300_000,
        write_scheduler=...,
    ) -> None:
        """
        Create write api configuration.

        :param write_type: methods of write (batching, asynchronous, synchronous)
        :param batch_size: the number of data point to collect in batch
        :param flush_interval: flush data at least in this interval (milliseconds)
        :param jitter_interval: this is primarily to avoid large write spikes for users running a large number of
               client instances ie, a jitter of 5s and flush duration 10s means flushes will happen every 10-15s
               (milliseconds)
        :param retry_interval: the time to wait before retry unsuccessful write (milliseconds)
        :param max_retries: the number of max retries when write fails, 0 means retry is disabled
        :param max_retry_delay: the maximum delay between each retry attempt in milliseconds
        :param max_retry_time: total timeout for all retry attempts in milliseconds, if 0 retry is disabled
        :param exponential_base: base for the exponential retry delay
        :parama max_close_wait: the maximum time to wait for writes to be flushed if close() is called
        :param write_scheduler:
        """
        ...
    def to_retry_strategy(self, **kwargs):
        """
        Create a Retry strategy from write options.

        :key retry_callback: The callable ``callback`` to run after retryable error occurred.
                             The callable must accept one argument:
                                - `Exception`: an retryable error
        """
        ...

SYNCHRONOUS: Incomplete
ASYNCHRONOUS: Incomplete

class PointSettings:
    """Settings to store default tags."""
    defaultTags: Incomplete
    def __init__(self, **default_tags) -> None:
        """
        Create point settings for write api.

        :param default_tags: Default tags which will be added to each point written by api.
        """
        ...
    def add_default_tag(self, key, value) -> None:
        """Add new default tag with key and value."""
        ...

class _BatchItemKey:
    bucket: Incomplete
    org: Incomplete
    precision: Incomplete
    def __init__(self, bucket, org, precision="ns") -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, o: object) -> bool: ...

class _BatchItem:
    key: Incomplete
    data: Incomplete
    size: Incomplete
    def __init__(self, key: _BatchItemKey, data, size: int = 1) -> None: ...
    def to_key_tuple(self) -> tuple[str, str, str]: ...

class _BatchResponse:
    data: Incomplete
    exception: Incomplete
    def __init__(self, data: _BatchItem, exception: Exception | None = None) -> None: ...

class WriteApi(_BaseWriteApi):
    """
    Implementation for '/api/v2/write' endpoint.

    Example:
        .. code-block:: python

            from influxdb_client import InfluxDBClient
            from influxdb_client.client.write_api import SYNCHRONOUS


            # Initialize SYNCHRONOUS instance of WriteApi
            with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:
                write_api = client.write_api(write_options=SYNCHRONOUS)
    """
    def __init__(
        self, influxdb_client, write_options: WriteOptions = ..., point_settings: PointSettings = ..., **kwargs
    ) -> None:
        """
        Initialize defaults.

        :param influxdb_client: with default settings (organization)
        :param write_options: write api configuration
        :param point_settings: settings to store default tags.
        :key success_callback: The callable ``callback`` to run after successfully writen a batch.

                               The callable must accept two arguments:
                                    - `Tuple`: ``(bucket, organization, precision)``
                                    - `str`: written data

                               **[batching mode]**
        :key error_callback: The callable ``callback`` to run after unsuccessfully writen a batch.

                             The callable must accept three arguments:
                                - `Tuple`: ``(bucket, organization, precision)``
                                - `str`: written data
                                - `Exception`: an occurred error

                             **[batching mode]**
        :key retry_callback: The callable ``callback`` to run after retryable error occurred.

                             The callable must accept three arguments:
                                - `Tuple`: ``(bucket, organization, precision)``
                                - `str`: written data
                                - `Exception`: an retryable error

                             **[batching mode]**
        """
        ...
    def write(
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
            | _Observable
            | _NamedTuple
            | Iterable[_NamedTuple]
            | _DataClass
            | Iterable[_DataClass]
        ) = None,
        write_precision: _WritePrecision = "ns",
        **kwargs,
    ) -> Any:
        """
        Write time-series data into InfluxDB.

        :param str bucket: specifies the destination bucket for writes (required)
        :param str, Organization org: specifies the destination organization for writes;
                                      take the ID, Name or Organization.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param WritePrecision write_precision: specifies the precision for the unix timestamps within
                                               the body line-protocol. The precision specified on a Point has precedes
                                               and is use for write.
        :param record: Point, Line Protocol, Dictionary, NamedTuple, Data Classes, Pandas DataFrame or
                       RxPY Observable to write
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

        Example:
            .. code-block:: python

                # Record as Line Protocol
                write_api.write("my-bucket", "my-org", "h2o_feet,location=us-west level=125i 1")

                # Record as Dictionary
                dictionary = {
                    "measurement": "h2o_feet",
                    "tags": {"location": "us-west"},
                    "fields": {"level": 125},
                    "time": 1
                }
                write_api.write("my-bucket", "my-org", dictionary)

                # Record as Point
                from influxdb_client import Point
                point = Point("h2o_feet").tag("location", "us-west").field("level", 125).time(1)
                write_api.write("my-bucket", "my-org", point)

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
    def flush(self) -> None:
        """Flush data."""
        ...
    def close(self) -> None:
        """Flush data and dispose a batching buffer."""
        ...
    def __enter__(self) -> Self:
        """
        Enter the runtime context related to this object.

        It will bind this method’s return value to the target(s)
        specified in the `as` clause of the statement.

        return: self instance
        """
        ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        """Exit the runtime context related to this object and close the WriteApi."""
        ...
    def __del__(self) -> None:
        """Close WriteApi."""
        ...
