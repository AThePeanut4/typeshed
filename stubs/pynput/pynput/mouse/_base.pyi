"""
This module contains the base implementation.

The actual interface to mouse classes is defined here, but the implementation
is located in a platform dependent module.
"""

import enum
import sys
from collections.abc import Callable
from types import TracebackType
from typing import Any
from typing_extensions import Self

from pynput._util import AbstractListener

class Button(enum.Enum):
    """
    The various buttons.

    The actual values for these items differ between platforms. Some
    platforms may have additional buttons, but these are guaranteed to be
    present everywhere.
    """
    unknown = 0
    left = 1
    middle = 2
    right = 3
    if sys.platform == "linux":
        button8 = 8
        button9 = 9
        button10 = 10
        button11 = 11
        button12 = 12
        button13 = 13
        button14 = 14
        button15 = 15
        button16 = 16
        button17 = 17
        button18 = 18
        button19 = 19
        button20 = 20
        button21 = 21
        button22 = 22
        button23 = 23
        button24 = 24
        button25 = 25
        button26 = 26
        button27 = 27
        button28 = 28
        button29 = 29
        button30 = 30
        scroll_down = 5
        scroll_left = 6
        scroll_right = 7
        scroll_up = 4
    if sys.platform == "win32":
        x1 = 0  # Value unknown
        x2 = 0  # Value unknown

class Controller:
    """
    A controller for sending virtual mouse events to the system.
    
    """
    def __init__(self) -> None: ...
    @property
    def position(self) -> tuple[int, int]:
        """
        The current position of the mouse pointer.

        This is the tuple ``(x, y)``, and setting it will move the pointer.
        """
        ...
    @position.setter
    def position(self, position: tuple[int, int]) -> None:
        """
        The current position of the mouse pointer.

        This is the tuple ``(x, y)``, and setting it will move the pointer.
        """
        ...
    def scroll(self, dx: int, dy: int) -> None:
        """
        Sends scroll events.

        :param int dx: The horizontal scroll. The units of scrolling is
            undefined.

        :param int dy: The vertical scroll. The units of scrolling is
            undefined.

        :raises ValueError: if the values are invalid, for example out of
            bounds
        """
        ...
    def press(self, button: Button) -> None:
        """
        Emits a button press event at the current position.

        :param Button button: The button to press.
        """
        ...
    def release(self, button: Button) -> None:
        """
        Emits a button release event at the current position.

        :param Button button: The button to release.
        """
        ...
    def move(self, dx: int, dy: int) -> None:
        """
        Moves the mouse pointer a number of pixels from its current
        position.

        :param int dx: The horizontal offset.

        :param int dy: The vertical offset.

        :raises ValueError: if the values are invalid, for example out of
            bounds
        """
        ...
    def click(self, button: Button, count: int = 1) -> None:
        """
        Emits a button click event at the current position.

        The default implementation sends a series of press and release events.

        :param Button button: The button to click.

        :param int count: The number of clicks to send.
        """
        ...
    def __enter__(self) -> Self:
        """
        Begins a series of clicks.

        In the default :meth:`click` implementation, the return value of this
        method is used for the calls to :meth:`press` and :meth:`release`
        instead of ``self``.

        The default implementation is a no-op.
        """
        ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        """
        Ends a series of clicks.
        
        """
        ...

class Listener(AbstractListener):
    """
    A listener for mouse events.

    Instances of this class can be used as context managers. This is equivalent
    to the following code::

        listener.start()
        try:
            listener.wait()
            with_statements()
        finally:
            listener.stop()

    This class inherits from :class:`threading.Thread` and supports all its
    methods. It will set :attr:`daemon` to ``True`` when created.

    :param callable on_move: The callback to call when mouse move events occur.

        It will be called with the arguments ``(x, y)``, which is the new
        pointer position. If this callback raises :class:`StopException` or
        returns ``False``, the listener is stopped.

    :param callable on_click: The callback to call when a mouse button is
        clicked.

        It will be called with the arguments ``(x, y, button, pressed)``,
        where ``(x, y)`` is the new pointer position, ``button`` is one of the
        :class:`Button` values and ``pressed`` is whether the button was
        pressed.

        If this callback raises :class:`StopException` or returns ``False``,
        the listener is stopped.

    :param callable on_scroll: The callback to call when mouse scroll
        events occur.

        It will be called with the arguments ``(x, y, dx, dy)``, where
        ``(x, y)`` is the new pointer position, and ``(dx, dy)`` is the scroll
        vector.

        If this callback raises :class:`StopException` or returns ``False``,
        the listener is stopped.

    :param bool suppress: Whether to suppress events. Setting this to ``True``
        will prevent the input events from being passed to the rest of the
        system.

    :param kwargs: Any non-standard platform dependent options. These should be
        prefixed with the platform name thus: ``darwin_``, ``xorg_`` or
        ``win32_``.

        Supported values are:

        ``darwin_intercept``
            A callable taking the arguments ``(event_type, event)``, where
            ``event_type`` is any mouse related event type constant, and
            ``event`` is a ``CGEventRef``.

            This callable can freely modify the event using functions like
            ``Quartz.CGEventSetIntegerValueField``. If this callable does not
            return the event, the event is suppressed system wide.

        ``win32_event_filter``
            A callable taking the arguments ``(msg, data)``, where ``msg`` is
            the current message, and ``data`` associated data as a
            `MSLLHOOKSTRUCT <https://docs.microsoft.com/en-gb/windows/win32/api/winuser/ns-winuser-msllhookstruct>`_.

            If this callback returns ``False``, the event will not
            be propagated to the listener callback.

            If ``self.suppress_event()`` is called, the event is suppressed
            system wide.
    """
    if sys.platform == "win32":
        WM_LBUTTONDOWN: int
        WM_LBUTTONUP: int
        WM_MBUTTONDOWN: int
        WM_MBUTTONUP: int
        WM_MOUSEMOVE: int
        WM_MOUSEWHEEL: int
        WM_MOUSEHWHEEL: int
        WM_RBUTTONDOWN: int
        WM_RBUTTONUP: int
        WM_XBUTTONDOWN: int
        WM_XBUTTONUP: int

        MK_XBUTTON1: int
        MK_XBUTTON2: int

        XBUTTON1: int
        XBUTTON2: int

        CLICK_BUTTONS: dict[int, tuple[Button, bool]]
        X_BUTTONS: dict[int, dict[int, tuple[Button, bool]]]
        SCROLL_BUTTONS: dict[int, tuple[int, int]]

    def __init__(
        self,
        on_move: Callable[[int, int], bool | None] | None = None,
        on_click: Callable[[int, int, Button, bool], bool | None] | None = None,
        on_scroll: Callable[[int, int, int, int], bool | None] | None = None,
        suppress: bool = False,
        **kwargs: Any,
    ) -> None: ...
