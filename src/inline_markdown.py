import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
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


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        text = node.text
        images = extract_markdown_images(text)
        
        if len(images) == 0:
            result.append(node)
            continue

        for (alt, url) in images:
            snippet = f"![{alt}]({url})"
            before, after = text.split(snippet, 1)
            if before != "":
                result.append(TextNode(before, TextType.TEXT))
            result.append(TextNode(alt, TextType.IMAGE, url))
            text = after
        
        if text != "":
            result.append(TextNode(text, TextType.TEXT))
                    
    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)

        if len(links) == 0:
            result.append(node)
            continue
        
        for (link_text, url) in links:
            snippet = f"[{link_text}]({url})"
            before, after = text.split(snippet, 1)
            if before != "":
                result.append(TextNode(before, TextType.TEXT))
            result.append(TextNode(link_text, TextType.LINK, url))
            text = after
        
        if text != "":
            result.append(TextNode(text, TextType.TEXT))
                    
    return result

def text_to_textnodes(text):
    textnode = TextNode(text, TextType.TEXT)
    textnode_list = [textnode]
    bold_split = split_nodes_delimiter(textnode_list, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "_", TextType.ITALIC)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    image_split = split_nodes_image(code_split)
    link_split = split_nodes_link(image_split)
    return link_split
