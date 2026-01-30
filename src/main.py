from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
import os
import shutil
from copystatic import sync_static_to_public
from pages import generate_page


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