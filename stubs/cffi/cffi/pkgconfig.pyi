from collections.abc import Sequence

def merge_flags(cfg1: dict[str, list[str]], cfg2: dict[str, list[str]]) -> dict[str, list[str]]: ...
def call(libname: str, flag: str, encoding: str = ...) -> str: ...
def flags_from_pkgconfig(libs: Sequence[str]) -> dict[str, list[str]]: ...
