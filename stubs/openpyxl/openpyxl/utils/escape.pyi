'OOXML has non-standard escaping for characters < \x19'

def escape(value: str) -> str:
    r"""Convert ASCII < 31 to OOXML: \n == _x + hex(ord(\n)) + _"""
    ...
def unescape(value: str) -> str:
    r"""Convert escaped strings to ASCIII: _x000a_ == \n"""
    ...
