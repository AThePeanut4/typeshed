"""
A compilation of various Python-Markdown extensions that imitates
[PHP Markdown Extra](http://michelf.com/projects/php-markdown/extra/).

Note that each of the individual extensions still need to be available
on your `PYTHONPATH`. This extension simply wraps them all up as a
convenience so that only one extension needs to be listed when
initiating Markdown. See the documentation for each individual
extension for specifics about that extension.

There may be additional extensions that are distributed with
Python-Markdown that are not included here in Extra. Those extensions
are not part of PHP Markdown Extra, and therefore, not part of
Python-Markdown Extra. If you really would like Extra to include
additional extensions, we suggest creating your own clone of Extra
under a different name. You could also edit the `extensions` global
variable defined below, but be aware that such changes may be lost
when you upgrade to any future version of Python-Markdown.

See the [documentation](https://Python-Markdown.github.io/extensions/extra)
for details.
"""

from markdown.extensions import Extension

extensions: list[str]

class ExtraExtension(Extension):
    """Add various extensions to Markdown class."""
    def __init__(self, **kwargs) -> None:
        """`config` is a dumb holder which gets passed to the actual extension later. """
        ...

def makeExtension(**kwargs) -> ExtraExtension: ...
