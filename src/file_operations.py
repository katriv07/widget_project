from pathlib import Path
from typing import Any, Dict, List, cast

import pandas as pd


def get_data_path() -> Path:
    """Возвращает абсолютный путь к папке data"""
    return Path(__file__).parent.parent / "data"


def read_csv_transactions(filename: str = "transactions.csv") -> List[Dict[str, Any]]:
    """
    Чтение транзакций из CSV файла в папке data

    Args:
        filename: Имя CSV файла в папке data

    Returns:
        Список словарей с транзакциями
    """
    file_path = get_data_path() / filename
    df = pd.read_csv(file_path)
    return cast(List[Dict[str, Any]], df.to_dict("records"))


def read_excel_transactions(filename: str = "transactions_excel.xlsx") -> List[Dict[str, Any]]:
    """
    Чтение транзакций из Excel файла в папке data

    Args:
        filename: Имя Excel файла в папке data

    Returns:
        Список словарей с транзакциями
    """
    file_path = get_data_path() / filename
    df = pd.read_excel(file_path)
    return cast(List[Dict[str, Any]], df.to_dict("records"))
