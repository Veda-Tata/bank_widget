from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(input_str: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от входных данных.

    Args:
        input_str: Строка содержащая либо номер карты, либо номер счета

    Returns:
        Маскированная строка в формате:
        - Для карт: "XXXX XX** **** XXXX"
        - Для счетов: "**XXXX"
        - Исходная строка если формат не распознан

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    if not input_str:
        return input_str

    parts = input_str.split()
    if not parts:
        return input_str

    last_part = parts[-1]

    # Проверяем, является ли последняя часть номером счета (содержит слово "счет" в любом регистре)
    if "счет" in input_str.lower():
        return f"{' '.join(parts[:-1])} {get_mask_account(last_part)}"
    else:
        return f"{' '.join(parts[:-1])} {get_mask_card_number(last_part)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат DD.MM.YYYY.

    Args:
        date_str: Дата в формате ISO (YYYY-MM-DDTHH:MM:SS.mmmmmm)

    Returns:
        Дата в формате DD.MM.YYYY или пустая строка при ошибке

    Examples:
        >>> get_date("2018-07-11T02:26:18.671407")
        '11.07.2018'
    """
    if not date_str:
        return ""

    try:
        return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return ""
