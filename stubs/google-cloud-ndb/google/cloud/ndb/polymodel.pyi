from _typeshed import Incomplete

from google.cloud.ndb import model

class _ClassKeyProperty(model.StringProperty):
    """
    Property to store the 'class key' of a polymorphic class.

    The class key is a list of strings describing a polymorphic entity's
    place within its class hierarchy.  This property is automatically
    calculated.  For example:

    .. testsetup:: class-key-property

        from google.cloud import ndb


        class Animal(ndb.PolyModel):
            pass


        class Feline(Animal):
            pass


        class Cat(Feline):
            pass

    .. doctest:: class-key-property

        >>> Animal().class_
        ['Animal']
        >>> Feline().class_
        ['Animal', 'Feline']
        >>> Cat().class_
        ['Animal', 'Feline', 'Cat']
    """
    def __init__(self, name=..., indexed: bool = ...) -> None:
        """
        Constructor.

        If you really want to you can give this a different datastore name
        or make it unindexed.  For example:

        .. code-block:: python

            class Foo(PolyModel):
                class_ = _ClassKeyProperty(indexed=False)
        """
        ...

class PolyModel(model.Model):
    class_: Incomplete
