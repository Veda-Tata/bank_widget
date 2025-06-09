import pytest

from src.decorators import log


def test_log_to_file(tmp_path):
    """Тестирование записи логов в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    add(1, 2)
    assert "add ok" in log_file.read_text()

    with pytest.raises(ZeroDivisionError):

        @log(filename=str(log_file))
        def div(a, b):
            return a / b

        div(1, 0)

    assert "div error" in log_file.read_text()


def test_log_to_console(capsys):
    """Тестирование вывода логов в консоль."""

    @log()
    def multiply(a, b):
        return a * b

    multiply(3, 4)
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out

    with pytest.raises(ValueError):

        @log()
        def raise_error():
            raise ValueError("test")

        raise_error()

    captured = capsys.readouterr()
    assert "raise_error error" in captured.out
