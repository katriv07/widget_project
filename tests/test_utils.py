from typing import Any, Dict, List
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_transactions


@pytest.mark.parametrize(
    "content,expected",
    [
        ('[{"id": 1}]', [{"id": 1}]),
        ("[]", []),
        ("{}", []),
        ("invalid", []),
    ],
)
def test_get_transactions(content: str, expected: List[Dict[str, Any]]) -> None:
    """Тестирует функцию get_transactions."""
    with patch("builtins.open", mock_open(read_data=content)):
        assert get_transactions("any_path") == expected
