import requests


def download_zip(url: str, output_path: str) -> str:
    """
    Downloads a ZIP file from the given URL and saves it locally.

    :param url: URL of the ZIP file
    :param output_path: Local path to save the ZIP
    :return: Path of the saved ZIP file
    """
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

    with open(output_path, "wb") as file:
        file.write(response.content)

    return output_path
