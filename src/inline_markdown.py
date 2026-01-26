import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
            
        for i, part in enumerate(parts):
            if part == "":
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))  # plain TextNode
            else:
                new_nodes.append(TextNode(part, text_type))      # plain TextNode
                
    return new_nodes


def extract_markdown_images(text):
    matches_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_images
    

def extract_markdown_links(text):
    matches_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_links