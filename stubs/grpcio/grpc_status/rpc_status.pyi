"""Reference implementation for status mapping in gRPC Python."""

from typing import Any

import grpc

# XXX: don't yet know how to add a stub for google.rpc.status_pb2.Status
# without affecting other stuff; may need to make a stub-only package for
# google.rpc as well.

# Returns a google.rpc.status.Status message corresponding to a given grpc.Call.
def from_call(call: grpc.Call) -> Any:
    """
    Returns a google.rpc.status.Status message corresponding to a given grpc.Call.

    This is an EXPERIMENTAL API.

    Args:
      call: A grpc.Call instance.

    Returns:
      A google.rpc.status.Status message representing the status of the RPC.

    Raises:
      ValueError: If the gRPC call's code or details are inconsistent with the
        status code and message inside of the google.rpc.status.Status.
    """
    ...

# Convert a google.rpc.status.Status message to grpc.Status.
def to_status(status: Any) -> grpc.Status:
    """
    Convert a google.rpc.status.Status message to grpc.Status.

    This is an EXPERIMENTAL API.

    Args:
      status: a google.rpc.status.Status message representing the non-OK status
        to terminate the RPC with and communicate it to the client.

    Returns:
      A grpc.Status instance representing the input google.rpc.status.Status message.
    """
    ...
