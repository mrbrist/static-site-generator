import sys
sys.path.append("src")

import unittest

from htmlnode import HTMLNode
from textnode import *
from main import *
from split_nodes_delimiter import split_nodes_delimiter


class TestDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT)])

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("bold block", TextType.BOLD),TextNode(" word", TextType.TEXT)])

    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("italic block", TextType.ITALIC),TextNode(" word", TextType.TEXT)])

    def test_double_bold(self):
        node = TextNode("This is **text** with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is ", TextType.TEXT),TextNode("text", TextType.BOLD),TextNode(" with a ", TextType.TEXT),TextNode("bold block", TextType.BOLD),TextNode(" word", TextType.TEXT)])


if __name__ == "__main__":
    unittest.main()