import os
from unittest.mock import Mock, patch

import pytest
import requests  # Добавляем импорт requests

from src.external_api import CurrencyConversionError, convert_transaction_to_rub


@pytest.fixture
def mock_transaction():
    """Фикстура для тестовой транзакции в USD."""
    return {"amount": "100", "currency": "USD"}


@pytest.fixture
def mock_exchange_rates():
    """Фикстура для мок-ответа API курсов валют."""
    return {"rates": {"RUB": 75.50}, "success": True}


@patch("src.external_api.requests.get")
@patch.dict("os.environ", {"EXCHANGE_RATE_API_KEY": "test_key"})
def test_convert_usd_to_rub(mock_get, mock_transaction, mock_exchange_rates):
    """Тест успешной конвертации USD в RUB."""
    mock_response = Mock()
    mock_response.json.return_value = mock_exchange_rates
    mock_get.return_value = mock_response

    result = convert_transaction_to_rub(mock_transaction)
    assert result == 7550.0  # 100 * 75.50
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_rub_to_rub(mock_get):
    """Тест конвертации RUB в RUB (без вызова API)."""
    transaction = {"amount": "500", "currency": "RUB"}
    result = convert_transaction_to_rub(transaction)
    assert result == 500.0
    mock_get.assert_not_called()


def test_missing_api_key():
    """Тест отсутствия API ключа."""
    if "EXCHANGE_RATE_API_KEY" in os.environ:
        del os.environ["EXCHANGE_RATE_API_KEY"]

    with pytest.raises(ValueError, match="API key not found"):
        convert_transaction_to_rub({"amount": "10", "currency": "USD"})


@patch("src.external_api.requests.get")
@patch.dict("os.environ", {"EXCHANGE_RATE_API_KEY": "test_key"})
def test_api_request_failure(mock_get):
    """Тест ошибки запроса к API."""
    mock_get.side_effect = requests.RequestException("API недоступен")

    with pytest.raises(CurrencyConversionError, match="API request failed"):
        convert_transaction_to_rub({"amount": "10", "currency": "EUR"})


@patch("src.external_api.requests.get")
@patch.dict("os.environ", {"EXCHANGE_RATE_API_KEY": "test_key"})
def test_invalid_api_response(mock_get):
    """Тест невалидного ответа API."""
    mock_response = Mock()
    mock_response.json.return_value = {"invalid": "response"}
    mock_get.return_value = mock_response

    with pytest.raises(CurrencyConversionError, match="Invalid API response"):
        convert_transaction_to_rub({"amount": "10", "currency": "GBP"})


@pytest.mark.parametrize(
    "transaction", [{"amount": "not_a_number", "currency": "USD"}, {"amount": "10"}, None, {"currency": "USD"}]
)
def test_invalid_transaction_data(transaction):
    """Тест невалидных данных транзакции."""
    with pytest.raises(ValueError):
        convert_transaction_to_rub(transaction)
