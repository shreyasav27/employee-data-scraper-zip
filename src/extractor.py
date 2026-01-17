import unittest
from src.extractor import extract_zip


class TestExtractor(unittest.TestCase):

    def test_invalid_zip(self):
        with self.assertRaises(Exception):
            extract_zip("invalid.txt", "output")
