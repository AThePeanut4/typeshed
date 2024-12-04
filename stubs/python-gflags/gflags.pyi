"""
This package is used to define and parse command line flags.

This package defines a *distributed* flag-definition policy: rather than
an application having to define all flags in or near main(), each python
module defines flags that are useful to it.  When one python module
imports another, it gains access to the other's flags.  (This is
implemented by having all modules share a common, global registry object
containing all the flag information.)

Flags are defined through the use of one of the DEFINE_xxx functions.
The specific function used determines how the flag is parsed, checked,
and optionally type-converted, when it's seen on the command line.
"""

from collections.abc import Callable, Iterable, Iterator, Sequence
from types import ModuleType
from typing import IO, Any

class Error(Exception):
    """The base class for all flags errors."""
    ...

FlagsError = Error

class DuplicateFlag(FlagsError): ...
class CantOpenFlagFileError(FlagsError):
    """Raised if flagfile fails to open: doesn't exist, wrong permissions, etc."""
    ...
class DuplicateFlagCannotPropagateNoneToSwig(DuplicateFlag):
    """
    Raised when redefining a SWIG flag and the default value is None.

    It's raised when redefining a SWIG flag with allow_override=True and the
    default value is None. Because it's currently impossible to pass None default
    value back to SWIG. See FlagValues.SetDefault for details.
    """
    ...

class DuplicateFlagError(DuplicateFlag):
    """Raised if there is a flag naming conflict."""
    def __init__(self, flagname: str, flag_values: FlagValues, other_flag_values: FlagValues = ...) -> None: ...

class IllegalFlagValueError(FlagsError):
    """Raised if the flag command line argument is illegal."""
    ...

IllegalFlagValue = IllegalFlagValueError

class UnrecognizedFlag(FlagsError): ...

class UnrecognizedFlagError(UnrecognizedFlag):
    """
    Raised if a flag is unrecognized.

    Attributes:
      flagname: Name of the unrecognized flag.
      flagvalue: Value of the flag, empty if the flag is not defined.
    """
    def __init__(self, flagname: str, flagvalue: str = ...) -> None: ...

def get_help_width() -> int:
    """Returns: an integer, the width of help lines that is used in TextWrap."""
    ...

GetHelpWidth = get_help_width

def text_wrap(text: str, length: int = ..., indent: str = ..., firstline_indent: str = ..., tabs: str = ...) -> str:
    """
    Wraps a given text to a maximum line length and returns it.

    It turns lines that only contain whitespace into empty lines, keeps new lines,
    and expands tabs using 4 spaces.

    Args:
      text:             str, Text to wrap.
      length:           int, Maximum length of a line, includes indentation.
                        If this is None then use GetHelpWidth()
      indent:           str, Indent for all but first line.
      firstline_indent: str, Indent for first line; if None, fall back to indent.

    Returns:
      Wrapped text.

    Raises:
      ValueError: if indent or firstline_indent not shorter than length.
    """
    ...

TextWrap = text_wrap

def doc_to_help(doc: str) -> str:
    """Takes a __doc__ string and reformats it as help."""
    ...

DocToHelp = doc_to_help

class FlagValues:
    """
    Registry of 'Flag' objects.

    A 'FlagValues' can then scan command line arguments, passing flag
    arguments through to the 'Flag' objects that it owns.  It also
    provides easy access to the flag values.  Typically only one
    'FlagValues' object is needed by an application: gflags.FLAGS

    This class is heavily overloaded:

    'Flag' objects are registered via __setitem__:
         FLAGS['longname'] = x   # register a new flag

    The .value attribute of the registered 'Flag' objects can be accessed
    as attributes of this 'FlagValues' object, through __getattr__.  Both
    the long and short name of the original 'Flag' objects can be used to
    access its value:
         FLAGS.longname          # parsed flag value
         FLAGS.x                 # parsed flag value (short name)

    Command line arguments are scanned and passed to the registered 'Flag'
    objects through the __call__ method.  Unparsed arguments, including
    argv[0] (e.g. the program name) are returned.
         argv = FLAGS(sys.argv)  # scan command line arguments

    The original registered Flag objects can be retrieved through the use
    of the dictionary-like operator, __getitem__:
         x = FLAGS['longname']   # access the registered Flag object

    The str() operator of a 'FlagValues' object provides help for all of
    the registered 'Flag' objects.
    """
    def UseGnuGetOpt(self, use_gnu_getopt: bool = ...) -> None:
        """
        Use GNU-style scanning. Allows mixing of flag and non-flag arguments.

        See http://docs.python.org/library/getopt.html#getopt.gnu_getopt

        Args:
          use_gnu_getopt: wether or not to use GNU style scanning.
        """
        ...
    def is_gnu_getopt(self) -> bool: ...
    IsGnuGetOpt = is_gnu_getopt
    # TODO dict type
    def FlagDict(self) -> dict[Any, Any]: ...
    def flags_by_module_dict(self) -> dict[str, list[Flag]]:
        """
        Returns the dictionary of module_name -> list of defined flags.

        Returns:
          A dictionary.  Its keys are module names (strings).  Its values
          are lists of Flag objects.
        """
        ...
    FlagsByModuleDict = flags_by_module_dict
    def flags_by_module_id_dict(self) -> dict[int, list[Flag]]:
        """
        Returns the dictionary of module_id -> list of defined flags.

        Returns:
          A dictionary.  Its keys are module IDs (ints).  Its values
          are lists of Flag objects.
        """
        ...
    FlagsByModuleIdDict = flags_by_module_id_dict
    def key_flags_by_module_dict(self) -> dict[str, list[Flag]]:
        """
        Returns the dictionary of module_name -> list of key flags.

        Returns:
          A dictionary.  Its keys are module names (strings).  Its values
          are lists of Flag objects.
        """
        ...
    KeyFlagsByModuleDict = key_flags_by_module_dict
    def find_module_defining_flag(self, flagname: str, default: str = ...) -> str:
        """
        Return the name of the module defining this flag, or default.

        Args:
          flagname: Name of the flag to lookup.
          default: Value to return if flagname is not defined. Defaults
              to None.

        Returns:
          The name of the module which registered the flag with this name.
          If no such module exists (i.e. no flag with this name exists),
          we return default.
        """
        ...
    FindModuleDefiningFlag = find_module_defining_flag
    def find_module_id_defining_flag(self, flagname: str, default: int = ...) -> int:
        """
        Return the ID of the module defining this flag, or default.

        Args:
          flagname: Name of the flag to lookup.
          default: Value to return if flagname is not defined. Defaults
              to None.

        Returns:
          The ID of the module which registered the flag with this name.
          If no such module exists (i.e. no flag with this name exists),
          we return default.
        """
        ...
    FindModuleIdDefiningFlag = find_module_id_defining_flag
    def append_flag_values(self, flag_values: FlagValues) -> None:
        """
        Appends flags registered in another FlagValues instance.

        Args:
          flag_values: registry to copy from
        """
        ...
    AppendFlagValues = append_flag_values
    def remove_flag_values(self, flag_values: FlagValues) -> None:
        """
        Remove flags that were previously appended from another FlagValues.

        Args:
          flag_values: registry containing flags to remove.
        """
        ...
    RemoveFlagValues = remove_flag_values
    def __setitem__(self, name: str, flag: Flag) -> None:
        """Registers a new flag variable."""
        ...
    def __getitem__(self, name: str) -> Flag:
        """Retrieves the Flag object for the flag --name."""
        ...
    def __getattr__(self, name: str) -> Any:
        """Retrieves the 'value' attribute of the flag --name."""
        ...
    def __setattr__(self, name: str, value: Any) -> None:
        """Sets the 'value' attribute of the flag --name."""
        ...
    def __delattr__(self, flag_name: str) -> None:
        """
        Deletes a previously-defined flag from a flag object.

        This method makes sure we can delete a flag by using

          del FLAGS.<flag_name>

        E.g.,

          gflags.DEFINE_integer('foo', 1, 'Integer flag.')
          del gflags.FLAGS.foo

        If a flag is also registered by its the other name (long name or short
        name), the other name won't be deleted.

        Args:
          flag_name: A string, the name of the flag to be deleted.

        Raises:
          AttributeError: When there is no registered flag named flag_name.
        """
        ...
    def set_default(self, name: str, value: Any) -> None:
        """
        Changes the default value (and current value) of the named flag object.

        Call this method at the top level of a module to avoid overwriting the value
        passed at the command line.

        Args:
          name: A string, the name of the flag to modify.
          value: The new default value.

        Raises:
          UnrecognizedFlagError: When there is no registered flag named name.
          IllegalFlagValueError: When value is not valid.
        """
        ...
    SetDefault = set_default
    def __contains__(self, name: str) -> bool:
        """Returns True if name is a value (flag) in the dict."""
        ...
    has_key = __contains__
    def __iter__(self) -> Iterator[str]: ...
    def __call__(self, argv: list[str], known_only: bool = ...) -> list[str]:
        """
        Parses flags from argv; stores parsed flags into this FlagValues object.

        All unparsed arguments are returned.

        Args:
           argv: argument list. Can be of any type that may be converted to a list.
           known_only: parse and remove known flags, return rest untouched.

        Returns:
           The list of arguments not parsed as options, including argv[0].

        Raises:
           Error: on any parsing error.
           ValueError: on flag value parsing error.
        """
        ...
    def reset(self) -> None: ...
    Reset = reset
    def RegisteredFlags(self) -> list[str]:
        """Returns: a list of the names and short names of all registered flags."""
        ...
    def flag_values_dict(self) -> dict[str, Any]:
        """Returns: a dictionary that maps flag names to flag values."""
        ...
    FlagValuesDict = flag_values_dict
    def GetHelp(self, prefix: str = ...) -> str:
        """
        Generates a help string for all known flags.

        Args:
          prefix: str, per-line output prefix.
          include_special_flags: bool, whether to include description of
            _SPECIAL_FLAGS, i.e. --flagfile and --undefok.

        Returns:
          str, formatted help message.
        """
        ...
    def module_help(self, module: ModuleType | str) -> str:
        """
        Describe the key flags of a module.

        Args:
          module: A module object or a module name (a string).

        Returns:
          string describing the key flags of a module.
        """
        ...
    ModuleHelp = module_help
    def main_module_help(self) -> str:
        """
        Describe the key flags of the main module.

        Returns:
          string describing the key flags of a module.
        """
        ...
    MainModuleHelp = main_module_help
    def get(self, name: str, default: Any) -> Any:
        """
        Returns the value of a flag (if not None) or a default value.

        Args:
          name: A string, the name of a flag.
          default: Default value to use if the flag value is None.

        Returns:
          Requested flag value or default.
        """
        ...
    def ShortestUniquePrefixes(self, fl: dict[str, Flag]) -> dict[str, str]: ...
    def ExtractFilename(self, flagfile_str: str) -> str:
        """
        Returns filename from a flagfile_str of form -[-]flagfile=filename.

        The cases of --flagfile foo and -flagfile foo shouldn't be hitting
        this function, as they are dealt with in the level above this
        function.

        Args:
          flagfile_str: flagfile string.

        Returns:
          str filename from a flagfile_str of form -[-]flagfile=filename.

        Raises:
          Error: when illegal --flagfile provided.
        """
        ...
    def read_flags_from_files(self, argv: list[str], force_gnu: bool = ...) -> list[str]:
        """
        Processes command line args, but also allow args to be read from file.

        Args:
          argv: A list of strings, usually sys.argv[1:], which may contain one or
            more flagfile directives of the form --flagfile="./filename".
            Note that the name of the program (sys.argv[0]) should be omitted.
          force_gnu: If False, --flagfile parsing obeys normal flag semantics.
            If True, --flagfile parsing instead follows gnu_getopt semantics.
            *** WARNING *** force_gnu=False may become the future default!

        Returns:
          A new list which has the original list combined with what we read
          from any flagfile(s).

        Raises:
          IllegalFlagValueError: when --flagfile provided with no argument.

        References: Global gflags.FLAG class instance.

        This function should be called before the normal FLAGS(argv) call.
        This function scans the input list for a flag that looks like:
        --flagfile=<somefile>. Then it opens <somefile>, reads all valid key
        and value pairs and inserts them into the input list in exactly the
        place where the --flagfile arg is found.

        Note that your application's flags are still defined the usual way
        using gflags DEFINE_flag() type functions.

        Notes (assuming we're getting a commandline of some sort as our input):
        --> For duplicate flags, the last one we hit should "win".
        --> Since flags that appear later win, a flagfile's settings can be "weak"
            if the --flagfile comes at the beginning of the argument sequence,
            and it can be "strong" if the --flagfile comes at the end.
        --> A further "--flagfile=<otherfile.cfg>" CAN be nested in a flagfile.
            It will be expanded in exactly the spot where it is found.
        --> In a flagfile, a line beginning with # or // is a comment.
        --> Entirely blank lines _should_ be ignored.
        """
        ...
    ReadFlagsFromFiles = read_flags_from_files
    def flags_into_string(self) -> str:
        """
        Returns a string with the flags assignments from this FlagValues object.

        This function ignores flags whose value is None.  Each flag
        assignment is separated by a newline.

        NOTE: MUST mirror the behavior of the C++ CommandlineFlagsIntoString
        from http://code.google.com/p/google-gflags

        Returns:
          string with the flags assignments from this FlagValues object.
        """
        ...
    FlagsIntoString = flags_into_string
    def append_flags_into_file(self, filename: str) -> None:
        """
        Appends all flags assignments from this FlagInfo object to a file.

        Output will be in the format of a flagfile.

        NOTE: MUST mirror the behavior of the C++ AppendFlagsIntoFile
        from http://code.google.com/p/google-gflags

        Args:
          filename: string, name of the file.
        """
        ...
    AppendFlagsIntoFile = append_flags_into_file
    def write_help_in_xml_format(self, outfile: IO[str] = ...) -> None:
        """
        Outputs flag documentation in XML format.

        NOTE: We use element names that are consistent with those used by
        the C++ command-line flag library, from
        http://code.google.com/p/google-gflags
        We also use a few new elements (e.g., <key>), but we do not
        interfere / overlap with existing XML elements used by the C++
        library.  Please maintain this consistency.

        Args:
          outfile: File object we write to.  Default None means sys.stdout.
        """
        ...
    WriteHelpInXMLFormat = write_help_in_xml_format
    # TODO validator: gflags_validators.Validator
    def AddValidator(self, validator: Any) -> None: ...
    def is_parsed(self) -> bool:
        """Whether flags were parsed."""
        ...
    IsParsed = is_parsed

FLAGS: FlagValues

class Flag:
    """
    Information about a command-line flag.

    'Flag' objects define the following fields:
      .name - the name for this flag;
      .default - the default value for this flag;
      .default_as_str - default value as repr'd string, e.g., "'true'" (or None);
      .value - the most recent parsed value of this flag; set by Parse();
      .help - a help string or None if no help is available;
      .short_name - the single letter alias for this flag (or None);
      .boolean - if 'true', this flag does not accept arguments;
      .present - true if this flag was parsed from command line flags;
      .parser - an ArgumentParser object;
      .serializer - an ArgumentSerializer object;
      .allow_override - the flag may be redefined without raising an error, and
                        newly defined flag overrides the old one.
      .allow_cpp_override - the flag may be redefined in C++ without raising an
                            error, value "transfered" to C++, and the flag is
                            replaced by the C++ flag after init;
      .allow_hide_cpp - the flag may be redefined despite hiding a C++ flag with
                        the same name;
      .using_default_value - the flag value has not been set by user;
      .allow_overwrite - the flag may be parsed more than once without raising
                         an error, the last set value will be used;

    The only public method of a 'Flag' object is Parse(), but it is
    typically only called by a 'FlagValues' object.  The Parse() method is
    a thin wrapper around the 'ArgumentParser' Parse() method.  The parsed
    value is saved in .value, and the .present attribute is updated.  If
    this flag was already present, an Error is raised.

    Parse() is also called during __init__ to parse the default value and
    initialize the .value attribute.  This enables other python modules to
    safely use flags even if the __main__ module neglects to parse the
    command line arguments.  The .present attribute is cleared after
    __init__ parsing.  If the default value is set to None, then the
    __init__ parsing step is skipped and the .value attribute is
    initialized to None.

    Note: The default value is also presented to the user in the help
    string, so it is important that it be a legal value for this flag.
    """
    name: str
    default: Any
    default_as_str: str
    value: Any
    help: str
    short_name: str
    boolean: bool
    present: bool
    parser: ArgumentParser
    serializer: ArgumentSerializer
    allow_override: bool
    def __init__(
        self,
        parser: ArgumentParser,
        serializer: ArgumentSerializer,
        name: str,
        default: str | None,
        help_string: str,
        short_name: str = ...,
        boolean: bool = ...,
        allow_override: bool = ...,
    ) -> None: ...
    def Parse(self, argument: Any) -> Any:
        """
        Parse string and set flag value.

        Args:
          argument: String, value to be parsed for flag.
        """
        ...
    def Unparse(self) -> None: ...
    def Serialize(self) -> str: ...
    def SetDefault(self, value: Any) -> None:
        """Changes the default value (and current value too) for this Flag."""
        ...
    def Type(self) -> str:
        """
        Get type of flag.

        NOTE: we use strings, and not the types.*Type constants because
        our flags can have more exotic types, e.g., 'comma separated list
        of strings', 'whitespace separated list of strings', etc.

        Returns:
          a string that describes the type of this Flag.
        """
        ...
    def WriteInfoInXMLFormat(self, outfile: IO[str], module_name: str, is_key: bool = ..., indent: str = ...) -> None: ...

class ArgumentParser:
    """
    Base class used to parse and convert arguments.

    The parse() method checks to make sure that the string argument is a
    legal value and convert it to a native type.  If the value cannot be
    converted, it should throw a 'ValueError' exception with a human
    readable explanation of why the value is illegal.

    Subclasses should also define a syntactic_help string which may be
    presented to the user to describe the form of the legal values.

    Argument parser classes must be stateless, since instances are cached
    and shared between flags. Initializer arguments are allowed, but all
    member variables must be derived from initializer arguments only.
    """
    syntactic_help: str
    # TODO what is this
    def parse(self, argument: Any) -> Any:
        """
        Parses the string argument and returns the native value.

        By default it returns its argument unmodified.

        Args:
          argument: string argument passed in the commandline.

        Raises:
          ValueError: Raised when it fails to parse the argument.

        Returns:
          The parsed value in native type.
        """
        ...
    Parser = parse
    def flag_type(self) -> str:
        """Returns a string representing the type of the flag."""
        ...
    Type = flag_type
    def WriteCustomInfoInXMLFormat(self, outfile: IO[str], indent: str) -> None: ...

class ArgumentSerializer:
    """Base class for generating string representations of a flag value."""
    def Serialize(self, value: Any) -> str: ...

class ListSerializer(ArgumentSerializer):
    def __init__(self, list_sep: str) -> None: ...
    def Serialize(self, value: list[Any]) -> str: ...

def register_validator(
    flag_name: str, checker: Callable[[Any], bool], message: str = ..., flag_values: FlagValues = ...
) -> None:
    """
    Adds a constraint, which will be enforced during program execution.

    The constraint is validated when flags are initially parsed, and after each
    change of the corresponding flag's value.
    Args:
      flag_name: str, Name of the flag to be checked.
      checker: callable, A function to validate the flag.
        input - A single positional argument: The value of the corresponding
          flag (string, boolean, etc.  This value will be passed to checker
          by the library).
        output - Boolean.
          Must return True if validator constraint is satisfied.
          If constraint is not satisfied, it should either return False or
            raise gflags.ValidationError(desired_error_message).
      message: Error text to be shown to the user if checker returns False.
        If checker raises gflags.ValidationError, message from the raised
          Error will be shown.
      flag_values: An optional FlagValues instance to validate against.
    Raises:
      AttributeError: If flag_name is not registered as a valid flag name.
    """
    ...

RegisterValidator = register_validator

def mark_flag_as_required(flag_name: str, flag_values: FlagValues = ...) -> None:
    """
    Ensures that flag is not None during program execution.

    Registers a flag validator, which will follow usual validator rules.
    Important note: validator will pass for any non-None value, such as False,
    0 (zero), '' (empty string) and so on.

    It is recommended to call this method like this:

      if __name__ == '__main__':
        gflags.mark_flag_as_required('your_flag_name')
        app.run()

    Because validation happens at app.run() we want to ensure required-ness
    is enforced at that time.  However, you generally do not want to force
    users who import your code to have additional required flags for their
    own binaries or tests.

    Args:
      flag_name: string, name of the flag
      flag_values: FlagValues
    Raises:
      AttributeError: if flag_name is not registered as a valid flag name.
    """
    ...

MarkFlagAsRequired = mark_flag_as_required

def mark_flags_as_required(flag_names: Iterable[str], flag_values: FlagValues = ...) -> None:
    """
    Ensures that flags are not None during program execution.

    Recommended usage:

      if __name__ == '__main__':
        gflags.mark_flags_as_required(['flag1', 'flag2', 'flag3'])
        app.run()

    Args:
      flag_names: list/tuple, names of the flags.
      flag_values: FlagValues
    Raises:
      AttributeError: If any of flag name has not already been defined as a flag.
    """
    ...

MarkFlagsAsRequired = mark_flags_as_required

def mark_flags_as_mutual_exclusive(flag_names: Iterable[str], required: bool = ..., flag_values: FlagValues = ...) -> None:
    """
    Ensures that only one flag among flag_names is set.

    Args:
      flag_names: [str], a list of the flag names to be checked.
      required: Boolean, if set, exactly one of the flags must be set.
          Otherwise, it is also valid for none of the flags to be set.
      flag_values: An optional FlagValues instance to validate against.
    """
    ...

MarkFlagsAsMutualExclusive = mark_flags_as_mutual_exclusive

def DEFINE(
    parser: ArgumentParser,
    name: str,
    default: Any,
    help: str,
    flag_values: FlagValues = ...,
    serializer: ArgumentSerializer = ...,
    **args: Any,
) -> None:
    """
    Registers a generic Flag object.

    NOTE: in the docstrings of all DEFINE* functions, "registers" is short
    for "creates a new flag and registers it".

    Auxiliary function: clients should use the specialized DEFINE_<type>
    function instead.

    Args:
      parser: ArgumentParser that is used to parse the flag arguments.
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      flag_values: FlagValues object with which the flag will be registered.
      serializer: ArgumentSerializer that serializes the flag value.
      module_name: A string, the name of the Python module declaring this flag.
          If not provided, it will be computed using the stack trace of this call.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...
def DEFINE_flag(flag: Flag, flag_values: FlagValues = ...) -> None:
    """
    Registers a 'Flag' object with a 'FlagValues' object.

    By default, the global FLAGS 'FlagValue' object is used.

    Typical users will use one of the more specialized DEFINE_xxx
    functions, such as DEFINE_string or DEFINE_integer.  But developers
    who need to create Flag objects themselves should use this function
    to register their flags.

    Args:
      flag: A Flag object, a flag that is key to the module.
      flag_values: FlagValues object with which the flag will be registered.
      module_name: A string, the name of the Python module declaring this flag.
          If not provided, it will be computed using the stack trace of this call.
    """
    ...
def declare_key_flag(flag_name: str, flag_values: FlagValues = ...) -> None:
    """
    Declares one flag as key to the current module.

    Key flags are flags that are deemed really important for a module.
    They are important when listing help messages; e.g., if the
    --helpshort command-line flag is used, then only the key flags of the
    main module are listed (instead of all flags, as in the case of
    --helpfull).

    Sample usage:

      gflags.DECLARE_key_flag('flag_1')

    Args:
      flag_name: A string, the name of an already declared flag.
        (Redeclaring flags as key, including flags implicitly key
        because they were declared in this module, is a no-op.)
      flag_values: A FlagValues object.  This should almost never
        need to be overridden.
    """
    ...

DECLARE_key_flag = declare_key_flag

def adopt_module_key_flags(module: ModuleType, flag_values: FlagValues = ...) -> None:
    """
    Declares that all flags key to a module are key to the current module.

    Args:
      module: A module object.
      flag_values: A FlagValues object.  This should almost never need
        to be overridden.

    Raises:
      Error: When given an argument that is a module name (a
      string), instead of a module object.
    """
    ...

ADOPT_module_key_flags = adopt_module_key_flags

def DEFINE_string(name: str, default: str | None, help: str, flag_values: FlagValues = ..., **args: Any) -> None:
    """Registers a flag whose value can be any string."""
    ...

class BooleanParser(ArgumentParser):
    """Parser of boolean values."""
    def Convert(self, argument: Any) -> bool:
        """Converts the argument to a boolean; raise ValueError on errors."""
        ...
    def Parse(self, argument: Any) -> bool: ...

class BooleanFlag(Flag):
    """
    Basic boolean flag.

    Boolean flags do not take any arguments, and their value is either
    True (1) or False (0).  The false value is specified on the command
    line by prepending the word 'no' to either the long or the short flag
    name.

    For example, if a Boolean flag was created whose long name was
    'update' and whose short name was 'x', then this flag could be
    explicitly unset through either --noupdate or --nox.
    """
    def __init__(self, name: str, default: bool | None, help: str, short_name: str = ..., **args: Any) -> None: ...

def DEFINE_boolean(name: str, default: bool | None, help: str, flag_values: FlagValues = ..., **args: Any) -> None:
    """
    Registers a boolean flag.

    Such a boolean flag does not take an argument.  If a user wants to
    specify a false value explicitly, the long option beginning with 'no'
    must be used: i.e. --noflag

    This flag will have a value of None, True or False.  None is possible
    if default=None and the user does not specify the flag on the command
    line.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      flag_values: FlagValues object with which the flag will be registered.
      module_name: A string, the name of the Python module declaring this flag.
          If not provided, it will be computed using the stack trace of this call.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...

DEFINE_bool = DEFINE_boolean

class HelpFlag(BooleanFlag):
    def __init__(self) -> None: ...
    def Parse(self, arg: Any) -> None: ...

class HelpXMLFlag(BooleanFlag):
    def __init__(self) -> None: ...
    def Parse(self, arg: Any) -> None: ...

class HelpshortFlag(BooleanFlag):
    def __init__(self) -> None: ...
    def Parse(self, arg: Any) -> None: ...

class NumericParser(ArgumentParser):
    def IsOutsideBounds(self, val: float) -> bool: ...
    def Parse(self, argument: Any) -> float: ...
    def WriteCustomInfoInXMLFormat(self, outfile: IO[str], indent: str) -> None: ...
    def Convert(self, argument: Any) -> Any: ...

class FloatParser(NumericParser):
    """
    Parser of floating point values.

    Parsed value may be bounded to a given upper and lower bound.
    """
    number_article: str
    number_name: str
    syntactic_help: str
    def __init__(self, lower_bound: float = ..., upper_bound: float = ...) -> None: ...
    def Convert(self, argument: Any) -> float:
        """Converts argument to a float; raises ValueError on errors."""
        ...

def DEFINE_float(
    name: str,
    default: float | None,
    help: str,
    lower_bound: float = ...,
    upper_bound: float = ...,
    flag_values: FlagValues = ...,
    **args: Any,
) -> None:
    """
    Registers a flag whose value must be a float.

    If lower_bound or upper_bound are set, then this flag must be
    within the given range.

    Args:
      name: str, flag name.
      default: float, default flag value.
      help: str, help message.
      lower_bound: float, min value of the flag.
      upper_bound: float, max value of the flag.
      flag_values: FlagValues object with which the flag will be registered.
      **args: additional arguments to pass to DEFINE.
    """
    ...

class IntegerParser(NumericParser):
    """
    Parser of an integer value.

    Parsed value may be bounded to a given upper and lower bound.
    """
    number_article: str
    number_name: str
    syntactic_help: str
    def __init__(self, lower_bound: int = ..., upper_bound: int = ...) -> None: ...
    def Convert(self, argument: Any) -> int: ...

def DEFINE_integer(
    name: str,
    default: int | None,
    help: str,
    lower_bound: int = ...,
    upper_bound: int = ...,
    flag_values: FlagValues = ...,
    **args: Any,
) -> None:
    """
    Registers a flag whose value must be an integer.

    If lower_bound, or upper_bound are set, then this flag must be
    within the given range.

    Args:
      name: str, flag name.
      default: int, default flag value.
      help: str, help message.
      lower_bound: int, min value of the flag.
      upper_bound: int, max value of the flag.
      flag_values: FlagValues object with which the flag will be registered.
      **args: additional arguments to pass to DEFINE.
    """
    ...

class EnumParser(ArgumentParser):
    """
    Parser of a string enum value (a string value from a given set).

    If enum_values (see below) is not specified, any string is allowed.
    """
    def __init__(self, enum_values: list[str]) -> None:
        """
        Initialize EnumParser.

        Args:
          enum_values: Array of values in the enum.
          case_sensitive: Whether or not the enum is to be case-sensitive.
        """
        ...
    def Parse(self, argument: Any) -> Any:
        """
        Determine validity of argument and return the correct element of enum.

        If self.enum_values is empty, then all arguments are valid and argument
        will be returned.

        Otherwise, if argument matches an element in enum, then the first
        matching element will be returned.

        Args:
          argument: The supplied flag value.

        Returns:
          The matching element from enum_values, or argument if enum_values is
          empty.

        Raises:
          ValueError: enum_values was non-empty, but argument didn't match
            anything in enum.
        """
        ...

class EnumFlag(Flag):
    """Basic enum flag; its value can be any string from list of enum_values."""
    def __init__(
        self, name: str, default: str | None, help: str, enum_values: list[str], short_name: str, **args: Any
    ) -> None: ...

def DEFINE_enum(
    name: str, default: str | None, enum_values: Iterable[str], help: str, flag_values: FlagValues = ..., **args: Any
) -> None:
    """
    Registers a flag whose value can be any string from enum_values.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      enum_values: A list of strings with the possible values for the flag.
      help: A help string.
      flag_values: FlagValues object with which the flag will be registered.
      module_name: A string, the name of the Python module declaring this flag.
          If not provided, it will be computed using the stack trace of this call.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...

class BaseListParser(ArgumentParser):
    """
    Base class for a parser of lists of strings.

    To extend, inherit from this class; from the subclass __init__, call

      BaseListParser.__init__(self, token, name)

    where token is a character used to tokenize, and name is a description
    of the separator.
    """
    def __init__(self, token: str = ..., name: str = ...) -> None: ...
    def Parse(self, argument: Any) -> list[Any]: ...

class ListParser(BaseListParser):
    """Parser for a comma-separated list of strings."""
    def __init__(self) -> None: ...

class WhitespaceSeparatedListParser(BaseListParser):
    """Parser for a whitespace-separated list of strings."""
    def __init__(self) -> None:
        """
        Initializer.

        Args:
          comma_compat: bool - Whether to support comma as an additional separator.
              If false then only whitespace is supported.  This is intended only for
              backwards compatibility with flags that used to be comma-separated.
        """
        ...

def DEFINE_list(name: str, default: list[str] | None, help: str, flag_values: FlagValues = ..., **args: Any) -> None:
    """
    Registers a flag whose value is a comma-separated list of strings.

    The flag value is parsed with a CSV parser.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      flag_values: FlagValues object with which the flag will be registered.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...
def DEFINE_spaceseplist(name: str, default: list[str] | None, help: str, flag_values: FlagValues = ..., **args: Any) -> None:
    """
    Registers a flag whose value is a whitespace-separated list of strings.

    Any whitespace can be used as a separator.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      comma_compat: bool - Whether to support comma as an additional separator.
          If false then only whitespace is supported.  This is intended only for
          backwards compatibility with flags that used to be comma-separated.
      flag_values: FlagValues object with which the flag will be registered.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...

class MultiFlag(Flag):
    """
    A flag that can appear multiple time on the command-line.

    The value of such a flag is a list that contains the individual values
    from all the appearances of that flag on the command-line.

    See the __doc__ for Flag for most behavior of this class.  Only
    differences in behavior are described here:

      * The default value may be either a single value or a list of values.
        A single value is interpreted as the [value] singleton list.

      * The value of the flag is always a list, even if the option was
        only supplied once, and even if the default value is a single
        value
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def Parse(self, arguments: Any) -> None:
        """
        Parses one or more arguments with the installed parser.

        Args:
          arguments: a single argument or a list of arguments (typically a
            list of default values); a single argument is converted
            internally into a list containing one item.
        """
        ...
    def Serialize(self) -> str: ...

def DEFINE_multi_string(
    name: str, default: str | list[str] | None, help: str, flag_values: FlagValues = ..., **args: Any
) -> None:
    """
    Registers a flag whose value can be a list of any strings.

    Use the flag on the command line multiple times to place multiple
    string values into the list.  The 'default' may be a single string
    (which will be converted into a single-element list) or a list of
    strings.


    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      flag_values: FlagValues object with which the flag will be registered.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...

DEFINE_multistring = DEFINE_multi_string

def DEFINE_multi_integer(
    name: str,
    default: int | list[int] | None,
    help: str,
    lower_bound: int = ...,
    upper_bound: int = ...,
    flag_values: FlagValues = ...,
    **args: Any,
) -> None:
    """
    Registers a flag whose value can be a list of arbitrary integers.

    Use the flag on the command line multiple times to place multiple
    integer values into the list.  The 'default' may be a single integer
    (which will be converted into a single-element list) or a list of
    integers.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      lower_bound: int, min values of the flag.
      upper_bound: int, max values of the flag.
      flag_values: FlagValues object with which the flag will be registered.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...

DEFINE_multi_int = DEFINE_multi_integer

def DEFINE_multi_float(
    name: str,
    default: float | list[float] | None,
    help: str,
    lower_bound: float = ...,
    upper_bound: float = ...,
    flag_values: FlagValues = ...,
    **args: Any,
) -> None:
    """
    Registers a flag whose value can be a list of arbitrary floats.

    Use the flag on the command line multiple times to place multiple
    float values into the list.  The 'default' may be a single float
    (which will be converted into a single-element list) or a list of
    floats.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      help: A help string.
      lower_bound: float, min values of the flag.
      upper_bound: float, max values of the flag.
      flag_values: FlagValues object with which the flag will be registered.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...
def DEFINE_multi_enum(
    name: str,
    default: Sequence[str] | str | None,
    enum_values: Sequence[str],
    help: str,
    flag_values: FlagValues = ...,
    case_sensitive: bool = ...,
    **args: Any,
) -> None:
    """
    Registers a flag whose value can be a list strings from enum_values.

    Use the flag on the command line multiple times to place multiple
    enum values into the list.  The 'default' may be a single string
    (which will be converted into a single-element list) or a list of
    strings.

    Args:
      name: A string, the flag name.
      default: The default value of the flag.
      enum_values: A list of strings with the possible values for the flag.
      help: A help string.
      flag_values: FlagValues object with which the flag will be registered.
      case_sensitive: Whether or not the enum is to be case-sensitive.
      **args: Dictionary with extra keyword args that are passed to the
          Flag __init__.
    """
    ...
