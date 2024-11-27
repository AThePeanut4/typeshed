from enum import Enum

class ExchangeType(Enum):
    """An enumeration."""
    direct = "direct"
    fanout = "fanout"
    headers = "headers"
    topic = "topic"
