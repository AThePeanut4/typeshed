from .enums import PageMode

class ViewerPreferences:
    """Specifies the way the document shall be displayed on the screen"""
    hide_toolbar: bool
    hide_menubar: bool
    hide_window_u_i: bool
    fit_window: bool
    center_window: bool
    display_doc_title: bool
    def __init__(
        self,
        hide_toolbar: bool = False,
        hide_menubar: bool = False,
        hide_window_u_i: bool = False,
        fit_window: bool = False,
        center_window: bool = False,
        display_doc_title: bool = False,
        non_full_screen_page_mode: PageMode | str = ...,
    ) -> None: ...
    @property
    def non_full_screen_page_mode(self):
        """(`fpdf.enums.PageMode`) The document’s page mode, specifying how to display the document on exiting full-screen mode"""
        ...
    @non_full_screen_page_mode.setter
    def non_full_screen_page_mode(self, page_mode) -> None:
        """(`fpdf.enums.PageMode`) The document’s page mode, specifying how to display the document on exiting full-screen mode"""
        ...
    def serialize(self) -> str: ...
