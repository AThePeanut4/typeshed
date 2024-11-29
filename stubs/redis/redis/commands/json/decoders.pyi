def bulk_of_jsons(d):
    """
    Replace serialized JSON values with objects in a
    bulk array response (list).
    """
    ...
def decode_dict_keys(obj):
    """Decode the keys of the given dictionary with utf-8."""
    ...
def unstring(obj):
    """
    Attempt to parse string to native integer formats.
    One can't simply call int/float in a try/catch because there is a
    semantic difference between (for example) 15.0 and 15.
    """
    ...
def decode_list(b):
    """
    Given a non-deserializable object, make a best effort to
    return a useful set of results.
    """
    ...
