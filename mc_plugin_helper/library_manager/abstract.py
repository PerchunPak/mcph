"""Module for abstract library manager."""

from abc import ABC, abstractmethod


class AbstractLibraryManager(ABC):
    """Abstract library Manager class."""

    @abstractmethod
    def get_latest_version(self, plugin_name: str) -> str:
        """Abstract getter for latest plugin version.

        Args:
            plugin_name: Plugin name to check.

        Returns:
            String with the latest plugin version.
        """
