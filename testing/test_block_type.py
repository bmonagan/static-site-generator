import unittest
from block_type import BlockType, block_to_block_type 

class TestBlockType(unittest.TestCase):

    def test_initial_paragraph(self):
        block = "This is **bolded** paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_initial_multiline_paragraph(self):
        block = "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_initial_unordered_list(self):
        block = "- This is a list\n- with items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_heading_h1(self):
        block = "# My Main Topic"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block_multiline(self):
        block = "```python\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_ordered_list_multidigit(self):
        block = "10. First item\n11. Second item\n12. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_non_contiguous(self):
        block = "10. First item\n12. Third item" 
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blockquote_with_space(self):
        block = "> This is the first line of the quote.\n> This is the second line."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_mixed_content(self):
        block = "- Item 1\nThis line is not a list item\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_too_long(self):
        block = "###### The End" 
        self.assertEqual(block_to_block_type(block), BlockType.HEADING) 

if __name__ == '__main__':
    unittest.main()