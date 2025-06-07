import csv
from typing import List, Dict
import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Reads financial transactions from CSV file and returns them as list of dictionaries.

    Args:
        file_path (str): Path to CSV file

    Returns:
        List[Dict]: List of transactions where each transaction is represented as dictionary
    """
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(dict(row))
    return transactions


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Reads financial transactions from Excel file and returns them as list of dictionaries.

    Args:
        file_path (str): Path to Excel file (.xlsx)

    Returns:
        List[Dict]: List of transactions where each transaction is represented as dictionary
    """
    df = pd.read_excel(file_path, engine='openpyxl')
    return df.to_dict('records')
