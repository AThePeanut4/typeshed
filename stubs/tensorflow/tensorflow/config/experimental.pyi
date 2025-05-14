"""Public API for tf._api.v2.config.experimental namespace"""

import typing_extensions
from typing import TypedDict

from tensorflow.config import PhysicalDevice

class _MemoryInfo(TypedDict):
    current: int
    peak: int

def get_memory_info(device: str) -> _MemoryInfo:
    """
    Get memory info for the chosen device, as a dict.

    This function returns a dict containing information about the device's memory
    usage. For example:

    >>> if tf.config.list_physical_devices('GPU'):
    ...   # Returns a dict in the form {'current': <current mem usage>,
    ...   #                             'peak': <peak mem usage>}
    ...   tf.config.experimental.get_memory_info('GPU:0')

    Currently returns the following keys:
      - `'current'`: The current memory used by the device, in bytes.
      - `'peak'`: The peak memory used by the device across the run of the
          program, in bytes. Can be reset with
          `tf.config.experimental.reset_memory_stats`.

    More keys may be added in the future, including device-specific keys.

    Currently only supports GPU and TPU. If called on a CPU device, an exception
    will be raised.

    For GPUs, TensorFlow will allocate all the memory by default, unless changed
    with `tf.config.experimental.set_memory_growth`. The dict specifies only the
    current and peak memory that TensorFlow is actually using, not the memory that
    TensorFlow has allocated on the GPU.

    Args:
      device: Device string to get the memory information for, e.g. `"GPU:0"`,
      `"TPU:0"`. See https://www.tensorflow.org/api_docs/python/tf/device for
        specifying device strings.

    Returns:
      A dict with keys `'current'` and `'peak'`, specifying the current and peak
      memory usage respectively.

    Raises:
      ValueError: No device found with the device name, like '"nonexistent"'.
      ValueError: Invalid device name, like '"GPU"', '"CPU:GPU"', '"CPU:"'.
      ValueError: Multiple devices matched with the device name.
      ValueError: Memory statistics not tracked, like '"CPU:0"'.
    """
    ...
def reset_memory_stats(device: str) -> None:
    """
    Resets the tracked memory stats for the chosen device.

    This function sets the tracked peak memory for a device to the device's
    current memory usage. This allows you to measure the peak memory usage for a
    specific part of your program. For example:

    >>> if tf.config.list_physical_devices('GPU'):
    ...   # Sets the peak memory to the current memory.
    ...   tf.config.experimental.reset_memory_stats('GPU:0')
    ...   # Creates the first peak memory usage.
    ...   x1 = tf.ones(1000 * 1000, dtype=tf.float64)
    ...   del x1 # Frees the memory referenced by `x1`.
    ...   peak1 = tf.config.experimental.get_memory_info('GPU:0')['peak']
    ...   # Sets the peak memory to the current memory again.
    ...   tf.config.experimental.reset_memory_stats('GPU:0')
    ...   # Creates the second peak memory usage.
    ...   x2 = tf.ones(1000 * 1000, dtype=tf.float32)
    ...   del x2
    ...   peak2 = tf.config.experimental.get_memory_info('GPU:0')['peak']
    ...   assert peak2 < peak1  # tf.float32 consumes less memory than tf.float64.

    Currently only supports GPU and TPU. If called on a CPU device, an exception
    will be raised.

    Args:
      device: Device string to reset the memory stats, e.g. `"GPU:0"`, `"TPU:0"`.
        See https://www.tensorflow.org/api_docs/python/tf/device for specifying
        device strings.

    Raises:
      ValueError: No device found with the device name, like '"nonexistent"'.
      ValueError: Invalid device name, like '"GPU"', '"CPU:GPU"', '"CPU:"'.
      ValueError: Multiple devices matched with the device name.
      ValueError: Memory statistics not tracked or clearing memory statistics not
        supported, like '"CPU:0"'.
    """
    ...
@typing_extensions.deprecated("This function is deprecated in favor of tf.config.experimental.get_memory_info")
def get_memory_usage(device: PhysicalDevice) -> int: ...
def get_memory_growth(device: PhysicalDevice) -> bool: ...
def set_memory_growth(device: PhysicalDevice, enable: bool) -> None: ...
def __getattr__(name: str): ...  # incomplete module
