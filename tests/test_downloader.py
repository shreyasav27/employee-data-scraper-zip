import unittest
from unittest.mock import patch, Mock
from src.downloader import download_zip


class TestDownloader(unittest.TestCase):

    @patch("src.downloader.requests.get")
    def test_download_zip_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"zip data"
        mock_get.return_value = mock_response

        result = download_zip("http://example.com/file.zip", "file.zip")
        self.assertEqual(result, "file.zip")
