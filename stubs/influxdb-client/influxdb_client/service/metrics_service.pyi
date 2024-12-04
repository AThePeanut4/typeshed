"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class MetricsService(_BaseService):
    """
    NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client: Incomplete | None = None) -> None:
        """MetricsService - a operation defined in OpenAPI."""
        ...
    def get_metrics(self, **kwargs):
        """
        Retrieve workload performance metrics.

        Returns metrics about the workload performance of an InfluxDB instance.  Use this endpoint to get performance, resource, and usage metrics.  #### Related guides  - For the list of metrics categories, see [InfluxDB OSS metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/). - Learn how to use InfluxDB to [scrape Prometheus metrics](https://docs.influxdata.com/influxdb/latest/write-data/developer-tools/scrape-prometheus-metrics/). - Learn how InfluxDB [parses the Prometheus exposition format](https://docs.influxdata.com/influxdb/latest/reference/prometheus-metrics/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def get_metrics_with_http_info(self, **kwargs):
        """
        Retrieve workload performance metrics.

        Returns metrics about the workload performance of an InfluxDB instance.  Use this endpoint to get performance, resource, and usage metrics.  #### Related guides  - For the list of metrics categories, see [InfluxDB OSS metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/). - Learn how to use InfluxDB to [scrape Prometheus metrics](https://docs.influxdata.com/influxdb/latest/write-data/developer-tools/scrape-prometheus-metrics/). - Learn how InfluxDB [parses the Prometheus exposition format](https://docs.influxdata.com/influxdb/latest/reference/prometheus-metrics/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    async def get_metrics_async(self, **kwargs):
        """
        Retrieve workload performance metrics.

        Returns metrics about the workload performance of an InfluxDB instance.  Use this endpoint to get performance, resource, and usage metrics.  #### Related guides  - For the list of metrics categories, see [InfluxDB OSS metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/). - Learn how to use InfluxDB to [scrape Prometheus metrics](https://docs.influxdata.com/influxdb/latest/write-data/developer-tools/scrape-prometheus-metrics/). - Learn how InfluxDB [parses the Prometheus exposition format](https://docs.influxdata.com/influxdb/latest/reference/prometheus-metrics/).
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
