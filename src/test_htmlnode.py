import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test basic attributes
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_none_props(self):
        # Test the "None" guard clause we just added
        node = HTMLNode(tag="p", value="hello")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        # Test the string representation
        node = HTMLNode(tag="h1", value="Title")
        self.assertIn("tag: h1", repr(node))
        self.assertIn("value: Title", repr(node))
        
if __name__ == "__main__":
    unittest.main()
    
    

