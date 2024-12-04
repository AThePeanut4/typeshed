"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class PasswordResetBody:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, password: Incomplete | None = None) -> None:
        """PasswordResetBody - a model defined in OpenAPI."""
        ...
    @property
    def password(self):
        """
        Get the password of this PasswordResetBody.

        :return: The password of this PasswordResetBody.
        :rtype: str
        """
        ...
    @password.setter
    def password(self, password) -> None:
        """
        Get the password of this PasswordResetBody.

        :return: The password of this PasswordResetBody.
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
