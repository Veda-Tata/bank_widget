import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("", ""),
        ("Invalid Data", "Invalid Data"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("", ""),
        ("invalid-date", ""),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected
