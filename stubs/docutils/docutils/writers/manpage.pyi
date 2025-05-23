"""
Simple man page writer for reStructuredText.

Man pages (short for "manual pages") contain system documentation on unix-like
systems. The pages are grouped in numbered sections:

 1 executable programs and shell commands
 2 system calls
 3 library functions
 4 special files
 5 file formats
 6 games
 7 miscellaneous
 8 system administration

Man pages are written *troff*, a text file formatting system.

See https://www.tldp.org/HOWTO/Man-Page for a start.

Man pages have no subsection only parts.
Standard parts

  NAME ,
  SYNOPSIS ,
  DESCRIPTION ,
  OPTIONS ,
  FILES ,
  SEE ALSO ,
  BUGS ,

and

  AUTHOR .

A unix-like system keeps an index of the DESCRIPTIONs, which is accessible
by the command whatis or apropos.
"""

import re
from _typeshed import Incomplete
from collections.abc import Callable
from typing import Protocol, type_check_only
from typing_extensions import Never

from docutils import nodes

@type_check_only
class _RegexPatternSub(Protocol):
    # Matches the signature of the bound instance method `re.Pattern[str].sub` exactly
    def __call__(self, /, repl: str | Callable[[re.Match[str]], str], string: str, count: int = 0) -> str: ...

class Translator(nodes.NodeVisitor):
    def visit_admonition(self, node: nodes.admonition, name: str | None = None) -> None: ...
    def visit_comment(self, node: nodes.comment, sub: _RegexPatternSub = ...) -> Never: ...
    def __getattr__(self, name: str, /) -> Incomplete: ...

def __getattr__(name: str): ...  # incomplete module
