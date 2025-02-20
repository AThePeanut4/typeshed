from collections.abc import Callable
from typing import IO, Any
from typing_extensions import TypeAlias

from ..main import ModulesType, QRCode
from .styles.moduledrawers.base import QRModuleDrawer

# The second element of the value tuple are keyword arguments used when
# constructing instances of the QRModuleDrawer type.
DrawerAliases: TypeAlias = dict[str, tuple[type[QRModuleDrawer], dict[str, Any]]]

class BaseImage:
    """Base QRCode image output class."""
    kind: str | None
    allowed_kinds: tuple[str] | None
    needs_context: bool
    needs_processing: bool
    needs_drawrect: bool
    border: int
    width: int
    box_size: int
    pixel_size: int
    modules: list[list[bool | None]]
    # the class accepts arbitrary additional positional arguments to accommodate
    # subclasses with additional arguments. kwargs are forwarded to the `new_image()` call.
    def __init__(
        self, border: int, width: int, box_size: int, *args: Any, qrcode_modules: ModulesType | None, **kwargs: Any
    ) -> None: ...
    def drawrect(self, row: int, col: int) -> None:
        """Draw a single rectangle of the QR code."""
        ...
    def drawrect_context(self, row: int, col: int, qr: QRCode[Any]) -> None:
        """Draw a single rectangle of the QR code given the surrounding context"""
        ...
    def process(self) -> None:
        """Processes QR code after completion"""
        ...
    def save(self, stream: IO[bytes], kind: str | None = None) -> None:
        """Save the image file."""
        ...
    def pixel_box(self, row: int, col: int) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        A helper method for pixel-based image generators that specifies the
        four pixel coordinates for a single rect.
        """
        ...
    # the new_image method accepts arbitrary keyword arguments to accommodate
    # subclasses with additional arguments.
    def new_image(self, **kwargs: Any) -> Any:
        """Build the image class. Subclasses should return the class created."""
        ...
    def init_new_image(self) -> None: ...
    # the get_image method accepts arbitrary keyword arguments to accommodate
    # subclasses with additional arguments.
    def get_image(self, **kwargs: Any) -> Any:
        """Return the image class for further processing."""
        ...
    def check_kind(self, kind: str | None, transform: Callable[[str | None], str | None] | None = None) -> str | None:
        """Get the image type."""
        ...
    def is_eye(self, row: int, col: int) -> bool:
        """Find whether the referenced module is in an eye."""
        ...

class BaseImageWithDrawer(BaseImage):
    default_drawer_class: type[QRModuleDrawer]
    drawer_aliases: DrawerAliases
    def get_default_module_drawer(self) -> QRModuleDrawer: ...
    def get_default_eye_drawer(self) -> QRModuleDrawer: ...
    needs_context: bool
    module_drawer: QRModuleDrawer
    eye_drawer: QRModuleDrawer
    # the class accepts arbitrary additional positional arguments to accommodate
    # subclasses with additional arguments. kwargs are forwarded to the `new_image()` call
    # via the BaseImage.__init__ method.
    def __init__(
        self,
        border: int,
        width: int,
        box_size: int,
        *args: Any,
        qrcode_modules: ModulesType | None,
        module_drawer: QRModuleDrawer | str | None = None,
        eye_drawer: QRModuleDrawer | str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def get_drawer(self, drawer: QRModuleDrawer | str | None) -> QRModuleDrawer | None: ...
    def init_new_image(self) -> None: ...
    def drawrect_context(self, row: int, col: int, qr: QRCode[Any]) -> None: ...
