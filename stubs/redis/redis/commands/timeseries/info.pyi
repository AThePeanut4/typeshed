from _typeshed import Incomplete
from typing import Any

class TSInfo:
    """
    Hold information and statistics on the time-series.
    Can be created using ``tsinfo`` command
    https://oss.redis.com/redistimeseries/commands/#tsinfo.
    """
    rules: list[Any]
    labels: list[Any]
    sourceKey: Incomplete | None
    chunk_count: Incomplete | None
    memory_usage: Incomplete | None
    total_samples: Incomplete | None
    retention_msecs: Incomplete | None
    last_time_stamp: Incomplete | None
    first_time_stamp: Incomplete | None

    max_samples_per_chunk: Incomplete | None
    chunk_size: Incomplete | None
    duplicate_policy: Incomplete | None
    def __init__(self, args) -> None:
        """
        Hold information and statistics on the time-series.

        The supported params that can be passed as args:

        rules:
            A list of compaction rules of the time series.
        sourceKey:
            Key name for source time series in case the current series
            is a target of a rule.
        chunkCount:
            Number of Memory Chunks used for the time series.
        memoryUsage:
            Total number of bytes allocated for the time series.
        totalSamples:
            Total number of samples in the time series.
        labels:
            A list of label-value pairs that represent the metadata
            labels of the time series.
        retentionTime:
            Retention time, in milliseconds, for the time series.
        lastTimestamp:
            Last timestamp present in the time series.
        firstTimestamp:
            First timestamp present in the time series.
        maxSamplesPerChunk:
            Deprecated.
        chunkSize:
            Amount of memory, in bytes, allocated for data.
        duplicatePolicy:
            Policy that will define handling of duplicate samples.

        Can read more about on
        https://oss.redis.com/redistimeseries/configuration/#duplicate_policy
        """
        ...
