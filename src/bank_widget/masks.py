def mask_card_number(card_number: str) -> str:
    """Маскирование номера карты."""
    if len(card_number) < 16:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def mask_account_number(account_number: str) -> str:
    """Маскирование номера счета."""
    if len(account_number) < 4:
        return account_number
    return f"**{account_number[-4:]}"
