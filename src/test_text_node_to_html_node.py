import unittest
from main import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        # Testing PLAIN text (matches your TextType.PLAIN)
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        # Testing the link conversion with a URL
        node = TextNode("Click here!", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here!")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        # Testing the image conversion (empty value, specific props)
        node = TextNode("alt text", TextType.IMAGE, "https://boot.dev/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, 
            {"src": "https://boot.dev/img.png", "alt": "alt text"}
        )

if __name__ == "__main__":
    unittest.main()