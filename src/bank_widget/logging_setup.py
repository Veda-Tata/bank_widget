"""Модуль для настройки логирования."""

import logging
import sys
from pathlib import Path

def setup_logging(log_file: Path = Path("../../logs/app.log")) -> logging.Logger:
    """Настраивает и возвращает логгер для банковских операций.

    Args:
        log_file: Путь к файлу логов

    Returns:
        Настроенный логгер

    Raises:
        PermissionError: Если нет прав на запись в файл
        OSError: При других ошибках файловой системы

    """
    logger = logging.getLogger("bank_transactions")
    logger.setLevel(logging.DEBUG)

    # Очистка существующих обработчиков
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    try:
        # Создание директории для логов
        log_file.parent.mkdir(exist_ok=True, parents=True)

        # Настройка форматтера
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Файловый обработчик
        file_handler = logging.FileHandler(
            log_file,
            mode='a',
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Консольный обработчик для Windows
        if sys.platform == "win32":
            sys.stdout.reconfigure(encoding='utf-8')
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        return logger

    except Exception as e:
        logger.error(f"Ошибка настройки логирования: {e}")
        raise

