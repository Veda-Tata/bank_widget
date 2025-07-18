"""Модуль вспомогательных утилит для работы с транзакциями."""

import json
from pathlib import Path
from typing import Any, Dict, List

from bank_widget import setup_logging


def read_transactions_from_json(file_path: Path) -> List[Dict[str, Any]]:
    """Читает транзакции из JSON файла."""
    logger = setup_logging()
    path = Path(file_path).absolute()
    logger.debug("Начало чтения файла: %s", path)

    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Ожидается список транзакций")

            logger.info("Успешно прочитано %d транзакций из %s", len(data), path)
            return data

    except json.JSONDecodeError as json_error:
        logger.error("Ошибка формата JSON в файле %s: %s", path, str(json_error))
        raise ValueError(f"Некорректный JSON формат: {json_error!s}") from json_error
    except FileNotFoundError:
        logger.error("Файл не найден: %s", path)
        raise
    except Exception:
        logger.critical("Ошибка чтения файла %s", path)
        return []
