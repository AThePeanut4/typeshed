"""
Helpers classes to make easier use the client in multiprocessing environment.

For more information how the multiprocessing works see Python's
`reference docs <https://docs.python.org/3/library/multiprocessing.html>`_.
"""

import multiprocessing
from _typeshed import Incomplete
from types import TracebackType

logger: Incomplete

class _PoisonPill:
    """To notify process to terminate."""
    ...

class MultiprocessingWriter(multiprocessing.Process):
    """
    The Helper class to write data into InfluxDB in independent OS process.

    Example:
        .. code-block:: python

            from influxdb_client import WriteOptions
            from influxdb_client.client.util.multiprocessing_helper import MultiprocessingWriter


            def main():
                writer = MultiprocessingWriter(url="http://localhost:8086", token="my-token", org="my-org",
                                               write_options=WriteOptions(batch_size=100))
                writer.start()

                for x in range(1, 1000):
                    writer.write(bucket="my-bucket", record=f"mem,tag=a value={x}i {x}")

                writer.__del__()


            if __name__ == '__main__':
                main()


    How to use with context_manager:
        .. code-block:: python

            from influxdb_client import WriteOptions
            from influxdb_client.client.util.multiprocessing_helper import MultiprocessingWriter


            def main():
                with MultiprocessingWriter(url="http://localhost:8086", token="my-token", org="my-org",
                                           write_options=WriteOptions(batch_size=100)) as writer:
                    for x in range(1, 1000):
                        writer.write(bucket="my-bucket", record=f"mem,tag=a value={x}i {x}")


            if __name__ == '__main__':
                main()


    How to handle batch events:
        .. code-block:: python

            from influxdb_client import WriteOptions
            from influxdb_client.client.exceptions import InfluxDBError
            from influxdb_client.client.util.multiprocessing_helper import MultiprocessingWriter


            class BatchingCallback(object):

                def success(self, conf: (str, str, str), data: str):
                    print(f"Written batch: {conf}, data: {data}")

                def error(self, conf: (str, str, str), data: str, exception: InfluxDBError):
                    print(f"Cannot write batch: {conf}, data: {data} due: {exception}")

                def retry(self, conf: (str, str, str), data: str, exception: InfluxDBError):
                    print(f"Retryable error occurs for batch: {conf}, data: {data} retry: {exception}")


            def main():
                callback = BatchingCallback()
                with MultiprocessingWriter(url="http://localhost:8086", token="my-token", org="my-org",
                                           success_callback=callback.success,
                                           error_callback=callback.error,
                                           retry_callback=callback.retry) as writer:

                    for x in range(1, 1000):
                        writer.write(bucket="my-bucket", record=f"mem,tag=a value={x}i {x}")


            if __name__ == '__main__':
                main()
    """
    __started__: bool
    __disposed__: bool
    kwargs: Incomplete
    client: Incomplete
    write_api: Incomplete
    queue_: Incomplete
    def __init__(self, **kwargs) -> None:
        """
        Initialize defaults.

        For more information how to initialize the writer see the examples above.

        :param kwargs: arguments are passed into ``__init__`` function of ``InfluxDBClient`` and ``write_api``.
        """
        ...
    def write(self, **kwargs) -> None:
        """
        Append time-series data into underlying queue.

        For more information how to pass arguments see the examples above.

        :param kwargs: arguments are passed into ``write`` function of ``WriteApi``
        :return: None
        """
        ...
    def run(self) -> None:
        """Initialize ``InfluxDBClient`` and waits for data to writes into InfluxDB."""
        ...
    def start(self) -> None:
        """Start independent process for writing data into InfluxDB."""
        ...
    def terminate(self) -> None:
        """
        Cleanup resources in independent process.

        This function **cannot be used** to terminate the ``MultiprocessingWriter``.
        If you want to finish your writes please call: ``__del__``.
        """
        ...
    def __enter__(self):
        """Enter the runtime context related to this object."""
        ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None:
        """Exit the runtime context related to this object."""
        ...
    def __del__(self) -> None:
        """Dispose the client and write_api."""
        ...
