# Bank Widget Project

Проект для маскирования номеров карт и счетов.

## Функционал

- Маскировка номера карты: `XXXX XX** **** XXXX`
- Маскировка номера счета: `**XXXX`

## Установка

1. Убедитесь, что установлен [Python](https://www.python.org/downloads/) (версия 3.10+).
2. Установите зависимости:
   ```bash
   poetry install
   ```

## Использование

```python
from src.masks import masks

masked_card = masks.get_mask_card_number("7000792289606361")  # "7000 79** **** 6361"
masked_account = masks.get_mask_account("73654108430135874305")  # "**4305"
```

## Модуль `generators`

Модуль содержит генераторы для работы с транзакциями и номерами карт.

### Функции

#### `filter_by_currency(transactions, currency)`
Фильтрует транзакции по заданной валюте и возвращает итератор.

**Пример использования:**
```python
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


### 4. Проверим покрытие тестами

Запустим тесты с проверкой покрытия:

```bash
pytest --cov=generators --cov-report=html

## Модуль generators

Реализует генераторы для работы с банковскими транзакциями.

### Функции

#### `filter_by_currency(transactions, currency)`
Фильтрует транзакции по валюте.

Пример:
```python
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
