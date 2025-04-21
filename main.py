"""
Главный исполняемый файл проекта.
Демонстрирует работу функций маскирования карт и счетов.
"""

from src.masks import get_mask_card_number, get_mask_account


def main() -> None:
    """Основная логика программы."""
    # Демонстрация работы функций
    card_number = "1234567890123456"
    account_number = "1234567890"

    print(f"Маска карты: {get_mask_card_number(card_number)}")
    print(f"Маска счета: {get_mask_account(account_number)}")


if __name__ == "__main__":
    main()
