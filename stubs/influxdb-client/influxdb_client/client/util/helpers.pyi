"""Functions to share utility across client classes."""

from influxdb_client.client.influxdb_client import InfluxDBClient
from influxdb_client.domain.organization import Organization

def get_org_query_param(org: Organization | str | None, client: InfluxDBClient, required_id: bool = False) -> str:
    """
    Get required type of Org query parameter.

    :param str, Organization org: value provided as a parameter into API (optional)
    :param InfluxDBClient client: with default value for Org parameter
    :param bool required_id: true if the query param has to be a ID
    :return: request type of org query parameter or None
    """
    ...
