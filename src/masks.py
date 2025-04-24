import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в формате 7000792289606361,
    и возвращает  маску в формате 7000 79** **** 6361"""
    card_number = card_number.replace(" ", "")
    if card_number.isdigit() and len(card_number) == 16:
        masked = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info(f"Успешное маскирование карты: {masked}")
        return masked
    else:
        error_msg = "Проверьте правильность введенного номера карты!"
        logger.error(f"Ошибка маскирования карты: {error_msg}")
        return error_msg


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета в формате 73654108430135874305,
    и возвращает его маску в формате - **4305"""
    account_number = account_number.replace(" ", "")
    if account_number.isdigit() and len(account_number) == 20:
        masked = "**" + account_number[-4:]
        logger.info(f"Успешное маскирование счета: {masked}")
        return masked
    else:
        error_msg = "Проверьте правильность введенного номера счета!"
        logger.error(f"Ошибка маскирования счета: {error_msg}")
        return error_msg
