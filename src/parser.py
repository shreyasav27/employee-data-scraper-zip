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

COLUMN_MAPPING = {
    "employeeid": "Employee ID",
    "firstname": "First Name",
    "lastname": "Last Name",
    "email": "Email",
    "jobtitle": "Job Title",
    "phonenumber": "Phone Number",
    "hiredate": "Hire Date",
}


def parse_employee_file(file_path: str) -> list:
    try:
        df = pd.read_excel(file_path)
        print("RAW COLUMNS FROM EXCEL:", list(df.columns))
    except Exception as e:
        raise Exception(f"Unable to read Excel file: {e}")

    # Normalize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    #  HANDLE REAL ZIP EXCEL ONLY
    if "eeid" in df.columns and "full name" in df.columns:
        df["Employee ID"] = df["eeid"]

        df["First Name"] = df["full name"].astype(str).str.split().str[0]
        df["Last Name"] = df["full name"].astype(str).str.split().str[-1]

        df["Job Title"] = df.get("job title")
        df["Hire Date"] = df.get("hire date")

        # Not present in real file  explicit nulls
        df["Email"] = None
        df["Phone Number"] = None

    else:
        # TEST DATA PATH 
        df.columns = df.columns.str.replace(" ", "")
        df.rename(columns=COLUMN_MAPPING, inplace=True)

    #  Required column validation 
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise Exception(f"Missing required column: {col}")

    #  Email validation
    if df["Email"].notna().any():
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        invalid_emails = df[
            ~df["Email"].astype(str).str.match(email_pattern)
        ]
        if not invalid_emails.empty:
            raise Exception("Invalid email format found")

    return df[REQUIRED_COLUMNS].to_dict(orient="records")
