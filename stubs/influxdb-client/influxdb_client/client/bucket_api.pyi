"""
A bucket is a named location where time series data is stored.

All buckets have a retention policy, a duration of time that each data point persists.
A bucket belongs to an organization.
"""

from _typeshed import Incomplete

from ..domain.bucket import Bucket
from ._pages import _PageIterator

class BucketsApi:
    """Implementation for '/api/v2/buckets' endpoint."""
    def __init__(self, influxdb_client) -> None:
        """Initialize defaults."""
        ...
    def create_bucket(
        self,
        bucket: Incomplete | None = None,
        bucket_name: Incomplete | None = None,
        org_id: Incomplete | None = None,
        retention_rules: Incomplete | None = None,
        description: Incomplete | None = None,
        org: Incomplete | None = None,
    ) -> Bucket:
        """
        Create a bucket.

        :param Bucket|PostBucketRequest bucket: bucket to create
        :param bucket_name: bucket name
        :param description: bucket description
        :param org_id: org_id
        :param bucket_name: bucket name
        :param retention_rules: retention rules array or single BucketRetentionRules
        :param str, Organization org: specifies the organization for create the bucket;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        ...
    def update_bucket(self, bucket: Bucket) -> Bucket:
        """
        Update a bucket.

        :param bucket: Bucket update to apply (required)
        :return: Bucket
        """
        ...
    def delete_bucket(self, bucket):
        """
        Delete a bucket.

        :param bucket: bucket id or Bucket
        :return: Bucket
        """
        ...
    def find_bucket_by_id(self, id):
        """
        Find bucket by ID.

        :param id:
        :return:
        """
        ...
    def find_bucket_by_name(self, bucket_name):
        """
        Find bucket by name.

        :param bucket_name: bucket name
        :return: Bucket
        """
        ...
    def find_buckets(self, **kwargs):
        """
        List buckets.

        :key int offset: Offset for pagination
        :key int limit: Limit for pagination
        :key str after: The last resource ID from which to seek from (but not including).
                        This is to be used instead of `offset`.
        :key str org: The organization name.
        :key str org_id: The organization ID.
        :key str name: Only returns buckets with a specific name.
        :return: Buckets
        """
        ...
    def find_buckets_iter(
        self, *, name: str = ..., org: str = ..., org_id: str = ..., after: str | None = None, limit: int = ...
    ) -> _PageIterator[Bucket]:
        """
        Iterate over all buckets with pagination.

        :key str name: Only returns buckets with the specified name
        :key str org: The organization name.
        :key str org_id: The organization ID.
        :key str after: The last resource ID from which to seek from (but not including).
        :key int limit: the maximum number of buckets in one page
        :return: Buckets iterator
        """
        ...
