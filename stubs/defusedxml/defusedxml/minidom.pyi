from xml.dom.minidom import Document

__origin__: str

def parse(
    file,
    parser=None,
    bufsize: int | None = None,
    forbid_dtd: bool = False,
    forbid_entities: bool = True,
    forbid_external: bool = True,
) -> Document:
    """Parse a file into a DOM by filename or file object."""
    ...
def parseString(
    string: str, parser=None, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True
) -> Document: ...
