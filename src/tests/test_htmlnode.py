import sys
sys.path.append("src")

import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", None, None, {"href":"google.com"})
        node2 = HTMLNode("a", None, None, {"href":"google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("a", None, None, {"href":"google.com"})
        node2 = HTMLNode("b", None, None, None)
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode("a", None, None, {"href":"google.com"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_3_children(self):
        child_node = LeafNode("span", "span")
        child_node2 = LeafNode("b", "bold")
        child_node3 = LeafNode(None, "Hello")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>span</span><b>bold</b>Hello</div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandgrandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = ParentNode("div", [child_node])
        parent_node = ParentNode("div", [child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><div><span><b>grandchild</b></span></div></div>",
        )


if __name__ == "__main__":
    unittest.main()