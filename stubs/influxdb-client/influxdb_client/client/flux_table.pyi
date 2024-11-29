"""
Flux employs a basic data model built from basic data types.

The data model consists of tables, records, columns.
"""

from _typeshed import Incomplete
from collections.abc import Iterator
from http.client import HTTPResponse
from json import JSONEncoder

class FluxStructure:
    """The data model consists of tables, records, columns."""
    ...

class FluxStructureEncoder(JSONEncoder):
    """The FluxStructure encoder to encode query results to JSON."""
    def default(self, obj):
        """Return serializable objects for JSONEncoder."""
        ...

class FluxTable(FluxStructure):
    """
    A table is set of records with a common set of columns and a group key.

    The table can be serialized into JSON by::

        import json
        from influxdb_client.client.flux_table import FluxStructureEncoder

        output = json.dumps(tables, cls=FluxStructureEncoder, indent=2)
        print(output)
    """
    columns: Incomplete
    records: Incomplete
    def __init__(self) -> None:
        """Initialize defaults."""
        ...
    def get_group_key(self):
        """
        Group key is a list of columns.

        A table’s group key denotes which subset of the entire dataset is assigned to the table.
        """
        ...
    def __iter__(self):
        """Iterate over records."""
        ...

class FluxColumn(FluxStructure):
    """A column has a label and a data type."""
    default_value: Incomplete
    group: Incomplete
    data_type: Incomplete
    label: Incomplete
    index: Incomplete
    def __init__(
        self,
        index: Incomplete | None = None,
        label: Incomplete | None = None,
        data_type: Incomplete | None = None,
        group: Incomplete | None = None,
        default_value: Incomplete | None = None,
    ) -> None:
        """Initialize defaults."""
        ...

class FluxRecord(FluxStructure):
    """A record is a tuple of named values and is represented using an object type."""
    table: Incomplete
    values: Incomplete
    row: Incomplete
    def __init__(self, table, values: Incomplete | None = None) -> None:
        """Initialize defaults."""
        ...
    def get_start(self):
        """Get '_start' value."""
        ...
    def get_stop(self):
        """Get '_stop' value."""
        ...
    def get_time(self):
        """Get timestamp."""
        ...
    def get_value(self):
        """Get field value."""
        ...
    def get_field(self):
        """Get field name."""
        ...
    def get_measurement(self):
        """Get measurement name."""
        ...
    def __getitem__(self, key):
        """Get value by key."""
        ...
    def __setitem__(self, key, value):
        """Set value with key and value."""
        ...

class TableList(list[FluxTable]):
    """:class:`~influxdb_client.client.flux_table.FluxTable` list with additionally functional to better handle of query result."""
    def to_values(self, columns: list[str] | None = None) -> list[list[object]]:
        """
        Serialize query results to a flattened list of values.

        :param columns: if not ``None`` then only specified columns are presented in results
        :return: :class:`~list` of values

        Output example:

        .. code-block:: python

            [
                ['New York', datetime.datetime(2022, 6, 7, 11, 3, 22, 917593, tzinfo=tzutc()), 24.3],
                ['Prague', datetime.datetime(2022, 6, 7, 11, 3, 22, 917593, tzinfo=tzutc()), 25.3],
                ...
            ]

        Configure required columns:

        .. code-block:: python

            from influxdb_client import InfluxDBClient

                with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using Table structure
                tables = client.query_api().query('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to values
                output = tables.to_values(columns=['location', '_time', '_value'])
                print(output)
        """
        ...
    def to_json(self, columns: list[str] | None = None, **kwargs) -> str:
        """
        Serialize query results to a JSON formatted :class:`~str`.

        :param columns: if not ``None`` then only specified columns are presented in results
        :return: :class:`~str`

        The query results is flattened to array:

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

        The JSON format could be configured via ``**kwargs`` arguments:

        .. code-block:: python

            from influxdb_client import InfluxDBClient

            with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using Table structure
                tables = client.query_api().query('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to JSON
                output = tables.to_json(indent=5)
                print(output)

        For all available options see - `json.dump <https://docs.python.org/3/library/json.html#json.dump>`_.
        """
        ...

class CSVIterator(Iterator[list[str]]):
    """:class:`Iterator[List[str]]` with additionally functional to better handle of query result."""
    delegate: Incomplete
    def __init__(self, response: HTTPResponse) -> None:
        """Initialize ``csv.reader``."""
        ...
    def __iter__(self):
        """Return an iterator object."""
        ...
    def __next__(self):
        """Retrieve the next item from the iterator."""
        ...
    def to_values(self) -> list[list[str]]:
        """
        Serialize query results to a flattened list of values.

        :return: :class:`~list` of values

        Output example:

        .. code-block:: python

            [
                ['New York', '2022-06-14T08:00:51.749072045Z', '24.3'],
                ['Prague', '2022-06-14T08:00:51.749072045Z', '25.3'],
                ...
            ]
        """
        ...
