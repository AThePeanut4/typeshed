from typing import Literal

def commonmark(text: str, format: Literal["html", "json", "ast", "rst"] = ...) -> str:
    r"""
    Render CommonMark into HTML, JSON or AST
    Optional keyword arguments:
    format:     'html' (default), 'json' or 'ast'

    >>> commonmark("*hello!*")
    '<p><em>hello</em></p>\n'
    """
    ...
