"""Модуль для обработки и фильтрации банковских транзакций.

Содержит функции для фильтрации и анализа банковских операций по различным критериям.
"""

from typing import Any, Dict, List, Literal, Optional

Transaction = Dict[str, Any]
StateType = Literal["EXECUTED", "CANCELED", "PENDING"]


def filter_by_state(
    transactions: Optional[List[Transaction]] = None, state: StateType = "EXECUTED"
) -> List[Transaction]:
    """Фильтрует список транзакций по указанному статусу.

    Args:
        transactions: Список транзакций для фильтрации. Если None, будет
                     преобразован в пустой список.
        state: Статус для фильтрации. Допустимые значения:
               - "EXECUTED" (по умолчанию)
               - "CANCELED"
               - "PENDING"

    Returns:
        Список транзакций, отфильтрованных по указанному статусу.
        Возвращает пустой список, если:
        - передан None
        - передан пустой список
        - нет совпадений по статусу

    Raises:
        TypeError: Если transactions не является списком или None.

    Examples:
        >>> filter_by_state([{"state": "EXECUTED"}])
        [{'state': 'EXECUTED'}]
        >>> filter_by_state(None)
        []

    """
    if transactions is None:
        transactions = []
    elif not isinstance(transactions, list):
        raise TypeError("transactions must be a list or None")

    return [t for t in transactions if t.get("state") == state]
