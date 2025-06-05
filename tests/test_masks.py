import pytest
from pathlib import Path
from src.masks import mask_card_number, mask_account, masks_logger


def test_mask_card_number_success():
    """Тест успешной маскировки номера карты"""
    assert mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_card_number_invalid():
    """Тест обработки невалидного номера карты"""
    with pytest.raises(ValueError):
        mask_card_number("1234")
    with pytest.raises(ValueError):
        mask_card_number("700079228960636A")
    with pytest.raises(ValueError):
        mask_card_number("700079228960636123")


def test_mask_account_success():
    """Тест успешной маскировки номера счета"""
    assert mask_account("73654108430135874305") == "**4305"


def test_mask_account_invalid():
    """Тест обработки невалидного номера счета"""
    with pytest.raises(ValueError):
        mask_account("123")
    with pytest.raises(ValueError):
        mask_account("7365410843013587430A")
    with pytest.raises(ValueError):
        mask_account("")


def test_log_file_created():
    """Проверка создания лог-файла"""
    log_file = Path("logs/masks.log")
    assert log_file.exists(), "Лог-файл не создан"


def test_log_content():
    """Проверка содержимого логов"""
    test_msg = "ТЕСТОВОЕ СООБЩЕНИЕ ДЛЯ ПРОВЕРКИ"
    masks_logger.debug(test_msg)

    # Принудительная запись
    for handler in masks_logger.handlers:
        if hasattr(handler, 'flush'):
            handler.flush()

    log_file = Path("logs/masks.log")
    content = log_file.read_text(encoding="utf-8")
    assert test_msg in content, f"Сообщение не найдено в логе. Содержимое: {content}"
