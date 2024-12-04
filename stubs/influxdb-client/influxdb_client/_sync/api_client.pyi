"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

class ApiClient:
    """
    Generic API client for OpenAPI client library Build.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """
    PRIMITIVE_TYPES: Incomplete
    NATIVE_TYPES_MAPPING: Incomplete
    configuration: Incomplete
    pool_threads: Incomplete
    rest_client: Incomplete
    default_headers: Incomplete
    cookie: Incomplete
    def __init__(
        self,
        configuration: Incomplete | None = None,
        header_name: Incomplete | None = None,
        header_value: Incomplete | None = None,
        cookie: Incomplete | None = None,
        pool_threads: Incomplete | None = None,
        retries: bool = False,
    ) -> None:
        """Initialize generic API client."""
        ...
    def __del__(self) -> None:
        """Dispose pools."""
        ...
    @property
    def pool(self):
        """Create thread pool on first request avoids instantiating unused threadpool for blocking clients."""
        ...
    @property
    def user_agent(self):
        """User agent for this API client."""
        ...
    @user_agent.setter
    def user_agent(self, value) -> None:
        """User agent for this API client."""
        ...
    def set_default_header(self, header_name, header_value) -> None:
        """Set HTTP header for this API client."""
        ...
    def sanitize_for_serialization(self, obj):
        """
        Build a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        ...
    def deserialize(self, response, response_type):
        """
        Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        ...
    def call_api(
        self,
        resource_path,
        method,
        path_params: Incomplete | None = None,
        query_params: Incomplete | None = None,
        header_params: Incomplete | None = None,
        body: Incomplete | None = None,
        post_params: Incomplete | None = None,
        files: Incomplete | None = None,
        response_type: Incomplete | None = None,
        auth_settings: Incomplete | None = None,
        async_req: Incomplete | None = None,
        _return_http_data_only: Incomplete | None = None,
        collection_formats: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
        urlopen_kw: Incomplete | None = None,
    ):
        """
        Make the HTTP request (synchronous) and Return deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param urlopen_kw: Additional parameters are passed to
                           :meth:`urllib3.request.RequestMethods.request`
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        ...
    def request(
        self,
        method,
        url,
        query_params: Incomplete | None = None,
        headers: Incomplete | None = None,
        post_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
        **urlopen_kw,
    ):
        """Make the HTTP request using RESTClient."""
        ...
    def parameters_to_tuples(self, params, collection_formats):
        """
        Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        ...
    def prepare_post_parameters(self, post_params: Incomplete | None = None, files: Incomplete | None = None):
        """
        Build form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        ...
    def select_header_accept(self, accepts):
        """
        Return `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        ...
    def select_header_content_type(self, content_types):
        """
        Return `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        ...
    def update_params_for_auth(self, headers, querys, auth_settings) -> None:
        """
        Update header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        ...
