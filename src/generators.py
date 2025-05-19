from typing import Iterator, List, TypedDict


class Currency(TypedDict):
    name: str
    code: str


class OperationAmount(TypedDict):
    amount: str
    currency: Currency


class Transaction(TypedDict):
    id: int
    state: str
    date: str
    operationAmount: OperationAmount
    description: str
    from_: str  # Используем from_ вместо from (ключевое слово)
    to: str


def filter_by_currency(transactions: List[Transaction], currency: str) -> Iterator[Transaction]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    Args:
        transactions: Список транзакций
        currency: Код валюты (например "USD")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Transaction]) -> Iterator[str]:
    """
    Генератор описаний транзакций.

    Args:
        transactions: Список транзакций

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт.

    Args:
        start: Начальный номер
        end: Конечный номер (включительно)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for number in range(start, end + 1):
        num_str = f"{number:016d}"
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
