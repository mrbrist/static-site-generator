def markdown_to_blocks(markdown):
    split = markdown.split("\n\n")
    blocks = []
    for i in split:
        if i.strip():
            blocks.append(i.strip())
    return blocks