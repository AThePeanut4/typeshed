def consolidate_linker_args(args: list[str]) -> str | list[str]:
    """
    Ensure the return value is a string for backward compatibility.

    Retain until at least 2025-04-31. See pypa/distutils#246
    """
    ...
