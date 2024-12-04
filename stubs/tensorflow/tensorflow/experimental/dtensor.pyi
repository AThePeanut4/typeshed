"""Public API for tf._api.v2.experimental.dtensor namespace"""

from _typeshed import Incomplete

from tensorflow._aliases import IntArray, IntDataSequence

Layout = Incomplete

class Mesh:
    """
    Represents a Mesh configuration over a certain list of Mesh Dimensions.

    A mesh consists of named dimensions with sizes, which describe how a set of
    devices are arranged. Defining tensor layouts in terms of mesh dimensions
    allows us to efficiently determine the communication required when computing
    an operation with tensors of different layouts.

    A mesh provides information not only about the placement of the tensors but
    also the topology of the underlying devices. For example, we can group 8 TPUs
    as a 1-D array for data parallelism or a `2x4` grid for (2-way) data
    parallelism and (4-way) model parallelism.

    Refer to [DTensor Concepts](https://www.tensorflow.org/guide/dtensor_overview)
    for in depth discussion and examples.

    Note: the utilities `dtensor.create_mesh` and
    `dtensor.create_distributed_mesh` provide a simpler API to create meshes for
    single- or multi-client use cases.
    """
    def __init__(
        self,
        dim_names: list[str],
        global_device_ids: IntArray | IntDataSequence,
        local_device_ids: list[int],
        local_devices: list[Incomplete | str],
        mesh_name: str = "",
        global_devices: list[Incomplete | str] | None = None,
        use_xla_spmd: bool = False,
    ) -> None:
        """
        Builds a Mesh.

        The `dim_names` and `global_device_ids` arguments describe the dimension
        names and shape for the mesh.

        For example,

        ```python
          dim_names = ('x', 'y'),
          global_device_ids = [[0, 1],
                               [2, 3],
                               [4, 5]]
        ```

        defines a 2D mesh of shape 3x2. A reduction over the 'x' dimension will
        reduce across columns (0, 2, 4) and (1, 3, 5), and a reduction over the 'y'
        dimension reduces across rows.

        Note: the utilities `dtensor.create_mesh` and
        `dtensor.create_distributed_mesh` provide a simpler API to create meshes for
        single- or multi-client use cases.

        Args:
          dim_names: A list of strings indicating dimension names.
          global_device_ids: An ndarray of global device IDs is used to compose
            DeviceSpecs describing the mesh. The shape of this array determines the
            size of each mesh dimension. Values in this array should increment
            sequentially from 0. This argument is the same for every DTensor client.
          local_device_ids: A list of local device IDs equal to a subset of values
            in global_device_ids. They indicate the position of local devices in the
            global mesh. Different DTensor clients must contain distinct
            local_device_ids contents. All local_device_ids from all DTensor clients
            must cover every element in global_device_ids.
          local_devices: The list of devices hosted locally. The elements correspond
            1:1 to those of local_device_ids.
          mesh_name: The name of the mesh. Currently, this is rarely used, and is
            mostly used to indicate whether it is a CPU, GPU, or TPU-based mesh.
          global_devices (optional): The list of global devices. Set when multiple
            device meshes are in use.
          use_xla_spmd (optional): Boolean when True, will use XLA SPMD instead of
            DTensor SPMD.
        """
        ...

def __getattr__(name: str) -> Incomplete: ...
