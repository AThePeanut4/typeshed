"""
Implements signals based on blinker if available, otherwise
falls silently back to a noop. Shamelessly stolen from flask.signals:
https://github.com/mitsuhiko/flask/blob/master/flask/signals.py
"""

from _typeshed import Incomplete
from typing import Any

signals_available: bool

class Namespace:
    def signal(self, name, doc: Incomplete | None = None): ...

class _FakeSignal:
    """
    If blinker is unavailable, create a fake class with the same
    interface that allows sending of signals but will fail with an
    error on anything else.  Instead of doing anything on send, it
    will just ignore the arguments and do nothing instead.
    """
    name: Any
    __doc__: Any
    def __init__(self, name, doc: Incomplete | None = None) -> None: ...
    send: Any
    connect: Any
    disconnect: Any
    has_receivers_for: Any
    receivers_for: Any
    temporarily_connected_to: Any
    connected_to: Any

scope_changed: Any
