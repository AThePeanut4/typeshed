"""
:mod:`itertools` is full of great examples of Python generator
usage. However, there are still some critical gaps. ``iterutils``
fills many of those gaps with featureful, tested, and Pythonic
solutions.

Many of the functions below have two versions, one which
returns an iterator (denoted by the ``*_iter`` naming pattern), and a
shorter-named convenience form that returns a list. Some of the
following are based on examples in itertools docs.
"""

from _typeshed import Incomplete
from collections.abc import Generator

def is_iterable(obj) -> bool:
    """
    Similar in nature to :func:`callable`, ``is_iterable`` returns
    ``True`` if an object is `iterable`_, ``False`` if not.

    >>> is_iterable([])
    True
    >>> is_iterable(object())
    False

    .. _iterable: https://docs.python.org/2/glossary.html#term-iterable
    """
    ...
def is_scalar(obj) -> bool:
    """
    A near-mirror of :func:`is_iterable`. Returns ``False`` if an
    object is an iterable container type. Strings are considered
    scalar as well, because strings are more often treated as whole
    values as opposed to iterables of 1-character substrings.

    >>> is_scalar(object())
    True
    >>> is_scalar(range(10))
    False
    >>> is_scalar('hello')
    True
    """
    ...
def is_collection(obj) -> bool:
    """
    The opposite of :func:`is_scalar`.  Returns ``True`` if an object
    is an iterable other than a string.

    >>> is_collection(object())
    False
    >>> is_collection(range(10))
    True
    >>> is_collection('hello')
    False
    """
    ...
def split(src, sep=None, maxsplit=None):
    """
    Splits an iterable based on a separator. Like :meth:`str.split`,
    but for all iterables. Returns a list of lists.

    >>> split(['hi', 'hello', None, None, 'sup', None, 'soap', None])
    [['hi', 'hello'], ['sup'], ['soap']]

    See :func:`split_iter` docs for more info.
    """
    ...
def split_iter(src, sep=None, maxsplit=None) -> Generator[Incomplete, None, Incomplete]:
    """
    Splits an iterable based on a separator, *sep*, a max of
    *maxsplit* times (no max by default). *sep* can be:

      * a single value
      * an iterable of separators
      * a single-argument callable that returns True when a separator is
        encountered

    ``split_iter()`` yields lists of non-separator values. A separator will
    never appear in the output.

    >>> list(split_iter(['hi', 'hello', None, None, 'sup', None, 'soap', None]))
    [['hi', 'hello'], ['sup'], ['soap']]

    Note that ``split_iter`` is based on :func:`str.split`, so if
    *sep* is ``None``, ``split()`` **groups** separators. If empty lists
    are desired between two contiguous ``None`` values, simply use
    ``sep=[None]``:

    >>> list(split_iter(['hi', 'hello', None, None, 'sup', None]))
    [['hi', 'hello'], ['sup']]
    >>> list(split_iter(['hi', 'hello', None, None, 'sup', None], sep=[None]))
    [['hi', 'hello'], [], ['sup'], []]

    Using a callable separator:

    >>> falsy_sep = lambda x: not x
    >>> list(split_iter(['hi', 'hello', None, '', 'sup', False], falsy_sep))
    [['hi', 'hello'], [], ['sup'], []]

    See :func:`split` for a list-returning version.
    """
    ...
def lstrip(iterable, strip_value=None):
    """
    Strips values from the beginning of an iterable. Stripped items will
    match the value of the argument strip_value. Functionality is analogous
    to that of the method str.lstrip. Returns a list.

    >>> lstrip(['Foo', 'Bar', 'Bam'], 'Foo')
    ['Bar', 'Bam']
    """
    ...
def lstrip_iter(iterable, strip_value=None) -> Generator[Incomplete, None, None]:
    """
    Strips values from the beginning of an iterable. Stripped items will
    match the value of the argument strip_value. Functionality is analogous
    to that of the method str.lstrip. Returns a generator.

    >>> list(lstrip_iter(['Foo', 'Bar', 'Bam'], 'Foo'))
    ['Bar', 'Bam']
    """
    ...
def rstrip(iterable, strip_value=None):
    """
    Strips values from the end of an iterable. Stripped items will
    match the value of the argument strip_value. Functionality is analogous
    to that of the method str.rstrip. Returns a list.

    >>> rstrip(['Foo', 'Bar', 'Bam'], 'Bam')
    ['Foo', 'Bar']
    """
    ...
def rstrip_iter(iterable, strip_value=None) -> Generator[Incomplete, None, None]:
    """
    Strips values from the end of an iterable. Stripped items will
    match the value of the argument strip_value. Functionality is analogous
    to that of the method str.rstrip. Returns a generator.

    >>> list(rstrip_iter(['Foo', 'Bar', 'Bam'], 'Bam'))
    ['Foo', 'Bar']
    """
    ...
def strip(iterable, strip_value=None):
    """
    Strips values from the beginning and end of an iterable. Stripped items
    will match the value of the argument strip_value. Functionality is
    analogous to that of the method str.strip. Returns a list.

    >>> strip(['Fu', 'Foo', 'Bar', 'Bam', 'Fu'], 'Fu')
    ['Foo', 'Bar', 'Bam']
    """
    ...
def strip_iter(iterable, strip_value=None):
    """
    Strips values from the beginning and end of an iterable. Stripped items
    will match the value of the argument strip_value. Functionality is
    analogous to that of the method str.strip. Returns a generator.

    >>> list(strip_iter(['Fu', 'Foo', 'Bar', 'Bam', 'Fu'], 'Fu'))
    ['Foo', 'Bar', 'Bam']
    """
    ...
def chunked(src, size, count=None, **kw):
    """
    Returns a list of *count* chunks, each with *size* elements,
    generated from iterable *src*. If *src* is not evenly divisible by
    *size*, the final chunk will have fewer than *size* elements.
    Provide the *fill* keyword argument to provide a pad value and
    enable padding, otherwise no padding will take place.

    >>> chunked(range(10), 3)
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    >>> chunked(range(10), 3, fill=None)
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, None, None]]
    >>> chunked(range(10), 3, count=2)
    [[0, 1, 2], [3, 4, 5]]

    See :func:`chunked_iter` for more info.
    """
    ...
def chunked_iter(src, size, **kw) -> Generator[Incomplete, None, Incomplete]:
    """
    Generates *size*-sized chunks from *src* iterable. Unless the
    optional *fill* keyword argument is provided, iterables not evenly
    divisible by *size* will have a final chunk that is smaller than
    *size*.

    >>> list(chunked_iter(range(10), 3))
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    >>> list(chunked_iter(range(10), 3, fill=None))
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, None, None]]

    Note that ``fill=None`` in fact uses ``None`` as the fill value.
    """
    ...
def chunk_ranges(
    input_size: int, chunk_size: int, input_offset: int = 0, overlap_size: int = 0, align: bool = False
) -> Generator[tuple[int, int], None, None]:
    """
    Generates *chunk_size*-sized chunk ranges for an input with length *input_size*.
    Optionally, a start of the input can be set via *input_offset*, and
    and overlap between the chunks may be specified via *overlap_size*.
    Also, if *align* is set to *True*, any items with *i % (chunk_size-overlap_size) == 0*
    are always at the beginning of the chunk.

    Returns an iterator of (start, end) tuples, one tuple per chunk.

    >>> list(chunk_ranges(input_offset=10, input_size=10, chunk_size=5))
    [(10, 15), (15, 20)]
    >>> list(chunk_ranges(input_offset=10, input_size=10, chunk_size=5, overlap_size=1))
    [(10, 15), (14, 19), (18, 20)]
    >>> list(chunk_ranges(input_offset=10, input_size=10, chunk_size=5, overlap_size=2))
    [(10, 15), (13, 18), (16, 20)]

    >>> list(chunk_ranges(input_offset=4, input_size=15, chunk_size=5, align=False))
    [(4, 9), (9, 14), (14, 19)]
    >>> list(chunk_ranges(input_offset=4, input_size=15, chunk_size=5, align=True))
    [(4, 5), (5, 10), (10, 15), (15, 19)]

    >>> list(chunk_ranges(input_offset=2, input_size=15, chunk_size=5, overlap_size=1, align=False))
    [(2, 7), (6, 11), (10, 15), (14, 17)]
    >>> list(chunk_ranges(input_offset=2, input_size=15, chunk_size=5, overlap_size=1, align=True))
    [(2, 5), (4, 9), (8, 13), (12, 17)]
    >>> list(chunk_ranges(input_offset=3, input_size=15, chunk_size=5, overlap_size=1, align=True))
    [(3, 5), (4, 9), (8, 13), (12, 17), (16, 18)]
    """
    ...
def pairwise(src, end=...):
    """
    Convenience function for calling :func:`windowed` on *src*, with
    *size* set to 2.

    >>> pairwise(range(5))
    [(0, 1), (1, 2), (2, 3), (3, 4)]
    >>> pairwise([])
    []

    Unless *end* is set, the number of pairs is always one less than 
    the number of elements in the iterable passed in, except on an empty input, 
    which will return an empty list.

    With *end* set, a number of pairs equal to the length of *src* is returned,
    with the last item of the last pair being equal to *end*.

    >>> list(pairwise(range(3), end=None))
    [(0, 1), (1, 2), (2, None)]

    This way, *end* values can be useful as sentinels to signal the end of the iterable.
    """
    ...
def pairwise_iter(src, end=...):
    """
    Convenience function for calling :func:`windowed_iter` on *src*,
    with *size* set to 2.

    >>> list(pairwise_iter(range(5)))
    [(0, 1), (1, 2), (2, 3), (3, 4)]
    >>> list(pairwise_iter([]))
    []

    Unless *end* is set, the number of pairs is always one less 
    than the number of elements in the iterable passed in, 
    or zero, when *src* is empty.

    With *end* set, a number of pairs equal to the length of *src* is returned,
    with the last item of the last pair being equal to *end*. 

    >>> list(pairwise_iter(range(3), end=None))
    [(0, 1), (1, 2), (2, None)]    

    This way, *end* values can be useful as sentinels to signal the end
    of the iterable. For infinite iterators, setting *end* has no effect.
    """
    ...
def windowed(src, size, fill=...):
    """
    Returns tuples with exactly length *size*. If *fill* is unset 
    and the iterable is too short to make a window of length *size*, 
    no tuples are returned. See :func:`windowed_iter` for more.
    """
    ...
def windowed_iter(src, size, fill=...):
    """
    Returns tuples with length *size* which represent a sliding
    window over iterable *src*.

    >>> list(windowed_iter(range(7), 3))
    [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

    If *fill* is unset, and the iterable is too short to make a window 
    of length *size*, then no window tuples are returned.

    >>> list(windowed_iter(range(3), 5))
    []

    With *fill* set, the iterator always yields a number of windows
    equal to the length of the *src* iterable.

    >>> windowed(range(4), 3, fill=None)
    [(0, 1, 2), (1, 2, 3), (2, 3, None), (3, None, None)]

    This way, *fill* values can be useful to signal the end of the iterable.
    For infinite iterators, setting *fill* has no effect.
    """
    ...
def xfrange(stop, start=None, step: float = 1.0) -> Generator[Incomplete, None, None]:
    """
    Same as :func:`frange`, but generator-based instead of returning a
    list.

    >>> tuple(xfrange(1, 3, step=0.75))
    (1.0, 1.75, 2.5)

    See :func:`frange` for more details.
    """
    ...
def frange(stop, start=None, step: float = 1.0):
    """
    A :func:`range` clone for float-based ranges.

    >>> frange(5)
    [0.0, 1.0, 2.0, 3.0, 4.0]
    >>> frange(6, step=1.25)
    [0.0, 1.25, 2.5, 3.75, 5.0]
    >>> frange(100.5, 101.5, 0.25)
    [100.5, 100.75, 101.0, 101.25]
    >>> frange(5, 0)
    []
    >>> frange(5, 0, step=-1.25)
    [5.0, 3.75, 2.5, 1.25]
    """
    ...
def backoff(start, stop, count=None, factor: float = 2.0, jitter: bool = False):
    """
    Returns a list of geometrically-increasing floating-point numbers,
    suitable for usage with `exponential backoff`_. Exactly like
    :func:`backoff_iter`, but without the ``'repeat'`` option for
    *count*. See :func:`backoff_iter` for more details.

    .. _exponential backoff: https://en.wikipedia.org/wiki/Exponential_backoff

    >>> backoff(1, 10)
    [1.0, 2.0, 4.0, 8.0, 10.0]
    """
    ...
def backoff_iter(start, stop, count=None, factor: float = 2.0, jitter: bool = False) -> Generator[Incomplete, None, None]:
    """
    Generates a sequence of geometrically-increasing floats, suitable
    for usage with `exponential backoff`_. Starts with *start*,
    increasing by *factor* until *stop* is reached, optionally
    stopping iteration once *count* numbers are yielded. *factor*
    defaults to 2. In general retrying with properly-configured
    backoff creates a better-behaved component for a larger service
    ecosystem.

    .. _exponential backoff: https://en.wikipedia.org/wiki/Exponential_backoff

    >>> list(backoff_iter(1.0, 10.0, count=5))
    [1.0, 2.0, 4.0, 8.0, 10.0]
    >>> list(backoff_iter(1.0, 10.0, count=8))
    [1.0, 2.0, 4.0, 8.0, 10.0, 10.0, 10.0, 10.0]
    >>> list(backoff_iter(0.25, 100.0, factor=10))
    [0.25, 2.5, 25.0, 100.0]

    A simplified usage example:

    .. code-block:: python

      for timeout in backoff_iter(0.25, 5.0):
          try:
              res = network_call()
              break
          except Exception as e:
              log(e)
              time.sleep(timeout)

    An enhancement for large-scale systems would be to add variation,
    or *jitter*, to timeout values. This is done to avoid a thundering
    herd on the receiving end of the network call.

    Finally, for *count*, the special value ``'repeat'`` can be passed to
    continue yielding indefinitely.

    Args:

        start (float): Positive number for baseline.
        stop (float): Positive number for maximum.
        count (int): Number of steps before stopping
            iteration. Defaults to the number of steps between *start* and
            *stop*. Pass the string, `'repeat'`, to continue iteration
            indefinitely.
        factor (float): Rate of exponential increase. Defaults to `2.0`,
            e.g., `[1, 2, 4, 8, 16]`.
        jitter (float): A factor between `-1.0` and `1.0`, used to
            uniformly randomize and thus spread out timeouts in a distributed
            system, avoiding rhythm effects. Positive values use the base
            backoff curve as a maximum, negative values use the curve as a
            minimum. Set to 1.0 or `True` for a jitter approximating
            Ethernet's time-tested backoff solution. Defaults to `False`.
    """
    ...
def bucketize(src, key=..., value_transform=None, key_filter=None):
    """
    Group values in the *src* iterable by the value returned by *key*.

    >>> bucketize(range(5))
    {False: [0], True: [1, 2, 3, 4]}
    >>> is_odd = lambda x: x % 2 == 1
    >>> bucketize(range(5), is_odd)
    {False: [0, 2, 4], True: [1, 3]}

    *key* is :class:`bool` by default, but can either be a callable or a string or a list
    if it is a string, it is the name of the attribute on which to bucketize objects.

    >>> bucketize([1+1j, 2+2j, 1, 2], key='real')
    {1.0: [(1+1j), 1], 2.0: [(2+2j), 2]}

    if *key* is a list, it contains the buckets where to put each object

    >>> bucketize([1,2,365,4,98],key=[0,1,2,0,2])
    {0: [1, 4], 1: [2], 2: [365, 98]}


    Value lists are not deduplicated:

    >>> bucketize([None, None, None, 'hello'])
    {False: [None, None, None], True: ['hello']}

    Bucketize into more than 3 groups

    >>> bucketize(range(10), lambda x: x % 3)
    {0: [0, 3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

    ``bucketize`` has a couple of advanced options useful in certain
    cases.  *value_transform* can be used to modify values as they are
    added to buckets, and *key_filter* will allow excluding certain
    buckets from being collected.

    >>> bucketize(range(5), value_transform=lambda x: x*x)
    {False: [0], True: [1, 4, 9, 16]}

    >>> bucketize(range(10), key=lambda x: x % 3, key_filter=lambda k: k % 3 != 1)
    {0: [0, 3, 6, 9], 2: [2, 5, 8]}

    Note in some of these examples there were at most two keys, ``True`` and
    ``False``, and each key present has a list with at least one
    item. See :func:`partition` for a version specialized for binary
    use cases.
    """
    ...
def partition(src, key=...):
    """
    No relation to :meth:`str.partition`, ``partition`` is like
    :func:`bucketize`, but for added convenience returns a tuple of
    ``(truthy_values, falsy_values)``.

    >>> nonempty, empty = partition(['', '', 'hi', '', 'bye'])
    >>> nonempty
    ['hi', 'bye']

    *key* defaults to :class:`bool`, but can be carefully overridden to
    use either a function that returns either ``True`` or ``False`` or
    a string name of the attribute on which to partition objects.

    >>> import string
    >>> is_digit = lambda x: x in string.digits
    >>> decimal_digits, hexletters = partition(string.hexdigits, is_digit)
    >>> ''.join(decimal_digits), ''.join(hexletters)
    ('0123456789', 'abcdefABCDEF')
    """
    ...
def unique(src, key=None):
    """
    ``unique()`` returns a list of unique values, as determined by
    *key*, in the order they first appeared in the input iterable,
    *src*.

    >>> ones_n_zeros = '11010110001010010101010'
    >>> ''.join(unique(ones_n_zeros))
    '10'

    See :func:`unique_iter` docs for more details.
    """
    ...
def unique_iter(src, key=None) -> Generator[Incomplete, None, Incomplete]:
    """
    Yield unique elements from the iterable, *src*, based on *key*,
    in the order in which they first appeared in *src*.

    >>> repetitious = [1, 2, 3] * 10
    >>> list(unique_iter(repetitious))
    [1, 2, 3]

    By default, *key* is the object itself, but *key* can either be a
    callable or, for convenience, a string name of the attribute on
    which to uniqueify objects, falling back on identity when the
    attribute is not present.

    >>> pleasantries = ['hi', 'hello', 'ok', 'bye', 'yes']
    >>> list(unique_iter(pleasantries, key=lambda x: len(x)))
    ['hi', 'hello', 'bye']
    """
    ...
def redundant(src, key=None, groups: bool = False):
    """
    The complement of :func:`unique()`.

    By default returns non-unique/duplicate values as a list of the
    *first* redundant value in *src*. Pass ``groups=True`` to get
    groups of all values with redundancies, ordered by position of the
    first redundant value. This is useful in conjunction with some
    normalizing *key* function.

    >>> redundant([1, 2, 3, 4])
    []
    >>> redundant([1, 2, 3, 2, 3, 3, 4])
    [2, 3]
    >>> redundant([1, 2, 3, 2, 3, 3, 4], groups=True)
    [[2, 2], [3, 3, 3]]

    An example using a *key* function to do case-insensitive
    redundancy detection.

    >>> redundant(['hi', 'Hi', 'HI', 'hello'], key=str.lower)
    ['Hi']
    >>> redundant(['hi', 'Hi', 'HI', 'hello'], groups=True, key=str.lower)
    [['hi', 'Hi', 'HI']]

    *key* should also be used when the values in *src* are not hashable.

    .. note::

       This output of this function is designed for reporting
       duplicates in contexts when a unique input is desired. Due to
       the grouped return type, there is no streaming equivalent of
       this function for the time being.
    """
    ...
def one(src, default=None, key=None):
    """
    Along the same lines as builtins, :func:`all` and :func:`any`, and
    similar to :func:`first`, ``one()`` returns the single object in
    the given iterable *src* that evaluates to ``True``, as determined
    by callable *key*. If unset, *key* defaults to :class:`bool`. If
    no such objects are found, *default* is returned. If *default* is
    not passed, ``None`` is returned.

    If *src* has more than one object that evaluates to ``True``, or
    if there is no object that fulfills such condition, return
    *default*. It's like an `XOR`_ over an iterable.

    >>> one((True, False, False))
    True
    >>> one((True, False, True))
    >>> one((0, 0, 'a'))
    'a'
    >>> one((0, False, None))
    >>> one((True, True), default=False)
    False
    >>> bool(one(('', 1)))
    True
    >>> one((10, 20, 30, 42), key=lambda i: i > 40)
    42

    See `Martín Gaitán's original repo`_ for further use cases.

    .. _Martín Gaitán's original repo: https://github.com/mgaitan/one
    .. _XOR: https://en.wikipedia.org/wiki/Exclusive_or
    """
    ...
def first(iterable, default=None, key=None):
    """
    Return first element of *iterable* that evaluates to ``True``, else
    return ``None`` or optional *default*. Similar to :func:`one`.

    >>> first([0, False, None, [], (), 42])
    42
    >>> first([0, False, None, [], ()]) is None
    True
    >>> first([0, False, None, [], ()], default='ohai')
    'ohai'
    >>> import re
    >>> m = first(re.match(regex, 'abc') for regex in ['b.*', 'a(.*)'])
    >>> m.group(1)
    'bc'

    The optional *key* argument specifies a one-argument predicate function
    like that used for *filter()*.  The *key* argument, if supplied, should be
    in keyword form. For example, finding the first even number in an iterable:

    >>> first([1, 1, 3, 4, 5], key=lambda x: x % 2 == 0)
    4

    Contributed by Hynek Schlawack, author of `the original standalone module`_.

    .. _the original standalone module: https://github.com/hynek/first
    """
    ...
def flatten_iter(iterable) -> Generator[Incomplete, None, None]:
    """
    ``flatten_iter()`` yields all the elements from *iterable* while
    collapsing any nested iterables.

    >>> nested = [[1, 2], [[3], [4, 5]]]
    >>> list(flatten_iter(nested))
    [1, 2, 3, 4, 5]
    """
    ...
def flatten(iterable):
    """
    ``flatten()`` returns a collapsed list of all the elements from
    *iterable* while collapsing any nested iterables.

    >>> nested = [[1, 2], [[3], [4, 5]]]
    >>> flatten(nested)
    [1, 2, 3, 4, 5]
    """
    ...
def same(iterable, ref=...):
    """
    ``same()`` returns ``True`` when all values in *iterable* are
    equal to one another, or optionally a reference value,
    *ref*. Similar to :func:`all` and :func:`any` in that it evaluates
    an iterable and returns a :class:`bool`. ``same()`` returns
    ``True`` for empty iterables.

    >>> same([])
    True
    >>> same([1])
    True
    >>> same(['a', 'a', 'a'])
    True
    >>> same(range(20))
    False
    >>> same([[], []])
    True
    >>> same([[], []], ref='test')
    False
    """
    ...
def default_visit(path, key, value): ...
def default_enter(path, key, value): ...
def default_exit(path, key, old_parent, new_parent, new_items): ...
def remap(root, visit=..., enter=..., exit=..., **kwargs):
    """
    The remap ("recursive map") function is used to traverse and
    transform nested structures. Lists, tuples, sets, and dictionaries
    are just a few of the data structures nested into heterogeneous
    tree-like structures that are so common in programming.
    Unfortunately, Python's built-in ways to manipulate collections
    are almost all flat. List comprehensions may be fast and succinct,
    but they do not recurse, making it tedious to apply quick changes
    or complex transforms to real-world data.

    remap goes where list comprehensions cannot.

    Here's an example of removing all Nones from some data:

    >>> from pprint import pprint
    >>> reviews = {'Star Trek': {'TNG': 10, 'DS9': 8.5, 'ENT': None},
    ...            'Babylon 5': 6, 'Dr. Who': None}
    >>> pprint(remap(reviews, lambda p, k, v: v is not None))
    {'Babylon 5': 6, 'Star Trek': {'DS9': 8.5, 'TNG': 10}}

    Notice how both Nones have been removed despite the nesting in the
    dictionary. Not bad for a one-liner, and that's just the beginning.
    See `this remap cookbook`_ for more delicious recipes.

    .. _this remap cookbook: http://sedimental.org/remap.html

    remap takes four main arguments: the object to traverse and three
    optional callables which determine how the remapped object will be
    created.

    Args:

        root: The target object to traverse. By default, remap
            supports iterables like :class:`list`, :class:`tuple`,
            :class:`dict`, and :class:`set`, but any object traversable by
            *enter* will work.
        visit (callable): This function is called on every item in
            *root*. It must accept three positional arguments, *path*,
            *key*, and *value*. *path* is simply a tuple of parents'
            keys. *visit* should return the new key-value pair. It may
            also return ``True`` as shorthand to keep the old item
            unmodified, or ``False`` to drop the item from the new
            structure. *visit* is called after *enter*, on the new parent.

            The *visit* function is called for every item in root,
            including duplicate items. For traversable values, it is
            called on the new parent object, after all its children
            have been visited. The default visit behavior simply
            returns the key-value pair unmodified.
        enter (callable): This function controls which items in *root*
            are traversed. It accepts the same arguments as *visit*: the
            path, the key, and the value of the current item. It returns a
            pair of the blank new parent, and an iterator over the items
            which should be visited. If ``False`` is returned instead of
            an iterator, the value will not be traversed.

            The *enter* function is only called once per unique value. The
            default enter behavior support mappings, sequences, and
            sets. Strings and all other iterables will not be traversed.
        exit (callable): This function determines how to handle items
            once they have been visited. It gets the same three
            arguments as the other functions -- *path*, *key*, *value*
            -- plus two more: the blank new parent object returned
            from *enter*, and a list of the new items, as remapped by
            *visit*.

            Like *enter*, the *exit* function is only called once per
            unique value. The default exit behavior is to simply add
            all new items to the new parent, e.g., using
            :meth:`list.extend` and :meth:`dict.update` to add to the
            new parent. Immutable objects, such as a :class:`tuple` or
            :class:`namedtuple`, must be recreated from scratch, but
            use the same type as the new parent passed back from the
            *enter* function.
        reraise_visit (bool): A pragmatic convenience for the *visit*
            callable. When set to ``False``, remap ignores any errors
            raised by the *visit* callback. Items causing exceptions
            are kept. See examples for more details.
        trace (bool): Pass ``trace=True`` to print out the entire
            traversal. Or pass a tuple of ``'visit'``, ``'enter'``,
            or ``'exit'`` to print only the selected events.

    remap is designed to cover the majority of cases with just the
    *visit* callable. While passing in multiple callables is very
    empowering, remap is designed so very few cases should require
    passing more than one function.

    When passing *enter* and *exit*, it's common and easiest to build
    on the default behavior. Simply add ``from boltons.iterutils import
    default_enter`` (or ``default_exit``), and have your enter/exit
    function call the default behavior before or after your custom
    logic. See `this example`_.

    Duplicate and self-referential objects (aka reference loops) are
    automatically handled internally, `as shown here`_.

    .. _this example: http://sedimental.org/remap.html#sort_all_lists
    .. _as shown here: http://sedimental.org/remap.html#corner_cases
    """
    ...

class PathAccessError(KeyError, IndexError, TypeError):
    """
    An amalgamation of KeyError, IndexError, and TypeError,
    representing what can occur when looking up a path in a nested
    object.
    """
    exc: Incomplete
    seg: Incomplete
    path: Incomplete
    def __init__(self, exc, seg, path) -> None: ...

def get_path(root, path, default=...):
    """
    Retrieve a value from a nested object via a tuple representing the
    lookup path.

    >>> root = {'a': {'b': {'c': [[1], [2], [3]]}}}
    >>> get_path(root, ('a', 'b', 'c', 2, 0))
    3

    The path tuple format is intentionally consistent with that of
    :func:`remap`, but a single dotted string can also be passed.

    One of get_path's chief aims is improved error messaging. EAFP is
    great, but the error messages are not.

    For instance, ``root['a']['b']['c'][2][1]`` gives back
    ``IndexError: list index out of range``

    What went out of range where? get_path currently raises
    ``PathAccessError: could not access 2 from path ('a', 'b', 'c', 2,
    1), got error: IndexError('list index out of range',)``, a
    subclass of IndexError and KeyError.

    You can also pass a default that covers the entire operation,
    should the lookup fail at any level.

    Args:
       root: The target nesting of dictionaries, lists, or other
          objects supporting ``__getitem__``.
       path (tuple): A sequence of strings and integers to be successively
          looked up within *root*. A dot-separated (``a.b``) string may 
          also be passed.
       default: The value to be returned should any
          ``PathAccessError`` exceptions be raised.
    """
    ...
def research(root, query=..., reraise: bool = False, enter=...):
    """
    The :func:`research` function uses :func:`remap` to recurse over
    any data nested in *root*, and find values which match a given
    criterion, specified by the *query* callable.

    Results are returned as a list of ``(path, value)`` pairs. The
    paths are tuples in the same format accepted by
    :func:`get_path`. This can be useful for comparing values nested
    in two or more different structures.

    Here's a simple example that finds all integers:

    >>> root = {'a': {'b': 1, 'c': (2, 'd', 3)}, 'e': None}
    >>> res = research(root, query=lambda p, k, v: isinstance(v, int))
    >>> print(sorted(res))
    [(('a', 'b'), 1), (('a', 'c', 0), 2), (('a', 'c', 2), 3)]

    Note how *query* follows the same, familiar ``path, key, value``
    signature as the ``visit`` and ``enter`` functions on
    :func:`remap`, and returns a :class:`bool`.

    Args:
       root: The target object to search. Supports the same types of
          objects as :func:`remap`, including :class:`list`,
          :class:`tuple`, :class:`dict`, and :class:`set`.
       query (callable): The function called on every object to
          determine whether to include it in the search results. The
          callable must accept three arguments, *path*, *key*, and
          *value*, commonly abbreviated *p*, *k*, and *v*, same as
          *enter* and *visit* from :func:`remap`.
       reraise (bool): Whether to reraise exceptions raised by *query*
          or to simply drop the result that caused the error.


    With :func:`research` it's easy to inspect the details of a data
    structure, like finding values that are at a certain depth (using
    ``len(p)``) and much more. If more advanced functionality is
    needed, check out the code and make your own :func:`remap`
    wrapper, and consider `submitting a patch`_!

    .. _submitting a patch: https://github.com/mahmoud/boltons/pulls
    """
    ...

class GUIDerator:
    """
    The GUIDerator is an iterator that yields a globally-unique
    identifier (GUID) on every iteration. The GUIDs produced are
    hexadecimal strings.

    Testing shows it to be around 12x faster than the uuid module. By
    default it is also more compact, partly due to its default 96-bit
    (24-hexdigit) length. 96 bits of randomness means that there is a
    1 in 2 ^ 32 chance of collision after 2 ^ 64 iterations. If more
    or less uniqueness is desired, the *size* argument can be adjusted
    accordingly.

    Args:
        size (int): character length of the GUID, defaults to 24. Lengths
                    between 20 and 36 are considered valid.

    The GUIDerator has built-in fork protection that causes it to
    detect a fork on next iteration and reseed accordingly.
    """
    size: Incomplete
    count: Incomplete
    def __init__(self, size: int = 24) -> None: ...
    pid: Incomplete
    salt: Incomplete
    def reseed(self) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Incomplete

class SequentialGUIDerator(GUIDerator):
    """
    Much like the standard GUIDerator, the SequentialGUIDerator is an
    iterator that yields a globally-unique identifier (GUID) on every
    iteration. The GUIDs produced are hexadecimal strings.

    The SequentialGUIDerator differs in that it picks a starting GUID
    value and increments every iteration. This yields GUIDs which are
    of course unique, but also ordered and lexicographically sortable.

    The SequentialGUIDerator is around 50% faster than the normal
    GUIDerator, making it almost 20x as fast as the built-in uuid
    module. By default it is also more compact, partly due to its
    96-bit (24-hexdigit) default length. 96 bits of randomness means that
    there is a 1 in 2 ^ 32 chance of collision after 2 ^ 64
    iterations. If more or less uniqueness is desired, the *size*
    argument can be adjusted accordingly.

    Args:
        size (int): character length of the GUID, defaults to 24.

    Note that with SequentialGUIDerator there is a chance of GUIDs
    growing larger than the size configured. The SequentialGUIDerator
    has built-in fork protection that causes it to detect a fork on
    next iteration and reseed accordingly.
    """
    start: Incomplete
    def reseed(self) -> None: ...
    def __next__(self): ...
    next: Incomplete

guid_iter: Incomplete
seq_guid_iter: Incomplete

def soft_sorted(iterable, first=None, last=None, key=None, reverse: bool = False):
    """
    For when you care about the order of some elements, but not about
    others.

    Use this to float to the top and/or sink to the bottom a specific
    ordering, while sorting the rest of the elements according to
    normal :func:`sorted` rules.

    >>> soft_sorted(['two', 'b', 'one', 'a'], first=['one', 'two'])
    ['one', 'two', 'a', 'b']
    >>> soft_sorted(range(7), first=[6, 15], last=[2, 4], reverse=True)
    [6, 5, 3, 1, 0, 2, 4]
    >>> import string
    >>> ''.join(soft_sorted(string.hexdigits, first='za1', last='b', key=str.lower))
    'aA1023456789cCdDeEfFbB'

    Args:
       iterable (list): A list or other iterable to sort.
       first (list): A sequence to enforce for elements which should
          appear at the beginning of the returned list.
       last (list): A sequence to enforce for elements which should
          appear at the end of the returned list.
       key (callable): Callable used to generate a comparable key for
          each item to be sorted, same as the key in
          :func:`sorted`. Note that entries in *first* and *last*
          should be the keys for the items. Defaults to
          passthrough/the identity function.
       reverse (bool): Whether or not elements not explicitly ordered
          by *first* and *last* should be in reverse order or not.

    Returns a new list in sorted order.
    """
    ...
def untyped_sorted(iterable, key=None, reverse: bool = False):
    """
    A version of :func:`sorted` which will happily sort an iterable of
    heterogeneous types and return a new list, similar to legacy Python's
    behavior.

    >>> untyped_sorted(['abc', 2.0, 1, 2, 'def'])
    [1, 2.0, 2, 'abc', 'def']

    Note how mutually orderable types are sorted as expected, as in
    the case of the integers and floats above.

    .. note::

       Results may vary across Python versions and builds, but the
       function will produce a sorted list, except in the case of
       explicitly unorderable objects.
    """
    ...
