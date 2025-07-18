import json
from pathlib import Path
from typing import List, Dict, Optional
import logging

def load_transactions(file_path: str) -> List[Dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                logging.warning(f"File {file_path} does not contain a list of transactions")
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading transactions: {str(e)}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return []

def main():
    """Основная функция выполнения скрипта."""
    logging.basicConfig(level=logging.INFO)
    print("Банковские транзакции")
    print("=" * 30)

    transactions = load_transactions("data/transactions.json")
    if not transactions:
        print("Не удалось загрузить транзакции")
        return

    for i, transaction in enumerate(transactions[:5], 1):
        print(f"{i}. {transaction.get('description', 'No description')}")

if __name__ == "__main__":
    main()
