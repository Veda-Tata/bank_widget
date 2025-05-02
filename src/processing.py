from typing import List, Dict, Optional


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список банковских операций по указанному статусу.

    Args:
        operations: Список словарей, где каждый словарь содержит данные об операции.
        state: Статус операции для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Список операций, отфильтрованных по статусу.

    Examples:
       Возвращает операции с state="EXECUTED"
    """
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations
