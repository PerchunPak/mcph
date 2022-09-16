"""Module for parse and interact with config."""

from dataclasses import dataclass
from enum import Enum
from os import environ
from pathlib import Path

from omegaconf import MISSING, OmegaConf
from omegaconf.dictconfig import DictConfig


class Protocol(Enum):
    """Protocols for file manager.

    .. note:: Currently supporting only local files protocol. In plans also FTP.
    """

    LOCAL = "local"


class Library(Enum):
    """Libraries for library manager.

    .. note:: Currently supporting only Spigot library.
    """

    SPIGOT = "spigot"


@dataclass
class RemoteData:
    """Data for remote connection."""

    host: str = MISSING
    port: int = MISSING
    username: str = MISSING
    password: str = MISSING


@dataclass
class Config:
    """Class for config."""

    protocol: Protocol = Protocol.LOCAL
    """Currently, supporting local files. In plans also support FTP and SFTP."""
    default_library: Library = Library.SPIGOT
    """At now only supporting spigot"""
    default_plugins_path: str = "./"
    remote: RemoteData = RemoteData()

    @classmethod
    def setup(cls) -> "Config":
        """Set up the config.

        It is just load config from file, also it is rewrite config with merged data.

        Returns:
            :class:`.Config` instance.
        """
        config_path = Path("~").expanduser() / "mcph.yml"
        cfg = OmegaConf.structured(Config)

        if config_path.exists():
            loaded_config = OmegaConf.load(config_path)
            cfg = OmegaConf.merge(cfg, loaded_config)

        with config_path.open("w") as config_file:
            OmegaConf.save(cfg, config_file)

        cls._handle_env_variables(cfg)

        return cfg  # type: ignore[no-any-return] # interface the same as in :class:`.Config`

    @staticmethod
    def _handle_env_variables(cfg: DictConfig) -> None:
        """Process all values, and redef them with values from env variables.

        Args:
            cfg: :class:`.Config` instance.
        """
        for key in cfg:
            if "MCPH_" + str(key).upper() in environ:
                cfg[str(key)] = environ[str(key).upper()]


config = Config.setup()
"""Initialised ``Config`` object."""
