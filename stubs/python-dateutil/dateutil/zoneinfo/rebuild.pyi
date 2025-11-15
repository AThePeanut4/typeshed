from _typeshed import StrOrBytesPath
from collections.abc import Iterable

from ..zoneinfo import _MetadataType

def rebuild(
    filename: StrOrBytesPath, tag=None, format: str = "gz", zonegroups: Iterable[str] = [], metadata: _MetadataType | None = None
) -> None:
    """
    Rebuild the internal timezone info in dateutil/zoneinfo/zoneinfo*tar*

    filename is the timezone tarball from ``ftp.iana.org/tz``.
    """
    ...
