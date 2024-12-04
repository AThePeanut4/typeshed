from _typeshed import FileDescriptorOrPath
from typing import Any

def main(template: FileDescriptorOrPath, data: FileDescriptorOrPath | None = None, **kwargs: Any) -> str: ...
def cli_main() -> None:
    """Render mustache templates using json files"""
    ...
