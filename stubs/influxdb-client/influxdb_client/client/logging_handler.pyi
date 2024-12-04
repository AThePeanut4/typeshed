"""Use the influxdb_client with python native logging."""

import logging
from _typeshed import Incomplete

class InfluxLoggingHandler(logging.Handler):
    """
    InfluxLoggingHandler instances dispatch logging events to influx.

    There is no need to set a Formatter.
    The raw input will be passed on to the influx write api.
    """
    DEFAULT_LOG_RECORD_KEYS: Incomplete
    bucket: Incomplete
    client: Incomplete
    write_api: Incomplete
    def __init__(
        self, *, url, token, org, bucket, client_args: Incomplete | None = None, write_api_args: Incomplete | None = None
    ) -> None:
        """
        Initialize defaults.

        The arguments `client_args` and `write_api_args` can be dicts of kwargs.
        They are passed on to the InfluxDBClient and write_api calls respectively.
        """
        ...
    def __del__(self) -> None:
        """Make sure all resources are closed."""
        ...
    def close(self) -> None:
        """Close the write_api, client and logger."""
        ...
    def emit(self, record: logging.LogRecord) -> None:
        """Emit a record via the influxDB WriteApi."""
        ...
