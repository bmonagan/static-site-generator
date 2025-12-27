import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestMarkdownExtraction(unittest.TestCase):
    def test_basic_output(self):
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)

    def test_only_unformatted_text(self):
        text = "Just plain text here."
        expected_nodes = [
            TextNode(text, TextType.TEXT)
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)
        
    def test_start_and_end_with_formatting(self):
        text = "**Start bold** and some text, then `end code`."
        expected_nodes = [
            TextNode("Start bold", TextType.BOLD),
            TextNode(" and some text, then ", TextType.TEXT),
            TextNode("end code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)

    def test_multiple_images_and_links(self):
        text = "[Link1](L1) ![ImageA](IA) text ![ImageB](IB) [Link2](L2)."
        expected_nodes = [
            TextNode("Link1", TextType.LINK, "L1"),
            TextNode(" ", TextType.TEXT),
            TextNode("ImageA", TextType.IMAGE, "IA"),
            TextNode(" text ", TextType.TEXT),
            TextNode("ImageB", TextType.IMAGE, "IB"),
            TextNode(" ", TextType.TEXT),
            TextNode("Link2", TextType.LINK, "L2"),
            TextNode(".", TextType.TEXT)
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)

    def test_only_one_type_of_formatting(self):
        text = "This is _just_ an italic text _example_."
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("just", TextType.ITALIC),
            TextNode(" an italic text ", TextType.TEXT),
            TextNode("example", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)


if __name__ == '__main__':
    unittest.main()