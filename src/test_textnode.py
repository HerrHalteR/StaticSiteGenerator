import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_bold_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq_different_text_types(self):
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node3, node4)
        
    def test_eq_same_link_with_url(self):
        node5 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node6 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node5, node6)
        
    def test_not_eq_link_url_differs(self):
        node7 = TextNode("This is another link with no url", TextType.LINK)
        node8 = TextNode("This is another link with no url", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node7, node8)
        

if __name__ == "__main__":
    unittest.main()