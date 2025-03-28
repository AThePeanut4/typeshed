"""Case-folding and whitespace normalization"""

def normalize_reference(string: str) -> str:
    """
    Normalize reference label: collapse internal whitespace
    to single space, remove leading/trailing whitespace, case fold.
    """
    ...

__all__ = ["normalize_reference"]
