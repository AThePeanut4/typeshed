"""
AXScript Client Framework

This module provides a core framework for an ActiveX Scripting client.
Derived classes actually implement the AX Client itself, including the
scoping rules, etc.

There are classes defined for the engine itself, and for ScriptItems
"""

from _typeshed import Incomplete
from typing import NoReturn

def RemoveCR(text): ...

SCRIPTTEXT_FORCEEXECUTION: int
SCRIPTTEXT_ISEXPRESSION: int
SCRIPTTEXT_ISPERSISTENT: int
state_map: Incomplete

def profile(fn, *args): ...

class SafeOutput:
    softspace: int
    redir: Incomplete
    def __init__(self, redir: Incomplete | None = None) -> None: ...
    def write(self, message) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

def MakeValidSysOuts() -> None: ...
def trace(*args) -> None:
    """A function used instead of "print" for debugging output."""
    ...
def RaiseAssert(scode, desc) -> NoReturn:
    """A debugging function that raises an exception considered an "Assertion"."""
    ...

class AXScriptCodeBlock:
    """An object which represents a chunk of code in an AX Script"""
    name: Incomplete
    codeText: Incomplete
    codeObject: Incomplete
    sourceContextCookie: Incomplete
    startLineNumber: Incomplete
    flags: Incomplete
    beenExecuted: int
    def __init__(self, name: str, codeText: str, sourceContextCookie: int, startLineNumber: int, flags) -> None: ...
    def GetFileName(self): ...
    def GetDisplayName(self): ...
    def GetLineNo(self, no: int): ...

class Event:
    """A single event for a ActiveX named object."""
    name: str
    def __init__(self) -> None: ...
    def Reset(self) -> None: ...
    def Close(self) -> None: ...
    dispid: Incomplete
    def Build(self, typeinfo, funcdesc) -> None: ...

class EventSink:
    """A set of events against an item.  Note this is a COM client for connection points."""
    events: Incomplete
    connection: Incomplete
    coDispatch: Incomplete
    myScriptItem: Incomplete
    myInvokeMethod: Incomplete
    iid: Incomplete
    def __init__(self, myItem, coDispatch) -> None: ...
    def Reset(self) -> None: ...
    def Close(self) -> None: ...
    def GetSourceTypeInfo(self, typeinfo):
        """Gets the typeinfo for the Source Events for the passed typeinfo"""
        ...
    def BuildEvents(self) -> None: ...
    def Connect(self) -> None: ...
    def Disconnect(self) -> None: ...

class ScriptItem:
    """An item (or subitem) that is exposed to the ActiveX script"""
    parentItem: Incomplete
    dispatch: Incomplete
    name: Incomplete
    flags: Incomplete
    eventSink: Incomplete
    subItems: Incomplete
    createdConnections: int
    isRegistered: int
    def __init__(self, parentItem, name, dispatch, flags) -> None: ...
    def Reset(self) -> None: ...
    def Close(self) -> None: ...
    def Register(self) -> None: ...
    def IsGlobal(self): ...
    def IsVisible(self): ...
    def GetEngine(self): ...
    def GetSubItemClass(self): ...
    def GetSubItem(self, name): ...
    def GetCreateSubItem(self, parentItem, name, dispatch, flags): ...
    def CreateConnections(self) -> None: ...
    def Connect(self) -> None: ...
    def Disconnect(self) -> None: ...
    def BuildEvents(self) -> None: ...
    def FindBuildSubItemEvents(self) -> None: ...
    def GetDefaultSourceTypeInfo(self, typeinfo):
        """Gets the typeinfo for the Default Dispatch for the passed typeinfo"""
        ...

IActiveScriptMethods: Incomplete
IActiveScriptParseMethods: Incomplete
IObjectSafetyMethods: Incomplete
IActiveScriptParseProcedureMethods: Incomplete

class COMScript:
    """
    An ActiveX Scripting engine base class.

    This class implements the required COM interfaces for ActiveX scripting.
    """
    baseThreadId: int
    debugManager: Incomplete
    threadState: Incomplete
    scriptState: Incomplete
    scriptSite: Incomplete
    safetyOptions: int
    lcid: int
    subItems: Incomplete
    scriptCodeBlocks: Incomplete
    def __init__(self) -> None: ...
    def InitNew(self) -> None: ...
    def AddScriptlet(
        self, defaultName, code, itemName, subItemName, eventName, delimiter, sourceContextCookie, startLineNumber
    ) -> None: ...
    def ParseScriptText(self, code, itemName, context, delimiter, sourceContextCookie, startLineNumber, flags, bWantResult): ...
    def ParseProcedureText(
        self, code, formalParams, procName, itemName, unkContext, delimiter, contextCookie, startingLineNumber, flags
    ) -> None: ...
    def SetScriptSite(self, site) -> None: ...
    def GetScriptSite(self, iid): ...
    def SetScriptState(self, state) -> None: ...
    def GetScriptState(self): ...
    persistLoaded: int
    def Close(self) -> None: ...
    def AddNamedItem(self, name, flags) -> None: ...
    def GetScriptDispatch(self, name) -> None: ...
    def GetCurrentScriptThreadID(self): ...
    def GetScriptThreadID(self, win32ThreadId): ...
    def GetScriptThreadState(self, scriptThreadId): ...
    def AddTypeLib(self, uuid, major, minor, flags) -> None: ...
    def Clone(self) -> None: ...
    def SetInterfaceSafetyOptions(self, iid, optionsMask, enabledOptions) -> None: ...
    def GetInterfaceSafetyOptions(self, iid): ...
    def ExecutePendingScripts(self) -> None: ...
    def ProcessScriptItemEvent(self, item, event, lcid, wFlags, args): ...
    def ResetNamedItems(self) -> None: ...
    def GetCurrentSafetyOptions(self): ...
    def ProcessNewNamedItemsConnections(self) -> None: ...
    def RegisterNewNamedItems(self) -> None: ...
    def RegisterNamedItem(self, item) -> None: ...
    def CheckConnectedOrDisconnected(self) -> None: ...
    def Connect(self) -> None: ...
    def Run(self) -> None: ...
    def Stop(self) -> None: ...
    def Disconnect(self) -> None: ...
    def ConnectEventHandlers(self) -> None: ...
    def DisconnectEventHandlers(self) -> None: ...
    def Reset(self) -> None: ...
    def ChangeScriptState(self, state) -> None: ...
    def ApplyInScriptedSection(self, codeBlock: AXScriptCodeBlock | None, fn, args): ...
    def CompileInScriptedSection(self, codeBlock: AXScriptCodeBlock, type, realCode: Incomplete | None = None): ...
    def ExecInScriptedSection(self, codeBlock: AXScriptCodeBlock, globals, locals: Incomplete | None = None): ...
    def EvalInScriptedSection(self, codeBlock, globals, locals: Incomplete | None = None): ...
    def HandleException(self, codeBlock: AXScriptCodeBlock | None) -> NoReturn:
        """Never returns - raises a ComException"""
        ...
    def BeginScriptedSection(self) -> None: ...
    def EndScriptedSection(self) -> None: ...
    def DisableInterrupts(self) -> None: ...
    def EnableInterrupts(self) -> None: ...
    def GetNamedItem(self, name): ...
    def GetNamedItemClass(self): ...

def dumptypeinfo(typeinfo) -> None: ...
