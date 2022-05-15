"""Module for parse and interact with config."""

from dataclasses import dataclass
from os import path
from typing import Literal

from decouple import AutoConfig, RepositoryIni

__all__ = ["Config", "config"]


# Customising decouple
class CustomRepositoryIni(RepositoryIni):
    """Just rename section in INI file."""

    SECTION = "mc-plugin-helper"


class CustomDecouple(AutoConfig):
    """Small patched ``decouple.AutoConfig``.

    It can't read ``.env`` files, also it read ``.mc-plugin-helper.ini``
    instead of just ``settings.ini``. And it looks for config in user home folder.
    """

    SUPPORTED = {".mc-plugin-helper.ini": CustomRepositoryIni}

    def __init__(self):
        """Overwrite __init__ method, so it is using only user home folder to find config file."""
        super().__init__(path.expanduser("~"))


decouple = CustomDecouple()  # type: ignore[no-untyped-call]


@dataclass
class Config:
    """Class for config."""

    protocol: Literal["local"] = decouple("protocol", default="local")
    """Currently, supporting local files. In plans also support FTP and SFTP."""
    default_library: Literal["spigot"] = decouple("default library", default="spigot")
    """At now only supporting spigot"""
    plugins_path: str = decouple("plugins path", default="./")
    remote_host: str = decouple("remote host", default="localhost")
    remote_port: int = decouple("remote port", default=5432, cast=int)
    remote_user: str = decouple("remote user", default="root")
    remote_password: str = decouple("remote password", default="123456")

    def __post_init__(self):
        """Check some types in user config."""
        if self.protocol.lower() not in ["local"]:
            raise TypeError("Config field `protocol` should be one of ['local']")
        if self.default_library.lower() not in ["spigot"]:
            raise TypeError("Config field `default library` should be one of ['spigot']")


config = Config()
"""Initialised ``Config`` object."""
