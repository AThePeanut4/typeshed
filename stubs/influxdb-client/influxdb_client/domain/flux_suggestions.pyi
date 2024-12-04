"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class FluxSuggestions:
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, funcs: Incomplete | None = None) -> None:
        """FluxSuggestions - a model defined in OpenAPI."""
        ...
    @property
    def funcs(self):
        """
        Get the funcs of this FluxSuggestions.

        :return: The funcs of this FluxSuggestions.
        :rtype: list[FluxSuggestion]
        """
        ...
    @funcs.setter
    def funcs(self, funcs) -> None:
        """
        Get the funcs of this FluxSuggestions.

        :return: The funcs of this FluxSuggestions.
        :rtype: list[FluxSuggestion]
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
