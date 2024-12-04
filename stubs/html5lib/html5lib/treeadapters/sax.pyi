from typing import Any

prefix_mapping: Any

def to_sax(walker, handler) -> None:
    """
    Call SAX-like content handler based on treewalker walker

    :arg walker: the treewalker to use to walk the tree to convert it

    :arg handler: SAX handler to use
    """
    ...
