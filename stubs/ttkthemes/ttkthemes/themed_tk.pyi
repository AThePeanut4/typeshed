"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""

import tkinter
from collections.abc import Callable
from typing import Any, Literal

from ._widget import ThemedWidget

class ThemedTk(tkinter.Tk, ThemedWidget):
    """
    Tk child class that supports the themes supplied in this package

    A theme can be set upon initialization or during runtime. Can be
    used as a drop-in replacement for the normal Tk class. Additional
    options:

    - Initial theme ``theme``:
      Sets the initial theme to the theme specified. If the theme is
      not available, fails silently (there is no indication that the
      theme is not set other than it not appearing to the user).

    - Toplevel background color ``toplevel``:
      Hooks into the Toplevel.__init__ function to set a default window
      background color in the options passed. The hook is not removed
      after the window is destroyed, which is by design because creating
      multiple Tk instances should not be done in the first place.

    - Tk background color ``themebg``:
      Set the default background color of a Tk window to the default
      theme background color. For example: The background of windows
      may take on a dark color for dark themes. Backwards-compatible
      with the ``background`` keyword argument of v2.3.0 and earlier.

    - GIF theme override ``gif_override``:
      Forces ttkthemes to load the GIF version of themes that also
      provide a PNG version even if the PNG version can be loaded. Can
      only be set at object initialization. GIF themes may provide a
      higher UI performance than other themes.
    """
    def __init__(
        self,
        # non-keyword-only args copied from tkinter.Tk
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
        theme: str | None = None,
        # fonts argument does nothing
        toplevel: bool | None = None,
        themebg: bool | None = None,
        background: bool | None = None,  # old alias for themebg
        gif_override: bool = False,
    ) -> None:
        """
        :param theme: Theme to set upon initialization. If theme is not
            available, fails silently.
        :param toplevel: Control Toplevel background color option,
            see class documentation for details.
        :param themebg: Control Tk background color option, see
            class documentation for details.
        """
        ...
    def set_theme(self, theme_name: str, toplevel: bool | None = None, themebg: bool | None = None) -> None:
        """Redirect the set_theme call to also set Tk background color"""
        ...
    # Keep this in sync with tkinter.Tk
    def config(  # type: ignore[override]
        self,
        kw: dict[str, Any] | None = None,
        *,
        themebg: bool | None = ...,
        toplevel: bool | None = ...,
        theme: str | None = ...,
        background: str = ...,
        bd: float | str = ...,
        bg: str = ...,
        border: float | str = ...,
        borderwidth: float | str = ...,
        cursor: tkinter._Cursor = ...,
        height: float | str = ...,
        highlightbackground: str = ...,
        highlightcolor: str = ...,
        highlightthickness: float | str = ...,
        menu: tkinter.Menu = ...,
        padx: float | str = ...,
        pady: float | str = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        takefocus: bool | Literal[0, 1, ""] | Callable[[str], bool | None] = ...,
        width: float | str = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None:
        """configure redirect to support additional options"""
        ...
    def cget(self, k: str) -> Any:
        """cget redirect to support additional options"""
        ...
    def configure(  # type: ignore[override]
        self,
        kw: dict[str, Any] | None = None,
        *,
        themebg: bool | None = ...,
        toplevel: bool | None = ...,
        theme: str | None = ...,
        background: str = ...,
        bd: float | str = ...,
        bg: str = ...,
        border: float | str = ...,
        borderwidth: float | str = ...,
        cursor: tkinter._Cursor = ...,
        height: float | str = ...,
        highlightbackground: str = ...,
        highlightcolor: str = ...,
        highlightthickness: float | str = ...,
        menu: tkinter.Menu = ...,
        padx: float | str = ...,
        pady: float | str = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        takefocus: bool | Literal[0, 1, ""] | Callable[[str], bool | None] = ...,
        width: float | str = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    def __getitem__(self, k: str) -> Any: ...
    def __setitem__(self, k: str, v: Any) -> None: ...
