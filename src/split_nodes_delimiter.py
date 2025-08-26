from enum import Enum
from textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for i in old_nodes:
        if i.text_type is not TextType.TEXT:
            new_nodes.append(i)
        elif i.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown Syntax")
        else:
            new_text_nodes = []
            split = i.text.split(delimiter)
            is_delim = False
            for s in split:
                if is_delim:
                    new_text_nodes.append(TextNode(s, text_type))
                else:
                    new_text_nodes.append(TextNode(s, TextType.TEXT))
                is_delim = not is_delim
            new_nodes.extend(new_text_nodes)


    return new_nodes