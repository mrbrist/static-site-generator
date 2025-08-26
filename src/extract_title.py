from markdown_to_blocks import *

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    found_header = False
    for i in blocks:
        if i.startswith("# "):
            found_header = True
            return i.lstrip("#").strip()
    if not found_header:
        raise Exception("No title found")