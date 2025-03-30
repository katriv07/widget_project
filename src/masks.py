def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в формате 7000792289606361,
    и возвращает  маску в формате 7000 79** **** 6361"""
    return card_number[:4] + " " + card_number[4:6] + "**" + " **** " + card_number[11:16]


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета в формате 73654108430135874305,
    и возвращает его маску в формате - **4305"""
    return "**" + account_number[-4:]
