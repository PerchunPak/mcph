"""Module for parse and interact with config."""

from __future__ import annotations

from configparser import ConfigParser
from os import path


class Config:
    """Class for config.

    Attributes:
        config: Main config object.
        config_path: Path to config, default "~/.mc-plugin-helper.ini".
    """

    def __init__(self, config_obj: ConfigParser = ConfigParser(), config_name: str = ".mc-plugin-helper.ini") -> None:
        """__init__ method."""
        self.config = config_obj
        self.config_path = path.join(path.expanduser("~"), config_name)

    @classmethod
    def init(cls, *args, **kwargs) -> Config:
        """Class-method for checking, if config already exist.

        Returns:
            Class instance.
        """
        instance = cls(*args, **kwargs)

        if path.exists(instance.config_path):
            instance.config.read(instance.config_path)
        else:
            instance.create()

        return instance

    def create(self) -> None:
        """Create a new config."""
        self.config["config"] = {
            # Currently, supporting local files.
            # In plans also support FTP and SFTP
            "protocol": "LOCAL",
            # At now only supporting spigot
            "default_library": "spigot",
            "plugins-path": "./",
        }
        self.config["remote-data"] = {
            "host": "localhost",
            "port": "5432",
            "user": "root",
            "password": "password",
        }
        self.update_config()

    def update_config(self) -> None:
        """Write in file configuration from `self.config`."""
        with open(self.config_path, "w") as config_file:
            self.config.write(config_file)


config = Config.init().config
