import unittest
from textnode import TextType, TextNode
from splitnodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_single_match(self):
        old_nodes = [TextNode("This is **bold** text.", TextType.TEXT)]
        delimiter = "**"
        
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        
        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.BOLD)
        self.assertEqual(result_nodes, expected_nodes)

    def test_multiple_matches(self):
        old_nodes = [TextNode("`First` and `Second` blocks.", TextType.TEXT)]
        delimiter = "`"
        
        expected_nodes = [
            TextNode("First", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("Second", TextType.CODE),
            TextNode(" blocks.", TextType.TEXT),
        ]
        
        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.CODE)
        self.assertEqual(result_nodes, expected_nodes)
        
    def test_delimiter_at_edges(self):
        old_nodes = [TextNode("~~italic at start and end~~", TextType.TEXT)]
        delimiter = "~~"
        
        expected_nodes = [
            TextNode("italic at start and end", TextType.ITALIC),
        ]
        
        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.ITALIC)
        self.assertEqual(result_nodes, expected_nodes)

    def test_no_delimiter_present(self):
        old_nodes = [TextNode("This text has no special formatting.", TextType.TEXT)]
        delimiter = "*"
        
        expected_nodes = [
            TextNode("This text has no special formatting.", TextType.TEXT),
        ]
        
        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.ITALIC)
        self.assertEqual(result_nodes, expected_nodes)
        
    def test_mismatched_delimiter_raises_error(self):
        old_nodes = [TextNode("This is missing a closing `delimiter.", TextType.TEXT)]
        delimiter = "`"
        
        with self.assertRaisesRegex(ValueError, "Mismatched delimiter"):
            split_nodes_delimiter(old_nodes, delimiter, TextType.CODE)
            
    def test_handling_non_text_node(self):
        old_nodes = [
            TextNode("Text before.", TextType.TEXT),
            TextNode("A link", TextType.LINK, "http://example.com"),
            TextNode(" and `code` here.", TextType.TEXT)
        ]
        delimiter = "`"
        
        expected_nodes = [
            TextNode("Text before.", TextType.TEXT),
            TextNode("A link", TextType.LINK, "http://example.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here.", TextType.TEXT),
        ]
        
        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.CODE)
        self.assertEqual(result_nodes, expected_nodes)
        
    def test_empty_string_between_delimiters(self):
        old_nodes = [TextNode("Example **empty** **test**", TextType.TEXT)]
        delimiter = "**"
        
        expected_nodes = [
            TextNode("Example ", TextType.TEXT),
            TextNode("empty", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("test", TextType.BOLD),
        ]
        
        result_nodes = split_nodes_delimiter(old_nodes, delimiter, TextType.BOLD)
        self.assertEqual(result_nodes, expected_nodes)

if __name__ == '__main__':
    unittest.main()