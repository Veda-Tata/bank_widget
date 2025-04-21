from src.masks import get_mask_card_number, get_mask_account


def test_card_mask():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_account_mask():
    assert get_mask_account("73654108430135874305") == "**4305"
