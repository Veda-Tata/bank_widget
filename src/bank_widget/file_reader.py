from pathlib import Path
from typing import List, Dict, Any, Union
import pandas as pd
import csv

def read_csv_transactions(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Чтение транзакций из CSV файла."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        transactions = []
        with open(path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(dict(row))
        return transactions
    except PermissionError as e:
        raise PermissionError(f"Permission denied: {path}") from e
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Invalid file encoding: {path}") from e

def read_excel_transactions(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Чтение транзакций из Excel файла."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        df = pd.read_excel(path, engine='openpyxl')
        return df.to_dict('records')
    except ImportError:
        raise ImportError("openpyxl package is required for Excel support")
    except PermissionError as e:
        raise PermissionError(f"Permission denied: {path}") from e
