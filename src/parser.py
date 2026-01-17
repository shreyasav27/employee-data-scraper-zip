import pandas as pd

REQUIRED_COLUMNS = [
    "Employee ID",
    "First Name",
    "Last Name",
    "Email",
    "Job Title",
    "Phone Number",
    "Hire Date",
]


def parse_employee_file(file_path: str) -> list:
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise Exception(f"Unable to read Excel file: {e}")

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise Exception(f"Missing required column: {col}")

    return df.to_dict(orient="records")
