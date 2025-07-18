"""Reader for existing document trees."""

from typing import ClassVar, TypeVar

from docutils import readers

_S = TypeVar("_S", bound=str | bytes)

class Reader(readers.ReReader[_S]):
    """
    Adapt the Reader API for an existing document tree.

    The existing document tree must be passed as the ``source`` parameter to
    the `docutils.core.Publisher` initializer, wrapped in a
    `docutils.io.DocTreeInput` object::

        pub = docutils.core.Publisher(
            ..., source=docutils.io.DocTreeInput(document), ...)

    The original document settings are overridden; if you want to use the
    settings of the original document, pass ``settings=document.settings`` to
    the Publisher call above.
    """
    config_section_dependencies: ClassVar[tuple[str, ...]]
