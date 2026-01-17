import os
from src.downloader import download_zip
from src.extractor import extract_zip
from src.parser import parse_employee_file


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
    return parse_employee_file(excel_path)
