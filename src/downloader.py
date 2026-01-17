import requests


def download_zip(url: str, output_path: str) -> str:
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Failed to download ZIP. Status: {response.status_code}")

    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path
