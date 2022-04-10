"""Tests for ``Config`` class."""
from os import path, remove

from pytest_mock import MockerFixture

from mc_plugin_helper.config import Config


def test_config_not_exists(mocker: MockerFixture) -> None:
    try:
        remove(path.join(path.expanduser("~"), ".TEST.mc-plugin-helper.ini.TEST."))
    except FileNotFoundError:
        pass

    stub_1 = mocker.stub("ConfigParser.read")
    mocker.patch("configparser.ConfigParser.read", stub_1)
    stub_2 = mocker.stub("Config.create")
    mocker.patch("mc_plugin_helper.config.Config.create", stub_2)

    Config.init(config_name=".TEST.mc-plugin-helper.ini.TEST.")

    stub_1.assert_not_called()
    stub_2.assert_called_once()
    mocker.stopall()


def test_config_exists(mocker: MockerFixture) -> None:
    Config(config_name=".TEST.mc-plugin-helper.ini.TEST.").create()

    stub_1 = mocker.stub("ConfigParser.read")
    mocker.patch("configparser.ConfigParser.read", stub_1)
    stub_2 = mocker.stub("Config.create")
    mocker.patch("mc_plugin_helper.config.Config.create", stub_2)

    Config.init(config_name=".TEST.mc-plugin-helper.ini.TEST.")

    stub_1.assert_called_once()
    stub_2.assert_not_called()
    mocker.stopall()
