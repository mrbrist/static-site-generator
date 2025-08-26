from htmlnode import *
from blocktype import *
from text_to_children import *
from text_to_list_children import *
from text_to_quote_children import *

def markdown_block_to_html_node(block, block_type):
    match block_type.value:
        case "heading":
            hnum = block.count("#")
            return ParentNode(f"h{hnum}", text_to_children(block.strip("#").strip()))
        case "code":
            return ParentNode("pre", [text_node_to_html_node(TextNode(block.strip("`").lstrip(), "code"))])
        case "quote":
            return LeafNode("blockquote", text_to_quote_children(block))
        case "unordered_list":
            return ParentNode("ul", text_to_list_children(block, block_type))
        case "ordered_list":
            return ParentNode("ol", text_to_list_children(block, block_type))
        case _:
            return ParentNode("p", text_to_children(" ".join(block.split())))