from inline_markdown import markdown_to_blocks
from textnode_to_htmlnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        pass


def text_to_children(text):
    pass

