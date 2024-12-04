from _cffi_backend import _CDataBase

class Refspec:
    """The constructor is for internal use only."""
    def __init__(self, owner: _CDataBase, ptr: _CDataBase) -> None: ...
    @property
    def src(self) -> str:
        """Source or lhs of the refspec"""
        ...
    @property
    def dst(self) -> str:
        """Destinaton or rhs of the refspec"""
        ...
    @property
    def force(self) -> bool:
        """Whether this refspeca llows non-fast-forward updates"""
        ...
    @property
    def string(self) -> str:
        """String which was used to create this refspec"""
        ...
    @property
    def direction(self) -> int:
        """Direction of this refspec (fetch or push)"""
        ...
    def src_matches(self, ref: str) -> bool:
        """
        Return True if the given string matches the source of this refspec,
        False otherwise.
        """
        ...
    def dst_matches(self, ref: str) -> bool:
        """
        Return True if the given string matches the destination of this
        refspec, False otherwise.
        """
        ...
    def transform(self, ref: str) -> str:
        """
        Transform a reference name according to this refspec from the lhs to
        the rhs. Return an string.
        """
        ...
    def rtransform(self, ref: str) -> str:
        """
        Transform a reference name according to this refspec from the lhs to
        the rhs. Return an string.
        """
        ...
