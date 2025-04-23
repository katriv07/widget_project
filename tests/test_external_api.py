from typing import Any, Dict
from unittest.mock import Mock, patch

from src.external_api import convert_amount_transaction


@patch("requests.get")
def test_convert_amount_transaction(mock_get: Mock) -> None:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.5}}
    mock_get.return_value.raise_for_status.return_value = None

    transaction: Dict[str, Any] = {"amount": "100", "currency": "USD"}
    assert convert_amount_transaction(transaction) == 7550.0
