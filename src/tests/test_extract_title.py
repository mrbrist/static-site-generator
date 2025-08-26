import sys
sys.path.append("src")

import unittest

from extract_title import *


class TestExtractTitle(unittest.TestCase):
    def test_heading1(self):
        md = "# Heading"
        title = extract_title(md)
        self.assertEqual(title, "Heading")

    def test_heading2(self):
        self.assertRaises(Exception, extract_title, "Heading")


if __name__ == "__main__":
    unittest.main()