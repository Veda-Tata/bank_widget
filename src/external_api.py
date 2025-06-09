import os
from typing import Dict

import requests


class CurrencyConversionError(Exception):
    """Кастомное исключение для ошибок конвертации валют"""

    pass


def convert_transaction_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма транзакции в рублях (float)

    Raises:
        CurrencyConversionError: Если произошла ошибка при конвертации
        ValueError: Если неверные входные данные или отсутствует API ключ
    """
    try:
        # Проверка входных данных
        if not isinstance(transaction, dict):
            raise ValueError("Transaction must be a dictionary")

        amount = float(transaction.get("amount", 0))
        currency = transaction.get("currency", "").upper()

        if currency == "RUB":
            return amount

        if not currency:
            raise ValueError("Currency not specified in transaction")

        # Получаем API ключ из переменных окружения
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables")

        # Запрос курса валют
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
        headers = {"apikey": api_key}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()

            if "rates" not in data or "RUB" not in data["rates"]:
                raise CurrencyConversionError("Invalid API response format")

            rub_rate = data["rates"]["RUB"]

            return amount * rub_rate

        except requests.RequestException as e:
            raise CurrencyConversionError(f"API request failed: {str(e)}")
        except (ValueError, KeyError) as e:
            raise CurrencyConversionError(f"Failed to parse API response: {str(e)}")

    except ValueError as e:
        raise ValueError(f"Invalid transaction data: {str(e)}")
