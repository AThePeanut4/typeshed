""""""

from _typeshed import Incomplete

class ObjectDef:
    """
    Represent an object in the LDAP server. AttrDefs are stored in a dictionary; the key is the friendly name defined in AttrDef.

    AttrDefs can be added and removed using the += and -= operators

    ObjectDef can be accessed either as a sequence and a dictionary. When accessed the whole AttrDef instance is returned
    """
    def __init__(
        self,
        object_class: Incomplete | None = None,
        schema: Incomplete | None = None,
        custom_validator: Incomplete | None = None,
        auxiliary_class: Incomplete | None = None,
    ) -> None: ...
    def __getitem__(self, item): ...
    def __getattr__(self, item: str): ...
    def __setattr__(self, key: str, value) -> None: ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, item): ...
    def add_from_schema(self, attribute_name, mandatory: bool = False) -> None: ...
    def add_attribute(self, definition: Incomplete | None = None) -> None:
        """
        Add an AttrDef to the ObjectDef. Can be called with the += operator.
        :param definition: the AttrDef object to add, can also be a string containing the name of attribute to add. Can be a list of both
        """
        ...
    def remove_attribute(self, item) -> None:
        """
        Remove an AttrDef from the ObjectDef. Can be called with the -= operator.
        :param item: the AttrDef to remove, can also be a string containing the name of attribute to remove
        """
        ...
    def clear_attributes(self) -> None:
        """
        Empty the ObjectDef attribute list

        
        """
        ...
