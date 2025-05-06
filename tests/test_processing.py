from datetime import datetime
import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "PENDING", "date": "2023-03-01T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-02-01T00:00:00.000000"},
        {"id": 4, "state": "CANCELED", "date": "2023-04-01T00:00:00.000000"},
    ]


class TestFilterByState:
    def test_filter_executed(self, sample_operations):
        result = filter_by_state(sample_operations, "EXECUTED")
        assert len(result) == 2
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_filter_pending(self, sample_operations):
        result = filter_by_state(sample_operations, "PENDING")
        assert len(result) == 1
        assert result[0]["id"] == 2

    def test_empty_result(self, sample_operations):
        result = filter_by_state(sample_operations, "UNKNOWN_STATE")
        assert len(result) == 0


class TestSortByDate:
    def test_sort_descending(self, sample_operations):
        result = sort_by_date(sample_operations)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, key=lambda x: datetime.fromisoformat(x), reverse=True)

    def test_sort_ascending(self, sample_operations):
        result = sort_by_date(sample_operations, reverse=False)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, key=lambda x: datetime.fromisoformat(x))

    def test_missing_date_key(self):
        with pytest.raises(KeyError, match="Все операции должны содержать ключ 'date'"):
            sort_by_date([{"id": 1}])

    def test_single_operation(self):
        operations = [{"date": "2023-01-01T00:00:00.000000"}]
        result = sort_by_date(operations)
        assert len(result) == 1
