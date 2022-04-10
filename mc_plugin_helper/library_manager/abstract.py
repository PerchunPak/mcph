"""Module for abstract library manager."""

from abc import ABC, abstractmethod

from mc_plugin_helper.models.plugin import Plugin


class AbstractLibraryManager(ABC):
    """Abstract library Manager class."""

    @abstractmethod
    def get_latest_version(self, plugin: Plugin) -> str:
        """Abstract getter for latest plugin version.

        Args:
            plugin: Plugin object to check.

        Returns:
            String with the latest plugin version.
        """
