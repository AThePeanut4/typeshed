"""
Python 3.4 HTML5 entity unescaping for all!

Based on
https://hg.python.org/cpython/file/500d3d6f22ff/Lib/html/__init__.py
"""

def _unescape(s: str) -> str:
    """
    Convert all named and numeric character references (e.g. &gt;, &#62;,
    &x3e;) in the string s to the corresponding unicode characters.
    This function uses the rules defined by the HTML 5 standard
    for both valid and invalid character references, and the list of
    HTML 5 named character references defined in html.entities.html5.
    """
    ...
