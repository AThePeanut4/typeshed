"""
A do-nothing Writer.

`self.output` will change from ``None`` to the empty string
in Docutils 0.22.
"""

from _typeshed import Incomplete

def __getattr__(name: str) -> Incomplete: ...
