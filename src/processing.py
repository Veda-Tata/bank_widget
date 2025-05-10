from datetime import datetime
from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список банковских операций по указанному статусу.

    Args:
        operations: Список словарей, где каждый словарь содержит данные об операции.
        state: Статус операции для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Список операций, отфильтрованных по статусу.

    Examples:
        >>> operations = [
        ...     {"state": "EXECUTED", "date": "2023-01-01"},
        ...     {"state": "PENDING", "date": "2023-02-01"}
        ... ]
        >>> filter_by_state(operations)
        [{'state': 'EXECUTED', 'date': '2023-01-01'}]
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате (по убыванию по умолчанию).

    Args:
        operations: Список словарей с операциями, каждый должен содержать ключ 'date'.
        reverse: Если True - сортировка по убыванию, False - по возрастанию.

    Returns:
        Отсортированный список операций.

    Raises:
        KeyError: Если в какой-либо операции отсутствует ключ 'date'.

    Examples:
        >>> operations = [
        ...     {"date": "2023-01-01T12:00:00.000000"},
        ...     {"date": "2023-02-01T15:30:00.000000"}
        ... ]
        >>> sort_by_date(operations)
        [{'date': '2023-02-01T15:30:00.000000'}, {'date': '2023-01-01T12:00:00.000000'}]
    """
    try:
        return sorted(operations, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    except KeyError as e:
        raise KeyError("Все операции должны содержать ключ 'date'") from e
