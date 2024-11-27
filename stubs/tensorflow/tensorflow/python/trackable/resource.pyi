"""Definitions for resource-type trackable object classes."""

from _typeshed import Incomplete

from tensorflow.python.trackable.base import Trackable

class _ResourceMetaclass(type):
    """Metaclass for CapturableResource."""
    ...

# Internal type that is commonly used as a base class
# it is needed for the public signatures of some APIs.
class CapturableResource(Trackable, metaclass=_ResourceMetaclass):
    """
    Holds a Tensor which a tf.function can capture.

    `CapturableResource`s are discovered by traversing the graph of object
    attributes, e.g. during `tf.saved_model.save`. They are excluded from the
    scope-based tracking of `TrackableResource`; generally things that require
    initialization should inherit from `TrackableResource` instead of
    `CapturableResource` directly.
    """
    ...

def __getattr__(name: str) -> Incomplete: ...
