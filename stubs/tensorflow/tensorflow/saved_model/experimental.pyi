"""Public API for tf._api.v2.saved_model.experimental namespace"""

from enum import Enum
from typing_extensions import Self

import tensorflow as tf
from tensorflow._aliases import Integer, TensorValue
from tensorflow.python.trackable.resource import CapturableResource

class Fingerprint:
    """
    The SavedModel fingerprint.

    Each attribute of this class is named after a field name in the
    FingerprintDef proto and contains the value of the respective field in the
    protobuf.

    Attributes:
      saved_model_checksum: A uint64 containing the `saved_model_checksum`.
      graph_def_program_hash: A uint64 containing `graph_def_program_hash`.
      signature_def_hash: A uint64 containing the `signature_def_hash`.
      saved_object_graph_hash: A uint64 containing the `saved_object_graph_hash`.
      checkpoint_hash: A uint64 containing the`checkpoint_hash`.
      version: An int32 containing the producer field of the VersionDef.
    """
    saved_model_checksum: TensorValue | None
    graph_def_program_hash: TensorValue | None = None
    signature_def_hash: TensorValue | None = None
    saved_object_graph_hash: TensorValue | None = None
    checkpoint_hash: TensorValue | None = None
    version: TensorValue | None = None
    # In practice it seems like any type is accepted, but that might cause issues later on.
    def __init__(
        self,
        saved_model_checksum: Integer | None = None,
        graph_def_program_hash: Integer | None = None,
        signature_def_hash: Integer | None = None,
        saved_object_graph_hash: Integer | None = None,
        checkpoint_hash: Integer | None = None,
        version: Integer | None = None,
    ) -> None:
        """
        Initializes the instance based on values in the SavedModel fingerprint.

        Args:
          saved_model_checksum: Value of the`saved_model_checksum`.
          graph_def_program_hash: Value of the `graph_def_program_hash`.
          signature_def_hash: Value of the `signature_def_hash`.
          saved_object_graph_hash: Value of the `saved_object_graph_hash`.
          checkpoint_hash: Value of the `checkpoint_hash`.
          version: Value of the producer field of the VersionDef.
        """
        ...
    @classmethod
    def from_proto(cls, proto) -> Self:
        """Constructs Fingerprint object from protocol buffer message."""
        ...
    def singleprint(self) -> str:
        """
        Canonical fingerprinting ID for a SavedModel.

        Uniquely identifies a SavedModel based on the regularized fingerprint
        attributes. (saved_model_checksum is sensitive to immaterial changes and
        thus non-deterministic.)

        Returns:
          The string concatenation of `graph_def_program_hash`,
          `signature_def_hash`, `saved_object_graph_hash`, and `checkpoint_hash`
          fingerprint attributes (separated by '/').

        Raises:
          ValueError: If the fingerprint fields cannot be used to construct the
          singleprint.
        """
        ...

class TrackableResource(CapturableResource):
    """
    Holds a Tensor which a tf.function can capture.

    A TrackableResource is most useful for stateful Tensors that require
    initialization, such as `tf.lookup.StaticHashTable`. `TrackableResource`s
    are discovered by traversing the graph of object attributes, e.g. during
    `tf.saved_model.save`.

    A TrackableResource has three methods to override:

    * `_create_resource` should create the resource tensor handle.
    * `_initialize` should initialize the resource held at `self.resource_handle`.
    * `_destroy_resource` is called upon a `TrackableResource`'s destruction
      and should decrement the resource's ref count. For most resources, this
      should be done with a call to `tf.raw_ops.DestroyResourceOp`.

    Example usage:

    >>> class DemoResource(tf.saved_model.experimental.TrackableResource):
    ...   def __init__(self):
    ...     super().__init__()
    ...     self._initialize()
    ...   def _create_resource(self):
    ...     return tf.raw_ops.VarHandleOp(dtype=tf.float32, shape=[2])
    ...   def _initialize(self):
    ...     tf.raw_ops.AssignVariableOp(
    ...         resource=self.resource_handle, value=tf.ones([2]))
    ...   def _destroy_resource(self):
    ...     tf.raw_ops.DestroyResourceOp(resource=self.resource_handle)
    >>> class DemoModule(tf.Module):
    ...   def __init__(self):
    ...     self.resource = DemoResource()
    ...   def increment(self, tensor):
    ...     return tensor + tf.raw_ops.ReadVariableOp(
    ...         resource=self.resource.resource_handle, dtype=tf.float32)
    >>> demo = DemoModule()
    >>> demo.increment([5, 1])
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([6., 2.], dtype=float32)>
    """
    @property
    def resource_handle(self) -> tf.Tensor:
        """Returns the resource handle associated with this Resource."""
        ...
    def __init__(self, device: str = "") -> None:
        """
        Initialize the `TrackableResource`.

        Args:
          device: A string indicating a required placement for this resource,
            e.g. "CPU" if this resource must be created on a CPU device. A blank
            device allows the user to place resource creation, so generally this
            should be blank unless the resource only makes sense on one device.
        """
        ...

class VariablePolicy(Enum):
    """
    Enum defining options for variable handling when saving.

    NONE
      No policy applied: Distributed variables are saved as one variable, with no
      device attached.

    SAVE_VARIABLE_DEVICES
      When saving variables, also save their device assignment.
      This is useful if one wants to hardcode devices in saved models, but it also
      makes them non-portable if soft device placement is disabled (more details
      in `tf.config.set_soft_device_placement`). This is currently not
      fully supported by `saved_model.load`, and is mainly intended to be used
      when one will be reading the saved model at a lower API level. In the
      example below, the graph saved by the call to `saved_model.save` will have
      the variable devices correctly specified:
      ```python
      exported = tf.train.Checkpoint()
      with tf.device('/GPU:0'):
        exported.x_gpu = tf.Variable(1.0)
      with tf.device('/CPU:0'):
        exported.x_cpu = tf.Variable(1.0)
      tf.saved_model.save(exported, export_dir,
          options = tf.saved_model.SaveOptions(
              experimental_variable_policy=
                tf.saved_model.experimental.VariablePolicy.SAVE_VARIABLE_DEVICES))
      ```
      Distributed variables are still saved as one variable under this policy.

    EXPAND_DISTRIBUTED_VARIABLES
      Distributed variables will be saved with information about their components,
      allowing for their restoration on load. Also, the saved graph will contain
      references to those variables. This is useful when one wants to use the
      model for training in environments where the original distribution strategy
      is not available.
    """
    EXPAND_DISTRIBUTED_VARIABLES = "expand_distributed_variables"
    NONE = None
    SAVE_VARIABLE_DEVICES = "save_variable_devices"

def read_fingerprint(export_dir: str) -> Fingerprint:
    """
    Reads the fingerprint of a SavedModel in `export_dir`.

    Returns a `tf.saved_model.experimental.Fingerprint` object that contains
    the values of the SavedModel fingerprint, which is persisted on disk in the
    `fingerprint.pb` file in the `export_dir`.

    Read more about fingerprints in the SavedModel guide at
    https://www.tensorflow.org/guide/saved_model.

    Args:
      export_dir: The directory that contains the SavedModel.

    Returns:
      A `tf.saved_model.experimental.Fingerprint`.

    Raises:
      FileNotFoundError: If no or an invalid fingerprint is found.
    """
    ...
