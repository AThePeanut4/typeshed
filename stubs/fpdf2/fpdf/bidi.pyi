from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Final, Literal, TypedDict, type_check_only

from .enums import TextDirection

MAX_DEPTH: Final = 125

@type_check_only
class _BracketInfo(TypedDict):
    pair: str
    type: Literal["o", "c"]

BIDI_BRACKETS: Final[dict[str, _BracketInfo]]

class BidiCharacter:
    character_index: int
    character: str
    bidi_class: str
    original_bidi_class: str
    embedding_level: str
    direction: Incomplete | None

    def __init__(self, character_index: int, character: str, embedding_level: str, debug: bool) -> None: ...
    def get_direction_from_level(self) -> Literal["L", "R"]: ...
    def set_class(self, cls: str) -> None: ...

@dataclass
class DirectionalStatus:
    """DirectionalStatus(embedding_level: int, directional_override_status: str, directional_isolate_status: bool)"""
    embedding_level: int  # between 0 and MAX_DEPTH
    directional_override_status: Literal["N", "L", "R"]
    directional_isolate_status: bool

class IsolatingRun:
    characters: list[BidiCharacter]
    previous_direction: str
    next_direction: str
    def __init__(self, characters: list[BidiCharacter], sos: str, eos: str) -> None: ...
    def resolve_weak_types(self) -> None: ...
    def pair_brackets(self) -> list[tuple[int, int]]:
        """
        Calculate all the bracket pairs on an isolate run, to be used on rule N0
        How to calculate bracket pairs:
        - Basic definitions 14, 15 and 16: http://www.unicode.org/reports/tr9/#BD14
        - BIDI brackets for dummies: https://www.unicode.org/notes/tn39/
        """
        ...
    def resolve_neutral_types(self) -> None: ...
    def resolve_implicit_levels(self) -> None: ...

def auto_detect_base_direction(string: str, stop_at_pdi: bool = False, debug: bool = False) -> TextDirection:
    """
    This function applies rules P2 and P3 to detect the direction of a paragraph, retuning
    the first strong direction and skipping over isolate sequences.
    P1 must be applied before calling this function (breaking into paragraphs)
    stop_at_pdi can be set to True to get the direction of a single isolate sequence
    """
    ...
def calculate_isolate_runs(paragraph: Sequence[BidiCharacter]) -> list[IsolatingRun]: ...

class BidiParagraph:
    text: str
    base_direction: TextDirection
    debug: bool
    base_embedding_level: int
    characters: list[BidiCharacter]

    def __init__(self, text: str, base_direction: TextDirection | None = None, debug: bool = False) -> None: ...
    def get_characters(self) -> list[BidiCharacter]: ...
    def get_characters_with_embedding_level(self) -> list[BidiCharacter]: ...
    def get_reordered_characters(self) -> list[BidiCharacter]: ...
    def get_all(self) -> tuple[list[BidiCharacter], tuple[BidiCharacter, ...]]: ...
    def get_reordered_string(self) -> str:
        """Used for conformance validation"""
        ...
    def get_bidi_fragments(self) -> tuple[tuple[str, Literal["L", "R"]], ...]: ...
    def get_bidi_characters(self) -> None: ...
    def split_bidi_fragments(self) -> tuple[tuple[str, Literal["L", "R"]], ...]: ...
    def reorder_resolved_levels(self) -> tuple[BidiCharacter, ...]: ...
