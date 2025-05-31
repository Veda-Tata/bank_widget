import json
from typing import Dict, List


def read_transactions_from_json(file_path: str) -> List[Dict]:
    """Читает транзакции из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу с транзакциями

    Returns:
        Список словарей с транзакциями или пустой список, если файл не существует
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
