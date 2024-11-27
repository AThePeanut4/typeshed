"""
Wikipedia Extractor:
Extracts and cleans text from a Wikipedia database dump and stores output in a
number of files of similar size in a given directory.
Each file will contain several documents in the format:

    <doc id="" revid="" url="" title="">
        ...
        </doc>

If the program is invoked with the --json flag, then each file will
contain several documents formatted as json ojects, one per line, with
the following structure

    {"id": "", "revid": "", "url":"", "title": "", "text": "..."}

Template expansion requires preprocesssng first the whole dump and
collecting template definitions.
"""

import typing
from _typeshed import Incomplete
from collections.abc import Generator
from math import (
    acos as acos,
    asin as asin,
    atan as atan,
    ceil as ceil,
    cos as cos,
    exp as exp,
    floor as floor,
    pi as pi,
    sin as sin,
    tan as tan,
    trunc as trunc,
)

PY2: Incomplete
text_type = str
version: str
options: Incomplete
templateKeys: Incomplete
filter_disambig_page_pattern: Incomplete
g_page_total: int
g_page_articl_total: int
g_page_articl_used_total: int

def keepPage(ns, catSet, page): ...
def get_url(uid): ...

selfClosingTags: Incomplete
placeholder_tags: Incomplete

def normalizeTitle(title):
    """Normalize title"""
    ...
def unescape(text):
    """
    Removes HTML or XML character references and entities from a text string.

    :param text The HTML (or XML) source text.
    :return The plain text, as a Unicode string, if necessary.
    """
    ...

comment: Incomplete
nowiki: Incomplete

def ignoreTag(tag) -> None: ...

selfClosing_tag_patterns: Incomplete
placeholder_tag_patterns: Incomplete
preformatted: Incomplete
externalLink: Incomplete
externalLinkNoAnchor: Incomplete
bold_italic: Incomplete
bold: Incomplete
italic_quote: Incomplete
italic: Incomplete
quote_quote: Incomplete
spaces: Incomplete
dots: Incomplete

_T = typing.TypeVar("_T")

class Template(list[_T]):
    """A Template is a list of TemplateText or TemplateArgs"""
    @classmethod
    def parse(cls, body): ...
    def subst(self, params, extractor, depth: int = 0): ...

class TemplateText(text_type):
    """Fixed text of template"""
    def subst(self, params, extractor, depth): ...

class TemplateArg:
    """
    parameter to a template.
    Has a name and a default value, both of which are Templates.
    """
    name: Incomplete
    default: Incomplete
    def __init__(self, parameter) -> None:
        """:param parameter: the parts of a tplarg."""
        ...
    def subst(self, params, extractor, depth):
        """
        Substitute value for this argument from dict :param params:
        Use :param extractor: to evaluate expressions for name and default.
        Limit substitution to the maximun :param depth:.
        """
        ...

class Frame:
    title: Incomplete
    args: Incomplete
    prev: Incomplete
    depth: Incomplete
    def __init__(self, title: str = "", args=[], prev: Incomplete | None = None) -> None: ...
    def push(self, title, args): ...
    def pop(self): ...

substWords: str

class Extractor:
    """An extraction task on a article."""
    id: Incomplete
    revid: Incomplete
    title: Incomplete
    text: Incomplete
    magicWords: Incomplete
    frame: Incomplete
    recursion_exceeded_1_errs: int
    recursion_exceeded_2_errs: int
    recursion_exceeded_3_errs: int
    template_title_errs: int
    def __init__(self, id, revid, title, lines) -> None:
        """
        :param id: id of page.
        :param title: tutle of page.
        :param lines: a list of lines.
        """
        ...
    def write_output(self, out, text) -> None:
        """
        :param out: a memory file
        :param text: the text of the page
        """
        ...
    def extract(self, out) -> None:
        """:param out: a memory file."""
        ...
    def transform(self, wikitext):
        """
        Transforms wiki markup.
        @see https://www.mediawiki.org/wiki/Help:Formatting
        """
        ...
    def transform1(self, text):
        """Transform text not containing <nowiki>"""
        ...
    def wiki2text(self, text): ...
    def clean(self, text):
        """Removes irrelevant parts from :param: text."""
        ...
    maxTemplateRecursionLevels: int
    maxParameterRecursionLevels: int
    reOpen: Incomplete
    def expand(self, wikitext):
        """
        :param wikitext: the text to be expanded.

        Templates are frequently nested. Occasionally, parsing mistakes may
        cause template insertion to enter an infinite loop, for instance when
        trying to instantiate Template:Country

        {{country_{{{1}}}|{{{2}}}|{{{2}}}|size={{{size|}}}|name={{{name|}}}}}

        which is repeatedly trying to insert template 'country_', which is
        again resolved to Template:Country. The straightforward solution of
        keeping track of templates that were already inserted for the current
        article would not work, because the same template may legally be used
        more than once, with different parameters in different parts of the
        article.  Therefore, we limit the number of iterations of nested
        template inclusion.
        """
        ...
    def templateParams(self, parameters):
        """
        Build a dictionary with positional or name key to expanded parameters.
        :param parameters: the parts[1:] of a template, i.e. all except the title.
        """
        ...
    def expandTemplate(self, body):
        """
        Expands template invocation.
        :param body: the parts of a template.

        :see http://meta.wikimedia.org/wiki/Help:Expansion for an explanation
        of the process.

        See in particular: Expansion of names and values
        http://meta.wikimedia.org/wiki/Help:Expansion#Expansion_of_names_and_values

        For most parser functions all names and values are expanded,
        regardless of what is relevant for the result. The branching functions
        (#if, #ifeq, #iferror, #ifexist, #ifexpr, #switch) are exceptions.

        All names in a template call are expanded, and the titles of the
        tplargs in the template body, after which it is determined which
        values must be expanded, and for which tplargs in the template body
        the first part (default) [sic in the original doc page].

        In the case of a tplarg, any parts beyond the first are never
        expanded.  The possible name and the value of the first part is
        expanded if the title does not match a name in the template call.

        :see code for braceSubstitution at
        https://doc.wikimedia.org/mediawiki-core/master/php/html/Parser_8php_source.html#3397:
        """
        ...

def splitParts(paramsList):
    """
    :param paramsList: the parts of a template or tplarg.

    Split template parameters at the separator "|".
    separator "=".

    Template parameters often contain URLs, internal links, text or even
    template expressions, since we evaluate templates outside in.
    This is required for cases like:
      {{#if: {{{1}}} | {{lc:{{{1}}} | "parameter missing"}}
    Parameters are separated by "|" symbols. However, we
    cannot simply split the string on "|" symbols, since these
    also appear inside templates and internal links, e.g.

     {{if:|
      |{{#if:the president|
           |{{#if:|
               [[Category:Hatnote templates|A{{PAGENAME}}]]
            }}
       }}
     }}

    We split parts at the "|" symbols that are not inside any pair
    {{{...}}}, {{...}}, [[...]], {|...|}.
    """
    ...
def findMatchingBraces(text, ldelim: int = 0) -> Generator[Incomplete]:
    """:param ldelim: number of braces to match. 0 means match [[]], {{}} and {{{}}}."""
    ...
def findBalanced(text, openDelim=["[["], closeDelim=["]]"]) -> Generator[Incomplete]:
    """
    Assuming that text contains a properly balanced expression using
    :param openDelim: as opening delimiters and
    :param closeDelim: as closing delimiters.
    :return: an iterator producing pairs (start, end) of start and end
    positions in text containing a balanced expression.
    """
    ...
def if_empty(*rest):
    """
    This implements If_empty from English Wikipedia module:

       <title>Module:If empty</title>
       <ns>828</ns>
       <text>local p = {}

    function p.main(frame)
            local args = require('Module:Arguments').getArgs(frame, {wrappers = 'Template:If empty', removeBlanks = false})

            -- For backwards compatibility reasons, the first 8 parameters can be unset instead of being blank,
            -- even though there's really no legitimate use case for this. At some point, this will be removed.
            local lowestNil = math.huge
            for i = 8,1,-1 do
                    if args[i] == nil then
                            args[i] = ''
                            lowestNil = i
                    end
            end

            for k,v in ipairs(args) do
                    if v ~= '' then
                            if lowestNil &lt; k then
                                    -- If any uses of this template depend on the behavior above, add them to a tracking category.
                                    -- This is a rather fragile, convoluted, hacky way to do it, but it ensures that this module's output won't be modified
                                    -- by it.
                                    frame:extensionTag('ref', '[[Category:Instances of Template:If_empty missing arguments]]', {group = 'TrackingCategory'})
                                    frame:extensionTag('references', '', {group = 'TrackingCategory'})
                            end
                            return v
                    end
            end
    end

    return p   </text>
    """
    ...
def functionParams(args, vars):
    """
    Build a dictionary of var/value from :param: args.
    Parameters can be either named or unnamed. In the latter case, their
    name is taken fron :param: vars.
    """
    ...
def string_sub(args): ...
def string_sublength(args): ...
def string_len(args): ...
def string_find(args): ...
def string_pos(args): ...
def string_replace(args): ...
def string_rep(args): ...
def roman_main(args):
    """Convert first arg to roman numeral if <= 5000 else :return: second arg."""
    ...

modules: Incomplete

class MagicWords:
    """
    One copy in each Extractor.

    @see https://doc.wikimedia.org/mediawiki-core/master/php/MagicWord_8php_source.html
    """
    names: Incomplete
    values: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    switches: Incomplete

magicWordsRE: Incomplete

def ucfirst(string):
    """
    :return: a string with just its first character uppercase
    We can't use title() since it coverts all words.
    """
    ...
def lcfirst(string):
    """:return: a string with its first character lowercase"""
    ...
def fullyQualifiedTemplateTitle(templateTitle):
    """
    Determine the namespace of the page being included through the template
    mechanism
    """
    ...
def normalizeNamespace(ns): ...

class Infix:
    """
    Infix operators.
    The calling sequence for the infix is:
      x |op| y
    """
    function: Incomplete
    def __init__(self, function) -> None: ...
    def __ror__(self, other): ...
    def __or__(self, other): ...
    def __rlshift__(self, other): ...
    def __rshift__(self, other): ...
    def __call__(self, value1, value2): ...

ROUND: Incomplete

def sharp_expr(extr, expr):
    """Tries converting a lua expr into a Python expr."""
    ...
def sharp_if(extr, testValue, valueIfTrue, valueIfFalse: Incomplete | None = None, *args): ...
def sharp_ifeq(extr, lvalue, rvalue, valueIfTrue, valueIfFalse: Incomplete | None = None, *args): ...
def sharp_iferror(extr, test, then: str = "", Else: Incomplete | None = None, *args): ...
def sharp_switch(extr, primary, *params): ...
def sharp_invoke(module, function, args): ...

parserFunctions: Incomplete

def callParserFunction(functionName, args, extractor):
    """
    Parser functions have similar syntax as templates, except that
    the first argument is everything after the first colon.
    :return: the result of the invocation, None in case of failure.

    :param: args not yet expanded (see branching functions).
    https://www.mediawiki.org/wiki/Help:Extension:ParserFunctions
    """
    ...

reNoinclude: Incomplete
reIncludeonly: Incomplete

def define_template(title, page) -> None:
    """
    Adds a template defined in the :param page:.
    @see https://en.wikipedia.org/wiki/Help:Template#Noinclude.2C_includeonly.2C_and_onlyinclude
    """
    ...
def dropNested(text, openDelim, closeDelim):
    """A matching function for nested expressions, e.g. namespaces and tables."""
    ...
def dropSpans(spans, text):
    """Drop from text the blocks identified in :param spans:, possibly nested."""
    ...
def replaceInternalLinks(text):
    """
    Replaces internal links of the form:
    [[title |...|label]]trail

    with title concatenated with trail, when present, e.g. 's' for plural.

    See https://www.mediawiki.org/wiki/Help:Links#Internal_links
    """
    ...
def makeInternalLink(title, label): ...

wgUrlProtocols: Incomplete
EXT_LINK_URL_CLASS: str
ANCHOR_CLASS: str
ExtLinkBracketedRegex: Incomplete
EXT_IMAGE_REGEX: Incomplete

def replaceExternalLinks(text):
    """
    https://www.mediawiki.org/wiki/Help:Links#External_links
    [URL anchor text]
    """
    ...
def makeExternalLink(url, anchor):
    """Function applied to wikiLinks"""
    ...
def makeExternalImage(url, alt: str = ""): ...

tailRE: Incomplete
syntaxhighlight: Incomplete
section: Incomplete
listOpen: Incomplete
listClose: Incomplete
listItem: Incomplete

def compact(text):
    """
    Deal with headers, lists, empty sections, residuals of tables.
    :param text: convert to HTML.
    """
    ...
def handle_unicode(entity): ...

class NextFile:
    """Synchronous generation of next available file name."""
    filesPerDir: int
    path_name: Incomplete
    dir_index: int
    file_index: int
    def __init__(self, path_name) -> None: ...
    def __next__(self): ...
    next = __next__

class OutputSplitter:
    """File-like object, that splits output to multiple files of a given max size."""
    nextFile: Incomplete
    compress: Incomplete
    max_file_size: Incomplete
    file: Incomplete
    def __init__(self, nextFile, max_file_size: int = 0, compress: bool = True) -> None:
        """
        :param nextFile: a NextFile object from which to obtain filenames
            to use.
        :param max_file_size: the maximum size of each file.
        :para compress: whether to write data with bzip compression.
        """
        ...
    def reserve(self, size) -> None: ...
    def write(self, data) -> None: ...
    def close(self) -> None: ...
    def open(self, filename): ...

tagRE: Incomplete
keyRE: Incomplete
catRE: Incomplete

def load_templates(file, output_file: Incomplete | None = None) -> None:
    """
    Load templates from :param file:.
    :param output_file: file where to save templates and modules.
    """
    ...
def pages_from(input) -> Generator[Incomplete]:
    """
    Scans input extracting pages.
    :return: (id, revid, title, namespace key, page), page is a list of lines.
    """
    ...
def process_dump(input_file, template_file, out_file, file_size, file_compress, process_count) -> None:
    """
    :param input_file: name of the wikipedia dump file; '-' to read from stdin
    :param template_file: optional file with template definitions.
    :param out_file: directory where to store extracted data, or '-' for stdout
    :param file_size: max size of each extracted file, or None for no max (one file)
    :param file_compress: whether to compress files with bzip.
    :param process_count: number of extraction processes to spawn.
    """
    ...
def extract_process(opts, i, jobs_queue, output_queue) -> None:
    """
    Pull tuples of raw page content, do CPU/regex-heavy fixup, push finished text
    :param i: process id.
    :param jobs_queue: where to get jobs.
    :param output_queue: where to queue extracted text for output.
    """
    ...

report_period: int

def reduce_process(
    opts, output_queue, spool_length, out_file: Incomplete | None = None, file_size: int = 0, file_compress: bool = True
) -> None:
    """
    Pull finished article text, write series of files (or stdout)
    :param opts: global parameters.
    :param output_queue: text to be output.
    :param spool_length: spool length.
    :param out_file: filename where to print.
    :param file_size: max file size.
    :param file_compress: whether to compress output.
    """
    ...

minFileSize: Incomplete

def main() -> None: ...
def createLogger(quiet, debug, log_file) -> None: ...
