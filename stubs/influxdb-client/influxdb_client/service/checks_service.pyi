"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class ChecksService(_BaseService):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """ChecksService - a operation defined in OpenAPI."""
        ...
    def create_check(self, post_check, **kwargs):
        """
        Add new check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_check(post_check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostCheck post_check: Check to create (required)
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def create_check_with_http_info(self, post_check, **kwargs):
        """
        Add new check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_check_with_http_info(post_check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostCheck post_check: Check to create (required)
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def create_check_async(self, post_check, **kwargs):
        """
        Add new check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param PostCheck post_check: Check to create (required)
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def delete_checks_id(self, check_id, **kwargs):
        """
        Delete a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def delete_checks_id_with_http_info(self, check_id, **kwargs):
        """
        Delete a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def delete_checks_id_async(self, check_id, **kwargs):
        """
        Delete a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def delete_checks_id_labels_id(self, check_id, label_id, **kwargs):
        """
        Delete label from a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id_labels_id(check_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str label_id: The ID of the label to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def delete_checks_id_labels_id_with_http_info(self, check_id, label_id, **kwargs):
        """
        Delete label from a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id_labels_id_with_http_info(check_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str label_id: The ID of the label to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def delete_checks_id_labels_id_async(self, check_id, label_id, **kwargs):
        """
        Delete label from a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str label_id: The ID of the label to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks(self, org_id, **kwargs):
        """
        List all checks.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: Only show checks that belong to a specific organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset: The offset for pagination. The number of records to skip.  For more information about pagination parameters, see [Pagination](https://docs.influxdata.com/influxdb/latest/api/#tag/Pagination).
        :param int limit: Limits the number of records returned. Default is `20`.
        :return: Checks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_with_http_info(self, org_id, **kwargs):
        """
        List all checks.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: Only show checks that belong to a specific organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset: The offset for pagination. The number of records to skip.  For more information about pagination parameters, see [Pagination](https://docs.influxdata.com/influxdb/latest/api/#tag/Pagination).
        :param int limit: Limits the number of records returned. Default is `20`.
        :return: Checks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_checks_async(self, org_id, **kwargs):
        """
        List all checks.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str org_id: Only show checks that belong to a specific organization ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :param int offset: The offset for pagination. The number of records to skip.  For more information about pagination parameters, see [Pagination](https://docs.influxdata.com/influxdb/latest/api/#tag/Pagination).
        :param int limit: Limits the number of records returned. Default is `20`.
        :return: Checks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_id(self, check_id, **kwargs):
        """
        Retrieve a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_id_with_http_info(self, check_id, **kwargs):
        """
        Retrieve a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_checks_id_async(self, check_id, **kwargs):
        """
        Retrieve a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_id_labels(self, check_id, **kwargs):
        """
        List all labels for a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_labels(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_id_labels_with_http_info(self, check_id, **kwargs):
        """
        List all labels for a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_labels_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_checks_id_labels_async(self, check_id, **kwargs):
        """
        List all labels for a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_id_query(self, check_id, **kwargs):
        """
        Retrieve a check query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_query(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_checks_id_query_with_http_info(self, check_id, **kwargs):
        """
        Retrieve a check query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_query_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_checks_id_query_async(self, check_id, **kwargs):
        """
        Retrieve a check query.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def patch_checks_id(self, check_id, check_patch, **kwargs):
        """
        Update a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_checks_id(check_id, check_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param CheckPatch check_patch: Check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def patch_checks_id_with_http_info(self, check_id, check_patch, **kwargs):
        """
        Update a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_checks_id_with_http_info(check_id, check_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param CheckPatch check_patch: Check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def patch_checks_id_async(self, check_id, check_patch, **kwargs):
        """
        Update a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param CheckPatch check_patch: Check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_checks_id_labels(self, check_id, label_mapping, **kwargs):
        """
        Add a label to a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_checks_id_labels(check_id, label_mapping, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param LabelMapping label_mapping: Label to add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def post_checks_id_labels_with_http_info(self, check_id, label_mapping, **kwargs):
        """
        Add a label to a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_checks_id_labels_with_http_info(check_id, label_mapping, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param LabelMapping label_mapping: Label to add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def post_checks_id_labels_async(self, check_id, label_mapping, **kwargs):
        """
        Add a label to a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param LabelMapping label_mapping: Label to add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def put_checks_id(self, check_id, check, **kwargs):
        """
        Update a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_checks_id(check_id, check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param Check check: Check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def put_checks_id_with_http_info(self, check_id, check, **kwargs):
        """
        Update a check.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_checks_id_with_http_info(check_id, check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param Check check: Check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def put_checks_id_async(self, check_id, check, **kwargs):
        """
        Update a check.

        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str check_id: The check ID. (required)
        :param Check check: Check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
