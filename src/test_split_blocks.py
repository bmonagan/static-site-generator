import unittest
from markdown_blocks import markdown_to_blocks
class TestBlockSplits(unittest.TestCase):
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

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        md = " \n\n \t\n\n "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_multiple_empty_lines_between_blocks(self):
        md = """
# Header 1


This is paragraph one.



Paragraph two with many blank lines.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Header 1",
                "This is paragraph one.",
                "Paragraph two with many blank lines.",
            ],
        )
    def test_block_with_leading_and_trailing_spaces(self):
        md = "  A block with spaces \n on newlines \n\n Another block "
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "A block with spaces \n on newlines",
                "Another block",
            ],
        )


if __name__ == '__main__':
    unittest.main()