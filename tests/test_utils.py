import json
import time
from pathlib import Path

import pytest

from src.utils import logger, read_transactions_from_json


def test_log_file_created(reset_logging, tmp_path):
    """Проверка создания и записи в лог-файл"""
    # Создаем тестовый файл
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps([{"test": 1}]), encoding="utf-8")

    # Вызываем тестируемую функцию
    read_transactions_from_json(test_file)

    # Даем время на запись логов
    time.sleep(0.1)

    # Проверяем лог-файл
    log_file = Path("src/logs/utils.log")
    assert log_file.exists(), "Лог-файл не создан"

    content = log_file.read_text(encoding="utf-8")
    assert "Успешно прочитано" in content, f"Лог не содержит записей. Содержимое: {content}"
