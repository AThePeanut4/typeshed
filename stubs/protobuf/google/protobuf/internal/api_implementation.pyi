"""Determine which implementation of the protobuf API is used in this process."""

def Type() -> str: ...
def Version() -> int: ...
def IsPythonDefaultSerializationDeterministic() -> bool: ...
