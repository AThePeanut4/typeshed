"""
Contains knowledge to build a COM object definition.

This module is used by both the @dynamic@ and @makepy@ modules to build
all knowledge of a COM object.

This module contains classes which contain the actual knowledge of the object.
This include parameter and return type information, the COM dispid and CLSID, etc.

Other modules may use this information to generate .py files, use the information
dynamically, or possibly even generate .html documentation for objects.
"""

from _typeshed import Incomplete

class OleItem:
    typename: str
    doc: Incomplete
    python_name: Incomplete
    bWritten: int
    bIsDispatch: int
    bIsSink: int
    clsid: Incomplete
    co_class: Incomplete
    def __init__(self, doc: Incomplete | None = ...) -> None: ...

class DispatchItem(OleItem):
    typename: str
    propMap: Incomplete
    propMapGet: Incomplete
    propMapPut: Incomplete
    mapFuncs: Incomplete
    defaultDispatchName: Incomplete
    hidden: int
    def __init__(
        self, typeinfo: Incomplete | None = ..., attr: Incomplete | None = ..., doc: Incomplete | None = ..., bForUser: int = ...
    ) -> None: ...
    clsid: Incomplete
    bIsDispatch: Incomplete
    def Build(self, typeinfo, attr, bForUser: int = ...) -> None: ...
    def CountInOutOptArgs(self, argTuple):
        """Return tuple counting in/outs/OPTS.  Sum of result may not be len(argTuple), as some args may be in/out."""
        ...
    def MakeFuncMethod(self, entry, name, bMakeClass: int = ...): ...
    def MakeDispatchFuncMethod(self, entry, name, bMakeClass: int = ...): ...
    def MakeVarArgsFuncMethod(self, entry, name, bMakeClass: int = ...): ...

class LazyDispatchItem(DispatchItem):
    typename: str
    clsid: Incomplete
    def __init__(self, attr, doc) -> None: ...
