from src.processing import filter_by_state

def test_filter_by_state():
    # Тест с state по умолчанию (EXECUTED)
    assert filter_by_state([{"state": "EXECUTED"}, {"state": "CANCELED"}]) == [{"state": "EXECUTED"}]

    # Тест с явным указанием state
    assert filter_by_state([{"state": "EXECUTED"}, {"state": "CANCELED"}], "CANCELED") == [{"state": "CANCELED"}]
