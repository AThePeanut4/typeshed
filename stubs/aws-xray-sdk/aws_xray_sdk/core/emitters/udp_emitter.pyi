from logging import Logger

from aws_xray_sdk.core.daemon_config import DaemonConfig as DaemonConfig

from ..exceptions.exceptions import InvalidDaemonAddressException as InvalidDaemonAddressException

log: Logger
PROTOCOL_HEADER: str
PROTOCOL_DELIMITER: str
DEFAULT_DAEMON_ADDRESS: str

class UDPEmitter:
    """
    The default emitter the X-Ray recorder uses to send segments/subsegments
    to the X-Ray daemon over UDP using a non-blocking socket. If there is an
    exception on the actual data transfer between the socket and the daemon,
    it logs the exception and continue.
    """
    def __init__(self, daemon_address="127.0.0.1:2000") -> None: ...
    def send_entity(self, entity) -> None:
        """
        Serializes a segment/subsegment and sends it to the X-Ray daemon
        over UDP. By default it doesn't retry on failures.

        :param entity: a trace entity to send to the X-Ray daemon
        """
        ...
    def set_daemon_address(self, address) -> None:
        """
        Set up UDP ip and port from the raw daemon address
        string using ``DaemonConfig`` class utlities.
        """
        ...
    @property
    def ip(self): ...
    @property
    def port(self): ...
