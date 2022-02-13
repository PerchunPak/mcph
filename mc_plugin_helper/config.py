"""Module for parse and interact with config."""

from configparser import ConfigParser
from os.path import exists, expanduser, join
from typing import TypeVar

config_class = TypeVar("config_class", bound="Config")


class Config(object):
    """Class for config.

    Attributes:
        config: Main config object.
        config_path: Path to config, usually "~/.mc-plugin-helper.ini".
    """

    def __init__(self) -> None:
        """__init__ method."""
        self.config = ConfigParser()
        self.config_path = join(expanduser("~"), ".mc-plugin-helper.ini")

    @classmethod
    def init(cls) -> config_class:
        """Class-method for checking, if config already exist.

        Returns:
            Class instance.
        """
        instance = cls()

        if exists(instance.config_path):
            instance.config.read(instance.config_path)
        else:
            instance.create()

        return instance

    def create(self) -> None:
        """Create a new config."""
        self.config["mc-plugin-helper"] = {
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
            self.config.write(config_file)
