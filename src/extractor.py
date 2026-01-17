import zipfile
import os


def extract_zip(zip_path: str, extract_to: str) -> list:
    """
    Extracts a ZIP file to the given directory.

    :param zip_path: Path to ZIP file
    :param extract_to: Directory to extract contents
    :return: List of extracted file names
    """
    if not zipfile.is_zipfile(zip_path):
        raise Exception("Invalid ZIP file")

    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    return os.listdir(extract_to)
