"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""

from _typeshed import Incomplete

def temporary_chdir(new_dir) -> None:
    """
    Like os.chdir(), but always restores the old working directory

    For example, code like this...

        old_curdir = os.getcwd()
        os.chdir('stuff')
        do_some_stuff()
        os.chdir(old_curdir)

    ...leaves the current working directory unchanged if do_some_stuff()
    raises an error, so it should be rewritten like this:

        old_curdir = os.getcwd()
        os.chdir('stuff')
        try:
            do_some_stuff()
        finally:
            os.chdir(old_curdir)

    Or equivalently, like this:

        with utils.temporary_chdir('stuff'):
            do_some_stuff()
    """
    ...
def get_file_directory():
    """Return an absolute path to the current file directory"""
    ...
def get_temp_directory():
    """Return an absolute path to an existing temporary directory"""
    ...
def get_themes_directory(theme_name: Incomplete | None = None, png: bool = False):
    """Return an absolute path the to /themes directory"""
    ...
def create_directory(directory):
    """Create directory but first delete it if it exists"""
    ...
