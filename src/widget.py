from datetime import datetime
from src.masks import mask_account, mask_card_number  # Изменен импорт на новые имена функций

def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты/счета в переданной строке.

    Args:
        data: строка формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        Строка с замаскированным номером (пример: "Visa Platinum 7000 79** **** 6361")
    """
    if "Счет" in data:
        return f"Счет {mask_account(data.split()[-1])}"  # Использование mask_account вместо get_mask_account
    else:
        *card_type, number = data.split()
        return f"{' '.join(card_type)} {mask_card_number(number)}"  # Использование mask_card_number вместо get_mask_card_number

def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO формата в DD.MM.YYYY.

    Args:
        date_str: дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        Строка с датой в формате "11.03.2024"
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")
