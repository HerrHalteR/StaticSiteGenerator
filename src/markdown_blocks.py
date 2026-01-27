def markdown_to_blocks(markdown):
    markdown_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            markdown_blocks.append(stripped_block)
    return markdown_blocks

