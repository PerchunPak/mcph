"""Module for `Plugin` model."""

from typing import Optional


class Plugin:
    """Create object for plugin.

    Attributes:
        name: Plugin name.
        version: Plugin version.
        last_version: Latest available plugin version.
        file_path: Path to file, where this plugin is.
        update_available: Is update available?
    """

    def __init__(
        self, name: str, version: str, last_version: str, file_path: str, update_available: Optional[bool] = None
    ) -> None:
        """__init__ method.

        Args:
            name: Plugin name.
            version: Plugin version.
            last_version: Latest available plugin version.
            file_path: Path to file, where this plugin is.
            update_available: Is update available?
        """
        self.name = name
        self.version = version
        self.last_version = last_version
        self.file_path = file_path
        self.update_available = self.is_update_available() if update_available is None else update_available

    def is_update_available(self) -> Optional[bool]:
        """Checker for plugin, answer on question 'is update available?'.

        Returns:
            True if update available, False if not and None if we can't check.
        """
        if self.last_version == "Not Found":
            return None
        if (self.version in self.last_version) or (self.last_version in self.version):
            return False
        return True
