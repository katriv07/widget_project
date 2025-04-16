from datetime import datetime
from typing import List

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_information: str) -> str:
    """
    Определяет тип входных данных (счет или карта) и маскирует номер.

    Аргумент может быть, например:
    - "Visa Platinum 7000792289606361"
    - "Maestro 7000792289606361"
    - "Счет 73654108430135874305"

    Возвращает замаскированную строку, например:
    - "Visa Platinum 7000 79** **** 6361" для карт
    - "Счет **4305" для счетов
    """
    parts: List[str] = input_information.split()
    number: str = ""
    bill_information: List[str] = []
    for item in parts:
        if item.isdigit():
            number += item
        else:
            bill_information.append(item)

    if len(number) == 16:
        return f'{" ".join(bill_information)} {get_mask_card_number(number)}'
    elif len(number) == 20:
        return f'{" ".join(bill_information)} {get_mask_account(number)}'
    else:
        return "Проверьте правильность ввода!"


def get_date(input_date: str) -> str:
    """
    Принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407
    и возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024).
    """
    try:
        formated_date = datetime.strptime(input_date[:10], "%Y-%m-%d")
        return f"{formated_date.day:02}.{formated_date.month:02}.{formated_date.year}"
    except ValueError:
        return "Проверьте правильность ввода даты!"
