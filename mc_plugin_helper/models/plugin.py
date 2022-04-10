"""File for Plugin class."""

from typing import Optional


class Plugin:
    """Create object for plugin."""

    def __init__(self, name: str, version: str, last_version: Optional[str], file_path: str) -> None:
        """__init__ method."""
        self.name = name
        self.version = version
        self.last_version = last_version
        self.file_path = file_path
