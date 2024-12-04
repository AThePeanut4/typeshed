from collections.abc import Iterator

from _cffi_backend import _CDataBase

from ._pygit2 import Oid, Signature

def wrap_signature(csig: _CDataBase) -> Signature: ...

class BlameHunk:
    @property
    def lines_in_hunk(self) -> int:
        """Number of lines"""
        ...
    @property
    def boundary(self) -> bool:
        """Tracked to a boundary commit"""
        ...
    @property
    def final_start_line_number(self) -> int:
        """Final start line number"""
        ...
    @property
    def final_committer(self) -> Signature:
        """Final committer"""
        ...
    @property
    def final_commit_id(self) -> Oid: ...
    @property
    def orig_start_line_number(self) -> int:
        """Origin start line number"""
        ...
    @property
    def orig_committer(self) -> Signature:
        """Original committer"""
        ...
    @property
    def orig_commit_id(self) -> Oid: ...
    @property
    def orig_path(self) -> str | None:
        """Original path"""
        ...

class Blame:
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> BlameHunk: ...
    def for_line(self, line_no: int) -> BlameHunk:
        """
        Returns the <BlameHunk> object for a given line given its number in the
        current Blame.

        Parameters:

        line_no
            Line number, starts at 1.
        """
        ...
    def __iter__(self) -> Iterator[BlameHunk]: ...
