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
    def test_valid_data_structure(self):
        df = pd.DataFrame({
            "Employee ID": [1],
            "First Name": ["John"],
            "Last Name": ["Doe"],
            "Email": ["john@example.com"],
            "Job Title": ["Engineer"],
            "Phone Number": ["1234567890"],
            "Hire Date": ["2022-01-01"]
        })

        file_name = "valid.xlsx"
        df.to_excel(file_name, index=False)

        try:
            result = parse_employee_file(file_name)
            self.assertIsNotNone(result)
        finally:
            os.remove(file_name)

    def test_invalid_email_data(self):
        df = pd.DataFrame({
            "Employee ID": [1],
            "First Name": ["John"],
            "Last Name": ["Doe"],
            "Email": ["invalid-email"],
            "Job Title": ["Engineer"],
            "Phone Number": ["1234567890"],
            "Hire Date": ["2022-01-01"]
        })

        file_name = "invalid_email.xlsx"
        df.to_excel(file_name, index=False)

        try:
            with self.assertRaises(Exception):
                parse_employee_file(file_name)
        finally:
            os.remove(file_name)
