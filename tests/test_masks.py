import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("", ""),  # пустая строка
        ("1234", "1234"),  # короткий номер
        ("abcdefghijklmnop", "abcdefghijklmnop"),  # не цифры
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),  # Стандартный случай
        ("1234567890", "**7890"),            # 10 цифр
        ("", ""),                            # Пустая строка
        ("123", "**123"),                    # 3 символа
        ("12", "**12"),                      # 2 символа
        ("1", "**1"),                        # 1 символ
        ("abcde", "**bcde"),                 # Буквы (5 символов)
        ("abcdefgh", "**efgh"),              # Буквы (8 символов)
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
