import unittest

from parentnode import ParentNode
from leafnode import LeafNode



class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children_and_props(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("a", "Link text", {"href": "https://example.com"})

        parent_node = ParentNode(
            "div",
            [child1, child2],
            {"class": "container", "id": "main"}
        )
        expected_html = (
            '<div class="container" id="main">'
            '<p>First paragraph</p>'
            '<a href="https://example.com">Link text</a>'
            '</div>'
        )
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_with_mixed_nested_structure(self):
        nested_leaf = LeafNode("i", "Italic text")
        nested_parent = ParentNode("em", [nested_leaf])

        sibling_leaf = LeafNode("strong", "Bold text")

        parent_node = ParentNode("body", [sibling_leaf, nested_parent])

        expected_html = "<body><strong>Bold text</strong><em><i>Italic text</i></em></body>"

        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_deep_nesting(self):
        great_grandchild = LeafNode("span", "Deepest content", {"style": "color: red"})
        grandchild = ParentNode("i", [great_grandchild])
        child = ParentNode("b", [grandchild])
        parent_node = ParentNode("p", [child])

        expected_html = (
            '<p>'
            '<b>'
            '<i>'
            '<span style="color: red">Deepest content</span>'
            '</i>'
            '</b>'
            '</p>'
        )
        self.assertEqual(parent_node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()