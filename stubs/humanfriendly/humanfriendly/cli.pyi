"""
Usage: humanfriendly [OPTIONS]

Human friendly input/output (text formatting) on the command
line based on the Python package with the same name.

Supported options:

  -c, --run-command

    Execute an external command (given as the positional arguments) and render
    a spinner and timer while the command is running. The exit status of the
    command is propagated.

  --format-table

    Read tabular data from standard input (each line is a row and each
    whitespace separated field is a column), format the data as a table and
    print the resulting table to standard output. See also the --delimiter
    option.

  -d, --delimiter=VALUE

    Change the delimiter used by --format-table to VALUE (a string). By default
    all whitespace is treated as a delimiter.

  -l, --format-length=LENGTH

    Convert a length count (given as the integer or float LENGTH) into a human
    readable string and print that string to standard output.

  -n, --format-number=VALUE

    Format a number (given as the integer or floating point number VALUE) with
    thousands separators and two decimal places (if needed) and print the
    formatted number to standard output.

  -s, --format-size=BYTES

    Convert a byte count (given as the integer BYTES) into a human readable
    string and print that string to standard output.

  -b, --binary

    Change the output of -s, --format-size to use binary multiples of bytes
    (base-2) instead of the default decimal multiples of bytes (base-10).

  -t, --format-timespan=SECONDS

    Convert a number of seconds (given as the floating point number SECONDS)
    into a human readable timespan and print that string to standard output.

  --parse-length=VALUE

    Parse a human readable length (given as the string VALUE) and print the
    number of metres to standard output.

  --parse-size=VALUE

    Parse a human readable data size (given as the string VALUE) and print the
    number of bytes to standard output.

  --demo

    Demonstrate changing the style and color of the terminal font using ANSI
    escape sequences.

  -h, --help

    Show this message and exit.
"""

from _typeshed import Incomplete

def main() -> None:
    """Command line interface for the ``humanfriendly`` program."""
    ...
def run_command(command_line) -> None:
    """Run an external command and show a spinner while the command is running."""
    ...
def print_formatted_length(value) -> None:
    """Print a human readable length."""
    ...
def print_formatted_number(value) -> None:
    """Print large numbers in a human readable format."""
    ...
def print_formatted_size(value, binary) -> None:
    """Print a human readable size."""
    ...
def print_formatted_table(delimiter) -> None:
    """Read tabular data from standard input and print a table."""
    ...
def print_formatted_timespan(value) -> None:
    """Print a human readable timespan."""
    ...
def print_parsed_length(value) -> None:
    """Parse a human readable length and print the number of metres."""
    ...
def print_parsed_size(value) -> None:
    """Parse a human readable data size and print the number of bytes."""
    ...
def demonstrate_ansi_formatting() -> None:
    """Demonstrate the use of ANSI escape sequences."""
    ...
def demonstrate_256_colors(i, j, group: Incomplete | None = None) -> None:
    """Demonstrate 256 color mode support."""
    ...
