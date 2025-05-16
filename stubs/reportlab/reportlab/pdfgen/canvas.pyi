"""
The Canvas object is the primary interface for creating PDF files. See
doc/reportlab-userguide.pdf for copious examples.
"""

from _typeshed import Incomplete
from typing import IO, Literal

from reportlab.lib.colors import Color, _ConvertibleToColor
from reportlab.pdfgen.textobject import PDFTextObject, _PDFColorSetter

class ShowBoundaryValue:
    color: _ConvertibleToColor | None
    width: float
    dashArray: Incomplete
    def __init__(
        self,
        color: _ConvertibleToColor | None = (0, 0, 0),
        width: float = 0.1,
        dashArray: list[float] | tuple[float, ...] | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class Canvas(_PDFColorSetter):
    """
    This class is the programmer's interface to the PDF file format.  Methods
    are (or will be) provided here to do just about everything PDF can do.

    The underlying model to the canvas concept is that of a graphics state machine
    that at any given point in time has a current font, fill color (for figure
    interiors), stroke color (for figure borders), line width and geometric transform, among
    many other characteristics.

    Canvas methods generally either draw something (like canvas.line) using the
    current state of the canvas or change some component of the canvas
    state (like canvas.setFont).  The current state can be saved and restored
    using the saveState/restoreState methods.

    Objects are "painted" in the order they are drawn so if, for example
    two rectangles overlap the last draw will appear "on top".  PDF form
    objects (supported here) are used to draw complex drawings only once,
    for possible repeated use.

    There are other features of canvas which are not visible when printed,
    such as outlines and bookmarks which are used for navigating a document
    in a viewer.

    Here is a very silly example usage which generates a Hello World pdf document.

    Example:: 

       from reportlab.pdfgen import canvas
       c = canvas.Canvas("hello.pdf")
       from reportlab.lib.units import inch
       # move the origin up and to the left
       c.translate(inch,inch)
       # define a large font
       c.setFont("Helvetica", 80)
       # choose some colors
       c.setStrokeColorRGB(0.2,0.5,0.3)
       c.setFillColorRGB(1,0,1)
       # draw a rectangle
       c.rect(inch,inch,6*inch,9*inch, fill=1)
       # make text go straight up
       c.rotate(90)
       # change color
       c.setFillColorRGB(0,0,0.77)
       # say hello (note after rotate the y coord needs to be negative!)
       c.drawString(3*inch, -3*inch, "Hello World")
       c.showPage()
       c.save()
    """
    bottomup: int
    imageCaching: Incomplete
    state_stack: Incomplete
    def __init__(
        self,
        filename: str | IO[bytes],
        pagesize: tuple[float, float] | None = None,
        bottomup: int = 1,
        pageCompression=None,
        invariant=None,
        verbosity: int = 0,
        encrypt=None,
        cropMarks=None,
        pdfVersion=None,
        enforceColorSpace=None,
        initialFontName: float | None = None,
        initialFontSize: float | None = None,
        initialLeading: float | None = None,
        cropBox=None,
        artBox=None,
        trimBox=None,
        bleedBox=None,
        lang=None,
    ) -> None: ...
    def setEncrypt(self, encrypt) -> None: ...
    def init_graphics_state(self) -> None: ...
    def push_state_stack(self) -> None: ...
    def pop_state_stack(self) -> None: ...
    STATE_ATTRIBUTES: Incomplete
    STATE_RANGE: Incomplete
    def setAuthor(self, author: str | None) -> None: ...
    def setDateFormatter(self, dateFormatter) -> None: ...
    def addOutlineEntry(self, title, key, level: int = 0, closed=None) -> None: ...
    def setOutlineNames0(self, *nametree) -> None: ...
    def setTitle(self, title: str | None) -> None: ...
    def setSubject(self, subject: str | None) -> None: ...
    def setCreator(self, creator: str | None) -> None: ...
    def setProducer(self, producer: str | None) -> None: ...
    def setKeywords(self, keywords: str | None) -> None: ...
    def pageHasData(self): ...
    def showOutline(self) -> None: ...
    def showFullScreen0(self) -> None: ...
    def setBlendMode(self, v) -> None: ...
    def showPage(self) -> None: ...
    def setPageCallBack(self, func) -> None: ...
    def bookmarkPage(self, key, fit: str = "Fit", left=None, top=None, bottom=None, right=None, zoom=None): ...
    def bookmarkHorizontalAbsolute(self, key, top, left: int = 0, fit: str = "XYZ", **kw): ...
    def bookmarkHorizontal(self, key, relativeX, relativeY, **kw) -> None: ...
    def doForm(self, name) -> None: ...
    def hasForm(self, name): ...
    def drawInlineImage(
        self,
        image,
        x: float,
        y: float,
        width: float | None = None,
        height: float | None = None,
        preserveAspectRatio: bool = False,
        anchor: str = "c",
        anchorAtXY: bool = False,
        showBoundary: bool = False,
        extraReturn=None,
    ): ...
    def drawImage(
        self,
        image,
        x: float,
        y: float,
        width: float | None = None,
        height: float | None = None,
        mask=None,
        preserveAspectRatio: bool = False,
        anchor: str = "c",
        anchorAtXY: bool = False,
        showBoundary: bool = False,
        extraReturn=None,
    ): ...
    def beginForm(self, name, lowerx: int = 0, lowery: int = 0, upperx=None, uppery=None) -> None: ...
    def endForm(self, **extra_attributes) -> None: ...
    def addPostScriptCommand(self, command, position: int = 1) -> None: ...
    def freeTextAnnotation(self, contents, DA, Rect=None, addtopage: int = 1, name=None, relative: int = 0, **kw) -> None: ...
    def textAnnotation(self, contents, Rect=None, addtopage: int = 1, name=None, relative: int = 0, **kw) -> None: ...
    textAnnotation0 = textAnnotation
    def highlightAnnotation(
        self, contents, Rect, QuadPoints=None, Color=[0.83, 0.89, 0.95], addtopage: int = 1, name=None, relative: int = 0, **kw
    ) -> None: ...
    def inkAnnotation(
        self, contents, InkList=None, Rect=None, addtopage: int = 1, name=None, relative: int = 0, **kw
    ) -> None: ...
    inkAnnotation0 = inkAnnotation
    def linkAbsolute(
        self,
        contents,
        destinationname,
        Rect=None,
        addtopage: int = 1,
        name=None,
        thickness: int = 0,
        color: Color | None = None,
        dashArray=None,
        **kw,
    ):
        """
        rectangular link annotation positioned wrt the default user space.
        The identified rectangle on the page becomes a "hot link" which
        when clicked will send the viewer to the page and position identified
        by the destination.

        Rect identifies (lowerx, lowery, upperx, uppery) for lower left
        and upperright points of the rectangle.  Translations and other transforms
        are IGNORED (the rectangular position is given with respect
        to the default user space.
        destinationname should be the name of a bookmark (which may be defined later
        but must be defined before the document is generated).

        You may want to use the keyword argument Border='[0 0 0]' to
        suppress the visible rectangle around the during viewing link.
        """
        ...
    def linkRect(
        self,
        contents,
        destinationname,
        Rect=None,
        addtopage: int = 1,
        name=None,
        relative: int = 1,
        thickness: int = 0,
        color: Color | None = None,
        dashArray=None,
        **kw,
    ):
        """
        rectangular link annotation w.r.t the current user transform.
        if the transform is skewed/rotated the absolute rectangle will use the max/min x/y
        """
        ...
    def linkURL(
        self,
        url,
        rect,
        relative: int = 0,
        thickness: int = 0,
        color: Color | None = None,
        dashArray=None,
        kind: str = "URI",
        **kw,
    ) -> None:
        """
        Create a rectangular URL 'hotspot' in the given rectangle.

        if relative=1, this is in the current coord system, otherwise
        in absolute page space.
        The remaining options affect the border appearance; the border is
        drawn by Acrobat, not us.  Set thickness to zero to hide it.
        Any border drawn this way is NOT part of the page stream and
        will not show when printed to a Postscript printer or distilled;
        it is safest to draw your own.
        """
        ...
    def getPageNumber(self) -> int:
        """get the page number for the current page being generated."""
        ...
    def save(self) -> None:
        """
        Saves and close the PDF document in the file.
        If there is current data a ShowPage is executed automatically.
        After this operation the canvas must not be used further.
        """
        ...
    def getpdfdata(self):
        """
        Returns the PDF data that would normally be written to a file.
        If there is current data a ShowPage is executed automatically.
        After this operation the canvas must not be used further.
        """
        ...
    def setPageSize(self, size: tuple[float, float]) -> None:
        """
        accepts a 2-tuple in points for paper size for this
        and subsequent pages
        """
        ...
    def setCropBox(self, size, name: str = "crop") -> None:
        """accepts a 2-tuple in points for name+'Box' size for this and subsequent pages"""
        ...
    def setTrimBox(self, size) -> None: ...
    def setArtBox(self, size) -> None: ...
    def setBleedBox(self, size) -> None: ...
    # NOTE: Only accepts right angles
    def setPageRotation(self, rot: float) -> None:
        """Instruct display device that this page is to be rotated"""
        ...
    def addLiteral(self, s: object, escaped: int = 1) -> None:
        """
        introduce the literal text of PDF operations s into the current stream.
        Only use this if you are an expert in the PDF file format.
        """
        ...
    def resetTransforms(self) -> None:
        """
        I want to draw something (eg, string underlines) w.r.t. the default user space.
        Reset the matrix! This should be used usually as follows::

           canv.saveState()
           canv.resetTransforms()
           #...draw some stuff in default space coords...
           canv.restoreState() # go back!
        """
        ...
    def transform(self, a: float, b: float, c: float, d: float, e: float, f: float) -> None:
        """
        adjoin a mathematical transform to the current graphics state matrix.
        Not recommended for beginners.
        """
        ...
    def absolutePosition(self, x: float, y: float) -> tuple[float, float]:
        """return the absolute position of x,y in user space w.r.t. default user space"""
        ...
    def translate(self, dx: float, dy: float) -> None:
        """
        move the origin from the current (0,0) point to the (dx,dy) point
        (with respect to the current graphics state).
        """
        ...
    def scale(self, x: float, y: float) -> None:
        """
        Scale the horizontal dimension by x and the vertical by y
        (with respect to the current graphics state).
        For example canvas.scale(2.0, 0.5) will make everything short and fat.
        """
        ...
    def rotate(self, theta: float) -> None:
        """
        Canvas.rotate(theta)

        Rotate the canvas by the angle theta (in degrees).
        """
        ...
    def skew(self, alpha: float, beta: float) -> None: ...
    def saveState(self) -> None:
        """
        Save the current graphics state to be restored later by restoreState.

        For example:
            canvas.setFont("Helvetica", 20)
            canvas.saveState()
            ...
            canvas.setFont("Courier", 9)
            ...
            canvas.restoreState()
            # if the save/restore pairs match then font is Helvetica 20 again.
        """
        ...
    def restoreState(self) -> None:
        """restore the graphics state to the matching saved state (see saveState)."""
        ...
    def line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        draw a line segment from (x1,y1) to (x2,y2) (with color, thickness and
        other attributes determined by the current graphics state).
        """
        ...
    def lines(self, linelist) -> None:
        """
        Like line(), permits many lines to be drawn in one call.
        for example for the figure::

            |
          -- --
            |

          crosshairs = [(20,0,20,10), (20,30,20,40), (0,20,10,20), (30,20,40,20)]
          canvas.lines(crosshairs)
        """
        ...
    def cross(
        self,
        x: float,
        y: float,
        size: float = 5,
        gap: float = 1,
        text=None,
        strokeColor=None,
        strokeWidth: float | None = None,
        fontSize: float = 3,
    ) -> None: ...
    def grid(self, xlist, ylist) -> None:
        """
        Lays out a grid in current line style.  Supply list of
        x an y positions.
        """
        ...
    def bezier(self, x1, y1, x2, y2, x3, y3, x4, y4) -> None:
        """Bezier curve with the four given control points"""
        ...
    def arc(self, x1, y1, x2, y2, startAng: int = 0, extent: int = 90) -> None:
        """
        Draw a partial ellipse inscribed within the rectangle x1,y1,x2,y2,
        starting at startAng degrees and covering extent degrees.   Angles
        start with 0 to the right (+x) and increase counter-clockwise.
        These should have x1<x2 and y1<y2.
        """
        ...
    def rect(self, x, y, width, height, stroke: int = 1, fill: int = 0) -> None:
        """draws a rectangle with lower left corner at (x,y) and width and height as given."""
        ...
    def ellipse(self, x1, y1, x2, y2, stroke: int = 1, fill: int = 0) -> None:
        """
        Draw an ellipse defined by an enclosing rectangle.

        Note that (x1,y1) and (x2,y2) are the corner points of
        the enclosing rectangle.
        """
        ...
    def wedge(self, x1, y1, x2, y2, startAng, extent, stroke: int = 1, fill: int = 0) -> None:
        """
        Like arc, but connects to the centre of the ellipse.
        Most useful for pie charts and PacMan!
        """
        ...
    def circle(self, x_cen, y_cen, r, stroke: int = 1, fill: int = 0) -> None:
        """draw a cirle centered at (x_cen,y_cen) with radius r (special case of ellipse)"""
        ...
    def roundRect(self, x, y, width, height, radius, stroke: int = 1, fill: int = 0) -> None:
        """
        Draws a rectangle with rounded corners.  The corners are
        approximately quadrants of a circle, with the given radius.
        """
        ...
    def shade(self, shading) -> None: ...
    def linearGradient(self, x0, y0, x1, y1, colors, positions=None, extend: bool = True) -> None: ...
    def radialGradient(self, x, y, radius, colors, positions=None, extend: bool = True) -> None: ...
    def drawString(
        self,
        x: float,
        y: float,
        text: str,
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
        shaping: bool = False,
    ) -> None:
        """Draws a string in the current text styles."""
        ...
    def drawRightString(
        self,
        x: float,
        y: float,
        text: str,
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
        shaping: bool = False,
    ) -> None:
        """Draws a string right-aligned with the x coordinate"""
        ...
    def drawCentredString(
        self,
        x: float,
        y: float,
        text: str,
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
        shaping: bool = False,
    ) -> None:
        """
        Draws a string centred on the x coordinate. 

        We're British, dammit, and proud of our spelling!
        """
        ...
    def drawAlignedString(
        self,
        x: float,
        y: float,
        text: str,
        pivotChar: str = ".",
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
        shaping: bool = False,
    ) -> None:
        """
        Draws a string aligned on the first '.' (or other pivot character).

        The centre position of the pivot character will be used as x.
        So, you could draw a straight line down through all the decimals in a
        column of numbers, and anything without a decimal should be
        optically aligned with those that have.

        There is one special rule to help with accounting formatting.  Here's
        how normal numbers should be aligned on the 'dot'. Look at the
        LAST two::

           12,345,67
              987.15
               42
           -1,234.56
             (456.78)
             (456)
               27 inches
               13cm

        Since the last three do not contain a dot, a crude dot-finding
        rule would place them wrong. So we test for the special case
        where no pivot is found, digits are present, but the last character
        is not a digit.  We then work back from the end of the string
        This case is a tad slower but hopefully rare.
        """
        ...
    def getAvailableFonts(self):
        """
        Returns the list of PostScript font names available.

        Standard set now, but may grow in future with font embedding.
        """
        ...
    def listLoadedFonts0(self):
        """Convenience function to list all loaded fonts"""
        ...
    def setFont(self, psfontname: str, size: float, leading: float | None = None) -> None:
        """
        Sets the font.  If leading not specified, defaults to 1.2 x
        font size. Raises a readable exception if an illegal font
        is supplied.  Font names are case-sensitive! Keeps track
        of font name and size for metrics.
        """
        ...
    def setFontSize(self, size: float | None = None, leading: float | None = None) -> None:
        """Sets font size or leading without knowing the font face"""
        ...
    def stringWidth(self, text: str, fontName: str | None = None, fontSize: float | None = None) -> float:
        """gets width of a string in the given font and size"""
        ...
    def setLineWidth(self, width: float) -> None: ...
    def setLineCap(self, mode) -> None:
        """0=butt,1=round,2=square"""
        ...
    def setLineJoin(self, mode) -> None:
        """0=mitre, 1=round, 2=bevel"""
        ...
    def setMiterLimit(self, limit) -> None: ...
    def setDash(self, array: list[float] | tuple[float, ...] | float = [], phase: float = 0) -> None: ...
    def beginPath(self): ...
    def drawPath(self, aPath, stroke: int = 1, fill: int = 0, fillMode=None) -> None: ...
    def clipPath(self, aPath, stroke: int = 1, fill: int = 0, fillMode=None) -> None: ...
    def beginText(self, x: float = 0, y: float = 0, direction: Literal["LTR", "RTL"] | None = None) -> PDFTextObject: ...
    def drawText(self, aTextObject: PDFTextObject) -> None: ...
    def setPageCompression(self, pageCompression: int = 1) -> None: ...
    def setPageDuration(self, duration=None) -> None: ...
    def setPageTransition(
        self, effectname: str | None = None, duration: float = 1, direction: float = 0, dimension: str = "H", motion: str = "I"
    ) -> None:
        """
        PDF allows page transition effects for use when giving
        presentations.  There are six possible effects.  You can
        just guive the effect name, or supply more advanced options
        to refine the way it works.  There are three types of extra
        argument permitted, and here are the allowed values::

            direction_arg = [0,90,180,270]
            dimension_arg = ['H', 'V']
            motion_arg = ['I','O'] (start at inside or outside)

        This table says which ones take which arguments::

            PageTransitionEffects = {
                'Split': [direction_arg, motion_arg],
                'Blinds': [dimension_arg],
                'Box': [motion_arg],
                'Wipe' : [direction_arg],
                'Dissolve' : [],
                'Glitter':[direction_arg]
                }

        Have fun!
        """
        ...
    def getCurrentPageContent(self):
        """
        Return uncompressed contents of current page buffer.

        This is useful in creating test cases and assertions of what
        got drawn, without necessarily saving pages to disk
        """
        ...
    def setViewerPreference(self, pref, value) -> None:
        """set one of the allowed enbtries in the documents viewer preferences"""
        ...
    def getViewerPreference(self, pref):
        """you'll get an error here if none have been set"""
        ...
    def delViewerPreference(self, pref) -> None:
        """you'll get an error here if none have been set"""
        ...
    def setCatalogEntry(self, key, value) -> None: ...
    def getCatalogEntry(self, key): ...
    def delCatalogEntry(self, key) -> None: ...
    def addPageLabel(self, pageNum, style=None, start=None, prefix=None) -> None: ...
    @property
    def acroForm(self):
        """get form from canvas, create the form if needed"""
        ...
    def drawBoundary(self, sb, x1: float, y1: float, width: float, height: float) -> None:
        """draw a boundary as a rectangle (primarily for debugging)."""
        ...

__all__ = ["Canvas", "ShowBoundaryValue"]
