from typing import Dict, List


def process_bank_operations(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Обрабатывает банковские операции и возвращает количество операций по категориям.
    """
    result = {category: 0 for category in categories}

    if not operations:
        return result

    for operation in operations:
        description = operation.get("description", "").lower()
        for category in categories:
            if category.lower() == description:
                result[category] += 1

    return result
