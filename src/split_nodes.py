from extract_markdown import *
from textnode import *

def split_nodes_image(old_nodes):
    new_nodes = []
    for i in old_nodes:
        extract = extract_markdown_images(i.text)
        if len(extract) == 0:
            new_nodes.append(i)
        else:
            original_text = i.text
            for n in extract:
                image_alt = n[0]
                image_link = n[1]
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                before = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(before)
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for i in old_nodes:
        extract = extract_markdown_links(i.text)
        if len(extract) == 0:
            new_nodes.append(i)
        else:
            original_text = i.text
            for n in extract:
                link_text = n[0]
                link_url = n[1]
                sections = original_text.split(f"[{link_text}]({link_url})", 1)
                before = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(before)
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes