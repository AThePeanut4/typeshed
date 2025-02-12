"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class SetupService(_BaseService):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """SetupService - a operation defined in OpenAPI."""
        ...
    def get_setup(self, **kwargs):
        """
        Check if database has default user, org, bucket.

        Returns `true` if no default user, organization, or bucket has been created.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_setup(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: IsOnboarding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_setup_with_http_info(self, **kwargs):
        """
        Check if database has default user, org, bucket.

        Returns `true` if no default user, organization, or bucket has been created.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_setup_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: IsOnboarding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_setup_async(self, **kwargs):
        """
        Check if database has default user, org, bucket.

        Returns `true` if no default user, organization, or bucket has been created.
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: IsOnboarding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_setup(self, onboarding_request, **kwargs):
        """
        Set up initial user, org and bucket.

        Post an onboarding request to set up initial user, org and bucket.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_setup(onboarding_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OnboardingRequest onboarding_request: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: OnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_setup_with_http_info(self, onboarding_request, **kwargs):
        """
        Set up initial user, org and bucket.

        Post an onboarding request to set up initial user, org and bucket.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_setup_with_http_info(onboarding_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OnboardingRequest onboarding_request: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: OnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def post_setup_async(self, onboarding_request, **kwargs):
        """
        Set up initial user, org and bucket.

        Post an onboarding request to set up initial user, org and bucket.
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param OnboardingRequest onboarding_request: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: OnboardingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
