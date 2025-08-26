import re
from htmlnode import *
from text_to_children import *

def text_to_list_children(text, block_type):
    children = []
    if block_type.value == "unordered_list":
        split = text.split("\n")
        for i in split:
            children_text = i.lstrip("- ")
            children_new = text_to_children(children_text)
            children.append(ParentNode("li", children_new))
        return children
    else:
        split = text.split("\n")
        for i in split:
            children_text = re.sub(r"^\d+\.\s*", "", i)
            children_new = text_to_children(children_text)
            children.append(ParentNode("li", children_new))
        return children