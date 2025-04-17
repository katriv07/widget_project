def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в формате 7000792289606361,
    и возвращает  маску в формате 7000 79** **** 6361"""
    card_number = card_number.replace(" ", "")
    if card_number.isdigit() and len(card_number) == 16:
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    else:
        return "Проверьте правильность введенного номера карты!"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета в формате 73654108430135874305,
    и возвращает его маску в формате - **4305"""
    account_number = account_number.replace(" ", "")
    if account_number.isdigit() and len(account_number) == 20:
        return "**" + account_number[-4:]
    else:
        return "Проверьте правильность введенного номера счета!"
