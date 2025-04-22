import os
from typing import cast, Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_amount_transaction(transaction: Dict[str, Any]) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR, обращается к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    """
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return float(amount)

    if currency not in ("USD", "EUR"):
        raise ValueError(f"Ошибка! Некорректный тип валюты: {currency}")

    response = requests.get(BASE_URL, params={"base": currency, "symbols": "RUB"}, headers={"apikey": API_KEY})
    response.raise_for_status()
    rate = float(response.json()["rates"]["RUB"])
    return float(amount) * rate
