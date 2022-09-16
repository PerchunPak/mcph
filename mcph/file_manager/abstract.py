"""Module for abstract file manager."""

from abc import ABC, abstractmethod
from typing import List


class AbstractFileManager(ABC):
    """Abstract File Manager class."""

    @abstractmethod
    def open_jar(self, jar_file: str) -> bytes:
        """Open specified jar.

        Args:
            jar_file: Path to plugin in jar.

        Returns:
            Raw text from plugin.yml.
        """

    @abstractmethod
    def get_all_files(self, path: str) -> List[str]:
        """List with all files in path.

        Args:
            path: Path to folder for list of all files.

        Returns:
            List with all files in folder.
        """
