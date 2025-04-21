"""
Главный исполняемый файл проекта.
Демонстрирует работу функций маскирования карт, счетов и обработки дат.
"""

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def main() -> None:
    """Основная логика программы."""
    # Демонстрация работы исходных функций
    card_number = "1234567890123456"
    account_number = "1234567890"

    print("\nБазовые функции:")
    print(f"Маска карты: {get_mask_card_number(card_number)}")
    print(f"Маска счета: {get_mask_account(account_number)}")

    # Демонстрация новых функций
    print("\nНовые функции:")
    print("Маскировка карты/счета из строки:")
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

    print("\nФорматирование даты:")
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024


if __name__ == "__main__":
    main()
