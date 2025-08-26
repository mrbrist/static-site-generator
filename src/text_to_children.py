from text_to_textnodes import *
from text_node_to_html_node import *

def text_to_children(text):
    nodes  = text_to_textnodes(text)
    html_nodes = []
    for i in nodes:
        html_nodes.append(text_node_to_html_node(i))

    return html_nodes