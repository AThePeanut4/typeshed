from typing import Literal
from typing_extensions import TypeAlias

_Key: TypeAlias = bytes | str | memoryview

ADD_CMD: Literal["TS.ADD"]
ALTER_CMD: Literal["TS.ALTER"]
CREATERULE_CMD: Literal["TS.CREATERULE"]
CREATE_CMD: Literal["TS.CREATE"]
DECRBY_CMD: Literal["TS.DECRBY"]
DELETERULE_CMD: Literal["TS.DELETERULE"]
DEL_CMD: Literal["TS.DEL"]
GET_CMD: Literal["TS.GET"]
INCRBY_CMD: Literal["TS.INCRBY"]
INFO_CMD: Literal["TS.INFO"]
MADD_CMD: Literal["TS.MADD"]
MGET_CMD: Literal["TS.MGET"]
MRANGE_CMD: Literal["TS.MRANGE"]
MREVRANGE_CMD: Literal["TS.MREVRANGE"]
QUERYINDEX_CMD: Literal["TS.QUERYINDEX"]
RANGE_CMD: Literal["TS.RANGE"]
REVRANGE_CMD: Literal["TS.REVRANGE"]

class TimeSeriesCommands:
    """RedisTimeSeries Commands."""
    def create(
        self,
        key: _Key,
        retention_msecs: int | None = None,
        uncompressed: bool | None = False,
        labels: dict[str, str] | None = None,
        chunk_size: int | None = None,
        duplicate_policy: str | None = None,
    ):
        """
        Create a new time-series.

        Args:

        key:
            time-series key
        retention_msecs:
            Maximum age for samples compared to highest reported timestamp (in milliseconds).
            If None or 0 is passed then  the series is not trimmed at all.
        uncompressed:
            Changes data storage from compressed (by default) to uncompressed
        labels:
            Set of label-value pairs that represent metadata labels of the key.
        chunk_size:
            Memory size, in bytes, allocated for each data chunk.
            Must be a multiple of 8 in the range [128 .. 1048576].
        duplicate_policy:
            Policy for handling multiple samples with identical timestamps.
            Can be one of:
            - 'block': an error will occur for any out of order sample.
            - 'first': ignore the new value.
            - 'last': override with latest value.
            - 'min': only override if the value is lower than the existing value.
            - 'max': only override if the value is higher than the existing value.

        For more information: https://redis.io/commands/ts.create/
        """
        ...
    def alter(
        self,
        key: _Key,
        retention_msecs: int | None = None,
        labels: dict[str, str] | None = None,
        chunk_size: int | None = None,
        duplicate_policy: str | None = None,
    ):
        """
        Update the retention, chunk size, duplicate policy, and labels of an existing
        time series.

        Args:

        key:
            time-series key
        retention_msecs:
            Maximum retention period, compared to maximal existing timestamp (in milliseconds).
            If None or 0 is passed then  the series is not trimmed at all.
        labels:
            Set of label-value pairs that represent metadata labels of the key.
        chunk_size:
            Memory size, in bytes, allocated for each data chunk.
            Must be a multiple of 8 in the range [128 .. 1048576].
        duplicate_policy:
            Policy for handling multiple samples with identical timestamps.
            Can be one of:
            - 'block': an error will occur for any out of order sample.
            - 'first': ignore the new value.
            - 'last': override with latest value.
            - 'min': only override if the value is lower than the existing value.
            - 'max': only override if the value is higher than the existing value.

        For more information: https://redis.io/commands/ts.alter/
        """
        ...
    def add(
        self,
        key: _Key,
        timestamp: int | str,
        value: float,
        retention_msecs: int | None = None,
        uncompressed: bool | None = False,
        labels: dict[str, str] | None = None,
        chunk_size: int | None = None,
        duplicate_policy: str | None = None,
    ):
        """
        Append (or create and append) a new sample to a time series.

        Args:

        key:
            time-series key
        timestamp:
            Timestamp of the sample. * can be used for automatic timestamp (using the system clock).
        value:
            Numeric data value of the sample
        retention_msecs:
            Maximum retention period, compared to maximal existing timestamp (in milliseconds).
            If None or 0 is passed then  the series is not trimmed at all.
        uncompressed:
            Changes data storage from compressed (by default) to uncompressed
        labels:
            Set of label-value pairs that represent metadata labels of the key.
        chunk_size:
            Memory size, in bytes, allocated for each data chunk.
            Must be a multiple of 8 in the range [128 .. 1048576].
        duplicate_policy:
            Policy for handling multiple samples with identical timestamps.
            Can be one of:
            - 'block': an error will occur for any out of order sample.
            - 'first': ignore the new value.
            - 'last': override with latest value.
            - 'min': only override if the value is lower than the existing value.
            - 'max': only override if the value is higher than the existing value.

        For more information: https://redis.io/commands/ts.add/
        """
        ...
    def madd(self, ktv_tuples):
        """
        Append (or create and append) a new `value` to series
        `key` with `timestamp`.
        Expects a list of `tuples` as (`key`,`timestamp`, `value`).
        Return value is an array with timestamps of insertions.

        For more information: https://redis.io/commands/ts.madd/
        """
        ...
    def incrby(
        self,
        key: _Key,
        value: float,
        timestamp: int | str | None = None,
        retention_msecs: int | None = None,
        uncompressed: bool | None = False,
        labels: dict[str, str] | None = None,
        chunk_size: int | None = None,
    ):
        """
        Increment (or create an time-series and increment) the latest sample's of a series.
        This command can be used as a counter or gauge that automatically gets history as a time series.

        Args:

        key:
            time-series key
        value:
            Numeric data value of the sample
        timestamp:
            Timestamp of the sample. * can be used for automatic timestamp (using the system clock).
        retention_msecs:
            Maximum age for samples compared to last event time (in milliseconds).
            If None or 0 is passed then  the series is not trimmed at all.
        uncompressed:
            Changes data storage from compressed (by default) to uncompressed
        labels:
            Set of label-value pairs that represent metadata labels of the key.
        chunk_size:
            Memory size, in bytes, allocated for each data chunk.

        For more information: https://redis.io/commands/ts.incrby/
        """
        ...
    def decrby(
        self,
        key: _Key,
        value: float,
        timestamp: int | str | None = None,
        retention_msecs: int | None = None,
        uncompressed: bool | None = False,
        labels: dict[str, str] | None = None,
        chunk_size: int | None = None,
    ):
        """
        Decrement (or create an time-series and decrement) the latest sample's of a series.
        This command can be used as a counter or gauge that automatically gets history as a time series.

        Args:

        key:
            time-series key
        value:
            Numeric data value of the sample
        timestamp:
            Timestamp of the sample. * can be used for automatic timestamp (using the system clock).
        retention_msecs:
            Maximum age for samples compared to last event time (in milliseconds).
            If None or 0 is passed then  the series is not trimmed at all.
        uncompressed:
            Changes data storage from compressed (by default) to uncompressed
        labels:
            Set of label-value pairs that represent metadata labels of the key.
        chunk_size:
            Memory size, in bytes, allocated for each data chunk.

        For more information: https://redis.io/commands/ts.decrby/
        """
        ...
    def delete(self, key, from_time, to_time):
        """
        Delete all samples between two timestamps for a given time series.

        Args:

        key:
            time-series key.
        from_time:
            Start timestamp for the range deletion.
        to_time:
            End timestamp for the range deletion.

        For more information: https://redis.io/commands/ts.del/
        """
        ...
    def createrule(
        self, source_key: _Key, dest_key: _Key, aggregation_type: str, bucket_size_msec: int, align_timestamp: int | None = None
    ):
        """
        Create a compaction rule from values added to `source_key` into `dest_key`.

        Args:

        source_key:
            Key name for source time series
        dest_key:
            Key name for destination (compacted) time series
        aggregation_type:
            Aggregation type: One of the following:
            [`avg`, `sum`, `min`, `max`, `range`, `count`, `first`, `last`, `std.p`,
            `std.s`, `var.p`, `var.s`, `twa`]
        bucket_size_msec:
            Duration of each bucket, in milliseconds
        align_timestamp:
            Assure that there is a bucket that starts at exactly align_timestamp and
            align all other buckets accordingly.

        For more information: https://redis.io/commands/ts.createrule/
        """
        ...
    def deleterule(self, source_key, dest_key):
        """
        Delete a compaction rule from `source_key` to `dest_key`..

        For more information: https://redis.io/commands/ts.deleterule/
        """
        ...
    def range(
        self,
        key: _Key,
        from_time: int | str,
        to_time: int | str,
        count: int | None = None,
        aggregation_type: str | None = None,
        bucket_size_msec: int | None = 0,
        filter_by_ts: list[int] | None = None,
        filter_by_min_value: int | None = None,
        filter_by_max_value: int | None = None,
        align: int | str | None = None,
        latest: bool | None = False,
        bucket_timestamp: str | None = None,
        empty: bool | None = False,
    ):
        """
        Query a range in forward direction for a specific time-serie.

        Args:

        key:
            Key name for timeseries.
        from_time:
            Start timestamp for the range query. - can be used to express the minimum possible timestamp (0).
        to_time:
            End timestamp for range query, + can be used to express the maximum possible timestamp.
        count:
            Limits the number of returned samples.
        aggregation_type:
            Optional aggregation type. Can be one of [`avg`, `sum`, `min`, `max`,
            `range`, `count`, `first`, `last`, `std.p`, `std.s`, `var.p`, `var.s`, `twa`]
        bucket_size_msec:
            Time bucket for aggregation in milliseconds.
        filter_by_ts:
            List of timestamps to filter the result by specific timestamps.
        filter_by_min_value:
            Filter result by minimum value (must mention also filter by_max_value).
        filter_by_max_value:
            Filter result by maximum value (must mention also filter by_min_value).
        align:
            Timestamp for alignment control for aggregation.
        latest:
            Used when a time series is a compaction, reports the compacted value of the
            latest possibly partial bucket
        bucket_timestamp:
            Controls how bucket timestamps are reported. Can be one of [`-`, `low`, `+`,
            `high`, `~`, `mid`].
        empty:
            Reports aggregations for empty buckets.

        For more information: https://redis.io/commands/ts.range/
        """
        ...
    def revrange(
        self,
        key: _Key,
        from_time: int | str,
        to_time: int | str,
        count: int | None = None,
        aggregation_type: str | None = None,
        bucket_size_msec: int | None = 0,
        filter_by_ts: list[int] | None = None,
        filter_by_min_value: int | None = None,
        filter_by_max_value: int | None = None,
        align: int | str | None = None,
        latest: bool | None = False,
        bucket_timestamp: str | None = None,
        empty: bool | None = False,
    ):
        """
        Query a range in reverse direction for a specific time-series.

        **Note**: This command is only available since RedisTimeSeries >= v1.4

        Args:

        key:
            Key name for timeseries.
        from_time:
            Start timestamp for the range query. - can be used to express the minimum possible timestamp (0).
        to_time:
            End timestamp for range query, + can be used to express the maximum possible timestamp.
        count:
            Limits the number of returned samples.
        aggregation_type:
            Optional aggregation type. Can be one of [`avg`, `sum`, `min`, `max`,
            `range`, `count`, `first`, `last`, `std.p`, `std.s`, `var.p`, `var.s`, `twa`]
        bucket_size_msec:
            Time bucket for aggregation in milliseconds.
        filter_by_ts:
            List of timestamps to filter the result by specific timestamps.
        filter_by_min_value:
            Filter result by minimum value (must mention also filter_by_max_value).
        filter_by_max_value:
            Filter result by maximum value (must mention also filter_by_min_value).
        align:
            Timestamp for alignment control for aggregation.
        latest:
            Used when a time series is a compaction, reports the compacted value of the
            latest possibly partial bucket
        bucket_timestamp:
            Controls how bucket timestamps are reported. Can be one of [`-`, `low`, `+`,
            `high`, `~`, `mid`].
        empty:
            Reports aggregations for empty buckets.

        For more information: https://redis.io/commands/ts.revrange/
        """
        ...
    def mrange(
        self,
        from_time: int | str,
        to_time: int | str,
        filters: list[str],
        count: int | None = None,
        aggregation_type: str | None = None,
        bucket_size_msec: int | None = 0,
        with_labels: bool | None = False,
        filter_by_ts: list[int] | None = None,
        filter_by_min_value: int | None = None,
        filter_by_max_value: int | None = None,
        groupby: str | None = None,
        reduce: str | None = None,
        select_labels: list[str] | None = None,
        align: int | str | None = None,
        latest: bool | None = False,
        bucket_timestamp: str | None = None,
        empty: bool | None = False,
    ):
        """
        Query a range across multiple time-series by filters in forward direction.

        Args:

        from_time:
            Start timestamp for the range query. `-` can be used to express the minimum possible timestamp (0).
        to_time:
            End timestamp for range query, `+` can be used to express the maximum possible timestamp.
        filters:
            filter to match the time-series labels.
        count:
            Limits the number of returned samples.
        aggregation_type:
            Optional aggregation type. Can be one of [`avg`, `sum`, `min`, `max`,
            `range`, `count`, `first`, `last`, `std.p`, `std.s`, `var.p`, `var.s`, `twa`]
        bucket_size_msec:
            Time bucket for aggregation in milliseconds.
        with_labels:
            Include in the reply all label-value pairs representing metadata labels of the time series.
        filter_by_ts:
            List of timestamps to filter the result by specific timestamps.
        filter_by_min_value:
            Filter result by minimum value (must mention also filter_by_max_value).
        filter_by_max_value:
            Filter result by maximum value (must mention also filter_by_min_value).
        groupby:
            Grouping by fields the results (must mention also reduce).
        reduce:
            Applying reducer functions on each group. Can be one of [`avg` `sum`, `min`,
            `max`, `range`, `count`, `std.p`, `std.s`, `var.p`, `var.s`].
        select_labels:
            Include in the reply only a subset of the key-value pair labels of a series.
        align:
            Timestamp for alignment control for aggregation.
        latest:
            Used when a time series is a compaction, reports the compacted
            value of the latest possibly partial bucket
        bucket_timestamp:
            Controls how bucket timestamps are reported. Can be one of [`-`, `low`, `+`,
            `high`, `~`, `mid`].
        empty:
            Reports aggregations for empty buckets.

        For more information: https://redis.io/commands/ts.mrange/
        """
        ...
    def mrevrange(
        self,
        from_time: int | str,
        to_time: int | str,
        filters: list[str],
        count: int | None = None,
        aggregation_type: str | None = None,
        bucket_size_msec: int | None = 0,
        with_labels: bool | None = False,
        filter_by_ts: list[int] | None = None,
        filter_by_min_value: int | None = None,
        filter_by_max_value: int | None = None,
        groupby: str | None = None,
        reduce: str | None = None,
        select_labels: list[str] | None = None,
        align: int | str | None = None,
        latest: bool | None = False,
        bucket_timestamp: str | None = None,
        empty: bool | None = False,
    ):
        """
        Query a range across multiple time-series by filters in reverse direction.

        Args:

        from_time:
            Start timestamp for the range query. - can be used to express the minimum possible timestamp (0).
        to_time:
            End timestamp for range query, + can be used to express the maximum possible timestamp.
        filters:
            Filter to match the time-series labels.
        count:
            Limits the number of returned samples.
        aggregation_type:
            Optional aggregation type. Can be one of [`avg`, `sum`, `min`, `max`,
            `range`, `count`, `first`, `last`, `std.p`, `std.s`, `var.p`, `var.s`, `twa`]
        bucket_size_msec:
            Time bucket for aggregation in milliseconds.
        with_labels:
            Include in the reply all label-value pairs representing metadata labels of the time series.
        filter_by_ts:
            List of timestamps to filter the result by specific timestamps.
        filter_by_min_value:
            Filter result by minimum value (must mention also filter_by_max_value).
        filter_by_max_value:
            Filter result by maximum value (must mention also filter_by_min_value).
        groupby:
            Grouping by fields the results (must mention also reduce).
        reduce:
            Applying reducer functions on each group. Can be one of [`avg` `sum`, `min`,
            `max`, `range`, `count`, `std.p`, `std.s`, `var.p`, `var.s`].
        select_labels:
            Include in the reply only a subset of the key-value pair labels of a series.
        align:
            Timestamp for alignment control for aggregation.
        latest:
            Used when a time series is a compaction, reports the compacted
            value of the latest possibly partial bucket
        bucket_timestamp:
            Controls how bucket timestamps are reported. Can be one of [`-`, `low`, `+`,
            `high`, `~`, `mid`].
        empty:
            Reports aggregations for empty buckets.

        For more information: https://redis.io/commands/ts.mrevrange/
        """
        ...
    def get(self, key: _Key, latest: bool | None = False):
        """
        # noqa
        Get the last sample of `key`.
        `latest` used when a time series is a compaction, reports the compacted
        value of the latest (possibly partial) bucket

        For more information: https://redis.io/commands/ts.get/
        """
        ...
    def mget(
        self,
        filters: list[str],
        with_labels: bool | None = False,
        select_labels: list[str] | None = None,
        latest: bool | None = False,
    ):
        """
        # noqa
        Get the last samples matching the specific `filter`.

        Args:

        filters:
            Filter to match the time-series labels.
        with_labels:
            Include in the reply all label-value pairs representing metadata
            labels of the time series.
        select_labels:
            Include in the reply only a subset of the key-value pair labels of a series.
        latest:
            Used when a time series is a compaction, reports the compacted
            value of the latest possibly partial bucket

        For more information: https://redis.io/commands/ts.mget/
        """
        ...
    def info(self, key):
        """
        # noqa
        Get information of `key`.

        For more information: https://redis.io/commands/ts.info/
        """
        ...
    def queryindex(self, filters):
        """
        # noqa
        Get all time series keys matching the `filter` list.

        For more information: https://redis.io/commands/ts.queryindex/
        """
        ...
