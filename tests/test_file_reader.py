import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from src.file_reader import read_csv_transactions, read_excel_transactions


class TestFileReader(unittest.TestCase):
    def test_read_csv_transactions(self):
        # Подготавливаем тестовые данные
        csv_data = "id,amount,date\n1,100,2023-01-01\n2,200,2023-01-02"

        # Мокаем открытие файла и чтение CSV
        with patch('builtins.open', mock_open(read_data=csv_data)):
            # Вызываем тестируемую функцию
            result = read_csv_transactions('dummy.csv')

            # Проверяем результаты
            expected = [
                {'id': '1', 'amount': '100', 'date': '2023-01-01'},
                {'id': '2', 'amount': '200', 'date': '2023-01-02'}
            ]
            self.assertEqual(result, expected)

    def test_read_excel_transactions(self):
        # Мокаем pandas.read_excel
        with patch('pandas.read_excel') as mock_read_excel:
            # Задаем возвращаемое значение для read_excel
            mock_read_excel.return_value = pd.DataFrame({
                'id': [1, 2],
                'amount': [100, 200],
                'date': ['2023-01-01', '2023-01-02']
            })

            # Вызываем тестируемую функцию
            result = read_excel_transactions('dummy.xlsx')

            # Проверяем результаты
            expected = [
                {'id': 1, 'amount': 100, 'date': '2023-01-01'},
                {'id': 2, 'amount': 200, 'date': '2023-01-02'}
            ]
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
