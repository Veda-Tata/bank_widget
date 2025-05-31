import pytest

from src.processing import filter_by_state


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми данными транзакций."""
    return [
        {"state": "EXECUTED"},
        {"state": "CANCELED"},
        {"state": "PENDING"},
        {"state": "EXECUTED"},
        {"state": "EXECUTED", "date": "2023-01-01"},
    ]


@pytest.mark.parametrize("state,expected_count,expected_states", [
    (None, 3, ["EXECUTED"]),
    ("EXECUTED", 3, ["EXECUTED"]),
    ("CANCELED", 1, ["CANCELED"]),
    ("PENDING", 1, ["PENDING"]),
    ("UNKNOWN", 0, []),
])
def test_filter_by_state(sample_transactions, state, expected_count, expected_states):
    """Параметризованный тест фильтрации транзакций по статусу."""
    result = filter_by_state(sample_transactions, state) if state else filter_by_state(sample_transactions)
    assert isinstance(result, list)
    assert len(result) == expected_count
    assert all(item["state"] in expected_states for item in result)


def test_filter_empty_list():
    """Тест обработки пустого списка транзакций."""
    assert filter_by_state([]) == []
    assert isinstance(filter_by_state([]), list)


def test_filter_original_unchanged(sample_transactions):
    """Тест, что исходный список не изменяется."""
    original_data = sample_transactions.copy()
    _ = filter_by_state(sample_transactions)
    assert sample_transactions == original_data


def test_filter_invalid_input():
    """Тест обработки некорректных входных данных."""
    assert filter_by_state(None) == []
    assert filter_by_state([{"invalid": "data"}]) == []


def test_transactions_without_state():
    """Тест обработки транзакций без поля state."""
    assert filter_by_state([{"id": 1}, {"id": 2, "state": "EXECUTED"}]) == [{"id": 2, "state": "EXECUTED"}]
