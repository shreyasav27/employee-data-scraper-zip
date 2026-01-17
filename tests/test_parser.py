import unittest
import pandas as pd
import os
from src.parser import parse_employee_file


class TestParser(unittest.TestCase):

    def test_missing_required_columns(self):
        df = pd.DataFrame({"Employee ID": [1]})
        file_name = "temp.xlsx"
        df.to_excel(file_name, index=False)

        with self.assertRaises(Exception):
            parse_employee_file(file_name)

        os.remove(file_name)
