import unittest
from src.extractor import extract_zip


class TestExtractor(unittest.TestCase):

    def test_invalid_zip_raises_exception(self):
        with self.assertRaises(Exception):
            extract_zip("not_a_zip.txt", "output")
