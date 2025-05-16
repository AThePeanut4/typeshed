"""
Python's built-in :mod:`functools` module builds several useful
utilities on top of Python's first-class function
support. ``funcutils`` generally stays in the same vein, adding to and
correcting Python's standard metaprogramming facilities.
"""

import functools
from _typeshed import Incomplete
from functools import total_ordering as total_ordering

NO_DEFAULT: Incomplete

def inspect_formatargspec(
    args,
    varargs=None,
    varkw=None,
    defaults=None,
    kwonlyargs=(),
    kwonlydefaults={},
    annotations={},
    formatarg=...,
    formatvarargs=...,
    formatvarkw=...,
    formatvalue=...,
    formatreturns=...,
    formatannotation=...,
): ...
def get_module_callables(mod, ignore=None): ...
def mro_items(type_obj): ...
def dir_dict(obj, raise_exc: bool = False): ...
def copy_function(orig, copy_dict: bool = True): ...
def partial_ordering(cls): ...

class InstancePartial(functools.partial[Incomplete]):
    """
    :class:`functools.partial` is a huge convenience for anyone
    working with Python's great first-class functions. It allows
    developers to curry arguments and incrementally create simpler
    callables for a variety of use cases.

    Unfortunately there's one big gap in its usefulness:
    methods. Partials just don't get bound as methods and
    automatically handed a reference to ``self``. The
    ``InstancePartial`` type remedies this by inheriting from
    :class:`functools.partial` and implementing the necessary
    descriptor protocol. There are no other differences in
    implementation or usage. :class:`CachedInstancePartial`, below,
    has the same ability, but is slightly more efficient.
    """
    def __get__(self, obj, obj_type): ...

class CachedInstancePartial(functools.partial[Incomplete]):
    """
    The ``CachedInstancePartial`` is virtually the same as
    :class:`InstancePartial`, adding support for method-usage to
    :class:`functools.partial`, except that upon first access, it
    caches the bound method on the associated object, speeding it up
    for future accesses, and bringing the method call overhead to
    about the same as non-``partial`` methods.

    See the :class:`InstancePartial` docstring for more details.
    """
    __name__: Incomplete
    def __set_name__(self, obj_type, name) -> None: ...
    __doc__: Incomplete
    __module__: Incomplete
    def __get__(self, obj, obj_type): ...

partial = CachedInstancePartial

def format_invocation(name: str = "", args=(), kwargs=None, **kw): ...
def format_exp_repr(obj, pos_names, req_names=None, opt_names=None, opt_key=None): ...
def format_nonexp_repr(obj, req_names=None, opt_names=None, opt_key=None): ...
def wraps(func, injected=None, expected=None, **kw): ...
def update_wrapper(wrapper, func, injected=None, expected=None, build_from=None, **kw): ...

class FunctionBuilder:
    """
    The FunctionBuilder type provides an interface for programmatically
    creating new functions, either based on existing functions or from
    scratch.

    Values are passed in at construction or set as attributes on the
    instance. For creating a new function based of an existing one,
    see the :meth:`~FunctionBuilder.from_func` classmethod. At any
    point, :meth:`~FunctionBuilder.get_func` can be called to get a
    newly compiled function, based on the values configured.

    >>> fb = FunctionBuilder('return_five', doc='returns the integer 5',
    ...                      body='return 5')
    >>> f = fb.get_func()
    >>> f()
    5
    >>> fb.varkw = 'kw'
    >>> f_kw = fb.get_func()
    >>> f_kw(ignored_arg='ignored_val')
    5

    Note that function signatures themselves changed quite a bit in
    Python 3, so several arguments are only applicable to
    FunctionBuilder in Python 3. Except for *name*, all arguments to
    the constructor are keyword arguments.

    Args:
        name (str): Name of the function.
        doc (str): `Docstring`_ for the function, defaults to empty.
        module (str): Name of the module from which this function was
            imported. Defaults to None.
        body (str): String version of the code representing the body
            of the function. Defaults to ``'pass'``, which will result
            in a function which does nothing and returns ``None``.
        args (list): List of argument names, defaults to empty list,
            denoting no arguments.
        varargs (str): Name of the catch-all variable for positional
            arguments. E.g., "args" if the resultant function is to have
            ``*args`` in the signature. Defaults to None.
        varkw (str): Name of the catch-all variable for keyword
            arguments. E.g., "kwargs" if the resultant function is to have
            ``**kwargs`` in the signature. Defaults to None.
        defaults (tuple): A tuple containing default argument values for
            those arguments that have defaults.
        kwonlyargs (list): Argument names which are only valid as
            keyword arguments. **Python 3 only.**
        kwonlydefaults (dict): A mapping, same as normal *defaults*,
            but only for the *kwonlyargs*. **Python 3 only.**
        annotations (dict): Mapping of type hints and so
            forth. **Python 3 only.**
        filename (str): The filename that will appear in
            tracebacks. Defaults to "boltons.funcutils.FunctionBuilder".
        indent (int): Number of spaces with which to indent the
            function *body*. Values less than 1 will result in an error.
        dict (dict): Any other attributes which should be added to the
            functions compiled with this FunctionBuilder.

    All of these arguments are also made available as attributes which
    can be mutated as necessary.

    .. _Docstring: https://en.wikipedia.org/wiki/Docstring#Python
    """
    name: Incomplete
    def __init__(self, name, **kw) -> None: ...
    def get_sig_str(self, with_annotations: bool = True):
        """
        Return function signature as a string.

        with_annotations is ignored on Python 2.  On Python 3 signature
        will omit annotations if it is set to False.
        """
        ...
    def get_invocation_str(self): ...
    @classmethod
    def from_func(cls, func): ...
    def get_func(self, execdict=None, add_source: bool = True, with_dict: bool = True): ...
    def get_defaults_dict(self): ...
    def get_arg_names(self, only_required: bool = False): ...
    defaults: Incomplete
    def add_arg(self, arg_name, default=..., kwonly: bool = False) -> None:
        """
        Add an argument with optional *default* (defaults to
        ``funcutils.NO_DEFAULT``). Pass *kwonly=True* to add a
        keyword-only argument
        """
        ...
    def remove_arg(self, arg_name) -> None:
        """
        Remove an argument from this FunctionBuilder's argument list. The
        resulting function will have one less argument per call to
        this function.

        Args:
            arg_name (str): The name of the argument to remove.

        Raises a :exc:`ValueError` if the argument is not present.
        """
        ...

class MissingArgument(ValueError): ...
class ExistingArgument(ValueError): ...

def noop(*args, **kwargs) -> None:
    """
    Simple function that should be used when no effect is desired.
    An alternative to checking for  an optional function type parameter.

    e.g.
    def decorate(func, pre_func=None, post_func=None):
        if pre_func:
            pre_func()
        func()
        if post_func:
            post_func()

    vs

    def decorate(func, pre_func=noop, post_func=noop):
        pre_func()
        func()
        post_func()
    """
    ...
