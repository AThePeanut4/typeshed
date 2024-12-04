"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.core.protobuf.tpu.optimization_parameters_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TPUEmbeddingConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Mode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TPUEmbeddingConfiguration._Mode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: TPUEmbeddingConfiguration._Mode.ValueType  # 0
        INFERENCE: TPUEmbeddingConfiguration._Mode.ValueType  # 1
        TRAINING: TPUEmbeddingConfiguration._Mode.ValueType  # 2
        BACKWARD_PASS_ONLY: TPUEmbeddingConfiguration._Mode.ValueType  # 3

    class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
        """Mode. Should the embedding layer program be run for inference (just forward
        pass), training (both forward and backward pass) or just the backward_pass.
        """

    UNSPECIFIED: TPUEmbeddingConfiguration.Mode.ValueType  # 0
    INFERENCE: TPUEmbeddingConfiguration.Mode.ValueType  # 1
    TRAINING: TPUEmbeddingConfiguration.Mode.ValueType  # 2
    BACKWARD_PASS_ONLY: TPUEmbeddingConfiguration.Mode.ValueType  # 3

    class _ShardingStrategy:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ShardingStrategyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TPUEmbeddingConfiguration._ShardingStrategy.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DIV_DEFAULT: TPUEmbeddingConfiguration._ShardingStrategy.ValueType  # 0
        MOD: TPUEmbeddingConfiguration._ShardingStrategy.ValueType  # 1

    class ShardingStrategy(_ShardingStrategy, metaclass=_ShardingStrategyEnumTypeWrapper):
        """Sharding strategy of the embedding tables among the hosts.
        If the sharding_strategy is "mod", each id is assigned to host
        "id % num_hosts". For instance, 13 ids are split across 5 hosts as:
        [[0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8], [4, 9]].
        If the sharding_strategy is "div", ids are assigned to hosts in a
        contiguous manner. In this case, 13 ids are split across 5 hosts as:
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]].
        In both the strategies, if the id space does not evenly divide the number
        of hosts, each of the first "table_descriptor.vocabulary_size % num_hosts"
        hosts will be assigned one more id.
        This partitioning strategy exactly follows that in the embedding_lookup
        TensorFlow function at tensorflow/python/ops/embedding_ops.py.
        """

    DIV_DEFAULT: TPUEmbeddingConfiguration.ShardingStrategy.ValueType  # 0
    MOD: TPUEmbeddingConfiguration.ShardingStrategy.ValueType  # 1

    @typing.final
    class TableDescriptor(google.protobuf.message.Message):
        """Description of the various embedding tables."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VOCABULARY_SIZE_FIELD_NUMBER: builtins.int
        DIMENSION_FIELD_NUMBER: builtins.int
        NUM_FEATURES_FIELD_NUMBER: builtins.int
        OPTIMIZATION_PARAMETERS_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Name of the table."""
        vocabulary_size: builtins.int
        """Size of the vocabulary (i.e., number of rows) in the table."""
        dimension: builtins.int
        """The embedding dimension (i.e., the width of the embedding table)."""
        num_features: builtins.int
        """Number of features mapped to this table."""
        @property
        def optimization_parameters(self) -> tensorflow.core.protobuf.tpu.optimization_parameters_pb2.OptimizationParameters:
            """Details of the learning algorithm used to update the embedding
            parameters.
            """

        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            vocabulary_size: builtins.int | None = ...,
            dimension: builtins.int | None = ...,
            num_features: builtins.int | None = ...,
            optimization_parameters: tensorflow.core.protobuf.tpu.optimization_parameters_pb2.OptimizationParameters | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["optimization_parameters", b"optimization_parameters"]) -> builtins.bool:
            """Checks if a message field is set."""
            ...
        def ClearField(self, field_name: typing.Literal["dimension", b"dimension", "name", b"name", "num_features", b"num_features", "optimization_parameters", b"optimization_parameters", "vocabulary_size", b"vocabulary_size"]) -> None:
            """Clears a message field."""
            ...

    @typing.final
    class FeatureDescriptor(google.protobuf.message.Message):
        """Description of different input features."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        TABLE_ID_FIELD_NUMBER: builtins.int
        INPUT_SHAPE_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Name of the input feature."""
        table_id: builtins.int
        """Index of the corresponding table in the TableDescriptor list."""
        @property
        def input_shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
            """Static shape of the inputs (excluding the reduction axis). Note that
            the shape of the actual inputs provided using the infeed op must be
            strictly smaller than input_shape. The outputs received at the TensorCore
            will have rank = input_shape.size() + 1. The innermost axis corresponds
            to the embedding dimension. If the input has shape [m, n, k] (excluding
            the reduction axis) and the embedding dimension is d, the output received
            at the TensorCore will have shape [m, n, k, d].
            """

        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            table_id: builtins.int | None = ...,
            input_shape: collections.abc.Iterable[builtins.int] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["input_shape", b"input_shape", "name", b"name", "table_id", b"table_id"]) -> None:
            """Clears a message field."""
            ...

    @typing.final
    class SpmdSharding(google.protobuf.message.Message):
        """SPMD (Single Program Multiple Data) sharding configuration for
        TPUEmbedding. When model parallelism is used on the TensorCore, the number
        of cores per replica must be passed to TPUEmbedding so that the right
        shapes can be computed in the TF/XLA bridge.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ENABLED_FIELD_NUMBER: builtins.int
        NUM_CORES_PER_REPLICA_FIELD_NUMBER: builtins.int
        enabled: builtins.bool
        """Whether SPMD sharding is enabled."""
        num_cores_per_replica: builtins.int
        """Number of cores per replica."""
        def __init__(
            self,
            *,
            enabled: builtins.bool | None = ...,
            num_cores_per_replica: builtins.int | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["enabled", b"enabled", "num_cores_per_replica", b"num_cores_per_replica"]) -> None:
            """Clears a message field."""
            ...

    TABLE_DESCRIPTOR_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    BATCH_SIZE_PER_TENSOR_CORE_FIELD_NUMBER: builtins.int
    NUM_HOSTS_FIELD_NUMBER: builtins.int
    NUM_TENSOR_CORES_FIELD_NUMBER: builtins.int
    SHARDING_STRATEGY_FIELD_NUMBER: builtins.int
    PIPELINE_EXECUTION_WITH_TENSOR_CORE_FIELD_NUMBER: builtins.int
    PROFILE_DATA_DIRECTORY_FIELD_NUMBER: builtins.int
    FEATURE_DESCRIPTOR_FIELD_NUMBER: builtins.int
    SPMD_SHARDING_FIELD_NUMBER: builtins.int
    mode: global___TPUEmbeddingConfiguration.Mode.ValueType
    batch_size_per_tensor_core: builtins.int
    """Number of samples in each batch of embedding layer activations sent to
    the TensorCore.
    """
    num_hosts: builtins.int
    """Number of TPU hosts used for inference/training."""
    num_tensor_cores: builtins.int
    """Number of TensorCore used for inference/training."""
    sharding_strategy: global___TPUEmbeddingConfiguration.ShardingStrategy.ValueType
    pipeline_execution_with_tensor_core: builtins.bool
    """This parameter determines if the execution of the sparse core will be
    pipelined with that of the TensorCore. This parameter only affects results
    when mode=TRAINING. If mode=INFERENCE or BACKWARD_PASS_ONLY, this parameter
    does not affect execution and hence, is a don't care value.

    false: The execution of the sparse core is not pipelined with that of the
    TensorCore. The forward pass of every step on the sparse core is executed
    only after the backward pass of the previous step is complete. And the
    backward pass on the sparse core is executed only after the embedding
    gradients have been computed on the TensorCore on every step. This ensures
    that the activations on every step observe the gradient updates from the
    previous step on both the sparse core and the TensorCore.

    true: The execution of the sparse core is pipelined with that of the
    TensorCore. The forward pass of every step on the sparse core can be
    executed after the forward pass of the previous step is complete without
    waiting for the backward pass. This improves the utilization of the sparse
    core allowing it to process step N+1 while the embedding gradients for step
    N are computed on the TensorCore. The backward pass of every step on the
    sparse core is executed directly after the forward pass for the next step
    is complete. The drawback is that embedding activations for step N+1 do not
    observe the embedding gradient updates from step N. This could affect model
    quality if step N and N+1 involve the same set of embedding IDs. However,
    since the embedding updates are sparse, this is generally not considered a
    problem.
    """
    profile_data_directory: builtins.str
    """Directory where embedding lookup statistics are stored. These statistics
    summarize information about the inputs to the embedding lookup
    operation, in particular, the average number of embedding IDs per example
    and how well the embedding IDs are load balanced across the system. The
    lookup statistics are used during TPU initialization for embedding table
    partitioning. Collection of lookup statistics is done at runtime by
    profiling the embedding inputs: only 3% of input samples are profiled to
    minimize host CPU overhead. Once a suitable number of samples are
    profiled, the lookup statistics are saved to table-specific files in the
    profile data directory generally at the end of a TPU training loop. The
    filename corresponding to each table is obtained by hashing table specific
    parameters (e.g., table name and number of features) and global
    configuration parameters (e.g., sharding strategy and TPU worker task
    count). The same profile data directory can be shared amongst several
    models to reuse embedding lookup statistics.
    """
    @property
    def table_descriptor(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TPUEmbeddingConfiguration.TableDescriptor]: ...
    @property
    def feature_descriptor(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TPUEmbeddingConfiguration.FeatureDescriptor]:
        """If the feature_descriptor field is populated, the model should NOT populate
        TableDescriptor.num_features and batch_size_per_tensor_core. These two
        fields will be auto-populated by the TPUEmbedding rewrite passes.
        """

    @property
    def spmd_sharding(self) -> global___TPUEmbeddingConfiguration.SpmdSharding: ...
    def __init__(
        self,
        *,
        table_descriptor: collections.abc.Iterable[global___TPUEmbeddingConfiguration.TableDescriptor] | None = ...,
        mode: global___TPUEmbeddingConfiguration.Mode.ValueType | None = ...,
        batch_size_per_tensor_core: builtins.int | None = ...,
        num_hosts: builtins.int | None = ...,
        num_tensor_cores: builtins.int | None = ...,
        sharding_strategy: global___TPUEmbeddingConfiguration.ShardingStrategy.ValueType | None = ...,
        pipeline_execution_with_tensor_core: builtins.bool | None = ...,
        profile_data_directory: builtins.str | None = ...,
        feature_descriptor: collections.abc.Iterable[global___TPUEmbeddingConfiguration.FeatureDescriptor] | None = ...,
        spmd_sharding: global___TPUEmbeddingConfiguration.SpmdSharding | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["spmd_sharding", b"spmd_sharding"]) -> builtins.bool:
        """Checks if a message field is set."""
        ...
    def ClearField(self, field_name: typing.Literal["batch_size_per_tensor_core", b"batch_size_per_tensor_core", "feature_descriptor", b"feature_descriptor", "mode", b"mode", "num_hosts", b"num_hosts", "num_tensor_cores", b"num_tensor_cores", "pipeline_execution_with_tensor_core", b"pipeline_execution_with_tensor_core", "profile_data_directory", b"profile_data_directory", "sharding_strategy", b"sharding_strategy", "spmd_sharding", b"spmd_sharding", "table_descriptor", b"table_descriptor"]) -> None:
        """Clears a message field."""
        ...

global___TPUEmbeddingConfiguration = TPUEmbeddingConfiguration

@typing.final
class TPUEmbeddingError(google.protobuf.message.Message):
    """A placeholder message that is used to define a unique Status payload
    URL for TPU embedding errors.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___TPUEmbeddingError = TPUEmbeddingError
