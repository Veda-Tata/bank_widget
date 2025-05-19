from typing import Callable, Any, Optional
import functools


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для записи логов. Если None, вывод в консоль.

    Returns:
        Декорированную функцию с логированием.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                log_message = f"{func_name} ok\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')
                return result
            except Exception as e:
                log_message = (
                    f"{func_name} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')
                raise

        return wrapper

    return decorator
