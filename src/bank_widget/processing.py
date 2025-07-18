"""Модуль для фильтрации транзакций по состоянию.

Содержит функцию для фильтрации списка транзакций по статусу выполнения.
"""

from typing import List, Dict, Optional, Literal


StateType = Literal["EXECUTED", "CANCELED", "PENDING"]


def filter_by_state(
        transactions: Optional[List[Dict]],
        state: StateType = "EXECUTED"
) -> List[Dict]:
    """Фильтрует транзакции по указанному состоянию.

    Args:
        transactions: Список транзакций для фильтрации. Может быть None.
        state: Состояние для фильтрации. По умолчанию "EXECUTED".

    Returns:
        Отфильтрованный список транзакций. Если transactions=None, возвращает [].

    Raises:
        TypeError: Если transactions не является списком или None.
        ValueError: Если указано недопустимое состояние.
    """
    if transactions is None:
        return []

    if not isinstance(transactions, list):
        raise TypeError("transactions must be a list or None")

    valid_states = {"EXECUTED", "CANCELED", "PENDING"}
    if state not in valid_states:
        raise ValueError(f"Invalid state. Allowed: {valid_states}")

    return [t for t in transactions if t.get("state") == state]
