from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", ""),  # пустая строка
    ("MasterCard 123", "MasterCard 123"),  # короткий номер
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

# Тесты для get_date()
@pytest.mark.parametrize("date_str, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("", ""),  # пустая строка
    ("invalid-date", ""),  # неверный формат
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
