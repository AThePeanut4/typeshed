"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class RemoteConnectionCreationRequest:
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
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        org_id: Incomplete | None = None,
        remote_url: Incomplete | None = None,
        remote_api_token: Incomplete | None = None,
        remote_org_id: Incomplete | None = None,
        allow_insecure_tls: bool = False,
    ) -> None:
        """RemoteConnectionCreationRequest - a model defined in OpenAPI."""
        ...
    @property
    def name(self):
        """
        Get the name of this RemoteConnectionCreationRequest.

        :return: The name of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @name.setter
    def name(self, name) -> None:
        """
        Get the name of this RemoteConnectionCreationRequest.

        :return: The name of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @property
    def description(self):
        """
        Get the description of this RemoteConnectionCreationRequest.

        :return: The description of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @description.setter
    def description(self, description) -> None:
        """
        Get the description of this RemoteConnectionCreationRequest.

        :return: The description of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @property
    def org_id(self):
        """
        Get the org_id of this RemoteConnectionCreationRequest.

        :return: The org_id of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @org_id.setter
    def org_id(self, org_id) -> None:
        """
        Get the org_id of this RemoteConnectionCreationRequest.

        :return: The org_id of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @property
    def remote_url(self):
        """
        Get the remote_url of this RemoteConnectionCreationRequest.

        :return: The remote_url of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @remote_url.setter
    def remote_url(self, remote_url) -> None:
        """
        Get the remote_url of this RemoteConnectionCreationRequest.

        :return: The remote_url of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @property
    def remote_api_token(self):
        """
        Get the remote_api_token of this RemoteConnectionCreationRequest.

        :return: The remote_api_token of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @remote_api_token.setter
    def remote_api_token(self, remote_api_token) -> None:
        """
        Get the remote_api_token of this RemoteConnectionCreationRequest.

        :return: The remote_api_token of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @property
    def remote_org_id(self):
        """
        Get the remote_org_id of this RemoteConnectionCreationRequest.

        :return: The remote_org_id of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @remote_org_id.setter
    def remote_org_id(self, remote_org_id) -> None:
        """
        Get the remote_org_id of this RemoteConnectionCreationRequest.

        :return: The remote_org_id of this RemoteConnectionCreationRequest.
        :rtype: str
        """
        ...
    @property
    def allow_insecure_tls(self):
        """
        Get the allow_insecure_tls of this RemoteConnectionCreationRequest.

        :return: The allow_insecure_tls of this RemoteConnectionCreationRequest.
        :rtype: bool
        """
        ...
    @allow_insecure_tls.setter
    def allow_insecure_tls(self, allow_insecure_tls) -> None:
        """
        Get the allow_insecure_tls of this RemoteConnectionCreationRequest.

        :return: The allow_insecure_tls of this RemoteConnectionCreationRequest.
        :rtype: bool
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
