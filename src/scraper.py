import os

from src.downloader import download_zip
from src.extractor import extract_zip
from src.parser import parse_employee_file


ZIP_URL = "https://www.thespreadsheetguru.com/wp-content/uploads/2022/12/EmployeeSampleData.zip"


def run_scraper():
    zip_path = "employee_data.zip"
    extract_dir = "extracted_data"

    # Step 1: Download ZIP
    download_zip(ZIP_URL, zip_path)

    # Step 2: Extract ZIP
    extracted_files = extract_zip(zip_path, extract_dir)

    # Step 3: Find Excel file
    excel_files = [f for f in extracted_files if f.endswith(".xlsx")]

    if not excel_files:
        raise Exception("No Excel file found in ZIP")

    excel_path = os.path.join(extract_dir, excel_files[0])

    # Step 4: Parse employee data
    return parse_employee_file(excel_path)
