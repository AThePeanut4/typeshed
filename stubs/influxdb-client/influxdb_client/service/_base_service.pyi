from _typeshed import Incomplete

class _BaseService:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """Init common services operation."""
        ...
    def build_type(self) -> str:
        """
        Return the build type of the connected InfluxDB Server.

        :return: The type of InfluxDB build.
        """
        ...
    async def build_type_async(self) -> str:
        """
        Return the build type of the connected InfluxDB Server.

        :return: The type of InfluxDB build.
        """
        ...
    def response_header(self, response, header_name: str = "X-Influxdb-Version") -> str: ...
