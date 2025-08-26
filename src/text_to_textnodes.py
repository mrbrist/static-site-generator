from split_nodes_delimiter import *
from split_nodes import *

delimiters = [
    ("**", TextType.BOLD),
    ("_", TextType.ITALIC),
    ("`", TextType.CODE),
]

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
    