"""Модуль для поиска банковских операций с использованием регулярных выражений."""

import re
import logging
from typing import Dict, List, Union, Pattern

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def process_bank_search(
        transactions: List[Dict[str, str]],
        search_term: Union[str, Pattern[str]]
) -> List[Dict[str, str]]:
    """Фильтрует транзакции по поисковому запросу с поддержкой regex.

    Args:
        transactions: Список транзакций для поиска. Каждая транзакция должна
                    содержать ключ 'description'.
        search_term: Строка или скомпилированное регулярное выражение для поиска.
                   Регистр не учитывается.

    Returns:
        Отфильтрованный список транзакций, где description содержит совпадение.

    Raises:
        ValueError: При некорректном регулярном выражении.
        TypeError: Если search_term не строка или не скомпилированный паттерн.

    Examples:
        >>> data = [{"description": "Payment"}, {"description": "Transfer"}]
        >>> process_bank_search(data, "pay")
        [{'description': 'Payment'}]

        >>> process_bank_search(data, re.compile("trans.*", re.I))
        [{'description': 'Transfer'}]
    """
    # Валидация входных данных
    if not isinstance(search_term, (str, re.Pattern)):
        logger.error("Invalid search term type: %s", type(search_term))
        raise TypeError("Search term must be string or compiled regex pattern")

    try:
        # Если search_term уже скомпилированный паттерн
        if isinstance(search_term, re.Pattern):
            pattern = search_term
        else:
            pattern = re.compile(search_term, re.IGNORECASE)

        # Фильтрация транзакций
        filtered = [
            t for t in transactions
            if pattern.search(t.get("description", ""))
        ]

        logger.info(
            "Search completed: term='%s', found=%d",
            search_term if isinstance(search_term, str) else search_term.pattern,
            len(filtered)
        )

        return filtered

    except re.error as e:
        logger.error("Regex error for term '%s': %s", search_term, str(e))
        raise ValueError(f"Invalid regular expression: '{search_term}'") from e


def simple_search(
        transactions: List[Dict[str, str]],
        search_term: str
) -> List[Dict[str, str]]:
    """Упрощенный поиск без regex (только подстрока)."""
    search_lower = search_term.lower()
    return [
        t for t in transactions
        if search_lower in t.get("description", "").lower()
    ]
