from textnode import TextNode, TextType
from leafnode import LeafNode # Need this to create the return objects

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
    # Test our new function directly in main
    node = TextNode("Hello World", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

if __name__ == "__main__":
    main()