import json
import logging
from pathlib import Path
from typing import List, Dict


def setup_logging():
    """Настройка логгера с безопасным доступом к файлу"""
    logger = logging.getLogger("utils")
    logger.setLevel(logging.DEBUG)

    # Очистка предыдущих обработчиков
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    # Создание папки для логов
    logs_dir = Path("src/logs")
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Настройка файлового обработчика с безопасным режимом
    log_file = logs_dir / "utils.log"
    try:
        file_handler = logging.FileHandler(
            log_file,
            mode="a",  # Режим дописывания вместо перезаписи
            encoding="utf-8"
        )
    except PermissionError:
        # Если файл заблокирован, используем временный файл
        temp_file = logs_dir / "utils_temp.log"
        file_handler = logging.FileHandler(
            temp_file,
            mode="a",
            encoding="utf-8"
        )

    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)

    return logger


# Инициализация логгера
logger = setup_logging()


def read_transactions_from_json(file_path: str) -> List[Dict]:
    """Чтение транзакций с безопасным логированием"""
    try:
        abs_path = str(Path(file_path).absolute())
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug(f"Успешно прочитано из {abs_path}")
            return data
    except Exception as e:
        logger.error(f"Ошибка при чтении {file_path}: {str(e)}", exc_info=True)
        return []
