# from text_to_textnodes import *
from blocktype import *
from markdown_to_blocks import *
from markdown_block_to_html_node import *
from htmlnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for b in blocks:
        block_type = block_to_block_type(b)
        html_node = markdown_block_to_html_node(b, block_type)
        html_blocks.append(html_node)

    return ParentNode("div", html_blocks)