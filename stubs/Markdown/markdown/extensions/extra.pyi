from markdown.extensions import Extension

extensions: list[str]

class ExtraExtension(Extension):
    """Add various extensions to Markdown class."""
    def __init__(self, **kwargs) -> None:
        """`config` is a dumb holder which gets passed to the actual extension later. """
        ...

def makeExtension(**kwargs) -> ExtraExtension: ...
