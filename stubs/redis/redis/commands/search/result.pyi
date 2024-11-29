from typing import Any

class Result:
    """
    Represents the result of a search query, and has an array of Document
    objects
    """
    total: Any
    duration: Any
    docs: Any
    def __init__(self, res, hascontent, duration: int = 0, has_payload: bool = False, with_scores: bool = False) -> None:
        """
        - **snippets**: An optional dictionary of the form
        {field: snippet_size} for snippet formatting
        """
        ...
