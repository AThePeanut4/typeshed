"""A module, encapsulating the Win32 help API's."""

import _win32typing

def WinHelp(hwnd: int, hlpFile: str, cmd, data: str | None = ..., /) -> None: ...
def HH_AKLINK() -> _win32typing.PyHH_AKLINK: ...
def HH_FTS_QUERY() -> _win32typing.PyHH_FTS_QUERY: ...
def HH_POPUP() -> _win32typing.PyHH_POPUP: ...
def HH_WINTYPE() -> _win32typing.PyHH_WINTYPE: ...
def NMHDR() -> _win32typing.PyNMHDR: ...
def HHN_NOTIFY() -> _win32typing.PyHHN_NOTIFY: ...
def HHNTRACK() -> _win32typing.PyHHNTRACK: ...
def HtmlHelp(hwnd: int, file: str, cmd, data: str | tuple[int] | int = ..., /): ...

debug: int
HH_ALINK_LOOKUP: int
HH_CLOSE_ALL: int
HH_DISPLAY_INDEX: int
HH_DISPLAY_SEARCH: int
HH_DISPLAY_TEXT_POPUP: int
HH_DISPLAY_TOC: int
HH_DISPLAY_TOPIC: int
HH_ENUM_CATEGORY: int
HH_ENUM_CATEGORY_IT: int
HH_ENUM_INFO_TYPE: int
HH_FTS_DEFAULT_PROXIMITY: int
HH_GET_LAST_ERROR: int
HH_GET_WIN_HANDLE: int
HH_GET_WIN_TYPE: int
HH_GPROPID_CONTENT_LANGUAGE: int
HH_GPROPID_CURRENT_SUBSET: int
HH_GPROPID_SINGLETHREAD: int
HH_GPROPID_TOOLBAR_MARGIN: int
HH_GPROPID_UI_LANGUAGE: int
HH_HELP_CONTEXT: int
HH_HELP_FINDER: int
HH_INITIALIZE: int
HH_KEYWORD_LOOKUP: int
HH_MAX_TABS_CUSTOM: int
HH_PRETRANSLATEMESSAGE: int
HH_RESERVED1: int
HH_RESERVED2: int
HH_RESERVED3: int
HH_RESET_IT_FILTER: int
HH_SET_EXCLUSIVE_FILTER: int
HH_SET_GLOBAL_PROPERTY: int
HH_SET_INCLUSIVE_FILTER: int
HH_SET_INFO_TYPE: int
HH_SET_WIN_TYPE: int
HH_SYNC: int
HH_TAB_AUTHOR: int
HH_TAB_CONTENTS: int
HH_TAB_CUSTOM_FIRST: int
HH_TAB_CUSTOM_LAST: int
HH_TAB_FAVORITES: int
HH_TAB_HISTORY: int
HH_TAB_INDEX: int
HH_TAB_SEARCH: int
HH_TP_HELP_CONTEXTMENU: int
HH_TP_HELP_WM_HELP: int
HH_UNINITIALIZE: int
HHACT_BACK: int
HHACT_CONTRACT: int
HHACT_CUSTOMIZE: int
HHACT_EXPAND: int
HHACT_FORWARD: int
HHACT_HIGHLIGHT: int
HHACT_HOME: int
HHACT_JUMP1: int
HHACT_JUMP2: int
HHACT_LAST_ENUM: int
HHACT_NOTES: int
HHACT_OPTIONS: int
HHACT_PRINT: int
HHACT_REFRESH: int
HHACT_STOP: int
HHACT_SYNC: int
HHACT_TAB_CONTENTS: int
HHACT_TAB_FAVORITES: int
HHACT_TAB_HISTORY: int
HHACT_TAB_INDEX: int
HHACT_TAB_SEARCH: int
HHACT_TOC_NEXT: int
HHACT_TOC_PREV: int
HHACT_ZOOM: int
HHN_FIRST: int
HHN_LAST: int
HHN_NAVCOMPLETE: int
HHN_TRACK: int
HHN_WINDOW_CREATE: int
HHWIN_BUTTON_BACK: int
HHWIN_BUTTON_BROWSE_BCK: int
HHWIN_BUTTON_BROWSE_FWD: int
HHWIN_BUTTON_CONTENTS: int
HHWIN_BUTTON_EXPAND: int
HHWIN_BUTTON_FAVORITES: int
HHWIN_BUTTON_FORWARD: int
HHWIN_BUTTON_HISTORY: int
HHWIN_BUTTON_HOME: int
HHWIN_BUTTON_INDEX: int
HHWIN_BUTTON_JUMP1: int
HHWIN_BUTTON_JUMP2: int
HHWIN_BUTTON_NOTES: int
HHWIN_BUTTON_OPTIONS: int
HHWIN_BUTTON_PRINT: int
HHWIN_BUTTON_REFRESH: int
HHWIN_BUTTON_SEARCH: int
HHWIN_BUTTON_STOP: int
HHWIN_BUTTON_SYNC: int
HHWIN_BUTTON_TOC_NEXT: int
HHWIN_BUTTON_TOC_PREV: int
HHWIN_BUTTON_ZOOM: int
HHWIN_DEF_BUTTONS: int
HHWIN_NAVTAB_BOTTOM: int
HHWIN_NAVTAB_LEFT: int
HHWIN_NAVTAB_TOP: int
HHWIN_PARAM_CUR_TAB: int
HHWIN_PARAM_EXPANSION: int
HHWIN_PARAM_EXSTYLES: int
HHWIN_PARAM_HISTORY_COUNT: int
HHWIN_PARAM_INFOTYPES: int
HHWIN_PARAM_NAV_WIDTH: int
HHWIN_PARAM_PROPERTIES: int
HHWIN_PARAM_RECT: int
HHWIN_PARAM_SHOWSTATE: int
HHWIN_PARAM_STYLES: int
HHWIN_PARAM_TABORDER: int
HHWIN_PARAM_TABPOS: int
HHWIN_PARAM_TB_FLAGS: int
HHWIN_PROP_AUTO_SYNC: int
HHWIN_PROP_CHANGE_TITLE: int
HHWIN_PROP_MENU: int
HHWIN_PROP_NAV_ONLY_WIN: int
HHWIN_PROP_NO_TOOLBAR: int
HHWIN_PROP_NODEF_EXSTYLES: int
HHWIN_PROP_NODEF_STYLES: int
HHWIN_PROP_NOTB_TEXT: int
HHWIN_PROP_NOTITLEBAR: int
HHWIN_PROP_ONTOP: int
HHWIN_PROP_POST_QUIT: int
HHWIN_PROP_TAB_ADVSEARCH: int
HHWIN_PROP_TAB_AUTOHIDESHOW: int
HHWIN_PROP_TAB_CUSTOM1: int
HHWIN_PROP_TAB_CUSTOM2: int
HHWIN_PROP_TAB_CUSTOM3: int
HHWIN_PROP_TAB_CUSTOM4: int
HHWIN_PROP_TAB_CUSTOM5: int
HHWIN_PROP_TAB_CUSTOM6: int
HHWIN_PROP_TAB_CUSTOM7: int
HHWIN_PROP_TAB_CUSTOM8: int
HHWIN_PROP_TAB_CUSTOM9: int
HHWIN_PROP_TAB_FAVORITES: int
HHWIN_PROP_TAB_HISTORY: int
HHWIN_PROP_TAB_SEARCH: int
HHWIN_PROP_TRACKING: int
HHWIN_PROP_TRI_PANE: int
HHWIN_PROP_USER_POS: int
HHWIN_TB_MARGIN: int
IDTB_BACK: int
IDTB_BROWSE_BACK: int
IDTB_BROWSE_FWD: int
IDTB_CONTENTS: int
IDTB_CONTRACT: int
IDTB_CUSTOMIZE: int
IDTB_EXPAND: int
IDTB_FAVORITES: int
IDTB_FORWARD: int
IDTB_HISTORY: int
IDTB_HOME: int
IDTB_INDEX: int
IDTB_JUMP1: int
IDTB_JUMP2: int
IDTB_NOTES: int
IDTB_OPTIONS: int
IDTB_PRINT: int
IDTB_REFRESH: int
IDTB_SEARCH: int
IDTB_STOP: int
IDTB_SYNC: int
IDTB_TOC_NEXT: int
IDTB_TOC_PREV: int
IDTB_ZOOM: int
