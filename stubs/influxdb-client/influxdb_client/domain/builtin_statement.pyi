"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.statement import Statement

class BuiltinStatement(Statement):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = None, id: Incomplete | None = None) -> None:
        """BuiltinStatement - a model defined in OpenAPI."""
        ...
    @property
    def type(self):
        """
        Get the type of this BuiltinStatement.

        Type of AST node

        :return: The type of this BuiltinStatement.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this BuiltinStatement.

        Type of AST node

        :return: The type of this BuiltinStatement.
        :rtype: str
        """
        ...
    @property
    def id(self):
        """
        Get the id of this BuiltinStatement.

        :return: The id of this BuiltinStatement.
        :rtype: Identifier
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this BuiltinStatement.

        :return: The id of this BuiltinStatement.
        :rtype: Identifier
        """
        ...
    def to_dict(self):
        """Return the model properties as a dict."""
        ...
    def to_str(self):
        """Return the string representation of the model."""
        ...
    def __eq__(self, other):
        """Return true if both objects are equal."""
        ...
    def __ne__(self, other):
        """Return true if both objects are not equal."""
        ...
