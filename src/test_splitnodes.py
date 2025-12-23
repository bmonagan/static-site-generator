import unittest
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_single_match(self):
        input_node = TextNode("This is a `code block`.", TextType.TEXT)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(len(expected_nodes), 3)

    def test_multiple_matches(self):
        input_node = TextNode("The **quick** brown fox jumped **over** the lazy dog.", TextType.TEXT)
        expected_nodes = [
            TextNode("The ", TextType.TEXT),
            TextNode("quick", TextType.BOLD),
            TextNode(" brown fox jumped ", TextType.TEXT),
            TextNode("over", TextType.BOLD),
            TextNode(" the lazy dog.", TextType.TEXT),
        ]
        self.assertEqual(len(expected_nodes), 5)
        
    def test_delimiter_at_edges(self):
        input_node = TextNode("**Bold text** in the middle and **end**.", TextType.TEXT)
        expected_nodes = [
            TextNode("Bold text", TextType.BOLD),
            TextNode(" in the middle and ", TextType.TEXT),
            TextNode("end", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(len(expected_nodes), 4)

    def test_no_delimiter_present(self):
        input_node = TextNode("This text has no special formatting.", TextType.TEXT)
        expected_nodes = [
            TextNode("This text has no special formatting.", TextType.TEXT),
        ]
        self.assertEqual(len(expected_nodes), 1)

    def test_mismatched_delimiter_raises_error(self):
        input_node = TextNode("This is missing a closing `delimiter.", TextType.TEXT)
        
        with self.assertRaises(ValueError):
            pass

if __name__ == '__main__':
    unittest.main()