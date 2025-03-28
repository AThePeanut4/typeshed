"""Management of documents for AXDebugging."""

from _typeshed import Incomplete

from win32comext.axdebug import gateways

def GetGoodFileName(fname): ...

class DebugDocumentProvider(gateways.DebugDocumentProvider):
    doc: Incomplete
    def __init__(self, doc) -> None: ...
    def GetName(self, dnt): ...
    def GetDocumentClassId(self): ...
    def GetDocument(self): ...

class DebugDocumentText(gateways.DebugDocumentText):
    codeContainer: Incomplete
    def __init__(self, codeContainer) -> None: ...
    def GetName(self, dnt): ...
    def GetDocumentClassId(self): ...
    def GetSize(self): ...
    def GetPositionOfLine(self, cLineNumber): ...
    def GetLineOfPosition(self, charPos): ...
    def GetText(self, charPos, maxChars, wantAttr): ...
    def GetPositionOfContext(self, context): ...
    def GetContextOfPosition(self, charPos, maxChars): ...

class CodeContainerProvider:
    """
    An abstract Python class which provides code containers!

    Given a Python file name (as the debugger knows it by) this will
    return a CodeContainer interface suitable for use.

    This provides a simple base implementation that simply supports
    a dictionary of nodes and providers.
    """
    ccsAndNodes: Incomplete
    def AddCodeContainer(self, cc, node: Incomplete | None = ...) -> None: ...
    def FromFileName(self, fname): ...
    def Close(self) -> None: ...
