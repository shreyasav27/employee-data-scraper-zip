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
    """
    Parses employee Excel file and returns employee records.

    :param file_path: Path to Excel file
    :return: List of employee records
    """
    try:
        df = pd.read_excel(file_path)
    except Exception as exc:
        raise Exception(f"Failed to read Excel file: {exc}")

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            raise Exception(f"Missing required column: {column}")

    return df.to_dict(orient="records")
