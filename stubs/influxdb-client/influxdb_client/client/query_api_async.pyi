"""
Querying InfluxDB by FluxLang.

Flux is InfluxData’s functional data scripting language designed for querying, analyzing, and acting on data.
"""

from _typeshed import Incomplete, SupportsItems
from collections.abc import AsyncGenerator

from influxdb_client.client._base import _BaseQueryApi
from influxdb_client.client.flux_table import FluxRecord, TableList
from influxdb_client.domain.dialect import Dialect
from influxdb_client.domain.organization import Organization

class QueryApiAsync(_BaseQueryApi):
    """Asynchronous implementation for '/api/v2/query' endpoint."""
    def __init__(self, influxdb_client, query_options=...) -> None:
        """
        Initialize query client.

        :param influxdb_client: influxdb client
        """
        ...
    async def query(
        self, query: str, org: Incomplete | None = None, params: SupportsItems[str, Incomplete] | None = None
    ) -> TableList:
        """
        Execute asynchronous Flux query and return result as a :class:`~influxdb_client.client.flux_table.FluxTable` list.

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClientAsync.org`` is used.
        :param params: bind parameters
        :return: :class:`~influxdb_client.client.flux_table.FluxTable` list wrapped into
                 :class:`~influxdb_client.client.flux_table.TableList`
        :rtype: TableList

        Serialization the query results to flattened list of values via :func:`~influxdb_client.client.flux_table.TableList.to_values`:

        .. code-block:: python

            from influxdb_client import InfluxDBClient

            async with InfluxDBClientAsync(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using Table structure
                tables = await client.query_api().query('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to values
                output = tables.to_values(columns=['location', '_time', '_value'])
                print(output)

        .. code-block:: python

            [
                ['New York', datetime.datetime(2022, 6, 7, 11, 3, 22, 917593, tzinfo=tzutc()), 24.3],
                ['Prague', datetime.datetime(2022, 6, 7, 11, 3, 22, 917593, tzinfo=tzutc()), 25.3],
                ...
            ]

        Serialization the query results to JSON via :func:`~influxdb_client.client.flux_table.TableList.to_json`:

        .. code-block:: python

            from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

            async with InfluxDBClientAsync(url="http://localhost:8086", token="my-token", org="my-org") as client:
                # Query: using Table structure
                tables = await client.query_api().query('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to JSON
                output = tables.to_json(indent=5)
                print(output)

        .. code-block:: javascript

            [
                {
                    "_measurement": "mem",
                    "_start": "2021-06-23T06:50:11.897825+00:00",
                    "_stop": "2021-06-25T06:50:11.897825+00:00",
                    "_time": "2020-02-27T16:20:00.897825+00:00",
                    "region": "north",
                     "_field": "usage",
                    "_value": 15
                },
                {
                    "_measurement": "mem",
                    "_start": "2021-06-23T06:50:11.897825+00:00",
                    "_stop": "2021-06-25T06:50:11.897825+00:00",
                    "_time": "2020-02-27T16:20:01.897825+00:00",
                    "region": "west",
                     "_field": "usage",
                    "_value": 10
                },
                ...
            ]
        """
        ...
    async def query_stream(
        self, query: str, org: Incomplete | None = None, params: SupportsItems[str, Incomplete] | None = None
    ) -> AsyncGenerator[FluxRecord, None]:
        """
        Execute asynchronous Flux query and return stream of :class:`~influxdb_client.client.flux_table.FluxRecord` as an AsyncGenerator[:class:`~influxdb_client.client.flux_table.FluxRecord`].

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClientAsync.org`` is used.
        :param params: bind parameters
        :return: AsyncGenerator[:class:`~influxdb_client.client.flux_table.FluxRecord`]
        """
        ...
    async def query_data_frame(
        self,
        query: str,
        org: str | Organization | None = None,
        data_frame_index: list[str] | None = None,
        params: SupportsItems[str, Incomplete] | None = None,
        use_extension_dtypes: bool = False,
    ):
        """
        Execute asynchronous Flux query and return :class:`~pandas.core.frame.DataFrame`.

        .. note:: If the ``query`` returns tables with differing schemas than the client generates a :class:`~DataFrame` for each of them.

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClientAsync.org`` is used.
        :param data_frame_index: the list of columns that are used as DataFrame index
        :param params: bind parameters
        :param use_extension_dtypes: set to ``True`` to use panda's extension data types.
                                     Useful for queries with ``pivot`` function.
                                     When data has missing values, column data type may change (to ``object`` or ``float64``).
                                     Nullable extension types (``Int64``, ``Float64``, ``boolean``) support ``panda.NA`` value.
                                     For more info, see https://pandas.pydata.org/docs/user_guide/missing_data.html.
        :return: :class:`~DataFrame` or :class:`~List[DataFrame]`

        .. warning:: For the optimal processing of the query results use the ``pivot() function`` which align results as a table.

            .. code-block:: text

                from(bucket:"my-bucket")
                    |> range(start: -5m, stop: now())
                    |> filter(fn: (r) => r._measurement == "mem")
                    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")

            For more info see:
                - https://docs.influxdata.com/resources/videos/pivots-in-flux/
                - https://docs.influxdata.com/flux/latest/stdlib/universe/pivot/
                - https://docs.influxdata.com/flux/latest/stdlib/influxdata/influxdb/schema/fieldsascols/
        """
        ...
    async def query_data_frame_stream(
        self,
        query: str,
        org: str | Organization | None = None,
        data_frame_index: list[str] | None = None,
        params: SupportsItems[str, Incomplete] | None = None,
        use_extension_dtypes: bool = False,
    ):
        """
        Execute asynchronous Flux query and return stream of :class:`~pandas.core.frame.DataFrame` as an AsyncGenerator[:class:`~pandas.core.frame.DataFrame`].

        .. note:: If the ``query`` returns tables with differing schemas than the client generates a :class:`~DataFrame` for each of them.

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClientAsync.org`` is used.
        :param data_frame_index: the list of columns that are used as DataFrame index
        :param params: bind parameters
        :param use_extension_dtypes: set to ``True`` to use panda's extension data types.
                                     Useful for queries with ``pivot`` function.
                                     When data has missing values, column data type may change (to ``object`` or ``float64``).
                                     Nullable extension types (``Int64``, ``Float64``, ``boolean``) support ``panda.NA`` value.
                                     For more info, see https://pandas.pydata.org/docs/user_guide/missing_data.html.
        :return: :class:`AsyncGenerator[:class:`DataFrame`]`

        .. warning:: For the optimal processing of the query results use the ``pivot() function`` which align results as a table.

            .. code-block:: text

                from(bucket:"my-bucket")
                    |> range(start: -5m, stop: now())
                    |> filter(fn: (r) => r._measurement == "mem")
                    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")

            For more info see:
                - https://docs.influxdata.com/resources/videos/pivots-in-flux/
                - https://docs.influxdata.com/flux/latest/stdlib/universe/pivot/
                - https://docs.influxdata.com/flux/latest/stdlib/influxdata/influxdb/schema/fieldsascols/
        """
        ...
    async def query_raw(
        self,
        query: str,
        org: str | Organization | None = None,
        dialect: Dialect = ...,
        params: SupportsItems[str, Incomplete] | None = None,
    ) -> str:
        """
        Execute asynchronous Flux query and return result as raw unprocessed result as a str.

        :param query: a Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClientAsync.org`` is used.
        :param dialect: csv dialect format
        :param params: bind parameters
        :return: :class:`~str`
        """
        ...
