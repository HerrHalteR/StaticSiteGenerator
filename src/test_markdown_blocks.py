from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
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


    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> a\n> b"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_ulist(self):
        block = "- a\n- b"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)

    def test_block_to_block_type_olist(self):
        block = "1. a\n2. b"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)

    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("just text"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()