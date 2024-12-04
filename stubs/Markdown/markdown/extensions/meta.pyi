"""
This extension adds Meta Data handling to markdown.

See the [documentation](https://Python-Markdown.github.io/extensions/meta_data)
for details.
"""

from re import Pattern
from typing import Any

from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

log: Any
META_RE: Pattern[str]
META_MORE_RE: Pattern[str]
BEGIN_RE: Pattern[str]
END_RE: Pattern[str]

class MetaExtension(Extension):
    """Meta-Data extension for Python-Markdown. """
    md: Markdown
    def reset(self) -> None: ...

class MetaPreprocessor(Preprocessor):
    """Get Meta-Data. """
    ...

def makeExtension(**kwargs) -> MetaExtension: ...
