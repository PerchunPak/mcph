"""Main point to run script."""

from mc_plugin_helper.cli import CLI
from mc_plugin_helper.config import Config

Config.init()
CLI()
