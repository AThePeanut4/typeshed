"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Error:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        code: Incomplete | None = None,
        message: Incomplete | None = None,
        op: Incomplete | None = None,
        err: Incomplete | None = None,
    ) -> None:
        """Error - a model defined in OpenAPI."""
        ...
    @property
    def code(self):
        """
        Get the code of this Error.

        code is the machine-readable error code.

        :return: The code of this Error.
        :rtype: str
        """
        ...
    @code.setter
    def code(self, code) -> None:
        """
        Get the code of this Error.

        code is the machine-readable error code.

        :return: The code of this Error.
        :rtype: str
        """
        ...
    @property
    def message(self):
        """
        Get the message of this Error.

        Human-readable message.

        :return: The message of this Error.
        :rtype: str
        """
        ...
    @message.setter
    def message(self, message) -> None:
        """
        Get the message of this Error.

        Human-readable message.

        :return: The message of this Error.
        :rtype: str
        """
        ...
    @property
    def op(self):
        """
        Get the op of this Error.

        Describes the logical code operation when the error occurred. Useful for debugging.

        :return: The op of this Error.
        :rtype: str
        """
        ...
    @op.setter
    def op(self, op) -> None:
        """
        Get the op of this Error.

        Describes the logical code operation when the error occurred. Useful for debugging.

        :return: The op of this Error.
        :rtype: str
        """
        ...
    @property
    def err(self):
        """
        Get the err of this Error.

        Stack of errors that occurred during processing of the request. Useful for debugging.

        :return: The err of this Error.
        :rtype: str
        """
        ...
    @err.setter
    def err(self, err) -> None:
        """
        Get the err of this Error.

        Stack of errors that occurred during processing of the request. Useful for debugging.

        :return: The err of this Error.
        :rtype: str
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
