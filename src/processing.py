def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует транзакции по статусу.

    Args:
        transactions: Список словарей с транзакциями
        state: Статус для фильтрации (по умолчанию "EXECUTED")

    Returns:
        Отфильтрованный список транзакций
    """
    if not transactions:
        return []

    return [t for t in transactions if t.get("state") == state]
