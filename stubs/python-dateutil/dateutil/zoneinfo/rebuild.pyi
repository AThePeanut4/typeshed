from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Sequence
from tarfile import TarInfo

def rebuild(
    filename: StrOrBytesPath,
    tag: Incomplete | None = None,
    format: str = "gz",
    zonegroups: Sequence[str | TarInfo] = [],
    metadata: Incomplete | None = None,
) -> None:
    """
    Rebuild the internal timezone info in dateutil/zoneinfo/zoneinfo*tar*

    filename is the timezone tarball from ``ftp.iana.org/tz``.
    """
    ...
