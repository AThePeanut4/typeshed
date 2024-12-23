"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class TelegrafPlugins:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, version: Incomplete | None = None, os: Incomplete | None = None, plugins: Incomplete | None = None
    ) -> None:
        """TelegrafPlugins - a model defined in OpenAPI."""
        ...
    @property
    def version(self):
        """
        Get the version of this TelegrafPlugins.

        :return: The version of this TelegrafPlugins.
        :rtype: str
        """
        ...
    @version.setter
    def version(self, version) -> None:
        """
        Get the version of this TelegrafPlugins.

        :return: The version of this TelegrafPlugins.
        :rtype: str
        """
        ...
    @property
    def os(self):
        """
        Get the os of this TelegrafPlugins.

        :return: The os of this TelegrafPlugins.
        :rtype: str
        """
        ...
    @os.setter
    def os(self, os) -> None:
        """
        Get the os of this TelegrafPlugins.

        :return: The os of this TelegrafPlugins.
        :rtype: str
        """
        ...
    @property
    def plugins(self):
        """
        Get the plugins of this TelegrafPlugins.

        :return: The plugins of this TelegrafPlugins.
        :rtype: list[TelegrafPlugin]
        """
        ...
    @plugins.setter
    def plugins(self, plugins) -> None:
        """
        Get the plugins of this TelegrafPlugins.

        :return: The plugins of this TelegrafPlugins.
        :rtype: list[TelegrafPlugin]
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
