"""Тесты для модуля обработки транзакций.

Содержит тесты функции filter_by_state из модуля processing.
"""

import pytest
from bank_widget.processing import filter_by_state
from typing import List, Dict, Any


class TestProcessing:
    """Тесты функции фильтрации транзакций."""

    @pytest.fixture
    def sample_transactions(self) -> List[Dict[str, Any]]:
        """Фикстура тестовых транзакций."""
        return [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "PENDING"},
        ]

    def test_filter_default(self, sample_transactions: List[Dict[str, Any]]) -> None:
        """Тест фильтрации со значением по умолчанию."""
        result = filter_by_state(sample_transactions)
        assert len(result) == 1
        assert result[0]["state"] == "EXECUTED"

    def test_filter_canceled(self, sample_transactions: List[Dict[str, Any]]) -> None:
        """Тест фильтрации отмененных транзакций."""
        result = filter_by_state(sample_transactions, "CANCELED")
        assert len(result) == 1
        assert result[0]["state"] == "CANCELED"

    def test_empty_input(self) -> None:
        """Тест обработки пустого ввода."""
        assert filter_by_state([]) == []
        assert filter_by_state(None) == []

    def test_invalid_state(self, sample_transactions: List[Dict[str, Any]]) -> None:
        """Тест обработки недопустимого состояния."""
        with pytest.raises(ValueError):
            filter_by_state(sample_transactions, "INVALID")
