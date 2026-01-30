from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
import os
import shutil
from copystatic import sync_static_to_public
from pages import generate_page


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")





def main():
    source_path = "./static"
    dest_path = "./public"
    sync_static_to_public(source_path, dest_path)  # copies static -> public

    # now generate HTML page
    generate_page(
        "content/index.md",    # markdown source
        "template.html",       # template in project root
        "public/index.html",   # output HTML file
    )


if __name__ == "__main__":
    main()