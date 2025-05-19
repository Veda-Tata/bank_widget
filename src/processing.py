from typing import List, Dict
from datetime import datetime


def filter_operations_by_status(operations: List[Dict], status: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует операции по статусу.

    Args:
        operations: Список операций
        status: Статус для фильтрации (по умолчанию "EXECUTED")

    Returns:
        Отфильтрованный список операций
    """
    return [op for op in operations if op.get("status") == status]


def sort_operations_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует операции по дате (по умолчанию от новых к старым).

    Args:
        operations: Список операций
        reverse: Порядок сортировки (True - по убыванию)

    Returns:
        Отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )
