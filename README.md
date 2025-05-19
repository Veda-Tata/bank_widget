# Bank Widget Project

Проект для работы с банковскими операциями, включая маскировку данных, фильтрацию и сортировку транзакций.

## Основной функционал

### 1. Маскировка данных
- Номера карт: `XXXX XX** **** XXXX`
- Номера счетов: `**XXXX`

### 2. Обработка операций
- Фильтрация по статусу (`EXECUTED`/`CANCELED`)
- Сортировка по дате (возрастание/убывание)

## Установка

1. Убедитесь, что установлен [Python](https://www.python.org/downloads/) (версия 3.10+)
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ## Изменения в версии 1.1

### Добавлено
- Функция сортировки операций по дате в модуле `processing.py`:
  ```python
  def sort_operations_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
      """
      Сортирует операции по дате (по умолчанию от новых к старым).
      Возвращает отсортированный список операций.
      """
  ```

### Исправлено
- Типизация для функций обработки операций
- Соответствие PEP 8 (стиль кода)

### Как использовать
```python
from src.processing import sort_operations_by_date

sorted_ops = sort_operations_by_date(operations)
```
