"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class BackupService(_BaseService):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """BackupService - a operation defined in OpenAPI."""
        ...
    def get_backup_kv(self, **kwargs):
        """
        Download snapshot of metadata stored in the server's embedded KV store. Don't use with InfluxDB versions greater than InfluxDB 2.1.x..

        Retrieves a snapshot of metadata stored in the server's embedded KV store. InfluxDB versions greater than 2.1.x don't include metadata stored in embedded SQL; avoid using this endpoint with versions greater than 2.1.x.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_kv(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_backup_kv_with_http_info(self, **kwargs):
        """
        Download snapshot of metadata stored in the server's embedded KV store. Don't use with InfluxDB versions greater than InfluxDB 2.1.x..

        Retrieves a snapshot of metadata stored in the server's embedded KV store. InfluxDB versions greater than 2.1.x don't include metadata stored in embedded SQL; avoid using this endpoint with versions greater than 2.1.x.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_kv_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_backup_kv_async(self, **kwargs):
        """
        Download snapshot of metadata stored in the server's embedded KV store. Don't use with InfluxDB versions greater than InfluxDB 2.1.x..

        Retrieves a snapshot of metadata stored in the server's embedded KV store. InfluxDB versions greater than 2.1.x don't include metadata stored in embedded SQL; avoid using this endpoint with versions greater than 2.1.x.
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_backup_metadata(self, **kwargs):
        """
        Download snapshot of all metadata in the server.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_metadata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: Indicates the content encoding (usually a compression algorithm) that the client can understand.
        :return: MetadataBackup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_backup_metadata_with_http_info(self, **kwargs):
        """
        Download snapshot of all metadata in the server.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_metadata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: Indicates the content encoding (usually a compression algorithm) that the client can understand.
        :return: MetadataBackup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_backup_metadata_async(self, **kwargs):
        """
        Download snapshot of all metadata in the server.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: Indicates the content encoding (usually a compression algorithm) that the client can understand.
        :return: MetadataBackup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_backup_shard_id(self, shard_id, **kwargs):
        """
        Download snapshot of all TSM data in a shard.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_shard_id(shard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int shard_id: The shard ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: Indicates the content encoding (usually a compression algorithm) that the client can understand.
        :param datetime since: The earliest time [RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp) to include in the snapshot.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_backup_shard_id_with_http_info(self, shard_id, **kwargs):
        """
        Download snapshot of all TSM data in a shard.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_shard_id_with_http_info(shard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int shard_id: The shard ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: Indicates the content encoding (usually a compression algorithm) that the client can understand.
        :param datetime since: The earliest time [RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp) to include in the snapshot.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_backup_shard_id_async(self, shard_id, **kwargs):
        """
        Download snapshot of all TSM data in a shard.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param int shard_id: The shard ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param str accept_encoding: Indicates the content encoding (usually a compression algorithm) that the client can understand.
        :param datetime since: The earliest time [RFC3339 date/time format](https://docs.influxdata.com/influxdb/latest/reference/glossary/#rfc3339-timestamp) to include in the snapshot.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
