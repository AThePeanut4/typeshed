def list_or_args(keys, args): ...
def nativestr(x):
    """Return the decoded binary string, or a string, depending on type."""
    ...
def delist(x):
    """Given a list of binaries, return the stringified version."""
    ...
def parse_to_list(response):
    """Optimistically parse the response to a list."""
    ...
def parse_list_to_dict(response): ...
def parse_to_dict(response): ...
def random_string(length: int = 10) -> str:
    """Returns a random N character long string."""
    ...
def quote_string(v):
    """
    RedisGraph strings must be quoted,
    quote_string wraps given v with quotes incase
    v is a string.
    """
    ...
def decode_dict_keys(obj):
    """Decode the keys of the given dictionary with utf-8."""
    ...
def stringify_param_value(value):
    """
    Turn a parameter value into a string suitable for the params header of
    a Cypher command.
    You may pass any value that would be accepted by `json.dumps()`.

    Ways in which output differs from that of `str()`:
        * Strings are quoted.
        * None --> "null".
        * In dictionaries, keys are _not_ quoted.

    :param value: The parameter value to be turned into a string.
    :return: string
    """
    ...
