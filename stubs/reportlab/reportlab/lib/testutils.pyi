import re
import unittest
from _typeshed import Incomplete, StrPath, Unused
from configparser import ConfigParser, _SectionName
from types import ModuleType
from typing import Final, Literal

__version__: Final[str]

def invariantSeed(n: float | str | bytes | bytearray | None) -> None: ...
def haveRenderPM() -> ModuleType | Literal[False]: ...

DEJAVUSANS: Final = ("DejaVuSans", "DejaVuSans-Bold", "DejaVuSans-Oblique", "DejaVuSans-BoldOblique")

def haveDejaVu() -> bool: ...
def isWritable(D: Unused) -> Literal[0, 1]: ...

RL_HOME: str | None
testsFolder: str | None

def setOutDir(name: str) -> str: ...
def mockUrlRead(name: str): ...
def outputfile(fn: StrPath | None) -> str: ...
def printLocation(depth: int = 1) -> None: ...
def makeSuiteForClasses(*classes: type[unittest.TestCase], testMethodPrefix: str | None = None) -> unittest.TestSuite: ...
def getCVSEntries(folder: StrPath, files: bool | Literal[1, 0] = 1, folders: bool | Literal[1, 0] = 0) -> list[str]: ...

class ExtConfigParser(ConfigParser):
    pat: re.Pattern[str]
    def getstringlist(self, section: _SectionName, option: str): ...

class GlobDirectoryWalker:
    """A forward iterator that traverses files in a directory tree."""
    index: int
    pattern: str
    stack: list[str]
    files: list[str]
    directory: str
    def __init__(self, directory: str, pattern: str = "*") -> None: ...
    def __getitem__(self, index) -> str | None: ...
    def filterFiles(self, folder, files): ...

class RestrictedGlobDirectoryWalker(GlobDirectoryWalker):
    """An restricted directory tree iterator."""
    ignorePatterns: Incomplete
    def __init__(self, directory, pattern: str = "*", ignore=None) -> None: ...
    def filterFiles(self, folder, files):
        """Filters all items from files matching patterns to ignore."""
        ...

class CVSGlobDirectoryWalker(GlobDirectoryWalker):
    """An directory tree iterator that checks for CVS data."""
    def filterFiles(self, folder, files):
        """
        Filters files not listed in CVS subfolder.

        This will look in the CVS subfolder of 'folder' for
        a file named 'Entries' and filter all elements from
        the 'files' list that are not listed in 'Entries'.
        """
        ...

class SecureTestCase(unittest.TestCase):
    """
    Secure testing base class with additional pre- and postconditions.

    We try to ensure that each test leaves the environment it has
    found unchanged after the test is performed, successful or not.

    Currently we restore sys.path and the working directory, but more
    of this could be added easily, like removing temporary files or
    similar things.

    Use this as a base class replacing unittest.TestCase and call
    these methods in subclassed versions before doing your own
    business!
    """
    def setUp(self) -> None:
        """Remember sys.path and current working directory."""
        ...
    def tearDown(self) -> None:
        """Restore previous sys.path and working directory."""
        ...

class NearTestCase(unittest.TestCase):
    @staticmethod
    def assertNear(a, b, accuracy: float = 1e-05) -> None: ...

class ScriptThatMakesFileTest(unittest.TestCase):
    """
    Runs a Python script at OS level, expecting it to produce a file.

    It CDs to the working directory to run the script.
    """
    scriptDir: Incomplete
    scriptName: Incomplete
    outFileName: Incomplete
    verbose: Incomplete
    def __init__(self, scriptDir, scriptName, outFileName, verbose: int = 0) -> None: ...
    cwd: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def runTest(self) -> None: ...

def equalStrings(a: str | bytes, b: str | bytes, enc: str = "utf8") -> bool: ...
def eqCheck(r, x) -> None: ...
def rlextraNeeded() -> bool: ...
def rlSkipIf(cond, reason, __module__=None): ...
def rlSkipUnless(cond, reason, __module__=None): ...
def rlSkip(reason, __module__=None): ...
