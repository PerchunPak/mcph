from abc import ABC, abstractmethod


class AbstractFileManager(ABC):
    """Abstract File Manager class."""

    @abstractmethod
    def open_jar(self, jar_file):
        """Open specified jar."""

    @abstractmethod
    def get_all_files(self, path):
        """List with all files in path."""
