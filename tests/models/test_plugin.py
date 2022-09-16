"""Tests for ``Plugin`` class."""
from typing import Optional

from pytest import mark

from mcph.models.plugin import Plugin


@mark.parametrize("current,latest,result", [("1", "Not Found", None), ("123", "321", True), ("123", "123", False)])
def test_is_update_available(current: str, latest: str, result: Optional[bool]):
    """Test ``Plugin.is_update_available`` method."""
    assert (
        Plugin(
            name="Test Plugin",
            version=current,
            last_version=latest,
            file_path="/etc/test_plugin.jar",
        ).is_update_available()
        == result
    )
