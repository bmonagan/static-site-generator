import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Just some plain text.")
        self.assertEqual(node.to_html(), "Just some plain text.")

    def test_leaf_to_html_with_props(self):
        props = {"href": "https://boot.dev", "target": "_blank"}
        node = LeafNode("a", "Click me!", props)
        expected_html_1 = '<a href="https://boot.dev" target="_blank">Click me!</a>'
        expected_html_2 = '<a target="_blank" href="https://boot.dev">Click me!</a>'
        print(node)
        actual_html = node.to_html()
        
        
        self.assertTrue(actual_html == expected_html_1 or actual_html == expected_html_2)
        



if __name__ == '__main__':
    unittest.main()