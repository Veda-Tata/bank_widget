from datetime import datetime
from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "PENDING", "date": "2023-03-01T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-02-01T00:00:00.000000"},
    ]


def test_filter_executed(sample_operations: List[Dict[str, Any]]) -> None:
    filtered = filter_by_state(sample_operations, "EXECUTED")
    assert len(filtered) == 2
    assert all(op["state"] == "EXECUTED" for op in filtered)


def test_filter_pending(sample_operations: List[Dict[str, Any]]) -> None:
    filtered = filter_by_state(sample_operations, "PENDING")
    assert len(filtered) == 1
    assert filtered[0]["id"] == 2


def test_empty_result(sample_operations: List[Dict[str, Any]]) -> None:
    filtered = filter_by_state(sample_operations, "UNKNOWN_STATE")
    assert len(filtered) == 0


def test_sort_descending(sample_operations: List[Dict[str, Any]]) -> None:
    sorted_ops = sort_by_date(sample_operations, reverse=True)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates, key=lambda x: datetime.fromisoformat(x), reverse=True)


def test_sort_ascending(sample_operations: List[Dict[str, Any]]) -> None:
    sorted_ops = sort_by_date(sample_operations, reverse=False)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates, key=lambda x: datetime.fromisoformat(x))


def test_missing_date_key() -> None:
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])


def test_single_operation() -> None:
    operations = [{"date": "2023-01-01T00:00:00.000000"}]
    result = sort_by_date(operations)
    assert len(result) == 1
