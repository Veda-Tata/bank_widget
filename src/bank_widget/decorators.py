"""Модуль с декораторами для банковского приложения."""

import logging
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


class LogDecorator:
    """Класс-декоратор для логирования вызовов функций с расширенной функциональностью."""

    def __init__(self: "LogDecorator", filename: Optional[str] = None, logger_name: str = "decorators") -> None:
        """Улучшенная инициализация декоратора логирования.

        Args:
            filename: Опциональный путь к файлу для логирования
            logger_name: Имя логгера (по умолчанию "decorators")
        """
        self.filename = filename
        self.logger = logging.getLogger(logger_name)

        # Настройка обработчиков при указании файла
        if self.filename:
            self._setup_file_handler()

    def _setup_file_handler(self) -> None:
        """Настройка файлового обработчика логирования."""
        file_handler = logging.FileHandler(self.filename)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        self.logger.addHandler(file_handler)

    def __call__(self: "LogDecorator", func: F) -> F:
        """Улучшенный декоратор с расширенным логированием.

        Args:
            func: Декорируемая функция

        Returns:
            Обернутую функцию с логированием
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Логирование аргументов
            self.logger.info(
                f"Вызов функции {func.__name__} с args: {args}, kwargs: {kwargs}"
            )

            try:
                result = func(*args, **kwargs)
                # Логирование успешного выполнения
                self.logger.info(
                    f"Функция {func.__name__} выполнена успешно. Результат: {result!r}"
                )
                return result
            except Exception as e:
                # Расширенное логирование ошибок
                self.logger.error(
                    f"Ошибка в функции {func.__name__}: {type(e).__name__}: {e!s}",
                    exc_info=True
                )
                raise

        return cast(F, wrapper)


# Пример использования
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)


    @LogDecorator()
    def example_function(x: int, y: int) -> int:
        """Пример функции для демонстрации декоратора."""
        return x + y


    example_function(2, 3)
