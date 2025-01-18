"""
This module contains the serialization logic that produces a PDF document from a FPDF instance.
Most of the code in this module is used when FPDF.output() is called.

The contents of this module are internal to fpdf2, and not part of the public API.
They may change at any time without prior warning or any deprecation period,
in non-backward-compatible ways.
"""

from _typeshed import Incomplete, Unused
from collections import defaultdict
from logging import Logger
from typing import Final

from .annotations import AnnotationDict
from .encryption import StandardSecurityHandler
from .enums import PageLabelStyle
from .fpdf import FPDF
from .image_datastructures import RasterImageInfo
from .line_break import TotalPagesSubstitutionFragment
from .syntax import Name, PDFArray, PDFContentStream, PDFObject, PDFString

LOGGER: Logger
ZOOM_CONFIGS: Final[dict[str, tuple[str, ...]]]

class ContentWithoutID:
    def serialize(self, _security_handler: StandardSecurityHandler | None = None) -> str | None: ...

class PDFHeader(ContentWithoutID):
    pdf_version: str
    def __init__(self, pdf_version: str) -> None: ...
    def serialize(self, _security_handler: StandardSecurityHandler | None = None) -> str: ...

class PDFFont(PDFObject):
    type: Name
    subtype: Name
    base_font: Name
    encoding: Name | None
    d_w: Incomplete | None
    w: Incomplete | None
    descendant_fonts: Incomplete | None
    to_unicode: Incomplete | None
    c_i_d_system_info: Incomplete | None
    font_descriptor: Incomplete | None
    c_i_d_to_g_i_d_map: Incomplete | None
    def __init__(
        self,
        subtype: str,
        base_font: str,
        encoding: str | None = None,
        d_w: Incomplete | None = None,
        w: Incomplete | None = None,
    ) -> None: ...

class CIDSystemInfo(PDFObject):
    registry: PDFString
    ordering: PDFString
    supplement: int

class PDFInfo(PDFObject):
    title: str | None
    subject: str | None
    author: str | None
    keywords: str | None
    creator: str | None
    producer: str | None
    creation_date: Incomplete
    def __init__(
        self,
        title: str | None,
        subject: str | None,
        author: str | None,
        keywords: str | None,
        creator: str | None,
        producer: str | None,
        creation_date,
    ) -> None: ...

class AcroForm:
    fields: Incomplete
    sig_flags: Incomplete
    def __init__(self, fields, sig_flags) -> None: ...
    def serialize(self) -> str: ...

class PDFCatalog(PDFObject):
    type: Name
    lang: str | None
    page_layout: Incomplete | None
    page_mode: Incomplete | None
    viewer_preferences: Incomplete | None
    pages: Incomplete | None
    acro_form: Incomplete | None
    open_action: Incomplete | None
    mark_info: Incomplete | None
    metadata: Incomplete | None
    names: Incomplete | None
    outlines: Incomplete | None
    struct_tree_root: Incomplete | None
    def __init__(
        self,
        lang: str | None = None,
        page_layout: Incomplete | None = None,
        page_mode: Incomplete | None = None,
        viewer_preferences: Incomplete | None = None,
    ) -> None: ...

class PDFResources(PDFObject):
    proc_set: Incomplete
    font: Incomplete
    x_object: Incomplete
    ext_g_state: Incomplete
    def __init__(self, proc_set, font, x_object, ext_g_state) -> None: ...

class PDFFontStream(PDFContentStream):
    length1: int
    def __init__(self, contents: bytes) -> None: ...

class PDFXmpMetadata(PDFContentStream):
    type: Name
    subtype: Name
    def __init__(self, contents: bytes) -> None: ...

class PDFXObject(PDFContentStream):
    type: Name
    subtype: Name
    width: Incomplete
    height: Incomplete
    color_space: Incomplete
    bits_per_component: Incomplete
    filter: Name
    decode: Incomplete | None
    decode_parms: Incomplete | None
    s_mask: Incomplete | None
    def __init__(
        self,
        contents,
        subtype: str,
        width,
        height,
        color_space,
        bits_per_component,
        img_filter: str | None = None,
        decode: Incomplete | None = None,
        decode_parms: Incomplete | None = None,
    ) -> None: ...

class PDFICCPObject(PDFContentStream):
    n: Incomplete
    alternate: Name
    def __init__(self, contents: bytes, n, alternate: str) -> None: ...

class PDFPageLabel:
    st: int
    def __init__(self, label_style: PageLabelStyle, label_prefix: str, label_start: int) -> None: ...
    @property
    def s(self) -> Name: ...
    @property
    def p(self) -> PDFString: ...
    def serialize(self) -> dict[str, str]: ...
    def get_style(self) -> PageLabelStyle: ...
    def get_prefix(self) -> str: ...
    def get_start(self) -> int: ...

class PDFPage(PDFObject):
    type: Name
    contents: Incomplete
    dur: Incomplete | None
    trans: Incomplete
    annots: PDFArray[AnnotationDict]
    group: Incomplete | None
    media_box: Incomplete | None
    struct_parents: Incomplete | None
    resources: Incomplete | None
    parent: Incomplete | None
    def __init__(self, duration: Incomplete | None, transition, contents, index) -> None: ...
    def index(self): ...
    def dimensions(self) -> tuple[float | None, float | None]:
        """Return a pair (width, height) in the unit specified to FPDF constructor"""
        ...
    def set_dimensions(self, width_pt: float | None, height_pt: float | None) -> None:
        """Accepts a pair (width, height) in the unit specified to FPDF constructor"""
        ...
    def set_page_label(self, previous_page_label: PDFPageLabel, page_label: PDFPageLabel) -> None: ...
    def get_page_label(self) -> PDFPageLabel: ...
    def get_label(self) -> str: ...
    def get_text_substitutions(self) -> list[TotalPagesSubstitutionFragment]: ...
    def add_text_substitution(self, fragment: TotalPagesSubstitutionFragment) -> None: ...

class PDFPagesRoot(PDFObject):
    type: Name
    count: Incomplete
    media_box: Incomplete
    kids: Incomplete | None
    def __init__(self, count, media_box) -> None: ...

class PDFExtGState(PDFObject):
    def __init__(self, dict_as_str) -> None: ...
    def serialize(self, obj_dict: Unused = None, _security_handler: StandardSecurityHandler | None = None) -> str: ...

class PDFXrefAndTrailer(ContentWithoutID):
    output_builder: Incomplete
    count: int
    catalog_obj: Incomplete | None
    info_obj: Incomplete | None
    def __init__(self, output_builder) -> None: ...
    def serialize(self, _security_handler: StandardSecurityHandler | None = None) -> str: ...

class OutputProducer:
    """Generates the final bytearray representing the PDF document, based on a FPDF instance."""
    fpdf: FPDF
    pdf_objs: list[Incomplete]
    obj_id: int
    offsets: dict[Incomplete, Incomplete]
    trace_labels_per_obj_id: dict[Incomplete, Incomplete]
    sections_size_per_trace_label: defaultdict[Incomplete, int]
    buffer: bytearray
    def __init__(self, fpdf: FPDF) -> None: ...
    def bufferize(self) -> bytearray:
        """
        This method alters the target FPDF instance
        by assigning IDs to all PDF objects,
        plus a few other properties on PDFPage instances
        """
        ...

def stream_content_for_raster_image(
    info: RasterImageInfo,
    x: float,
    y: float,
    w: float,
    h: float,
    keep_aspect_ratio: bool = False,
    scale: float = 1,
    pdf_height_to_flip: float | None = None,
) -> str: ...
