from typing import List, Dict
from bank_widget import mask_card_number, mask_account_number
from datetime import datetime

class TransactionWidget:
    def __init__(self, transactions: List[Dict]):
        self.transactions = transactions

    def _get_date(self, date_str: str) -> str:
        """Форматирование даты."""
        try:
            date = datetime.fromisoformat(date_str)
            return date.strftime("%d.%m.%Y")
        except ValueError:
            return "Дата: неверный формат"

    def _mask_account_card(self, number: str) -> str:
        """Маскирование карты/счета."""
        if "счет" in number.lower():
            return mask_account_number(number.split()[-1])
        return mask_card_number(number.split()[-1])

    def display(self, limit: int = None):
        """Вывод транзакций."""
        for i, transaction in enumerate(self.transactions[:limit], 1):
            print(f"\nТранзакция #{i}")
            print("-" * 30)
            self._print_transaction(transaction)
            print("-" * 30)

    def _print_transaction(self, transaction: Dict):
        """Вывод одной транзакции."""
        if 'date' in transaction:
            print(f"Дата: {self._get_date(transaction['date'])}")
        if 'description' in transaction:
            print(f"Описание: {transaction['description']}")
        if 'from' in transaction:
            print(f"Отправитель: {self._mask_account_card(transaction['from'])}")
        if 'to' in transaction:
            print(f"Получатель: {self._mask_account_card(transaction['to'])}")
        if 'amount' in transaction:
            currency = transaction.get('currency', '')
            print(f"Сумма: {transaction['amount']} {currency}".strip())
