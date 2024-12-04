"""Point data structure to represent LineProtocol."""

from _typeshed import Incomplete, SupportsContainsAndGetItem, SupportsItems
from collections.abc import Iterable
from datetime import datetime, timedelta
from numbers import Integral
from typing import Any, Literal
from typing_extensions import Self, TypeAlias

from influxdb_client.domain.write_precision import _WritePrecision

_Value: TypeAlias = Incomplete
_Time: TypeAlias = Integral | str | datetime | timedelta

EPOCH: datetime
DEFAULT_WRITE_PRECISION: _WritePrecision

class Point:
    """
    Point defines the values that will be written to the database.

    Ref: https://docs.influxdata.com/influxdb/latest/reference/key-concepts/data-elements/#point
    """
    @staticmethod
    def measurement(measurement: str) -> Point:
        """Create a new Point with specified measurement name."""
        ...
    @staticmethod
    def from_dict(
        dictionary: SupportsContainsAndGetItem[str, Any],
        write_precision: _WritePrecision = "ns",
        *,
        record_measurement_name: str | None = ...,
        record_measurement_key: str = ...,
        record_tag_keys: Iterable[str] | None = ...,
        record_field_keys: Iterable[str] | None = ...,
        record_time_key: str = ...,
        fields: SupportsItems[str, Literal["int", "uint", "float"]] = ...,
    ) -> Point:
        """
        Initialize point from 'dict' structure.

        The expected dict structure is:
            - measurement
            - tags
            - fields
            - time

        Example:
            .. code-block:: python

                # Use default dictionary structure
                dict_structure = {
                    "measurement": "h2o_feet",
                    "tags": {"location": "coyote_creek"},
                    "fields": {"water_level": 1.0},
                    "time": 1
                }
                point = Point.from_dict(dict_structure, WritePrecision.NS)

        Example:
            .. code-block:: python

                # Use custom dictionary structure
                dictionary = {
                    "name": "sensor_pt859",
                    "location": "warehouse_125",
                    "version": "2021.06.05.5874",
                    "pressure": 125,
                    "temperature": 10,
                    "created": 1632208639,
                }
                point = Point.from_dict(dictionary,
                                        write_precision=WritePrecision.S,
                                        record_measurement_key="name",
                                        record_time_key="created",
                                        record_tag_keys=["location", "version"],
                                        record_field_keys=["pressure", "temperature"])

        Int Types:
            The following example shows how to configure the types of integers fields.
            It is useful when you want to serialize integers always as ``float`` to avoid ``field type conflict``
            or use ``unsigned 64-bit integer`` as the type for serialization.

            .. code-block:: python

                # Use custom dictionary structure
                dict_structure = {
                    "measurement": "h2o_feet",
                    "tags": {"location": "coyote_creek"},
                    "fields": {
                        "water_level": 1.0,
                        "some_counter": 108913123234
                    },
                    "time": 1
                }

                point = Point.from_dict(dict_structure, field_types={"some_counter": "uint"})

        :param dictionary: dictionary for serialize into data Point
        :param write_precision: sets the precision for the supplied time values
        :key record_measurement_key: key of dictionary with specified measurement
        :key record_measurement_name: static measurement name for data Point
        :key record_time_key: key of dictionary with specified timestamp
        :key record_tag_keys: list of dictionary keys to use as a tag
        :key record_field_keys: list of dictionary keys to use as a field
        :key field_types: optional dictionary to specify types of serialized fields. Currently, is supported customization for integer types.
                          Possible integers types:
                            - ``int`` - serialize integers as "**Signed 64-bit integers**" - ``9223372036854775807i`` (default behaviour)
                            - ``uint`` - serialize integers as "**Unsigned 64-bit integers**" - ``9223372036854775807u``
                            - ``float`` - serialize integers as "**IEEE-754 64-bit floating-point numbers**". Useful for unify number types in your pipeline to avoid field type conflict - ``9223372036854775807``
                          The ``field_types`` can be also specified as part of incoming dictionary. For more info see an example above.
        :return: new data point
        """
        ...
    def __init__(self, measurement_name: str) -> None:
        """Initialize defaults."""
        ...
    def time(self, time: _Time, write_precision: _WritePrecision = "ns") -> Self:
        """
        Specify timestamp for DataPoint with declared precision.

        If time doesn't have specified timezone we assume that timezone is UTC.

        Examples::
            Point.measurement("h2o").field("val", 1).time("2009-11-10T23:00:00.123456Z")
            Point.measurement("h2o").field("val", 1).time(1257894000123456000)
            Point.measurement("h2o").field("val", 1).time(datetime(2009, 11, 10, 23, 0, 0, 123456))
            Point.measurement("h2o").field("val", 1).time(1257894000123456000, write_precision=WritePrecision.NS)


        :param time: the timestamp for your data
        :param write_precision: sets the precision for the supplied time values
        :return: this point
        """
        ...
    def tag(self, key: str, value: _Value) -> Self:
        """Add tag with key and value."""
        ...
    def field(self, field: str, value: _Value) -> Self:
        """Add field with key and value."""
        ...
    def to_line_protocol(self, precision: _WritePrecision | None = None) -> str:
        """
        Create LineProtocol.

         :param precision: required precision of LineProtocol. If it's not set then use the precision from ``Point``.
        """
        ...
    @property
    def write_precision(self) -> _WritePrecision:
        """Get precision."""
        ...
    @classmethod
    def set_str_rep(cls, rep_function: Any) -> None:
        """Set the string representation for all Points."""
        ...
    def __eq__(self, other: object) -> bool:
        """Return true iff other is equal to self."""
        ...
