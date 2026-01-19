import unittest
import os
import zipfile
import pandas as pd
from src.extractor import extract_zip


class TestExtractor(unittest.TestCase):

    def test_invalid_zip_raises_exception(self):
        with self.assertRaises(Exception):
            extract_zip("not_a_zip.txt", "output")

    def test_valid_zip_extracts_excel(self):
        zip_path = "test.zip"
        output_dir = "output"
        excel_name = "EmployeeSampleData.xlsx"

        # ---- Create a real Excel file ----
        df = pd.DataFrame({
            "Employee ID": [1],
            "First Name": ["John"]
        })
        df.to_excel(excel_name, index=False)

        # ---- Create a real ZIP containing the Excel file ----
        with zipfile.ZipFile(zip_path, "w") as zipf:
            zipf.write(excel_name)

        # ---- Run extraction ----
        extract_zip(zip_path, output_dir)

        # ---- Assertion ----
        extracted_files = os.listdir(output_dir)
        self.assertIn(excel_name, extracted_files)

        # ---- Cleanup ----
        os.remove(zip_path)
        os.remove(excel_name)
        for file in extracted_files:
            os.remove(os.path.join(output_dir, file))
        os.rmdir(output_dir)
