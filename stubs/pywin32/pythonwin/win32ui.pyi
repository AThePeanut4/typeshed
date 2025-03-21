"""A module, encapsulating the Microsoft Foundation Classes."""

from _typeshed import Incomplete, OptExcInfo, Unused
from collections.abc import Callable

import _win32typing

class error(Exception): ...

def ComparePath(path1: str, path2: str, /): ...
def CreateMDIFrame() -> _win32typing.PyCMDIFrameWnd: ...
def CreateMDIChild() -> _win32typing.PyCMDIChildWnd: ...
def CreateBitmap(*args: Unused) -> _win32typing.PyCBitmap: ...
def CreateBitmapFromHandle(): ...
def CreateBrush() -> _win32typing.PyCBrush: ...
def CreateButton() -> _win32typing.PyCButton: ...
def CreateColorDialog(
    initColor: int = ..., flags: int = ..., parent: _win32typing.PyCWnd | None = ..., /
) -> _win32typing.PyCColorDialog: ...
def CreateControl(
    classId: str,
    windowName: str,
    style,
    rect: tuple[Incomplete, Incomplete, Incomplete, Incomplete],
    parent: _win32typing.PyCWnd,
    _id,
    bStorage,
    obPersist: Incomplete | None = ...,
    licKey: str | None = ...,
    /,
) -> _win32typing.PyCWnd: ...
def CreateControlBar() -> _win32typing.PyCControlBar: ...
def CreateCtrlView(doc: _win32typing.PyCDocument, className: str, style: int = ..., /) -> _win32typing.PyCCtrlView: ...
def CreateDC() -> None: ...
def CreateDCFromHandle(hwnd: int | _win32typing.PyHANDLE, /) -> _win32typing.PyCDC: ...
def CreateDialog(idRes, dll: _win32typing.PyDLL | None = ..., /) -> _win32typing.PyCDialog: ...
def CreateDialogBar() -> _win32typing.PyCDialogBar: ...
def CreateDialogIndirect(oblist, /) -> _win32typing.PyCDialog: ...
def CreatePrintDialog(
    idRes, bPrintSetupOnly, dwFlags, parent: _win32typing.PyCWnd | None = ..., dll: _win32typing.PyDLL | None = ..., /
) -> _win32typing.PyCPrintDialog: ...
def CreateDocTemplate(idRes, /) -> _win32typing.PyCDocTemplate: ...
def CreateEdit() -> _win32typing.PyCEdit: ...
def CreateFileDialog(
    bFileOpen,
    arg,
    defExt: str | None = ...,
    fileName: str | None = ...,
    _filter: str | None = ...,
    parent: _win32typing.PyCWnd | None = ...,
    /,
) -> _win32typing.PyCFileDialog: ...
def CreateFontDialog(
    arg, font: Incomplete | None = ..., dcPrinter: _win32typing.PyCDC | None = ..., parent: _win32typing.PyCWnd | None = ..., /
) -> _win32typing.PyCFontDialog: ...
def CreateFormView(doc: _win32typing.PyCDocument, Template, /) -> _win32typing.PyCFormView: ...
def CreateFrame(): ...
def CreateTreeCtrl() -> _win32typing.PyCTreeCtrl: ...
def CreateTreeView(doc: _win32typing.PyCDocument, /) -> _win32typing.PyCTreeView: ...
def CreatePalette(lp, /): ...
def CreatePopupMenu() -> _win32typing.PyCMenu: ...
def CreateMenu() -> _win32typing.PyCMenu: ...
def CreatePen(style, width, color, /): ...
def CreateProgressCtrl() -> _win32typing.PyCProgressCtrl: ...
def CreatePropertyPage(resource: _win32typing.PyResourceId, caption: int = ..., /) -> _win32typing.PyCPropertyPage: ...
def CreatePropertyPageIndirect(resourcelist: _win32typing.PyDialogTemplate, caption=..., /) -> _win32typing.PyCPropertyPage: ...
def CreatePropertySheet(
    caption: _win32typing.PyResourceId, parent: _win32typing.PyCWnd | None = ..., select=..., /
) -> _win32typing.PyCPropertySheet: ...
def CreateRgn() -> _win32typing.PyCRgn: ...
def CreateRichEditCtrl() -> _win32typing.PyCRichEditCtrl: ...
def CreateRichEditDocTemplate(idRes, /) -> _win32typing.PyCRichEditDocTemplate: ...
def CreateRichEditView(doc: _win32typing.PyCDocument | None = ..., /) -> _win32typing.PyCRichEditView: ...
def CreateSliderCtrl() -> _win32typing.PyCSliderCtrl: ...
def CreateSplitter() -> _win32typing.PyCSplitterWnd: ...
def CreateStatusBar(
    parent: _win32typing.PyCWnd, style: int = ..., windowId: int = ..., ctrlStype: int = ..., /
) -> _win32typing.PyCStatusBar: ...
def CreateStatusBarCtrl() -> _win32typing.PyCStatusBarCtrl: ...
def CreateFont(properties, /) -> _win32typing.PyCFont: ...
def CreateToolBar(parent: _win32typing.PyCWnd, style: int, windowId: int = ..., /) -> _win32typing.PyCToolBar: ...
def CreateToolBarCtrl() -> _win32typing.PyCToolBarCtrl: ...
def CreateToolTipCtrl() -> _win32typing.PyCToolTipCtrl: ...
def CreateThread() -> _win32typing.PyCWinThread: ...
def CreateView(doc: _win32typing.PyCDocument, /) -> _win32typing.PyCScrollView: ...
def CreateEditView(doc: _win32typing.PyCDocument, /) -> _win32typing.PyCEditView: ...
def CreateDebuggerThread() -> None: ...
def CreateWindowFromHandle(hwnd: int, /) -> _win32typing.PyCWnd: ...
def CreateWnd() -> _win32typing.PyCWnd: ...
def DestroyDebuggerThread() -> None: ...
def DoWaitCursor(code, /) -> None: ...
def DisplayTraceback(exc_info: OptExcInfo, title: str, /) -> None: ...
def Enable3dControls(): ...
def FindWindow(className: str, windowName: str, /) -> _win32typing.PyCWnd: ...
def FindWindowEx(
    parentWindow: _win32typing.PyCWnd, childAfter: _win32typing.PyCWnd, className: str, windowName: str, /
) -> _win32typing.PyCWnd: ...
def FullPath(path: str, /) -> str: ...
def GetActiveWindow() -> _win32typing.PyCWnd: ...
def GetApp() -> _win32typing.PyCWinApp: ...
def GetAppName(): ...
def GetAppRegistryKey() -> None: ...
def GetBytes(address, size, /) -> str: ...
def GetCommandLine() -> str: ...
def GetDeviceCaps(hdc, index, /): ...
def GetFileTitle(fileName: str, /) -> str: ...
def GetFocus() -> _win32typing.PyCWnd: ...
def GetForegroundWindow() -> _win32typing.PyCWnd: ...
def GetHalftoneBrush() -> _win32typing.PyCBrush: ...
def GetInitialStateRequest(): ...
def GetMainFrame() -> _win32typing.PyCWnd: ...
def GetName() -> str: ...
def GetProfileFileName() -> str: ...
def GetProfileVal(section: str, entry: str, defValue: str, /) -> str: ...
def GetResource() -> _win32typing.PyDLL: ...
def GetThread() -> _win32typing.PyCWinApp: ...
def GetType(): ...
def InitRichEdit() -> str: ...
def InstallCallbackCaller(caller: Callable[..., Incomplete] | None): ...
def IsDebug() -> int: ...
def IsWin32s() -> int: ...
def IsObject(o: object, /) -> bool: ...
def LoadDialogResource(idRes, dll: _win32typing.PyDLL | None = ..., /): ...
def LoadLibrary(fileName: str, /) -> _win32typing.PyDLL: ...
def LoadMenu(_id, dll: _win32typing.PyDLL | None = ..., /) -> _win32typing.PyCMenu: ...
def LoadStdProfileSettings(maxFiles: int = ..., /) -> None: ...
def LoadString(stringId, /) -> str: ...
def MessageBox(message: str, title: str | None = ..., style=..., /): ...
def OutputDebugString(msg: str, /) -> None: ...
def EnableControlContainer(): ...
def PrintTraceback(tb, output, /) -> None: ...
def PumpWaitingMessages(firstMessage: int = ..., lastMessage: int = ..., /) -> int: ...
def RegisterWndClass(style, hCursor: int = ..., hBrush: int = ..., hIcon=..., /) -> str: ...
def RemoveRecentFile(index: int = ..., /) -> None: ...
def SetAppHelpPath(): ...
def SetAppName(appName: str, /): ...
def SetCurrentInstanceHandle(newVal, /): ...
def SetCurrentResourceHandle(newVal, /): ...
def SetDialogBkColor(clrCtlBk: int = ..., clrCtlText: int = ..., /) -> None: ...
def SetProfileFileName(filename: str, /) -> None: ...
def SetRegistryKey(key: str, /) -> None: ...
def SetResource(dll, /) -> _win32typing.PyDLL: ...
def SetStatusText(msg: str, bForce: int = ..., /) -> None: ...
def StartDebuggerPump() -> None: ...
def StopDebuggerPump() -> None: ...
def TranslateMessage(): ...
def TranslateVirtualKey(vk, /) -> str: ...
def WinHelp(arg, data: str, /) -> None: ...
def WriteProfileVal(section: str, entry: str, value: str, /) -> None: ...
def AddToRecentFileList(*args): ...  # incomplete
def CreateImageList(*args): ...  # incomplete
def CreateListCtrl(*args): ...  # incomplete
def CreateListView(*args): ...  # incomplete
def CreateRectRgn(*args): ...  # incomplete
def GetRecentFileList(*args): ...  # incomplete
def OutputDebug(*args): ...  # incomplete

AFX_IDW_PANE_FIRST: int
AFX_IDW_PANE_LAST: int
AFX_WS_DEFAULT_VIEW: int
CDocTemplate_Confidence_maybeAttemptForeign: int
CDocTemplate_Confidence_maybeAttemptNative: int
CDocTemplate_Confidence_noAttempt: int
CDocTemplate_Confidence_yesAlreadyOpen: int
CDocTemplate_Confidence_yesAttemptForeign: int
CDocTemplate_Confidence_yesAttemptNative: int
CDocTemplate_docName: int
CDocTemplate_fileNewName: int
CDocTemplate_filterExt: int
CDocTemplate_filterName: int
CDocTemplate_regFileTypeId: int
CDocTemplate_regFileTypeName: int
CDocTemplate_windowTitle: int
CRichEditView_WrapNone: int
CRichEditView_WrapToTargetDevice: int
CRichEditView_WrapToWindow: int
debug: int
FWS_ADDTOTITLE: int
FWS_PREFIXTITLE: int
FWS_SNAPTOBARS: int
ID_APP_ABOUT: int
ID_APP_EXIT: int
ID_EDIT_CLEAR: int
ID_EDIT_CLEAR_ALL: int
ID_EDIT_COPY: int
ID_EDIT_CUT: int
ID_EDIT_FIND: int
ID_EDIT_GOTO_LINE: int
ID_EDIT_PASTE: int
ID_EDIT_REDO: int
ID_EDIT_REPEAT: int
ID_EDIT_REPLACE: int
ID_EDIT_SELECT_ALL: int
ID_EDIT_SELECT_BLOCK: int
ID_EDIT_UNDO: int
ID_FILE_CHECK: int
ID_FILE_CLOSE: int
ID_FILE_IMPORT: int
ID_FILE_LOCATE: int
ID_FILE_MRU_FILE1: int
ID_FILE_MRU_FILE2: int
ID_FILE_MRU_FILE3: int
ID_FILE_MRU_FILE4: int
ID_FILE_NEW: int
ID_FILE_OPEN: int
ID_FILE_PAGE_SETUP: int
ID_FILE_PRINT: int
ID_FILE_PRINT_PREVIEW: int
ID_FILE_PRINT_SETUP: int
ID_FILE_RUN: int
ID_FILE_SAVE: int
ID_FILE_SAVE_ALL: int
ID_FILE_SAVE_AS: int
ID_HELP_GUI_REF: int
ID_HELP_OTHER: int
ID_HELP_PYTHON: int
ID_INDICATOR_COLNUM: int
ID_INDICATOR_LINENUM: int
ID_NEXT_PANE: int
ID_PREV_PANE: int
ID_SEPARATOR: int
ID_VIEW_BROWSE: int
ID_VIEW_EOL: int
ID_VIEW_FIXED_FONT: int
ID_VIEW_FOLD_COLLAPSE: int
ID_VIEW_FOLD_COLLAPSE_ALL: int
ID_VIEW_FOLD_EXPAND: int
ID_VIEW_FOLD_EXPAND_ALL: int
ID_VIEW_INDENTATIONGUIDES: int
ID_VIEW_INTERACTIVE: int
ID_VIEW_OPTIONS: int
ID_VIEW_RIGHT_EDGE: int
ID_VIEW_STATUS_BAR: int
ID_VIEW_TOOLBAR: int
ID_VIEW_TOOLBAR_DBG: int
ID_VIEW_WHITESPACE: int
ID_WINDOW_ARRANGE: int
ID_WINDOW_CASCADE: int
ID_WINDOW_NEW: int
ID_WINDOW_SPLIT: int
ID_WINDOW_TILE_HORZ: int
ID_WINDOW_TILE_VERT: int
IDB_BROWSER_HIER: int
IDB_DEBUGGER_HIER: int
IDB_HIERFOLDERS: int
IDC_ABOUT_VERSION: int
IDC_AUTO_RELOAD: int
IDC_AUTOCOMPLETE: int
IDC_BUTTON1: int
IDC_BUTTON2: int
IDC_BUTTON3: int
IDC_BUTTON4: int
IDC_CALLTIPS: int
IDC_CHECK1: int
IDC_CHECK2: int
IDC_CHECK3: int
IDC_COMBO1: int
IDC_COMBO2: int
IDC_EDIT1: int
IDC_EDIT2: int
IDC_EDIT3: int
IDC_EDIT4: int
IDC_EDIT_TABS: int
IDC_INDENT_SIZE: int
IDC_KEYBOARD_CONFIG: int
IDC_PROMPT1: int
IDC_PROMPT2: int
IDC_PROMPT3: int
IDC_PROMPT4: int
IDC_PROMPT_TABS: int
IDC_RADIO1: int
IDC_RADIO2: int
IDC_RIGHTEDGE_COLUMN: int
IDC_RIGHTEDGE_DEFINE: int
IDC_RIGHTEDGE_ENABLE: int
IDC_RIGHTEDGE_SAMPLE: int
IDC_SPIN1: int
IDC_SPIN2: int
IDC_SPIN3: int
IDC_TAB_SIZE: int
IDC_USE_SMART_TABS: int
IDC_USE_TABS: int
IDC_VIEW_WHITESPACE: int
IDC_VSS_INTEGRATE: int
IDD_ABOUTBOX: int
IDD_DUMMYPROPPAGE: int
IDD_GENERAL_STATUS: int
IDD_LARGE_EDIT: int
IDD_PP_DEBUGGER: int
IDD_PP_EDITOR: int
IDD_PP_FORMAT: int
IDD_PP_IDE: int
IDD_PP_TABS: int
IDD_PP_TOOLMENU: int
IDD_PROPDEMO1: int
IDD_PROPDEMO2: int
IDD_RUN_SCRIPT: int
IDD_SET_TABSTOPS: int
IDD_SIMPLE_INPUT: int
IDD_TREE: int
IDD_TREE_MB: int
IDR_CNTR_INPLACE: int
IDR_DEBUGGER: int
IDR_MAINFRAME: int
IDR_PYTHONCONTYPE: int
IDR_PYTHONTYPE: int
IDR_PYTHONTYPE_CNTR_IP: int
IDR_TEXTTYPE: int
LM_COMMIT: int
LM_HORZ: int
LM_HORZDOCK: int
LM_LENGTHY: int
LM_MRUWIDTH: int
LM_STRETCH: int
LM_VERTDOCK: int
MFS_4THICKFRAME: int
MFS_BLOCKSYSMENU: int
MFS_MOVEFRAME: int
MFS_SYNCACTIVE: int
MFS_THICKFRAME: int
PD_ALLPAGES: int
PD_COLLATE: int
PD_DISABLEPRINTTOFILE: int
PD_ENABLEPRINTHOOK: int
PD_ENABLEPRINTTEMPLATE: int
PD_ENABLEPRINTTEMPLATEHANDLE: int
PD_ENABLESETUPHOOK: int
PD_ENABLESETUPTEMPLATE: int
PD_ENABLESETUPTEMPLATEHANDLE: int
PD_HIDEPRINTTOFILE: int
PD_NONETWORKBUTTON: int
PD_NOPAGENUMS: int
PD_NOSELECTION: int
PD_NOWARNING: int
PD_PAGENUMS: int
PD_PRINTSETUP: int
PD_PRINTTOFILE: int
PD_RETURNDC: int
PD_RETURNDEFAULT: int
PD_RETURNIC: int
PD_SELECTION: int
PD_SHOWHELP: int
PD_USEDEVMODECOPIES: int
PD_USEDEVMODECOPIESANDCOLLATE: int
PSWIZB_BACK: int
PSWIZB_DISABLEDFINISH: int
PSWIZB_FINISH: int
PSWIZB_NEXT: int
IDC_DBG_ADD: int
IDC_DBG_BREAKPOINTS: int
IDC_DBG_CLEAR: int
IDC_DBG_CLOSE: int
IDC_DBG_GO: int
IDC_DBG_STACK: int
IDC_DBG_STEP: int
IDC_DBG_STEPOUT: int
IDC_DBG_STEPOVER: int
IDC_DBG_WATCH: int
IDC_EDITOR_COLOR: int
IDC_FOLD_ENABLE: int
IDC_FOLD_ON_OPEN: int
IDC_FOLD_SHOW_LINES: int
IDC_LIST1: int
IDC_MARGIN_FOLD: int
IDC_MARGIN_LINENUMBER: int
IDC_MARGIN_MARKER: int
IDC_TABTIMMY_BG: int
IDC_TABTIMMY_IND: int
IDC_TABTIMMY_NONE: int
IDC_VIEW_EOL: int
IDC_VIEW_INDENTATIONGUIDES: int
ID_VIEW_FOLD_TOPLEVEL: int
UNICODE: int
copyright: str
dllhandle: int
types: dict[str, type]
