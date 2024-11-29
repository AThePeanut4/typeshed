"""
Manages the cache of generated Python code.

Description
  This file manages the cache of generated Python code.  When run from the
  command line, it also provides a number of options for managing that cache.

Implementation
  Each typelib is generated into a filename of format "{guid}x{lcid}x{major}x{minor}.py"

  An external persistant dictionary maps from all known IIDs in all known type libraries
  to the type library itself.

  Thus, whenever Python code knows the IID of an object, it can find the IID, LCID and version of
  the type library which supports it.  Given this information, it can find the Python module
  with the support.

  If necessary, this support can be generated on the fly.

Hacks, to do, etc
  Currently just uses a pickled dictionary, but should used some sort of indexed file.
  Maybe an OLE2 compound file, or a bsddb file?
"""

from win32com.client import dynamic

def EnsureDispatch(
    prog_id: str | dynamic.PyIDispatchType | dynamic._GoodDispatchTypes | dynamic.PyIUnknownType, bForDemand: int = ...
) -> dynamic.CDispatch:
    """Given a COM prog_id, return an object that is using makepy support, building if necessary"""
    ...
