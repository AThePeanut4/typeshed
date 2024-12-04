from _typeshed import Incomplete

from reportlab.graphics.barcode.common import Barcode

class USPS_4State(Barcode):
    """
    USPS 4-State OneView (TM) barcode. All info from USPS-B-3200A
    
    """
    tops: Incomplete
    bottoms: Incomplete
    dimensions: Incomplete
    def __init__(self, value: str = "01234567094987654321", routing: str = "", **kwd) -> None: ...
    @staticmethod
    def scale(kind, D, s): ...
    @property
    def tracking(self): ...
    @tracking.setter
    def tracking(self, tracking) -> None: ...
    @property
    def routing(self): ...
    @routing.setter
    def routing(self, routing) -> None: ...
    @property
    def widthSize(self): ...
    @widthSize.setter
    def widthSize(self, value) -> None: ...
    @property
    def heightSize(self): ...
    @heightSize.setter
    def heightSize(self, value) -> None: ...
    @property
    def fontSize(self): ...
    @fontSize.setter
    def fontSize(self, value) -> None: ...
    @property
    def humanReadable(self): ...
    @humanReadable.setter
    def humanReadable(self, value) -> None: ...
    @property
    def binary(self):
        """
        convert the 4 state string values to binary
        >>> print(nhex(USPS_4State('01234567094987654321','').binary))
        0x1122103b5c2004b1
        >>> print(nhex(USPS_4State('01234567094987654321','01234').binary))
        0xd138a87bab5cf3804b1
        >>> print(nhex(USPS_4State('01234567094987654321','012345678').binary))
        0x202bdc097711204d21804b1
        >>> print(nhex(USPS_4State('01234567094987654321','01234567891').binary))
        0x16907b2a24abc16a2e5c004b1
        """
        ...
    @property
    def codewords(self):
        """
        convert binary value into codewords
        >>> print(USPS_4State('01234567094987654321','01234567891').codewords)
        (673, 787, 607, 1022, 861, 19, 816, 1294, 35, 602)
        """
        ...
    @property
    def table1(self): ...
    @property
    def table2(self): ...
    @property
    def characters(self):
        """
        convert own codewords to characters
        >>> print(' '.join(hex(c)[2:] for c in USPS_4State('01234567094987654321','01234567891').characters))
        dcb 85c 8e4 b06 6dd 1740 17c6 1200 123f 1b2b
        """
        ...
    @property
    def barcodes(self):
        """
        Get 4 state bar codes for current routing and tracking
        >>> print(USPS_4State('01234567094987654321','01234567891').barcodes)
        AADTFFDFTDADTAADAATFDTDDAAADDTDTTDAFADADDDTFFFDDTTTADFAAADFTDAADA
        """
        ...
    table4: Incomplete
    @property
    def horizontalClearZone(self): ...
    @property
    def verticalClearZone(self): ...
    @property
    def barWidth(self): ...
    @barWidth.setter
    def barWidth(self, value) -> None: ...
    @property
    def pitch(self): ...
    @pitch.setter
    def pitch(self, value) -> None: ...
    @property
    def barHeight(self): ...
    @barHeight.setter
    def barHeight(self, value) -> None: ...
    @property
    def widthScale(self): ...
    @property
    def heightScale(self): ...
    @property
    def width(self): ...
    @width.setter
    def width(self, v) -> None: ...
    @property
    def height(self): ...
    @height.setter
    def height(self, v) -> None: ...
    def computeSize(self) -> None: ...
    def wrap(self, aW, aH): ...
    def draw(self) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def drawHumanReadable(self) -> None: ...
    def annotate(self, x, y, text, fontName, fontSize, anchor: str = "middle") -> None: ...
