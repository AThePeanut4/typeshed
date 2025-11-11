from logging import Logger

from .connector import ServiceConnector
from .rule_cache import RuleCache
from .rule_poller import RulePoller

log: Logger

class TargetPoller:
    """
    The poller to report the current statistics of all
    centralized sampling rules and retrieve the new allocated
    sampling quota and TTL from X-Ray service.
    """
    def __init__(self, cache: RuleCache, rule_poller: RulePoller, connector: ServiceConnector) -> None: ...
    def start(self) -> None: ...
