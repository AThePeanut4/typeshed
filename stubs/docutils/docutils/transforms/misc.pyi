"""Miscellaneous transforms."""

from typing import ClassVar, Final

from docutils import nodes
from docutils.transforms import Transform

__docformat__: Final = "reStructuredText"

class CallBack(Transform):
    """
    Inserts a callback into a document.  The callback is called when the
    transform is applied, which is determined by its priority.

    For use with `nodes.pending` elements.  Requires a ``details['callback']``
    entry, a bound method or function which takes one parameter: the pending
    node.  Other data can be stored in the ``details`` attribute or in the
    object hosting the callback method.
    """
    default_priority: ClassVar[int]
    def apply(self) -> None: ...

class ClassAttribute(Transform):
    """
    Move the "class" attribute specified in the "pending" node into the
    immediately following non-comment element.
    """
    default_priority: ClassVar[int]
    def apply(self) -> None: ...

class Transitions(Transform):
    """
    Move transitions at the end of sections up the tree.  Complain
    on transitions after a title, at the beginning or end of the
    document, and after another transition.

    For example, transform this::

        <section>
            ...
            <transition>
        <section>
            ...

    into this::

        <section>
            ...
        <transition>
        <section>
            ...
    """
    default_priority: ClassVar[int]
    def apply(self) -> None: ...
    def visit_transition(self, node: nodes.transition) -> None: ...
