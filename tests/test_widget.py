import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_information, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счёт 64686473678894779589", "Счёт **9589"),
        ("MasterCard 71583007347267584", "Проверьте правильность ввода!"),
        ("Счет 3538303347444789556", "Проверьте правильность ввода!"),
        ("Visa Classic 6831 9824 7673 7658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 599941422842635", "Проверьте правильность ввода!"),
        ("Счет 7365 4108 4301 3587 4305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_information: str, expected: str) -> None:
    """Тесты для проверки функции маскировки банковских данных"""
    assert mask_account_card(input_information) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2003-10-15", "15.10.2003"),
        ("", "Проверьте правильность ввода даты!"),
        ("11 октября", "Проверьте правильность ввода даты!"),
        ("2003-15-15", "Проверьте правильность ввода даты!"),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    """Тест для функции преобразования даты - норма"""
    assert get_date(input_date) == expected
