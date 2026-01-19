import zipfile
import os


def extract_zip(zip_path: str, extract_to: str) -> list:
    if not zipfile.is_zipfile(zip_path):
        raise Exception("Invalid ZIP file")

    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    return os.listdir(extract_to)
