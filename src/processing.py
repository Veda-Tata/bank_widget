from datetime import datetime
from typing import List, Dict


def sort_operations_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список операций (словарей)
        reverse: Если True - сортировка по убыванию (новые сначала),
                 если False - по возрастанию (старые сначала)

    Returns:
        Отсортированный список операций
    """

    def get_operation_date(op: Dict) -> datetime:
        # Предполагаем, что дата хранится в поле 'date' в формате ISO
        return datetime.fromisoformat(op['date'])

    return sorted(operations, key=get_operation_date, reverse=reverse)
