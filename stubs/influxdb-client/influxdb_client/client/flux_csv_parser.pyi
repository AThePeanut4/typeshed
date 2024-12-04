"""Parsing response from InfluxDB to FluxStructures or DataFrame."""

from _typeshed import Incomplete
from collections.abc import Generator
from enum import Enum
from types import TracebackType
from typing_extensions import Self

from influxdb_client.client.flux_table import TableList

ANNOTATION_DEFAULT: str
ANNOTATION_GROUP: str
ANNOTATION_DATATYPE: str
ANNOTATIONS: Incomplete

class FluxQueryException(Exception):
    """The exception from InfluxDB."""
    message: Incomplete
    reference: Incomplete
    def __init__(self, message, reference) -> None:
        """Initialize defaults."""
        ...

class FluxCsvParserException(Exception):
    """The exception for not parsable data."""
    ...

class FluxSerializationMode(Enum):
    """The type how we want to serialize data."""
    tables = 1
    stream = 2
    dataFrame = 3

class FluxResponseMetadataMode(Enum):
    """The configuration for expected amount of metadata response from InfluxDB."""
    full = 1
    only_names = 2

class _FluxCsvParserMetadata:
    table_index: int
    table_id: int
    start_new_table: bool
    table: Incomplete
    groups: Incomplete
    parsing_state_error: bool
    def __init__(self) -> None: ...

class FluxCsvParser:
    """Parse to processing response from InfluxDB to FluxStructures or DataFrame."""
    tables: Incomplete
    def __init__(
        self,
        response,
        serialization_mode: FluxSerializationMode,
        data_frame_index: list[str] | None = None,
        query_options: Incomplete | None = None,
        response_metadata_mode: FluxResponseMetadataMode = ...,
        use_extension_dtypes: bool = False,
    ) -> None:
        """
        Initialize defaults.

        :param response: HTTP response from a HTTP client.
                         Acceptable types: `urllib3.response.HTTPResponse`, `aiohttp.client_reqrep.ClientResponse`.
        """
        ...
    def __enter__(self) -> Self:
        """Initialize CSV reader."""
        ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        """Close HTTP response."""
        ...
    async def __aenter__(self) -> Self:
        """Initialize CSV reader."""
        ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        """Shutdown the client."""
        ...
    def generator(self) -> Generator[Incomplete, None, None]:
        """Return Python generator."""
        ...
    def generator_async(self):
        """Return Python async-generator."""
        ...
    def parse_record(self, table_index, table, csv):
        """Parse one record."""
        ...
    @staticmethod
    def add_data_types(table, data_types) -> None:
        """Add data types to columns."""
        ...
    @staticmethod
    def add_groups(table, csv) -> None:
        """Add group keys to columns."""
        ...
    @staticmethod
    def add_default_empty_values(table, default_values) -> None:
        """Add default values to columns."""
        ...
    @staticmethod
    def add_column_names_and_tags(table, csv) -> None:
        """Add labels to columns."""
        ...
    def table_list(self) -> TableList:
        """Get the list of flux tables."""
        ...

class _StreamReaderToWithAsyncRead:
    response: Incomplete
    decoder: Incomplete
    def __init__(self, response) -> None: ...
    async def read(self, size: int) -> str: ...
