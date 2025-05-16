from os import PathLike
from typing import Any

__author__: str
__copyright__: str
__license__: str

class FlexTemplate:
    """
    A flexible templating class.

    Allows to apply one or several template definitions to any page of
    a document in any combination.
    """
    pdf: Any
    splitting_pdf: Any
    handlers: Any
    texts: Any
    def __init__(self, pdf, elements=None) -> None: ...
    elements: Any
    keys: Any
    def load_elements(self, elements) -> None:
        """
        Load a template definition.

        Arguments:

            elements (list of dicts): A template definition in a list of dicts
        """
        ...
    def parse_json(self, infile: PathLike[Any], encoding: str = "utf-8") -> None:
        """
        Load the template definition from a JSON file.
        The data must be structured as an array of objects, with names and values exactly
        equivalent to what would get supplied to load_elements(),

        Arguments:

            infile (string or path-like object): The filepath of the JSON file.

            encoding (string): The character encoding of the file. Default is UTF-8.
        """
        ...
    def parse_csv(
        self, infile: PathLike[Any], delimiter: str = ",", decimal_sep: str = ".", encoding: str | None = None
    ) -> None:
        """
        Load the template definition from a CSV file.

        Arguments:

            infile (string or path-like object): The filepath of the CSV file.

            delimiter (single character): The character that separates the fields in the CSV file:
                Usually a comma, semicolon, or tab.

            decimal_sep (single character): The decimal separator used in the file.
                Usually either a point or a comma.

            encoding (string): The character encoding of the file.
                Default is the system default encoding.
        """
        ...
    def __setitem__(self, name, value) -> None: ...
    set: Any
    def __contains__(self, name): ...
    def __getitem__(self, name): ...
    def split_multicell(self, text, element_name):
        r"""
        Split a string between words, for the parts to fit into a given element
        width. Additional splits will be made replacing any '\n' characters.

        Arguments:

            text (string): The input text string.

            element_name (string): The name of the template element to fit the text inside.

        Returns:
            A list of substrings, each of which will fit into the element width
            when rendered in the element font style and size.
        """
        ...
    def render(self, offsetx: float = 0.0, offsety: float = 0.0, rotate: float = 0.0, scale: float = 1.0):
        """
        Add the contents of the template to the PDF document.

        Arguments:

            offsetx, offsety (float): Place the template to move its origin to the given coordinates.

            rotate (float): Rotate the inserted template around its (offset) origin.

            scale (float): Scale the inserted template by this factor.
        """
        ...

class Template(FlexTemplate):
    """
    A simple templating class.

    Allows to apply a single template definition to all pages of a document.
    """
    def __init__(
        self,
        infile=None,
        elements=None,
        format: str = "A4",
        orientation: str = "portrait",
        unit: str = "mm",
        title: str = "",
        author: str = "",
        subject: str = "",
        creator: str = "",
        keywords: str = "",
    ) -> None: ...
    def add_page(self) -> None: ...
    def render(self, outfile=None, dest=None) -> None: ...  # type: ignore[override]
