"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""

import _tkinter
from _typeshed import StrPath
from typing import ClassVar

class ThemedWidget:
    """
    Provides functions to manipulate themes in order to reduce code
    duplication in the ThemedTk and ThemedStyle classes.
    """
    pixmap_themes: ClassVar[list[str]]
    PACKAGES: ClassVar[dict[str, str]]
    tk: _tkinter.TkappType
    png_support: bool
    def __init__(self, tk_interpreter: _tkinter.TkappType, gif_override: bool = False) -> None: ...
    def set_theme(self, theme_name: str) -> None: ...
    def get_themes(self) -> list[str]: ...
    @property
    def themes(self) -> list[str]:
        """Property alias of get_themes()"""
        ...
    @property
    def current_theme(self) -> str:
        """Property to get the currently enabled theme"""
        ...
    def set_theme_advanced(
        self,
        theme_name: str,
        brightness: float = 1.0,
        saturation: float = 1.0,
        hue: float = 1.0,
        preserve_transparency: bool = True,
        output_dir: StrPath | None = None,
        advanced_name: str = "advanced",
    ) -> None:
        """
        Load an advanced theme that is dynamically created

        Applies the given modifiers to the images of the theme given and
        then creates a theme from these new images with the name
        'advanced' and then applies this theme. Is not available without
        support for PNG-based themes, then raises RuntimeError.
        """
        ...
