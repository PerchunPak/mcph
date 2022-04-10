"""Tests for PluginManager class."""
from typing import Optional

from pytest import mark

from mc_plugin_helper.plugin_manager import PluginManager


@mark.parametrize("current,latest,result", [("1", "Not Found", None), ("123", "321", True), ("123", "123", False)])
def test_is_update_available(current: str, latest: str, result: Optional[bool]):
    assert PluginManager.is_update_available(current, latest) == result
