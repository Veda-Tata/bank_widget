import logging
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def reset_logging():
    """Фикстура для безопасной настройки логгера"""
    from src.utils import setup_logging

    # Закрываем все предыдущие обработчики
    logger = logging.getLogger("utils")
    for handler in logger.handlers[:]:
        handler.close()

    # Удаляем старый лог-файл если существует
    log_file = Path("src/logs/utils.log")
    if log_file.exists():
        try:
            log_file.unlink()
        except PermissionError:
            pass  # Игнорируем ошибку, если файл заблокирован

    # Инициализируем новый логгер
    return setup_logging()
