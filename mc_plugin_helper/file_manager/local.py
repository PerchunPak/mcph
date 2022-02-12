from os import listdir
from zipfile import ZipFile
from typing import List
from mc_plugin_helper.file_manager.factory import AbstractFileManager


class LocalFileManager(AbstractFileManager):
    """File manager for local files."""

    def open_jar(self, jar_file) -> bytes:
        """Open specified jar."""
        with ZipFile(jar_file.name, "r") as opened_jar_file:
            # FIXME See what it return, and continue code
            return opened_jar_file.read("plugin.yml")

    def get_all_files(self, path) -> List[str]:
        """List with all files in path."""
        return listdir(path)
