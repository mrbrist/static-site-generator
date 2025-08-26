from htmlnode import *
def text_to_quote_children(text):
    split = text.split("\n")
    children = []
    for i in split:
        children.append(i.lstrip("> ").strip())
    return "\n".join(children)