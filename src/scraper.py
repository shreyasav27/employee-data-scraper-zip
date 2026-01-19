import os
<<<<<<< Updated upstream
from src.downloader import download_zip
from src.extractor import extract_zip
from src.parser import parse_employee_file
=======
from downloader import download_zip
from extractor import extract_zip
from parser import parse_employee_file
import re
>>>>>>> Stashed changes


ZIP_URL = "https://www.thespreadsheetguru.com/wp-content/uploads/2022/12/EmployeeSampleData.zip"


def run_scraper():
    zip_file = "employees.zip"
    extract_dir = "extracted"

    download_zip(ZIP_URL, zip_file)
    files = extract_zip(zip_file, extract_dir)

    excel_files = [f for f in files if f.endswith(".xlsx")]
    if not excel_files:
        raise Exception("No Excel file found in ZIP")

    excel_path = os.path.join(extract_dir, excel_files[0])
<<<<<<< Updated upstream
    return parse_employee_file(excel_path)
=======
    return parse_employee_file(excel_path)
>>>>>>> Stashed changes
