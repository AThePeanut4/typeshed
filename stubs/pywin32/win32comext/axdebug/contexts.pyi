"""A module for managing the AXDebug I*Contexts"""

from _typeshed import Incomplete

from win32comext.axdebug import gateways

class DebugCodeContext(gateways.DebugCodeContext, gateways.DebugDocumentContext):
    debugSite: Incomplete
    offset: Incomplete
    length: Incomplete
    breakPointState: int
    lineno: Incomplete
    codeContainer: Incomplete
    def __init__(self, lineNo, charPos, len, codeContainer, debugSite) -> None: ...
    def GetDocumentContext(self): ...
    def SetBreakPoint(self, bps) -> None: ...
    def GetDocument(self): ...
    def EnumCodeContexts(self): ...

class EnumDebugCodeContexts(gateways.EnumDebugCodeContexts): ...
