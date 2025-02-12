"""Pretty-print tabular data."""

from collections.abc import Callable, Container, Iterable, Mapping, Sequence
from typing import Any, Final, NamedTuple
from typing_extensions import Self, TypeAlias

from .version import __version__ as __version__

__all__ = ["tabulate", "tabulate_formats", "simple_separated_format"]

# These constants are meant to be configurable
# https://github.com/astanin/python-tabulate#text-formatting
PRESERVE_WHITESPACE: bool
MIN_PADDING: int
# https://github.com/astanin/python-tabulate#wide-fullwidth-cjk-symbols
WIDE_CHARS_MODE: bool
SEPARATING_LINE: str

class Line(NamedTuple):
    """Line(begin, hline, sep, end)"""
    begin: str
    hline: str
    sep: str
    end: str

class DataRow(NamedTuple):
    """DataRow(begin, sep, end)"""
    begin: str
    sep: str
    end: str

_TableFormatLine: TypeAlias = None | Line | Callable[[list[int], list[str]], str]
_TableFormatRow: TypeAlias = None | DataRow | Callable[[list[Any], list[int], list[str]], str]

class TableFormat(NamedTuple):
    """TableFormat(lineabove, linebelowheader, linebetweenrows, linebelow, headerrow, datarow, padding, with_header_hide)"""
    lineabove: _TableFormatLine
    linebelowheader: _TableFormatLine
    linebetweenrows: _TableFormatLine
    linebelow: _TableFormatLine
    headerrow: _TableFormatRow
    datarow: _TableFormatRow
    padding: int
    with_header_hide: Container[str] | None

LATEX_ESCAPE_RULES: Final[dict[str, str]]
tabulate_formats: list[str]
multiline_formats: dict[str, str]

def simple_separated_format(separator: str) -> TableFormat:
    r"""
    Construct a simple TableFormat with columns separated by a separator.

    >>> tsv = simple_separated_format("\t") ;         tabulate([["foo", 1], ["spam", 23]], tablefmt=tsv) == 'foo \t 1\nspam\t23'
    True
    """
    ...
def tabulate(
    # The key is converted using str().
    tabular_data: Mapping[Any, Iterable[Any]] | Iterable[Iterable[Any]],
    headers: str | dict[str, str] | Sequence[str] = (),
    tablefmt: str | TableFormat = "simple",
    floatfmt: str | Iterable[str] = "g",
    intfmt: str | Iterable[str] = "",
    numalign: str | None = "default",
    stralign: str | None = "default",
    missingval: str | Iterable[str] = "",
    showindex: str | bool | Iterable[Any] = "default",
    disable_numparse: bool | Iterable[int] = False,
    colalign: Iterable[str | None] | None = None,
    maxcolwidths: int | Iterable[int | None] | None = None,
    rowalign: str | Iterable[str] | None = None,
    maxheadercolwidths: int | Iterable[int] | None = None,
) -> str:
    r"""
    Format a fixed width table for pretty printing.

    >>> print(tabulate([[1, 2.34], [-56, "8.999"], ["2", "10001"]]))
    ---  ---------
      1      2.34
    -56      8.999
      2  10001
    ---  ---------

    The first required argument (`tabular_data`) can be a
    list-of-lists (or another iterable of iterables), a list of named
    tuples, a dictionary of iterables, an iterable of dictionaries,
    an iterable of dataclasses (Python 3.7+), a two-dimensional NumPy array,
    NumPy record array, or a Pandas' dataframe.


    Table headers
    -------------

    To print nice column headers, supply the second argument (`headers`):

      - `headers` can be an explicit list of column headers
      - if `headers="firstrow"`, then the first row of data is used
      - if `headers="keys"`, then dictionary keys or column indices are used

    Otherwise a headerless table is produced.

    If the number of headers is less than the number of columns, they
    are supposed to be names of the last columns. This is consistent
    with the plain-text format of R and Pandas' dataframes.

    >>> print(tabulate([["sex","age"],["Alice","F",24],["Bob","M",19]],
    ...       headers="firstrow"))
           sex      age
    -----  -----  -----
    Alice  F         24
    Bob    M         19

    By default, pandas.DataFrame data have an additional column called
    row index. To add a similar column to all other types of data,
    use `showindex="always"` or `showindex=True`. To suppress row indices
    for all types of data, pass `showindex="never" or `showindex=False`.
    To add a custom row index column, pass `showindex=some_iterable`.

    >>> print(tabulate([["F",24],["M",19]], showindex="always"))
    -  -  --
    0  F  24
    1  M  19
    -  -  --


    Column alignment
    ----------------

    `tabulate` tries to detect column types automatically, and aligns
    the values properly. By default it aligns decimal points of the
    numbers (or flushes integer numbers to the right), and flushes
    everything else to the left. Possible column alignments
    (`numalign`, `stralign`) are: "right", "center", "left", "decimal"
    (only for `numalign`), and None (to disable alignment).


    Table formats
    -------------

    `intfmt` is a format specification used for columns which
    contain numeric data without a decimal point. This can also be
    a list or tuple of format strings, one per column.

    `floatfmt` is a format specification used for columns which
    contain numeric data with a decimal point. This can also be
    a list or tuple of format strings, one per column.

    `None` values are replaced with a `missingval` string (like
    `floatfmt`, this can also be a list of values for different
    columns):

    >>> print(tabulate([["spam", 1, None],
    ...                 ["eggs", 42, 3.14],
    ...                 ["other", None, 2.7]], missingval="?"))
    -----  --  ----
    spam    1  ?
    eggs   42  3.14
    other   ?  2.7
    -----  --  ----

    Various plain-text table formats (`tablefmt`) are supported:
    'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
    'latex', 'latex_raw', 'latex_booktabs', 'latex_longtable' and tsv.
    Variable `tabulate_formats`contains the list of currently supported formats.

    "plain" format doesn't use any pseudographics to draw tables,
    it separates columns with a double space:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                 ["strings", "numbers"], "plain"))
    strings      numbers
    spam         41.9999
    eggs        451

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="plain"))
    spam   41.9999
    eggs  451

    "simple" format is like Pandoc simple_tables:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                 ["strings", "numbers"], "simple"))
    strings      numbers
    ---------  ---------
    spam         41.9999
    eggs        451

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="simple"))
    ----  --------
    spam   41.9999
    eggs  451
    ----  --------

    "grid" is similar to tables produced by Emacs table.el package or
    Pandoc grid_tables:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "grid"))
    +-----------+-----------+
    | strings   |   numbers |
    +===========+===========+
    | spam      |   41.9999 |
    +-----------+-----------+
    | eggs      |  451      |
    +-----------+-----------+

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="grid"))
    +------+----------+
    | spam |  41.9999 |
    +------+----------+
    | eggs | 451      |
    +------+----------+

    "simple_grid" draws a grid using single-line box-drawing
    characters:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "simple_grid"))
    ┌───────────┬───────────┐
    │ strings   │   numbers │
    ├───────────┼───────────┤
    │ spam      │   41.9999 │
    ├───────────┼───────────┤
    │ eggs      │  451      │
    └───────────┴───────────┘

    "rounded_grid" draws a grid using single-line box-drawing
    characters with rounded corners:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "rounded_grid"))
    ╭───────────┬───────────╮
    │ strings   │   numbers │
    ├───────────┼───────────┤
    │ spam      │   41.9999 │
    ├───────────┼───────────┤
    │ eggs      │  451      │
    ╰───────────┴───────────╯

    "heavy_grid" draws a grid using bold (thick) single-line box-drawing
    characters:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "heavy_grid"))
    ┏━━━━━━━━━━━┳━━━━━━━━━━━┓
    ┃ strings   ┃   numbers ┃
    ┣━━━━━━━━━━━╋━━━━━━━━━━━┫
    ┃ spam      ┃   41.9999 ┃
    ┣━━━━━━━━━━━╋━━━━━━━━━━━┫
    ┃ eggs      ┃  451      ┃
    ┗━━━━━━━━━━━┻━━━━━━━━━━━┛

    "mixed_grid" draws a grid using a mix of light (thin) and heavy (thick) lines
    box-drawing characters:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "mixed_grid"))
    ┍━━━━━━━━━━━┯━━━━━━━━━━━┑
    │ strings   │   numbers │
    ┝━━━━━━━━━━━┿━━━━━━━━━━━┥
    │ spam      │   41.9999 │
    ├───────────┼───────────┤
    │ eggs      │  451      │
    ┕━━━━━━━━━━━┷━━━━━━━━━━━┙

    "double_grid" draws a grid using double-line box-drawing
    characters:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "double_grid"))
    ╔═══════════╦═══════════╗
    ║ strings   ║   numbers ║
    ╠═══════════╬═══════════╣
    ║ spam      ║   41.9999 ║
    ╠═══════════╬═══════════╣
    ║ eggs      ║  451      ║
    ╚═══════════╩═══════════╝

    "fancy_grid" draws a grid using a mix of single and
    double-line box-drawing characters:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "fancy_grid"))
    ╒═══════════╤═══════════╕
    │ strings   │   numbers │
    ╞═══════════╪═══════════╡
    │ spam      │   41.9999 │
    ├───────────┼───────────┤
    │ eggs      │  451      │
    ╘═══════════╧═══════════╛

    "outline" is the same as the "grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "outline"))
    +-----------+-----------+
    | strings   |   numbers |
    +===========+===========+
    | spam      |   41.9999 |
    | eggs      |  451      |
    +-----------+-----------+

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="outline"))
    +------+----------+
    | spam |  41.9999 |
    | eggs | 451      |
    +------+----------+

    "simple_outline" is the same as the "simple_grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "simple_outline"))
    ┌───────────┬───────────┐
    │ strings   │   numbers │
    ├───────────┼───────────┤
    │ spam      │   41.9999 │
    │ eggs      │  451      │
    └───────────┴───────────┘

    "rounded_outline" is the same as the "rounded_grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "rounded_outline"))
    ╭───────────┬───────────╮
    │ strings   │   numbers │
    ├───────────┼───────────┤
    │ spam      │   41.9999 │
    │ eggs      │  451      │
    ╰───────────┴───────────╯

    "heavy_outline" is the same as the "heavy_grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "heavy_outline"))
    ┏━━━━━━━━━━━┳━━━━━━━━━━━┓
    ┃ strings   ┃   numbers ┃
    ┣━━━━━━━━━━━╋━━━━━━━━━━━┫
    ┃ spam      ┃   41.9999 ┃
    ┃ eggs      ┃  451      ┃
    ┗━━━━━━━━━━━┻━━━━━━━━━━━┛

    "mixed_outline" is the same as the "mixed_grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "mixed_outline"))
    ┍━━━━━━━━━━━┯━━━━━━━━━━━┑
    │ strings   │   numbers │
    ┝━━━━━━━━━━━┿━━━━━━━━━━━┥
    │ spam      │   41.9999 │
    │ eggs      │  451      │
    ┕━━━━━━━━━━━┷━━━━━━━━━━━┙

    "double_outline" is the same as the "double_grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "double_outline"))
    ╔═══════════╦═══════════╗
    ║ strings   ║   numbers ║
    ╠═══════════╬═══════════╣
    ║ spam      ║   41.9999 ║
    ║ eggs      ║  451      ║
    ╚═══════════╩═══════════╝

    "fancy_outline" is the same as the "fancy_grid" format but doesn't draw lines between rows:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "fancy_outline"))
    ╒═══════════╤═══════════╕
    │ strings   │   numbers │
    ╞═══════════╪═══════════╡
    │ spam      │   41.9999 │
    │ eggs      │  451      │
    ╘═══════════╧═══════════╛

    "pipe" is like tables in PHP Markdown Extra extension or Pandoc
    pipe_tables:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "pipe"))
    | strings   |   numbers |
    |:----------|----------:|
    | spam      |   41.9999 |
    | eggs      |  451      |

    "presto" is like tables produce by the Presto CLI:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "presto"))
     strings   |   numbers
    -----------+-----------
     spam      |   41.9999
     eggs      |  451

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="pipe"))
    |:-----|---------:|
    | spam |  41.9999 |
    | eggs | 451      |

    "orgtbl" is like tables in Emacs org-mode and orgtbl-mode. They
    are slightly different from "pipe" format by not using colons to
    define column alignment, and using a "+" sign to indicate line
    intersections:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "orgtbl"))
    | strings   |   numbers |
    |-----------+-----------|
    | spam      |   41.9999 |
    | eggs      |  451      |


    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="orgtbl"))
    | spam |  41.9999 |
    | eggs | 451      |

    "rst" is like a simple table format from reStructuredText; please
    note that reStructuredText accepts also "grid" tables:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]],
    ...                ["strings", "numbers"], "rst"))
    =========  =========
    strings      numbers
    =========  =========
    spam         41.9999
    eggs        451
    =========  =========

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="rst"))
    ====  ========
    spam   41.9999
    eggs  451
    ====  ========

    "mediawiki" produces a table markup used in Wikipedia and on other
    MediaWiki-based sites:

    >>> print(tabulate([["strings", "numbers"], ["spam", 41.9999], ["eggs", "451.0"]],
    ...                headers="firstrow", tablefmt="mediawiki"))
    {| class="wikitable" style="text-align: left;"
    |+ <!-- caption -->
    |-
    ! strings   !! align="right"|   numbers
    |-
    | spam      || align="right"|   41.9999
    |-
    | eggs      || align="right"|  451
    |}

    "html" produces HTML markup as an html.escape'd str
    with a ._repr_html_ method so that Jupyter Lab and Notebook display the HTML
    and a .str property so that the raw HTML remains accessible
    the unsafehtml table format can be used if an unescaped HTML format is required:

    >>> print(tabulate([["strings", "numbers"], ["spam", 41.9999], ["eggs", "451.0"]],
    ...                headers="firstrow", tablefmt="html"))
    <table>
    <thead>
    <tr><th>strings  </th><th style="text-align: right;">  numbers</th></tr>
    </thead>
    <tbody>
    <tr><td>spam     </td><td style="text-align: right;">  41.9999</td></tr>
    <tr><td>eggs     </td><td style="text-align: right;"> 451     </td></tr>
    </tbody>
    </table>

    "latex" produces a tabular environment of LaTeX document markup:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="latex"))
    \begin{tabular}{lr}
    \hline
     spam &  41.9999 \\
     eggs & 451      \\
    \hline
    \end{tabular}

    "latex_raw" is similar to "latex", but doesn't escape special characters,
    such as backslash and underscore, so LaTeX commands may embedded into
    cells' values:

    >>> print(tabulate([["spam$_9$", 41.9999], ["\\emph{eggs}", "451.0"]], tablefmt="latex_raw"))
    \begin{tabular}{lr}
    \hline
     spam$_9$    &  41.9999 \\
     \emph{eggs} & 451      \\
    \hline
    \end{tabular}

    "latex_booktabs" produces a tabular environment of LaTeX document markup
    using the booktabs.sty package:

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="latex_booktabs"))
    \begin{tabular}{lr}
    \toprule
     spam &  41.9999 \\
     eggs & 451      \\
    \bottomrule
    \end{tabular}

    "latex_longtable" produces a tabular environment that can stretch along
    multiple pages, using the longtable package for LaTeX.

    >>> print(tabulate([["spam", 41.9999], ["eggs", "451.0"]], tablefmt="latex_longtable"))
    \begin{longtable}{lr}
    \hline
     spam &  41.9999 \\
     eggs & 451      \\
    \hline
    \end{longtable}


    Number parsing
    --------------
    By default, anything which can be parsed as a number is a number.
    This ensures numbers represented as strings are aligned properly.
    This can lead to weird results for particular strings such as
    specific git SHAs e.g. "42992e1" will be parsed into the number
    429920 and aligned as such.

    To completely disable number parsing (and alignment), use
    `disable_numparse=True`. For more fine grained control, a list column
    indices is used to disable number parsing only on those columns
    e.g. `disable_numparse=[0, 2]` would disable number parsing only on the
    first and third columns.

    Column Widths and Auto Line Wrapping
    ------------------------------------
    Tabulate will, by default, set the width of each column to the length of the
    longest element in that column. However, in situations where fields are expected
    to reasonably be too long to look good as a single line, tabulate can help automate
    word wrapping long fields for you. Use the parameter `maxcolwidth` to provide a
    list of maximal column widths

    >>> print(tabulate(           [('1', 'John Smith',             'This is a rather long description that might look better if it is wrapped a bit')],           headers=("Issue Id", "Author", "Description"),           maxcolwidths=[None, None, 30],           tablefmt="grid"          ))
    +------------+------------+-------------------------------+
    |   Issue Id | Author     | Description                   |
    +============+============+===============================+
    |          1 | John Smith | This is a rather long         |
    |            |            | description that might look   |
    |            |            | better if it is wrapped a bit |
    +------------+------------+-------------------------------+

    Header column width can be specified in a similar way using `maxheadercolwidth`
    """
    ...

class JupyterHTMLStr(str):
    """
    Wrap the string with a _repr_html_ method so that Jupyter
    displays the HTML table
    """
    @property
    def str(self) -> Self:
        """add a .str property so that the raw string is still accessible"""
        ...
