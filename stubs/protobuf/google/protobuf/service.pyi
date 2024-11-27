"""
DEPRECATED:  Declares the RPC service interfaces.

This module declares the abstract interfaces underlying proto2 RPC
services.  These are intended to be independent of any particular RPC
implementation, so that proto2 services can be used on top of a variety
of implementations.  Starting with version 2.3.0, RPC implementations should
not try to build on these, but should instead provide code generator plugins
which generate code specific to the particular RPC implementation.  This way
the generated code can be more appropriate for the implementation in use
and can avoid unnecessary layers of indirection.
"""

from collections.abc import Callable
from concurrent.futures import Future

from google.protobuf.descriptor import MethodDescriptor, ServiceDescriptor
from google.protobuf.message import Message

class RpcException(Exception):
    """Exception raised on failed blocking RPC method call."""
    ...

class Service:
    """
    Abstract base interface for protocol-buffer-based RPC services.

    Services themselves are abstract classes (implemented either by servers or as
    stubs), but they subclass this base interface. The methods of this
    interface can be used to call the methods of the service without knowing
    its exact type at compile time (analogous to the Message interface).
    """
    @staticmethod
    def GetDescriptor() -> ServiceDescriptor:
        """Retrieves this service's descriptor."""
        ...
    def CallMethod(
        self,
        method_descriptor: MethodDescriptor,
        rpc_controller: RpcController,
        request: Message,
        done: Callable[[Message], None] | None,
    ) -> Future[Message] | None:
        """
        Calls a method of the service specified by method_descriptor.

        If "done" is None then the call is blocking and the response
        message will be returned directly.  Otherwise the call is asynchronous
        and "done" will later be called with the response value.

        In the blocking case, RpcException will be raised on error.

        Preconditions:

        * method_descriptor.service == GetDescriptor
        * request is of the exact same classes as returned by
          GetRequestClass(method).
        * After the call has started, the request must not be modified.
        * "rpc_controller" is of the correct type for the RPC implementation being
          used by this Service.  For stubs, the "correct type" depends on the
          RpcChannel which the stub is using.

        Postconditions:

        * "done" will be called when the method is complete.  This may be
          before CallMethod() returns or it may be at some point in the future.
        * If the RPC failed, the response value passed to "done" will be None.
          Further details about the failure can be found by querying the
          RpcController.
        """
        ...
    def GetRequestClass(self, method_descriptor: MethodDescriptor) -> type[Message]:
        """
        Returns the class of the request message for the specified method.

        CallMethod() requires that the request is of a particular subclass of
        Message. GetRequestClass() gets the default instance of this required
        type.

        Example:
          method = service.GetDescriptor().FindMethodByName("Foo")
          request = stub.GetRequestClass(method)()
          request.ParseFromString(input)
          service.CallMethod(method, request, callback)
        """
        ...
    def GetResponseClass(self, method_descriptor: MethodDescriptor) -> type[Message]:
        """
        Returns the class of the response message for the specified method.

        This method isn't really needed, as the RpcChannel's CallMethod constructs
        the response protocol message. It's provided anyway in case it is useful
        for the caller to know the response type in advance.
        """
        ...

class RpcController:
    """
    An RpcController mediates a single method call.

    The primary purpose of the controller is to provide a way to manipulate
    settings specific to the RPC implementation and to find out about RPC-level
    errors. The methods provided by the RpcController interface are intended
    to be a "least common denominator" set of features which we expect all
    implementations to support.  Specific implementations may provide more
    advanced features (e.g. deadline propagation).
    """
    def Reset(self) -> None:
        """
        Resets the RpcController to its initial state.

        After the RpcController has been reset, it may be reused in
        a new call. Must not be called while an RPC is in progress.
        """
        ...
    def Failed(self) -> bool:
        """
        Returns true if the call failed.

        After a call has finished, returns true if the call failed.  The possible
        reasons for failure depend on the RPC implementation.  Failed() must not
        be called before a call has finished.  If Failed() returns true, the
        contents of the response message are undefined.
        """
        ...
    def ErrorText(self) -> str | None:
        """If Failed is true, returns a human-readable description of the error."""
        ...
    def StartCancel(self) -> None:
        """
        Initiate cancellation.

        Advises the RPC system that the caller desires that the RPC call be
        canceled.  The RPC system may cancel it immediately, may wait awhile and
        then cancel it, or may not even cancel the call at all.  If the call is
        canceled, the "done" callback will still be called and the RpcController
        will indicate that the call failed at that time.
        """
        ...
    def SetFailed(self, reason: str) -> None:
        """
        Sets a failure reason.

        Causes Failed() to return true on the client side.  "reason" will be
        incorporated into the message returned by ErrorText().  If you find
        you need to return machine-readable information about failures, you
        should incorporate it into your response protocol buffer and should
        NOT call SetFailed().
        """
        ...
    def IsCanceled(self) -> bool:
        """
        Checks if the client cancelled the RPC.

        If true, indicates that the client canceled the RPC, so the server may
        as well give up on replying to it.  The server should still call the
        final "done" callback.
        """
        ...
    def NotifyOnCancel(self, callback: Callable[[], None]) -> None:
        """
        Sets a callback to invoke on cancel.

        Asks that the given callback be called when the RPC is canceled.  The
        callback will always be called exactly once.  If the RPC completes without
        being canceled, the callback will be called after completion.  If the RPC
        has already been canceled when NotifyOnCancel() is called, the callback
        will be called immediately.

        NotifyOnCancel() must be called no more than once per request.
        """
        ...

class RpcChannel:
    """
    Abstract interface for an RPC channel.

    An RpcChannel represents a communication line to a service which can be used
    to call that service's methods.  The service may be running on another
    machine. Normally, you should not use an RpcChannel directly, but instead
    construct a stub {@link Service} wrapping it.  Example:

    Example:
      RpcChannel channel = rpcImpl.Channel("remotehost.example.com:1234")
      RpcController controller = rpcImpl.Controller()
      MyService service = MyService_Stub(channel)
      service.MyMethod(controller, request, callback)
    """
    def CallMethod(
        self,
        method_descriptor: MethodDescriptor,
        rpc_controller: RpcController,
        request: Message,
        response_class: type[Message],
        done: Callable[[Message], None] | None,
    ) -> Future[Message] | None:
        """
        Calls the method identified by the descriptor.

        Call the given method of the remote service.  The signature of this
        procedure looks the same as Service.CallMethod(), but the requirements
        are less strict in one important way:  the request object doesn't have to
        be of any specific class as long as its descriptor is method.input_type.
        """
        ...
