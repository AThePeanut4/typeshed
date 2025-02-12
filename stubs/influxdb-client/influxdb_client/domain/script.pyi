"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class Script:
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
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        org_id: Incomplete | None = None,
        script: Incomplete | None = None,
        language: Incomplete | None = None,
        url: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
    ) -> None:
        """Script - a model defined in OpenAPI."""
        ...
    @property
    def id(self):
        """
        Get the id of this Script.

        :return: The id of this Script.
        :rtype: str
        """
        ...
    @id.setter
    def id(self, id) -> None:
        """
        Get the id of this Script.

        :return: The id of this Script.
        :rtype: str
        """
        ...
    @property
    def name(self):
        """
        Get the name of this Script.

        :return: The name of this Script.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this Script.

        :return: The name of this Script.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this Script.

        :return: The description of this Script.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this Script.

        :return: The description of this Script.
        :rtype: str
        """
        ...
    @property
    def org_id(self):
        """
        Get the org_id of this Script.

        :return: The org_id of this Script.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id) -> None:
        """
        Get the org_id of this Script.

        :return: The org_id of this Script.
        :rtype: str
        """
        ...
    @property
    def script(self):
        """
        Get the script of this Script.

        The script to execute.

        :return: The script of this Script.
        :rtype: str
        """
        ...
    @script.setter
    def script(self, script) -> None:
        """
        Get the script of this Script.

        The script to execute.

        :return: The script of this Script.
        :rtype: str
        """
        ...
    @property
    def language(self):
        """
        Get the language of this Script.

        :return: The language of this Script.
        :rtype: ScriptLanguage
        """
        ...
    @language.setter
    def language(self, language) -> None:
        """
        Get the language of this Script.

        :return: The language of this Script.
        :rtype: ScriptLanguage
        """
        ...
    @property
    def url(self):
        """
        Get the url of this Script.

        The invocation endpoint address.

        :return: The url of this Script.
        :rtype: str
        """
        ...
    @url.setter
    def url(self, url) -> None:
        """
        Get the url of this Script.

        The invocation endpoint address.

        :return: The url of this Script.
        :rtype: str
        """
        ...
    @property
    def created_at(self):
        """
        Get the created_at of this Script.

        :return: The created_at of this Script.
        :rtype: datetime
        """
        ...
    @created_at.setter
    def created_at(self, created_at) -> None:
        """
        Get the created_at of this Script.

        :return: The created_at of this Script.
        :rtype: datetime
        """
        ...
    @property
    def updated_at(self):
        """
        Get the updated_at of this Script.

        :return: The updated_at of this Script.
        :rtype: datetime
        """
        ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None:
        """
        Get the updated_at of this Script.

        :return: The updated_at of this Script.
        :rtype: datetime
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
