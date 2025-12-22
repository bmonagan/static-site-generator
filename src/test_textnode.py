import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD,"space_station")
        node2 = TextNode("This is a text node", TextType.BOLD,"space_station")
        self.assertEqual(node, node2)
    def test_differentURL(self):
        node = TextNode("This is a text node", TextType.BOLD,"space_station")
        node2 = TextNode("This is a text node", TextType.BOLD,"NOTspace_station")
        self.assertNotEqual(node, node2)
    def test_URLeqNONE(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,None )
        self.assertEqual(node, node2)
    def test_textType_notEqual(self):
        node = TextNode("This is a text node", TextType.PLAIN,"space_station")
        node2 = TextNode("This is a text node", TextType.BOLD,"space_station")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
