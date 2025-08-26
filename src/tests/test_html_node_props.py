import sys
sys.path.append("src")

import unittest

from markdown_to_html_node import *


class TestProps(unittest.TestCase):
    def test_image(self):
        md = """
![JRR Tolkien sitting](/images/tolkien.png)
"""
        test = markdown_to_html_node(md)
        self.assertEqual(test.to_html(), '<div><p><img src="/images/tolkien.png" alt="JRR Tolkien sitting"></img></p></div>')

    def test_link(self):
        md = """
[Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
"""
        test = markdown_to_html_node(md)
        self.assertEqual(test.to_html(), '<div><p><a href="/blog/glorfindel">Why Glorfindel is More Impressive than Legolas</a></p></div>')


if __name__ == "__main__":
    unittest.main()