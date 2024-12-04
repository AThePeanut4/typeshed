"""Public API for tf._api.v2.raw_ops namespace"""

from _typeshed import Incomplete
from typing import Literal

from tensorflow import Operation, Tensor
from tensorflow._aliases import TensorCompatible

def Fingerprint(data: TensorCompatible, method: Literal["farmhash64"], name: str | None = None) -> Tensor:
    """
    Generates fingerprint values.

    Generates fingerprint values of `data`.

    Fingerprint op considers the first dimension of `data` as the batch dimension,
    and `output[i]` contains the fingerprint value generated from contents in
    `data[i, ...]` for all `i`.

    Fingerprint op writes fingerprint values as byte arrays. For example, the
    default method `farmhash64` generates a 64-bit fingerprint value at a time.
    This 8-byte value is written out as an `uint8` array of size 8, in little-endian
    order.

    For example, suppose that `data` has data type `DT_INT32` and shape (2, 3, 4),
    and that the fingerprint method is `farmhash64`. In this case, the output shape
    is (2, 8), where 2 is the batch dimension size of `data`, and 8 is the size of
    each fingerprint value in bytes. `output[0, :]` is generated from 12 integers in
    `data[0, :, :]` and similarly `output[1, :]` is generated from other 12 integers
    in `data[1, :, :]`.

    Note that this op fingerprints the raw underlying buffer, and it does not
    fingerprint Tensor's metadata such as data type and/or shape. For example, the
    fingerprint values are invariant under reshapes and bitcasts as long as the
    batch dimension remain the same:

    ```
    Fingerprint(data) == Fingerprint(Reshape(data, ...))
    Fingerprint(data) == Fingerprint(Bitcast(data, ...))
    ```

    For string data, one should expect `Fingerprint(data) !=
    Fingerprint(ReduceJoin(data))` in general.

    Args:
      data: A `Tensor`. Must have rank 1 or higher.
      method: A `Tensor` of type `string`.
        Fingerprint method used by this op. Currently available method is
        `farmhash::fingerprint64`.
      name: A name for the operation (optional).

    Returns:
      A `Tensor` of type `uint8`.
    """
    ...
def Snapshot(input: TensorCompatible, name: str | None = None) -> Tensor:
    """
    Returns a copy of the input tensor.

    Args:
      input: A `Tensor`.
      name: A name for the operation (optional).

    Returns:
      A `Tensor`. Has the same type as `input`.
    """
    ...
def ResourceApplyAdagradV2(
    var: Tensor,
    accum: Tensor,
    lr: TensorCompatible,
    epsilon: TensorCompatible,
    grad: TensorCompatible,
    use_locking: bool = False,
    update_slots: bool = True,
    name: str | None = None,
) -> Operation:
    """
    Update '*var' according to the adagrad scheme.

    accum += grad * grad
    var -= lr * grad * (1 / (sqrt(accum) + epsilon))

    Args:
      var: A `Tensor` of type `resource`. Should be from a Variable().
      accum: A `Tensor` of type `resource`. Should be from a Variable().
      lr: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
        Scaling factor. Must be a scalar.
      epsilon: A `Tensor`. Must have the same type as `lr`.
        Constant factor. Must be a scalar.
      grad: A `Tensor`. Must have the same type as `lr`. The gradient.
      use_locking: An optional `bool`. Defaults to `False`.
        If `True`, updating of the var and accum tensors will be protected
        by a lock; otherwise the behavior is undefined, but may exhibit less
        contention.
      update_slots: An optional `bool`. Defaults to `True`.
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """
    ...
def ResourceSparseApplyAdagradV2(
    var: Tensor,
    accum: Tensor,
    lr: TensorCompatible,
    epsilon: TensorCompatible,
    grad: TensorCompatible,
    indices: TensorCompatible,
    use_locking: bool = False,
    update_slots: bool = True,
    name: str | None = None,
) -> Operation:
    """
    Update relevant entries in '*var' and '*accum' according to the adagrad scheme.

    That is for rows we have grad for, we update var and accum as follows:
    accum += grad * grad
    var -= lr * grad * (1 / sqrt(accum))

    Args:
      var: A `Tensor` of type `resource`. Should be from a Variable().
      accum: A `Tensor` of type `resource`. Should be from a Variable().
      lr: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
        Learning rate. Must be a scalar.
      epsilon: A `Tensor`. Must have the same type as `lr`.
        Constant factor. Must be a scalar.
      grad: A `Tensor`. Must have the same type as `lr`. The gradient.
      indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
        A vector of indices into the first dimension of var and accum.
      use_locking: An optional `bool`. Defaults to `False`.
        If `True`, updating of the var and accum tensors will be protected
        by a lock; otherwise the behavior is undefined, but may exhibit less
        contention.
      update_slots: An optional `bool`. Defaults to `True`.
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """
    ...
def ResourceApplyAdam(
    var: Tensor,
    m: Tensor,
    v: Tensor,
    beta1_power: TensorCompatible,
    beta2_power: TensorCompatible,
    lr: TensorCompatible,
    beta1: TensorCompatible,
    beta2: TensorCompatible,
    epsilon: TensorCompatible,
    grad: TensorCompatible,
    use_locking: bool = False,
    use_nesterov: bool = False,
    name: str | None = None,
) -> Operation:
    r"""
    Update '*var' according to the Adam algorithm.

    $$\text{lr}_t := \mathrm{lr} \cdot \frac{\sqrt{1 - \beta_2^t}}{1 - \beta_1^t}$$
    $$m_t := \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g$$
    $$v_t := \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g^2$$
    $$\text{var} := \begin{cases} \text{var} - (m_t \beta_1 + g \cdot (1 - \beta_1))\cdot\text{lr}_t/(\sqrt{v_t} + \epsilon), &\text{if use_nesterov}\\\\  \text{var} - m_t \cdot \text{lr}_t /(\sqrt{v_t} + \epsilon), &\text{otherwise} \end{cases}$$

    Args:
      var: A `Tensor` of type `resource`. Should be from a Variable().
      m: A `Tensor` of type `resource`. Should be from a Variable().
      v: A `Tensor` of type `resource`. Should be from a Variable().
      beta1_power: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
        Must be a scalar.
      beta2_power: A `Tensor`. Must have the same type as `beta1_power`.
        Must be a scalar.
      lr: A `Tensor`. Must have the same type as `beta1_power`.
        Scaling factor. Must be a scalar.
      beta1: A `Tensor`. Must have the same type as `beta1_power`.
        Momentum factor. Must be a scalar.
      beta2: A `Tensor`. Must have the same type as `beta1_power`.
        Momentum factor. Must be a scalar.
      epsilon: A `Tensor`. Must have the same type as `beta1_power`.
        Ridge term. Must be a scalar.
      grad: A `Tensor`. Must have the same type as `beta1_power`. The gradient.
      use_locking: An optional `bool`. Defaults to `False`.
        If `True`, updating of the var, m, and v tensors will be protected
        by a lock; otherwise the behavior is undefined, but may exhibit less
        contention.
      use_nesterov: An optional `bool`. Defaults to `False`.
        If `True`, uses the nesterov update.
      name: A name for the operation (optional).

    Returns:
      The created Operation.
    """
    ...
def __getattr__(name: str) -> Incomplete: ...
