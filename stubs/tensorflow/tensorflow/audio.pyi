"""Public API for tf._api.v2.audio namespace"""

import tensorflow as tf
from tensorflow._aliases import Integer, StringTensorCompatible

def decode_wav(
    contents: StringTensorCompatible, desired_channels: int = -1, desired_samples: int = -1, name: str | None = None
) -> tuple[tf.Tensor, tf.Tensor]:
    """
    Decode a 16-bit PCM WAV file to a float tensor.

    The -32768 to 32767 signed 16-bit values will be scaled to -1.0 to 1.0 in float.

    When desired_channels is set, if the input contains fewer channels than this
    then the last channel will be duplicated to give the requested number, else if
    the input has more channels than requested then the additional channels will be
    ignored.

    If desired_samples is set, then the audio will be cropped or padded with zeroes
    to the requested length.

    The first output contains a Tensor with the content of the audio samples. The
    lowest dimension will be the number of channels, and the second will be the
    number of samples. For example, a ten-sample-long stereo WAV file should give an
    output shape of [10, 2].

    Args:
      contents: A `Tensor` of type `string`.
        The WAV-encoded audio, usually from a file.
      desired_channels: An optional `int`. Defaults to `-1`.
        Number of sample channels wanted.
      desired_samples: An optional `int`. Defaults to `-1`.
        Length of audio requested.
      name: A name for the operation (optional).

    Returns:
      A tuple of `Tensor` objects (audio, sample_rate).

      audio: A `Tensor` of type `float32`.
      sample_rate: A `Tensor` of type `int32`.
    """
    ...
def encode_wav(audio: tf.Tensor, sample_rate: Integer, name: str | None = None) -> tf.Tensor:
    """
    Encode audio data using the WAV file format.

    This operation will generate a string suitable to be saved out to create a .wav
    audio file. It will be encoded in the 16-bit PCM format. It takes in float
    values in the range -1.0f to 1.0f, and any outside that value will be clamped to
    that range.

    `audio` is a 2-D float Tensor of shape `[length, channels]`.
    `sample_rate` is a scalar Tensor holding the rate to use (e.g. 44100).

    Args:
      audio: A `Tensor` of type `float32`. 2-D with shape `[length, channels]`.
      sample_rate: A `Tensor` of type `int32`.
        Scalar containing the sample frequency.
      name: A name for the operation (optional).

    Returns:
      A `Tensor` of type `string`.
    """
    ...
