"""
Functions for serialize Pandas DataFrame.

Much of the code here is inspired by that in the aioinflux packet found here: https://github.com/gusutabopb/aioinflux
"""

from _typeshed import Incomplete

logger: Incomplete

class DataframeSerializer:
    """Serialize DataFrame into LineProtocols."""
    data_frame: Incomplete
    f: Incomplete
    field_indexes: Incomplete
    first_field_maybe_null: Incomplete
    chunk_size: Incomplete
    def __init__(self, data_frame, point_settings, precision="ns", chunk_size: int | None = None, **kwargs) -> None:
        """
        Init serializer.

        :param data_frame: Pandas DataFrame to serialize
        :param point_settings: Default Tags
        :param precision: The precision for the unix timestamps within the body line-protocol.
        :param chunk_size: The size of chunk for serializing into chunks.
        :key data_frame_measurement_name: name of measurement for writing Pandas DataFrame
        :key data_frame_tag_columns: list of DataFrame columns which are tags, rest columns will be fields
        :key data_frame_timestamp_column: name of DataFrame column which contains a timestamp. The column can be defined as a :class:`~str` value
                                          formatted as `2018-10-26`, `2018-10-26 12:00`, `2018-10-26 12:00:00-05:00`
                                          or other formats and types supported by `pandas.to_datetime <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime>`_ - ``DataFrame``
        :key data_frame_timestamp_timezone: name of the timezone which is used for timestamp column - ``DataFrame``
        """
        ...
    def serialize(self, chunk_idx: int | None = None):
        """
        Serialize chunk into LineProtocols.

        :param chunk_idx: The index of chunk to serialize. If `None` then serialize whole dataframe.
        """
        ...
    def number_of_chunks(self):
        """
        Return the number of chunks.

        :return: number of chunks or None if chunk_size is not specified.
        """
        ...

def data_frame_to_list_of_points(data_frame, point_settings, precision="ns", **kwargs):
    """
    Serialize DataFrame into LineProtocols.

    :param data_frame: Pandas DataFrame to serialize
    :param point_settings: Default Tags
    :param precision: The precision for the unix timestamps within the body line-protocol.
    :key data_frame_measurement_name: name of measurement for writing Pandas DataFrame
    :key data_frame_tag_columns: list of DataFrame columns which are tags, rest columns will be fields
    :key data_frame_timestamp_column: name of DataFrame column which contains a timestamp. The column can be defined as a :class:`~str` value
                                      formatted as `2018-10-26`, `2018-10-26 12:00`, `2018-10-26 12:00:00-05:00`
                                      or other formats and types supported by `pandas.to_datetime <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime>`_ - ``DataFrame``
    :key data_frame_timestamp_timezone: name of the timezone which is used for timestamp column - ``DataFrame``
    """
    ...
