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


def markdown_to_html_node(markdown):
    root = HTMLNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        root.children.append(block_node)
    return root


def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        p_node = HTMLNode(tag="p", children=[])
        paragraph_text = " ".join(block.split("\n"))  # join lines with spaces
        text_nodes = text_to_textnodes(paragraph_text)
        for node in text_nodes:
            child_html = text_node_to_html_node(node)
            p_node.children.append(child_html)
        return p_node
    
    elif block_type == BlockType.CODE:
        lines = block.split("\n")                           # split into lines
        inner_lines = lines[1:-1]                           # drop first and last ``` lines
        code_text = "\n".join(inner_lines) + "\n"           # rejoin with \n, keep trailing \n

        text_node = TextNode(code_text, TextType.TEXT)      # plain text
        code_child = text_node_to_html_node(text_node)      # <code> text child

        code_node = HTMLNode(tag="code", children=[code_child])
        pre_node = HTMLNode(tag="pre", children=[code_node])
        return pre_node
        
    elif block_type == BlockType.HEADING:
        level = 0
        for ch in block:
            if ch == "#":
                level += 1
            else:
                break

        tag_string = f"h{level}"                      # e.g. "h2"
        stripped_heading_block = block[level + 1:].lstrip()  # skip '#' * level + space

        h_node = HTMLNode(tag=tag_string, children=[])
        heading_nodes = text_to_textnodes(stripped_heading_block)
        for node in heading_nodes:
            h_node_child = text_node_to_html_node(node)
            h_node.children.append(h_node_child)
        return h_node
        
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        # lines 81 to 85 can be shortened to this:  
        # stripped_lines = [line.lstrip("> ") for line in lines if line] 
        stripped_lines = []             
        for line in lines:
            if line:                                                  # skip empty lines
                stripped_line = line.lstrip("> ")
                stripped_lines.append(stripped_line)
        quote_text = " ".join(stripped_lines)

        quote_text_nodes = text_to_textnodes(quote_text)
        q_node = HTMLNode(tag="blockquote", children=[])

        for node in quote_text_nodes:
            q_node_child = text_node_to_html_node(node)
            q_node.children.append(q_node_child)

        return q_node

    elif block_type == BlockType.ULIST:
        lines = block.split("\n")
        ul_node = HTMLNode(tag="ul", children=[])
        for line in lines:
            if line:
                stripped_line = line.lstrip("- ")
                li_text_nodes = text_to_textnodes(stripped_line)
                li_node = HTMLNode(tag="li", children=[])
                for tn in li_text_nodes:
                    li_child = text_node_to_html_node(tn)
                    li_node.children.append(li_child)
                ul_node.children.append(li_node)
        return ul_node
    
    elif block_type == BlockType.OLIST:
        lines = block.split("\n")
        ol_node = HTMLNode(tag="ol", children=[])
        for line in lines:
            if line:
                i = 0
                while i < len(line) and line[i].isdigit():
                    i += 1
                stripped_line = line[i + 2 :]
                li_text_nodes = text_to_textnodes(stripped_line)
                li_node = HTMLNode(tag="li", children=[])
                for tn in li_text_nodes:
                    li_child = text_node_to_html_node(tn)
                    li_node.children.append(li_child)
                ol_node.children.append(li_node)
        return ol_node



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