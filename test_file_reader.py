import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from file_reader import read_csv_file, read_excel_file


class TestFileReader(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data='id,amount,date\n1,100,2023-01-01\n2,200,2023-01-02'))
    @patch('csv.DictReader')
    def test_read_csv_file(self, mock_dict_reader):
        mock_dict_reader.return_value = [
            {'id': '1', 'amount': '100', 'date': '2023-01-01'},
            {'id': '2', 'amount': '200', 'date': '2023-01-02'}
        ]
        result = read_csv_file('dummy.csv')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['amount'], '100')

    @patch('pandas.read_excel')
    def test_read_excel_file(self, mock_read_excel):
        mock_data = {
            'id': [1, 2],
            'amount': [100, 200],
            'date': ['2023-01-01', '2023-01-02']
        }
        mock_df = pd.DataFrame(mock_data)
        mock_read_excel.return_value = mock_df
        result = read_excel_file('dummy.xlsx')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['amount'], 100)


if __name__ == '__main__':
    unittest.main()
