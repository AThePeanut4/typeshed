"""
Simple man page writer for reStructuredText.

Man pages (short for "manual pages") contain system documentation on unix-like
systems. The pages are grouped in numbered sections:

 1 executable programs and shell commands
 2 system calls
 3 library functions
 4 special files
 5 file formats
 6 games
 7 miscellaneous
 8 system administration

Man pages are written *troff*, a text file formatting system.

See https://www.tldp.org/HOWTO/Man-Page for a start.

Man pages have no subsection only parts.
Standard parts

  NAME ,
  SYNOPSIS ,
  DESCRIPTION ,
  OPTIONS ,
  FILES ,
  SEE ALSO ,
  BUGS ,

and

  AUTHOR .

A unix-like system keeps an index of the DESCRIPTIONs, which is accessible
by the command whatis or apropos.
"""

from _typeshed import Incomplete

def __getattr__(name: str) -> Incomplete: ...
