from htmlnode import HTMLNode
from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_raw_text(self):                                                   # Requirement: If tag is None, return raw value
        node = LeafNode(None, "Just some raw text here")
        self.assertEqual(node.to_html(), "Just some raw text here")

    def test_leaf_to_html_with_props(self):                                                 # Test with attributes like a link
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_leaf_to_html_no_value(self):                                                   # Create a node with no value (which is illegal for a LeafNode)
        node = LeafNode("p", None)                                                          # This context manager passes if the code inside raises a ValueError
        with self.assertRaises(ValueError):
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()