import re
from typing import Final
from typing_extensions import Self

reContainer: Final[re.Pattern[str]]

def is_container(node: Node) -> bool: ...

class NodeWalker:
    current: Node | None
    root: Node
    entering: bool
    def __init__(self, root: Node) -> None: ...
    def __next__(self) -> tuple[Node, bool]: ...
    next = __next__
    def __iter__(self) -> Self: ...
    def nxt(self) -> dict[str, Node | bool] | None:
        """for backwards compatibility """
        ...
    def resume_at(self, node: Node, entering: bool) -> None: ...

class Node:
    t: str
    parent: Node | None
    first_child: Node | None
    last_child: Node | None
    prv: Node | None
    nxt: Node | None
    sourcepos: list[list[int]] | None
    last_line_blank: bool
    last_line_checked: bool
    is_open: bool
    string_content: str
    literal: str | None
    list_data: dict[str, str | int | bool | None]
    info: str | None
    destination: str | None
    title: str | None
    is_fenced: bool
    fence_char: str | None
    fence_length: int
    fence_offset: int | None
    level: int | None
    on_enter: str | None
    on_exit: str | None
    def __init__(self, node_type: str, sourcepos: list[list[int]] | None) -> None: ...
    def pretty(self) -> None: ...
    def normalize(self) -> None: ...
    def is_container(self) -> bool: ...
    def append_child(self, child: Node) -> None: ...
    def prepend_child(self, child: Node) -> None: ...
    def unlink(self) -> None: ...
    def insert_after(self, sibling: Node) -> None: ...
    def insert_before(self, sibling: Node) -> None: ...
    def walker(self) -> NodeWalker: ...
