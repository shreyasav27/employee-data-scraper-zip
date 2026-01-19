import unittest
import pandas as pd
import os
from src.parser import parse_employee_file


class TestParser(unittest.TestCase):

    def test_missing_required_columns(self):
        df = pd.DataFrame({"Employee ID": [1]})
        file_name = "temp.xlsx"
        df.to_excel(file_name, index=False)

<<<<<<< Updated upstream
        with self.assertRaises(Exception):
            parse_employee_file(file_name)

        os.remove(file_name)
=======
        try:
            with self.assertRaises(Exception):
                parse_employee_file(file_name)
        finally:
            os.remove(file_name)

    def test_excel_file_format(self):
        file_name = "EmployeeSampleData.xlsx"
        self.assertTrue(
            file_name.endswith(".xlsx"),
            "File is not in Excel format"
        )

    
>>>>>>> Stashed changes
