import sys
sys.path.append("src")

import unittest

from markdown_to_html_node import *


class TestBlockType(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ulist(self):
        md = """
- This is list item 1
- This is list item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is list item 1</li><li>This is list item 2</li></ul></div>",
        )

    def test_ulist1(self):
        md = """
- This is list _item_ 1
- This is list item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is list <i>item</i> 1</li><li>This is list item 2</li></ul></div>",
        )

    def test_olist(self):
        md = """
1. This is list item 1
2. This is list item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is list item 1</li><li>This is list item 2</li></ol></div>",
        )

    def test_olist1(self):
        md = """
1. This is _list_ item 1
2. This is list item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <i>list</i> item 1</li><li>This is list item 2</li></ol></div>",
        )

    def test_quote(self):
        md = """
> This is a quote block in Markdown.  
> It can span multiple lines.  
> Each line should start with a `>`.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote block in Markdown.\nIt can span multiple lines.\nEach line should start with a `>`.</blockquote></div>",
        )

    def test_h1(self):
        md = """
# Heading 1
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1></div>",
        )
    def test_h3(self):
        md = """
### Heading 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading 3</h3></div>",
        )
    def test_h6(self):
        md = """
###### Heading 6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Heading 6</h6></div>",
        )


if __name__ == "__main__":
    unittest.main()