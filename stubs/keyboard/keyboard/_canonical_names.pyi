canonical_names: dict[str, str]
sided_modifiers: set[str]
all_modifiers: set[str]

def normalize_name(name: str) -> str:
    """
    Given a key name (e.g. "LEFT CONTROL"), clean up the string and convert to
    the canonical representation (e.g. "left ctrl") if one is known.
    """
    ...
