import unittest
import pandas as pd
from src.parser import parse_employee_file


class TestParser(unittest.TestCase):

    def test_missing_columns(self):
        df = pd.DataFrame({"Employee ID": [1]})
        df.to_excel("temp.xlsx", index=False)

        with self.assertRaises(Exception):
            parse_employee_file("temp.xlsx")
