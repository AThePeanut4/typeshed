class RequestAborted(Exception):
    """
    Raised when the incoming request tells us it's aborted partway through
    reading the body.
    """
    ...
class RequestTimeout(RequestAborted):
    """Aborted specifically due to timeout."""
    ...
class InvalidChannelLayerError(ValueError):
    """Raised when a channel layer is configured incorrectly."""
    ...
class AcceptConnection(Exception):
    """
    Raised during a websocket.connect (or other supported connection) handler
    to accept the connection.
    """
    ...
class DenyConnection(Exception):
    """
    Raised during a websocket.connect (or other supported connection) handler
    to deny the connection.
    """
    ...
class ChannelFull(Exception):
    """Raised when a channel cannot be sent to as it is over capacity."""
    ...
class MessageTooLarge(Exception):
    """Raised when a message cannot be sent as it's too big."""
    ...
class StopConsumer(Exception):
    """Raised when a consumer wants to stop and close down its application instance."""
    ...
