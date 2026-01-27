from markdown_blocks import markdown_to_blocks
import unittest

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_leading_and_trailing_blank_lines(self):
        md = """

    Hello

    World


    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Hello", "World"])


    def test_multiple_blank_lines_between_blocks(self):
        md = "A\n\n\n\nB"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["A", "B"])


    def test_single_block_no_blank_lines(self):
        md = "Just one block\nwith two lines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one block\nwith two lines"])


if __name__ == "__main__":
    unittest.main()