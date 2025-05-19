import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from_": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from_": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from_": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


@pytest.mark.parametrize("currency,expected_count", [
    ("USD", 2),
    ("RUB", 1),
    ("EUR", 0)
])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
    for transaction in result:
        assert transaction['operationAmount']['currency']['code'] == currency


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]


@pytest.mark.parametrize("start,end,expected", [
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999, 10001, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001"
    ])
])
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected
