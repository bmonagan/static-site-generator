import unittest
from textnode import TextNode,TextType
from markdown_split import split_nodes_image, split_nodes_link  

class TestMarkdownSplit(unittest.TestCase):
    
    def test_split_images_at_edges(self):
        node = TextNode(
            "![Start](start.jpg)text in the middle![End](end.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.IMAGE, "start.jpg"),
                TextNode("text in the middle", TextType.TEXT),
                TextNode("End", TextType.IMAGE, "end.jpg"),
            ],
            new_nodes,
        )

    def test_split_images_multiple_non_text_node(self):
        node1 = TextNode("Already bold", TextType.BOLD)
        node2 = TextNode("Text with ![one](1.png) and ![two](2.png) images.", TextType.TEXT)
        node3 = TextNode("Another bold section", TextType.BOLD)
        
        new_nodes = split_nodes_image([node1, node2, node3])
        self.assertListEqual(
            [
                TextNode("Already bold", TextType.BOLD),
                TextNode("Text with ", TextType.TEXT),
                TextNode("one", TextType.IMAGE, "1.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "2.png"),
                TextNode(" images.", TextType.TEXT),
                TextNode("Another bold section", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_split_images_adjacent(self):
        node = TextNode(
            "Here are two images: ![first](1.png)![second](2.png) end.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here are two images: ", TextType.TEXT),
                TextNode("first", TextType.IMAGE, "1.png"),
                TextNode("second", TextType.IMAGE, "2.png"),
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_links_at_edges(self):
        node = TextNode(
            "[Start](start.html)text in the middle[End](end.html)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.LINK, "start.html"),
                TextNode("text in the middle", TextType.TEXT),
                TextNode("End", TextType.LINK, "end.html"),
            ],
            new_nodes,
        )

    def test_split_links_mixed_with_images(self):
        node = TextNode(
            "Check out my ![image](image.png) and my [link](website.com).",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Check out my ![image](image.png) and my ", TextType.TEXT),
                TextNode("link", TextType.LINK, "website.com"),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_adjacent(self):
        node = TextNode(
            "Here are two links: [first](1.html)[second](2.html) end.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here are two links: ", TextType.TEXT),
                TextNode("first", TextType.LINK, "1.html"),
                TextNode("second", TextType.LINK, "2.html"),
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_images_original(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

if __name__ == '__main__':
    unittest.main()