#!/usr/bin/env python3

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path

from main import EXTRA_APT_DEPENDENCIES, EXTRA_BREW_DEPENDENCIES, EXTRA_CHOCO_DEPENDENCIES
from utils import parse_metadata, subprocess_run


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "--sudo",
        action="store_true",
    )
    arg_parser.add_argument(
        "package_manager",
        metavar="PACKAGE_MANAGER",
        choices=(
            "apt-get",
            "brew",
            "choco",
        ),
    )

    args = arg_parser.parse_args()

    sudo = args.sudo
    pkg_manager = args.package_manager

    packages: set[str] = set()

    if pkg_manager == "apt-get":
        packages.update(EXTRA_APT_DEPENDENCIES)
    elif pkg_manager == "brew":
        packages.update(EXTRA_BREW_DEPENDENCIES)
    elif pkg_manager == "choco":
        packages.update(EXTRA_CHOCO_DEPENDENCIES)

    for path in Path("stubs").iterdir():
        meta = parse_metadata(path)
        if pkg_manager == "apt-get":
            packages.update(meta.apt_dependencies)
        elif pkg_manager == "brew":
            packages.update(meta.brew_dependencies)
        elif pkg_manager == "choco":
            packages.update(meta.choco_dependencies)

    if packages:
        cmd = [pkg_manager, "install", *packages]
        if sudo:
            cmd.insert(0, "sudo")
        print(" ".join(cmd))
        subprocess_run(*cmd)


if __name__ == "__main__":
    main()
