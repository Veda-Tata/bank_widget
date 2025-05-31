import json

import pytest  # noqa: F401

from src.utils import read_transactions_from_json


def test_read_transactions_from_json_valid_file(tmp_path):
    """Тест чтения из валидного JSON-файла."""
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(data))

    result = read_transactions_from_json(file_path)
    assert result == data


def test_read_transactions_from_json_invalid_file(tmp_path):
    """Тест чтения из несуществующего файла."""
    file_path = tmp_path / "nonexistent.json"
    result = read_transactions_from_json(file_path)
    assert result == []
