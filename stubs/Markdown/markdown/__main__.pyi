import optparse
from logging import Logger
from typing import Any

logger: Logger

def parse_options(
    args: list[str] | None = None, values: optparse.Values | None = None
) -> tuple[dict[str, Any], Any]:
    """Define and parse `optparse` options for command-line usage."""
    ...
def run() -> None:
    """Run Markdown from the command line."""
    ...
