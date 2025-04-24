from pathlib import Path
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.file_operations import read_csv_transactions


def test_read_csv_transactions(mock_csv_data: str, mock_df: pd.DataFrame) -> None:
    """Тест чтения CSV с моками"""
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        with patch("pandas.read_csv", return_value=mock_df) as mock_read_csv:
            result = read_csv_transactions()
            expected = mock_df.to_dict("records")
            assert result == expected
            mock_read_csv.assert_called_once()


@pytest.mark.skipif(
    not (Path(__file__).parent.parent / "data" / "transactions.csv").exists(), reason="CSV file not found"
)
def test_real_csv_reading() -> None:
    """Интеграционный тест с реальным CSV"""
    result = read_csv_transactions()
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)
