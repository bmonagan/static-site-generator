import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_anchor_props_to_html(self): 
        node = HTMLNode(
            tag=None, 
            value=None, 
            children=None, 
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        htmltest = node.props_to_html()
        correct_output = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(htmltest, correct_output)

    def test_single_prop(self):
        node = HTMLNode(
            tag="div", 
            value="Content", 
            children=None, 
            props={"class": "main-container"}
        )
        htmltest = node.props_to_html()
        correct_output = 'class="main-container"'
        self.assertEqual(htmltest, correct_output)

    def test_mixed_props(self):
        node = HTMLNode(
            tag="button", 
            value="Click Me", 
            children=None, 
            props={
                "id": "submit-btn",
                "disabled": "true",
                "style": "color: red; font-size: 16px;"
            }
        )
        htmltest = node.props_to_html()
        correct_output = 'id="submit-btn" disabled="true" style="color: red; font-size: 16px;"'
        self.assertEqual(htmltest, correct_output)


if __name__ == "__main__":
    unittest.main()