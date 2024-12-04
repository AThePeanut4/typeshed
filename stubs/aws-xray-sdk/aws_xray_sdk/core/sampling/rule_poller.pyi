from typing import Any

log: Any
DEFAULT_INTERVAL: Any

class RulePoller:
    def __init__(self, cache, connector) -> None: ...
    def start(self) -> None: ...
    def wake_up(self) -> None:
        """
        Force the rule poller to pull the sampling rules from the service
        regardless of the polling interval.
        This method is intended to be used by ``TargetPoller`` only.
        """
        ...
