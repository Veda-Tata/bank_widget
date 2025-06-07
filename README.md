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

## Модуль decorators

### Декоратор `log`

Логирует вызовы функций и их результаты.

**Параметры:**
- `filename` (str, optional): Имя файла для записи логов. Если не указан, вывод в консоль.

**Примеры использования:**
```python
@log(filename="operations.log")
def add(a, b):
    return a + b

@log()
def greet(name):
    return f"Hello, {name}"

## Новые возможности. Поддержка CSV и Excel файлов

Теперь проект поддерживает чтение финансовых транзакций из:
- CSV файлов (функция `read_csv_transactions()`)
- Excel файлов (функция `read_excel_transactions()`)

### Использование:
```python
from src.file_reader import read_csv_transactions, read_excel_transactions

csv_data = read_csv_transactions('transactions.csv')
excel_data = read_excel_transactions('transactions.xlsx')
