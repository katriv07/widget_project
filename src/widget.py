from src.masks import get_mask_card_number
from src.masks import get_mask_account_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
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
    account_card_split = account_card.split()
    if "Счет" in account_card_split:
        return f"Счет {get_mask_account_number(account_card_split[1])}"
    else:
        card_numbers = []
        card_name =[]
        for i in account_card_split:
            if i.isdigit():
                card_numbers.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_numbers = "".join(card_numbers)
        str_card_name = " ".join(card_name)
        return f"{str_card_name} {get_mask_card_number(str_card_numbers)}"


def get_date(date_str: str) -> str:
    """
    Принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407
    и возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024).
    """
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")

