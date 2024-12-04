"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.domain.expression import Expression

class ArrayExpression(Expression):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = None, elements: Incomplete | None = None) -> None:
        """ArrayExpression - a model defined in OpenAPI."""
        ...
    @property
    def type(self):
        """
        Get the type of this ArrayExpression.

        Type of AST node

        :return: The type of this ArrayExpression.
        :rtype: str
        """
        ...
    @type.setter
    def type(self, type) -> None:
        """
        Get the type of this ArrayExpression.

        Type of AST node

        :return: The type of this ArrayExpression.
        :rtype: str
        """
        ...
    @property
    def elements(self):
        """
        Get the elements of this ArrayExpression.

        Elements of the array

        :return: The elements of this ArrayExpression.
        :rtype: list[Expression]
        """
        ...
    @elements.setter
    def elements(self, elements) -> None:
        """
        Get the elements of this ArrayExpression.

        Elements of the array

        :return: The elements of this ArrayExpression.
        :rtype: list[Expression]
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
