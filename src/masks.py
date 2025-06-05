import logging
from pathlib import Path
import sys


def setup_logging():
    """Настройка логгера с гарантированной кодировкой UTF-8"""
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')

    logger = logging.getLogger("masks")
    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(
        logs_dir / "masks.log",
        mode="w",
        encoding="utf-8"
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)

    return logger


masks_logger = setup_logging()


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Пример: "7000792289606361" → "7000 79** **** 6361".
    """
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Номер карты должен состоять из 16 цифр")

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        masks_logger.debug(f"Успешно замаскирован номер карты: {card_number}")
        return masked
    except Exception as e:
        masks_logger.error(f"Ошибка маскировки карты {card_number}: {str(e)}", exc_info=True)
        raise


def mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта в формате **XXXX.
    Пример: "73654108430135874305" → "**4305".
    """
    try:
        if len(account_number) < 4 or not account_number.isdigit():
            raise ValueError("Номер счёта должен содержать минимум 4 цифры")

        masked = f"**{account_number[-4:]}"
        masks_logger.debug(f"Успешно замаскирован номер счета: {account_number}")
        return masked
    except Exception as e:
        masks_logger.error(f"Ошибка маскировки счета {account_number}: {str(e)}", exc_info=True)
        raise
