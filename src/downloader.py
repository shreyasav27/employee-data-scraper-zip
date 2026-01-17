import unittest
from unittest.mock import patch, Mock
from src.downloader import download_zip


class TestDownloader(unittest.TestCase):

    @patch("src.downloader.requests.get")
    def test_download_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"fake zip content"
        mock_get.return_value = mock_response

        path = download_zip("http://fake-url", "test.zip")
        self.assertEqual(path, "test.zip")
