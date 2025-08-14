"""
Auxiliary transforms mainly to be used by Writer components.

This module is called "writer_aux" because otherwise there would be
conflicting imports like this one::

    from docutils import writers
    from docutils.transforms import writers
"""

from typing import ClassVar, Final

from docutils.transforms import Transform

__docformat__: Final = "reStructuredText"

class Admonitions(Transform):
    """
    Transform specific admonitions, like this:

        <note>
            <paragraph>
                 Note contents ...

    into generic admonitions, like this::

        <admonition classes="note">
            <title>
                Note
            <paragraph>
                Note contents ...

    The admonition title is localized.
    """
    default_priority: ClassVar[int]
    def apply(self) -> None: ...
