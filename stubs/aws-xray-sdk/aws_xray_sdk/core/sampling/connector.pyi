class ServiceConnector:
    """
    Connector class that translates Centralized Sampling poller functions to
    actual X-Ray back-end APIs and communicates with X-Ray daemon as the
    signing proxy.
    """
    def __init__(self) -> None: ...
    def fetch_sampling_rules(self): ...
    def fetch_sampling_target(self, rules): ...
    def setup_xray_client(self, ip, port, client) -> None:
        """
        Setup the xray client based on ip and port.
        If a preset client is specified, ip and port
        will be ignored.
        """
        ...
    @property
    def context(self): ...
    @context.setter
    def context(self, v) -> None: ...
