"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete
from typing import ClassVar, Final

class ScriptLanguage:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    FLUX: Final = "flux"
    SQL: Final = "sql"
    INFLUXQL: Final = "influxql"

    openapi_types: ClassVar[dict[Incomplete, Incomplete]]
    attribute_map: ClassVar[dict[Incomplete, Incomplete]]
    def to_dict(self) -> dict[Incomplete, Incomplete]:
        """Return the model properties as a dict."""
        ...
    def to_str(self) -> str:
        """Return the string representation of the model."""
        ...
    def __eq__(self, other: object) -> bool:
        """Return true if both objects are equal."""
        ...
    def __ne__(self, other: object) -> bool:
        """Return true if both objects are not equal."""
        ...
