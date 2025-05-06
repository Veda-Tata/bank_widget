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
## Тестирование

- Покрытие кода: >80%
- Запуск тестов:
  ```bash
  pytest --cov=src --cov-report=html
  ```
- Отчёт: Откройте `htmlcov/index.html` в браузере

**Зависимости для тестов:**
- pytest
- pytest-cov
