"""Main point to run script."""

from mc_plugin_helper.cli import CLI
from mc_plugin_helper.config import Config


def main() -> None:
    """Main function to run all."""
    Config.init()
    CLI()


if __name__ == "__main__":
    main()
