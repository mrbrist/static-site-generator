import sys
sys.path.append("src")

import unittest

from blocktype import *


class TestBlockType(unittest.TestCase):
    def test_heading1(self):
        block = "# Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    def test_heading3(self):
        block = "### Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    def test_heading6(self):
        block = "###### Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    def test_code(self):
        block = "```This is some code```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    def test_quote(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    def test_ulist(self):
        block = "- Item 1\n-Item 2\n- Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ULIST)
    def test_olist(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.OLIST)


if __name__ == "__main__":
    unittest.main()