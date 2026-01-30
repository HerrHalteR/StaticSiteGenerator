from enum import Enum


def markdown_to_blocks(markdown):
    markdown_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            markdown_blocks.append(stripped_block)
    return markdown_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(markdown):
    # 1. code
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE

    # 2. quote
    lines = markdown.split("\n")
    is_quote = True
    for line in lines:
        if not (line.startswith(">") or line.startswith("> ")):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    # 3. unordered list
    is_unordered_list = True
    for line in lines:
        if not (line.startswith("- ")):                  # if not (line.startswith("- ") or line.startswith("* ") or line.startswith("+ ")):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.ULIST

    # 4. ordered list
    is_ordered_list = True
    expected_num = 1
    for line in lines:
        if ". " not in line:
            is_ordered_list = False
            break
        num_text, rest = line.split(". ", 1)            # "1. item" -> "1", "item"
        if not num_text.isdigit():
            is_ordered_list = False
            break
        if int(num_text) != expected_num:
            is_ordered_list = False
            break
        expected_num += 1
        
    if is_ordered_list:
        return BlockType.OLIST

    # 5. heading
    if markdown.startswith("#"):
        count = 0
        for ch in markdown:
            if ch == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and len(markdown) > count and markdown[count] == " ":
            return BlockType.HEADING


    # 6. default
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    root = HTMLNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        root.children.append(block_node)
    return root