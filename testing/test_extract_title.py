from src.extract_title import extract_title
import unittest


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        """Test extracting a simple title at the beginning"""
        md = "# My Title\n\nSome content here"
        result = extract_title(md)
        self.assertEqual(result, "My Title")

    def test_extract_title_with_content(self):
        """Test extracting title when there's content after it"""
        md = "# Welcome\n\nThis is a paragraph\n\nMore content"
        result = extract_title(md)
        self.assertEqual(result, "Welcome")

    def test_extract_title_with_leading_whitespace(self):
        """Test extracting title with leading/trailing whitespace"""
        md = "#   Spaced Title   \n\nContent"
        result = extract_title(md)
        self.assertEqual(result, "Spaced Title")

    def test_extract_title_not_found(self):
        """Test ValueError when no title is found"""
        md = "This is just content\n\nNo title here"
        with self.assertRaises(ValueError) as context:
            extract_title(md)
        self.assertIn("No title found", str(context.exception))


if __name__ == '__main__':
    unittest.main()
