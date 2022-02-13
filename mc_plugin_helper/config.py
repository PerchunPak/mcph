"""Module for parse and interact with config."""

from __future__ import annotations
from configparser import ConfigParser, SectionProxy
from os.path import exists, expanduser, join


class Config(object):
    """Class for config.

    Attributes:
        _config: Main config object.
        config_path: Path to config, usually "~/.mc-plugin-helper.ini".
    """

    def __init__(self) -> None:
        """__init__ method."""
        self._config = ConfigParser()
        self.config_path = join(expanduser("~"), ".mc-plugin-helper.ini")

    @classmethod
    def init(cls) -> Config:
        """Class-method for checking, if config already exist.

        Returns:
            Class instance.
        """
        instance = cls()

        if exists(instance.config_path):
            instance._config.read(instance.config_path)  # noqa: WPS437
        else:
            instance.create()

        return instance

    @property
    def config(self) -> SectionProxy:
        """Property with config object.

        Returns:
            Main section from config.
        """
        return self._config["mc-plugin-helper"]

    def create(self) -> None:
        """Create a new config."""
        self._config["mc-plugin-helper"] = {
            # Currently, supporting local files.
            # In plans also support FTP and SFTP
            "protocol": "LOCAL",
            "plugins-path": "./",
            "remote-host": "localhost",
            "remote-port": "5432",
            "remote-user": "root",
            "remote-password": "password",
        }
        self.update_config()

    def update_config(self) -> None:
        """Write in file configuration from `self.config`."""
        with open(self.config_path, "w") as config_file:
            self._config.write(config_file)
