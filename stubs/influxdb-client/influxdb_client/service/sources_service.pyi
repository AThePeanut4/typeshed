"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class SourcesService(_BaseService):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """SourcesService - a operation defined in OpenAPI."""
        ...
    def delete_sources_id(self, source_id, **kwargs):
        """
        Delete a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sources_id(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def delete_sources_id_with_http_info(self, source_id, **kwargs):
        """
        Delete a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sources_id_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def delete_sources_id_async(self, source_id, **kwargs):
        """
        Delete a source.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources(self, **kwargs):
        """
        List all sources.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org: The name of the organization.
        :return: Sources
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_with_http_info(self, **kwargs):
        """
        List all sources.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org: The name of the organization.
        :return: Sources
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_sources_async(self, **kwargs):
        """
        List all sources.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org: The name of the organization.
        :return: Sources
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_id(self, source_id, **kwargs):
        """
        Retrieve a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_id_with_http_info(self, source_id, **kwargs):
        """
        Retrieve a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_sources_id_async(self, source_id, **kwargs):
        """
        Retrieve a source.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_id_buckets(self, source_id, **kwargs):
        """
        Get buckets in a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_buckets(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The name of the organization.
        :return: Buckets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_id_buckets_with_http_info(self, source_id, **kwargs):
        """
        Get buckets in a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_buckets_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The name of the organization.
        :return: Buckets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_sources_id_buckets_async(self, source_id, **kwargs):
        """
        Get buckets in a source.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The name of the organization.
        :return: Buckets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_id_health(self, source_id, **kwargs):
        """
        Get the health of a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_health(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_sources_id_health_with_http_info(self, source_id, **kwargs):
        """
        Get the health of a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sources_id_health_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_sources_id_health_async(self, source_id, **kwargs):
        """
        Get the health of a source.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: HealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def patch_sources_id(self, source_id, source, **kwargs):
        """
        Update a Source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_sources_id(source_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param Source source: Source update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def patch_sources_id_with_http_info(self, source_id, source, **kwargs):
        """
        Update a Source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_sources_id_with_http_info(source_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param Source source: Source update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def patch_sources_id_async(self, source_id, source, **kwargs):
        """
        Update a Source.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str source_id: The source ID. (required)
        :param Source source: Source update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_sources(self, source, **kwargs):
        """
        Create a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sources(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Source source: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_sources_with_http_info(self, source, **kwargs):
        """
        Create a source.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sources_with_http_info(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Source source: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def post_sources_async(self, source, **kwargs):
        """
        Create a source.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param Source source: Source to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
