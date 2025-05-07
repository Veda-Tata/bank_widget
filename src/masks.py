def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 4 и последние 4 цифры.

    Args:
        card_number: Номер карты (16 цифр без пробелов)

    Returns:
        Маскированный номер в формате "XXXX XX** **** XXXX"

    Raises:
        ValueError: Если номер карты не содержит 16 цифр
    """
    if not card_number.isdigit() or len(card_number) != 16:
        return card_number  # Или можно raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 символа.

    Args:
        account_number: Номер счета (любая строка)

    Returns:
        Маскированный номер в формате "**XXXX" (где XXXX - последние 4 символа)
        Для строк короче 4 символов возвращает "**" + всю строку
        Для пустой строки возвращает пустую строку
    """
    if not account_number:  # Пустая строка
        return ""

    if len(account_number) <= 4:
        return f"**{account_number}"
    return f"**{account_number[-4:]}"
