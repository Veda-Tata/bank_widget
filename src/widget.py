from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты/счета в переданной строке.

    Args:
        data: строка формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        Строка с замаскированным номером (пример: "Visa Platinum 7000 79** **** 6361")
    """
    if "Счет" in data:
        return f"Счет {get_mask_account(data.split()[-1])}"
    else:
        *card_type, number = data.split()
        return f"{' '.join(card_type)} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO формата в DD.MM.YYYY.

    Args:
        date_str: дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        Строка с датой в формате "11.03.2024"
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")
