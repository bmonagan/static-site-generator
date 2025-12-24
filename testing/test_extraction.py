import unittest
from extraction import extract_markdown_links, extract_markdown_images
class TestMarkdownExtraction(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Start ![image1](https://url1.png) middle ![image2](https://url2.jpg) end"
        )
        self.assertListEqual(
            [
                ("image1", "https://url1.png"),
                ("image2", "https://url2.jpg"),
            ],
            matches
        )

    def test_extract_markdown_images_no_alt_text(self):
        matches = extract_markdown_images(
            "This is an image with no alt text: ![](/path/to/img.gif)"
        )
        self.assertListEqual([("", "/path/to/img.gif")], matches)

    def test_extract_markdown_images_next_to_text(self):
        matches = extract_markdown_images(
            "Text![image](https://url.png)Next"
        )
        self.assertListEqual([("image", "https://url.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and an ![image](image.png)"
        )
        self.assertListEqual([("link", "https://boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Link 1: [a link](https://boot.dev/link1). Link 2: [another](https://boot.dev/link2) and an ![image](image.png)"
        )
        self.assertListEqual(
            [
                ("a link", "https://boot.dev/link1"),
                ("another", "https://boot.dev/link2"),
            ],
            matches
        )

if __name__ == '__main__':
    unittest.main()