import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")                                      # Create a single child leaf node
        parent_node = ParentNode("div", [child_node])                               # Wrap it in a parent div
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")    # Verify it renders the parent tag wrapping the child tag

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")                # Create a deep nest: Leaf -> Parent -> Parent
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(                                            # Verify the recursion correctly drills down to the bottom
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(                                           # Test a mix of tagged leaves and raw text (None tags)
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(                                            # Verify they are all concatenated in order without extra spaces
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_headings(self):
        node = ParentNode(                                           # Verify that ParentNode still correctly handles 'props' (attributes)
            "h2",
            [LeafNode("span", "Subtitle")],
            {"class": "main-title"}
        )
        self.assertEqual(
            node.to_html(),
            '<h2 class="main-title"><span>Subtitle</span></h2>'
        )

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "bold")])            # Ensure the guard clause raises ValueError if the tag is missing
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)                              # Ensure the guard clause raises ValueError if the children are missing 
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":                                          # Standard entry point to run all tests in this file
    unittest.main()