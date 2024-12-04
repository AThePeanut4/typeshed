"""an interactive shell for the netaddr library"""

from typing import Any

SHELL_NAMESPACE: dict[str, Any]
ASCII_ART_LOGO: str

def main() -> None: ...
def shell() -> None: ...
def info(network_input: str) -> None: ...
