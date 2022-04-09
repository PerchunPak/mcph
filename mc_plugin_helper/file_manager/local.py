"""Module for LocalFileManager class."""
from os import listdir
from typing import List
from zipfile import ZipFile

from mc_plugin_helper.file_manager.abstract import AbstractFileManager


class LocalFileManager(AbstractFileManager):
    """File manager for local files."""

    def open_jar(self, jar_file: str) -> bytes:
        """Open specified jar.

        Args:
            jar_file: Path to plugin in jar.

        Returns:
            Raw text from plugin.yml.
        """
        with ZipFile(jar_file, "r") as opened_jar_file:
            # FIXME See what it return, and continue code
            return opened_jar_file.read("plugin.yml")

    def get_all_files(self, path: str) -> List[str]:
        """List with all files in path.

        Args:
            path: Path to folder for list of all files.

        Returns:
            List with all files in folder.
        """
        return listdir(path)
