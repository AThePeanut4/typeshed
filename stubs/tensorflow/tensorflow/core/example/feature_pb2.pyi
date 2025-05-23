"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol messages for describing features for machine learning model
training or inference.

There are three base Feature types:
  - bytes
  - float
  - int64

A Feature contains Lists which may hold zero or more values.  These
lists are the base values BytesList, FloatList, Int64List.

Features are organized into categories by name.  The Features message
contains the mapping from name to Feature.

Example Features for a movie recommendation application:
  feature {
    key: "age"
    value { float_list {
      value: 29.0
    }}
  }
  feature {
    key: "movie"
    value { bytes_list {
      value: "The Shawshank Redemption"
      value: "Fight Club"
    }}
  }
  feature {
    key: "movie_ratings"
    value { float_list {
      value: 9.0
      value: 9.7
    }}
  }
  feature {
    key: "suggestion"
    value { bytes_list {
      value: "Inception"
    }}
  }
  feature {
    key: "suggestion_purchased"
    value { int64_list {
      value: 1
    }}
  }
  feature {
    key: "purchase_price"
    value { float_list {
      value: 9.99
    }}
  }
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BytesList(google.protobuf.message.Message):
    """LINT.IfChange
    Containers to hold repeated fundamental values.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self, *, value: collections.abc.Iterable[builtins.bytes] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___BytesList = BytesList

@typing.final
class FloatList(google.protobuf.message.Message):
    """
    Used in `tf.train.Example` protos. Holds a list of floats.

    An `Example` proto is a representation of the following python type:

    ```
    Dict[str,
         Union[List[bytes],
               List[int64],
               List[float]]]
    ```

    This proto implements the `List[float]` portion.

    >>> from google.protobuf import text_format
    >>> example = text_format.Parse('''
    ...   features {
    ...     feature {key: "my_feature"
    ...              value {float_list {value: [1., 2., 3., 4. ]}}}
    ...   }''',
    ...   tf.train.Example())
    >>>
    >>> example.features.feature['my_feature'].float_list.value
    [1.0, 2.0, 3.0, 4.0]

    Use `tf.io.parse_example` to extract tensors from a serialized `Example` proto:

    >>> tf.io.parse_example(
    ...     example.SerializeToString(),
    ...     features = {'my_feature': tf.io.RaggedFeature(dtype=tf.float32)})
    {'my_feature': <tf.Tensor: shape=(4,), dtype=float32,
                               numpy=array([1., 2., 3., 4.], dtype=float32)>}

    See the [`tf.train.Example`](https://www.tensorflow.org/tutorials/load_data/tfrecord#tftrainexample)
    guide for usage details.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(self, *, value: collections.abc.Iterable[builtins.float] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___FloatList = FloatList

@typing.final
class Int64List(google.protobuf.message.Message):
    """
    Used in `tf.train.Example` protos. Holds a list of Int64s.

    An `Example` proto is a representation of the following python type:

    ```
    Dict[str,
         Union[List[bytes],
               List[int64],
               List[float]]]
    ```

    This proto implements the `List[int64]` portion.

    >>> from google.protobuf import text_format
    >>> example = text_format.Parse('''
    ...   features {
    ...     feature {key: "my_feature"
    ...              value {int64_list {value: [1, 2, 3, 4]}}}
    ...   }''',
    ...   tf.train.Example())
    >>>
    >>> example.features.feature['my_feature'].int64_list.value
    [1, 2, 3, 4]

    Use `tf.io.parse_example` to extract tensors from a serialized `Example` proto:

    >>> tf.io.parse_example(
    ...     example.SerializeToString(),
    ...     features = {'my_feature': tf.io.RaggedFeature(dtype=tf.int64)})
    {'my_feature': <tf.Tensor: shape=(4,), dtype=float32,
                               numpy=array([1, 2, 3, 4], dtype=int64)>}

    See the [`tf.train.Example`](https://www.tensorflow.org/tutorials/load_data/tfrecord#tftrainexample)
    guide for usage details.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self, *, value: collections.abc.Iterable[builtins.int] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None:
        """Clears a message field."""
        ...

global___Int64List = Int64List

@typing.final
class Feature(google.protobuf.message.Message):
    """Containers for non-sequential data."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BYTES_LIST_FIELD_NUMBER: builtins.int
    FLOAT_LIST_FIELD_NUMBER: builtins.int
    INT64_LIST_FIELD_NUMBER: builtins.int
    @property
    def bytes_list(self) -> global___BytesList: ...
    @property
    def float_list(self) -> global___FloatList: ...
    @property
    def int64_list(self) -> global___Int64List: ...
    def __init__(
        self,
        *,
        bytes_list: global___BytesList | None = ...,
        float_list: global___FloatList | None = ...,
        int64_list: global___Int64List | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "bytes_list", b"bytes_list", "float_list", b"float_list", "int64_list", b"int64_list", "kind", b"kind"
        ],
    ) -> builtins.bool:
        """Checks if a message field is set."""
        ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "bytes_list", b"bytes_list", "float_list", b"float_list", "int64_list", b"int64_list", "kind", b"kind"
        ],
    ) -> None:
        """Clears a message field."""
        ...
    def WhichOneof(
        self, oneof_group: typing.Literal["kind", b"kind"]
    ) -> typing.Literal["bytes_list", "float_list", "int64_list"] | None:
        """Returns the name of the field set inside a oneof, or None if no field is set."""
        ...

global___Feature = Feature

@typing.final
class Features(google.protobuf.message.Message):
    """
    Used in `tf.train.Example` protos. Contains the mapping from keys to `Feature`.

    An `Example` proto is a representation of the following python type:

    ```
    Dict[str,
         Union[List[bytes],
               List[int64],
               List[float]]]
    ```

    This proto implements the `Dict`.

    >>> int_feature = tf.train.Feature(
    ...     int64_list=tf.train.Int64List(value=[1, 2, 3, 4]))
    >>> float_feature = tf.train.Feature(
    ...     float_list=tf.train.FloatList(value=[1., 2., 3., 4.]))
    >>> bytes_feature = tf.train.Feature(
    ...     bytes_list=tf.train.BytesList(value=[b"abc", b"1234"]))
    >>>
    >>> example = tf.train.Example(
    ...     features=tf.train.Features(feature={
    ...         'my_ints': int_feature,
    ...         'my_floats': float_feature,
    ...         'my_bytes': bytes_feature,
    ...     }))

    Use `tf.io.parse_example` to extract tensors from a serialized `Example` proto:

    >>> tf.io.parse_example(
    ...     example.SerializeToString(),
    ...     features = {
    ...         'my_ints': tf.io.RaggedFeature(dtype=tf.int64),
    ...         'my_floats': tf.io.RaggedFeature(dtype=tf.float32),
    ...         'my_bytes': tf.io.RaggedFeature(dtype=tf.string)})
    {'my_bytes': <tf.Tensor: shape=(2,), dtype=string,
                             numpy=array([b'abc', b'1234'], dtype=object)>,
     'my_floats': <tf.Tensor: shape=(4,), dtype=float32,
                              numpy=array([1., 2., 3., 4.], dtype=float32)>,
     'my_ints': <tf.Tensor: shape=(4,), dtype=int64,
                            numpy=array([1, 2, 3, 4])>}
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FeatureEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Feature: ...
        def __init__(self, *, key: builtins.str | None = ..., value: global___Feature | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool:
            """Checks if a message field is set."""
            ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None:
            """Clears a message field."""
            ...

    FEATURE_FIELD_NUMBER: builtins.int
    @property
    def feature(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Feature]:
        """Map from feature name to feature."""

    def __init__(self, *, feature: collections.abc.Mapping[builtins.str, global___Feature] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature", b"feature"]) -> None:
        """Clears a message field."""
        ...

global___Features = Features

@typing.final
class FeatureList(google.protobuf.message.Message):
    """Containers for sequential data.

    A FeatureList contains lists of Features.  These may hold zero or more
    Feature values.

    FeatureLists are organized into categories by name.  The FeatureLists message
    contains the mapping from name to FeatureList.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURE_FIELD_NUMBER: builtins.int
    @property
    def feature(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Feature]: ...
    def __init__(self, *, feature: collections.abc.Iterable[global___Feature] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature", b"feature"]) -> None:
        """Clears a message field."""
        ...

global___FeatureList = FeatureList

@typing.final
class FeatureLists(google.protobuf.message.Message):
    """
    Mainly used as part of a `tf.train.SequenceExample`.

    Contains a list of `tf.train.Feature`s.

    The `tf.train.SequenceExample` proto can be thought of as a
    proto implementation of the following python type:

    ```
    # tf.train.Feature
    Feature = Union[List[bytes],
                    List[int64],
                    List[float]]

    # tf.train.FeatureList
    FeatureList = List[Feature]

    # tf.train.FeatureLists
    FeatureLists = Dict[str, FeatureList]

    class SequenceExample(typing.NamedTuple):
      context: Dict[str, Feature]
      feature_lists: FeatureLists
    ```

    This proto implements the `Dict[str, FeatureList]` portion.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FeatureListEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___FeatureList: ...
        def __init__(self, *, key: builtins.str | None = ..., value: global___FeatureList | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool:
            """Checks if a message field is set."""
            ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None:
            """Clears a message field."""
            ...

    FEATURE_LIST_FIELD_NUMBER: builtins.int
    @property
    def feature_list(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___FeatureList]:
        """Map from feature name to feature list."""

    def __init__(self, *, feature_list: collections.abc.Mapping[builtins.str, global___FeatureList] | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature_list", b"feature_list"]) -> None:
        """Clears a message field."""
        ...

global___FeatureLists = FeatureLists
