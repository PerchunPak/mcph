"""Module for abstract library manager."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class AbstractLibraryManager(ABC):
    """Abstract library Manager class."""

    @abstractmethod
    def get_latest_version(self, plugin_name: str) -> str:
        """Abstract getter for latest plugin version.

        Args:
            plugin_name: Plugin name to check.

        Returns:
            String with the latest plugin version or "Not Found" if we can't find plugin.
        """

    @abstractmethod
    def get_plugin_data(self, plugin_name: str) -> Optional[Dict[str, Any]]:  # type: ignore[misc]
        """Getter for plugin data.

        Args:
            plugin_name: Name of plugin to check.

        Returns:
            Parsed JSON answer or None if no plugins found.
        """

    @abstractmethod
    def _api_request(self, url: str) -> Any:  # type: ignore[misc]
        """Perform API requests to plugin host.

        Args:
            url: URL to request.

        Returns:
            Raw answer.
        """
