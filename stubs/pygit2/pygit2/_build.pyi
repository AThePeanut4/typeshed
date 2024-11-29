"""
This is an special module, it provides stuff used by setup.py at build time.
But also used by pygit2 at run time.
"""

from pathlib import Path

__version__: str

def get_libgit2_paths() -> tuple[Path, dict[str, list[str]]]: ...
