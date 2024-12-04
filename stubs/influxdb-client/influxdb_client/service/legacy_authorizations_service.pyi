"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class LegacyAuthorizationsService(_BaseService):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """LegacyAuthorizationsService - a operation defined in OpenAPI."""
        ...
    def delete_legacy_authorizations_id(self, auth_id, **kwargs):
        """
        Delete a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_legacy_authorizations_id(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def delete_legacy_authorizations_id_with_http_info(self, auth_id, **kwargs):
        """
        Delete a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_legacy_authorizations_id_with_http_info(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def delete_legacy_authorizations_id_async(self, auth_id, **kwargs):
        """
        Delete a legacy authorization.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_legacy_authorizations(self, **kwargs):
        """
        List all legacy authorizations.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show legacy authorizations that belong to a user ID.
        :param str user: Only show legacy authorizations that belong to a user name.
        :param str org_id: Only show legacy authorizations that belong to an organization ID.
        :param str org: Only show legacy authorizations that belong to a organization name.
        :param str token: Only show legacy authorizations with a specified token (auth name).
        :param str auth_id: Only show legacy authorizations with a specified auth ID.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_legacy_authorizations_with_http_info(self, **kwargs):
        """
        List all legacy authorizations.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show legacy authorizations that belong to a user ID.
        :param str user: Only show legacy authorizations that belong to a user name.
        :param str org_id: Only show legacy authorizations that belong to an organization ID.
        :param str org: Only show legacy authorizations that belong to a organization name.
        :param str token: Only show legacy authorizations with a specified token (auth name).
        :param str auth_id: Only show legacy authorizations with a specified auth ID.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_legacy_authorizations_async(self, **kwargs):
        """
        List all legacy authorizations.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show legacy authorizations that belong to a user ID.
        :param str user: Only show legacy authorizations that belong to a user name.
        :param str org_id: Only show legacy authorizations that belong to an organization ID.
        :param str org: Only show legacy authorizations that belong to a organization name.
        :param str token: Only show legacy authorizations with a specified token (auth name).
        :param str auth_id: Only show legacy authorizations with a specified auth ID.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_legacy_authorizations_id(self, auth_id, **kwargs):
        """
        Retrieve a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations_id(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_legacy_authorizations_id_with_http_info(self, auth_id, **kwargs):
        """
        Retrieve a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legacy_authorizations_id_with_http_info(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_legacy_authorizations_id_async(self, auth_id, **kwargs):
        """
        Retrieve a legacy authorization.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def patch_legacy_authorizations_id(self, auth_id, authorization_update_request, **kwargs):
        """
        Update a legacy authorization to be active or inactive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_legacy_authorizations_id(auth_id, authorization_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Legacy authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def patch_legacy_authorizations_id_with_http_info(self, auth_id, authorization_update_request, **kwargs):
        """
        Update a legacy authorization to be active or inactive.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_legacy_authorizations_id_with_http_info(auth_id, authorization_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Legacy authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def patch_legacy_authorizations_id_async(self, auth_id, authorization_update_request, **kwargs):
        """
        Update a legacy authorization to be active or inactive.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Legacy authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_legacy_authorizations(self, legacy_authorization_post_request, **kwargs):
        """
        Create a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations(legacy_authorization_post_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LegacyAuthorizationPostRequest legacy_authorization_post_request: Legacy authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_legacy_authorizations_with_http_info(self, legacy_authorization_post_request, **kwargs):
        """
        Create a legacy authorization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations_with_http_info(legacy_authorization_post_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LegacyAuthorizationPostRequest legacy_authorization_post_request: Legacy authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def post_legacy_authorizations_async(self, legacy_authorization_post_request, **kwargs):
        """
        Create a legacy authorization.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param LegacyAuthorizationPostRequest legacy_authorization_post_request: Legacy authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_legacy_authorizations_id_password(self, auth_id, password_reset_body, **kwargs):
        """
        Set a legacy authorization password.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations_id_password(auth_id, password_reset_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param PasswordResetBody password_reset_body: New password (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_legacy_authorizations_id_password_with_http_info(self, auth_id, password_reset_body, **kwargs):
        """
        Set a legacy authorization password.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_legacy_authorizations_id_password_with_http_info(auth_id, password_reset_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param PasswordResetBody password_reset_body: New password (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def post_legacy_authorizations_id_password_async(self, auth_id, password_reset_body, **kwargs):
        """
        Set a legacy authorization password.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str auth_id: The ID of the legacy authorization to update. (required)
        :param PasswordResetBody password_reset_body: New password (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
