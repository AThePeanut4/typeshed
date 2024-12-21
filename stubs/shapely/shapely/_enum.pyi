from enum import IntEnum

class ParamEnum(IntEnum):  # type: ignore[misc]  # Enum with no members
    @classmethod
    def get_value(cls, item: str) -> int:
        """Validate incoming item and raise a ValueError with valid options if not present."""
        ...
