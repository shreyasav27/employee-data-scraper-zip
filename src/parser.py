import pandas as pd
import re

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

    # ---- Email format validation ----
    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
    invalid_emails = df[~df["Email"].astype(str).str.match(email_pattern)]

    if not invalid_emails.empty:
        raise Exception("Invalid email format found")

    return df.to_dict(orient="records")
