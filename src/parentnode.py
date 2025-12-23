from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if not self.children:
            raise ValueError("Parent node must have children")

        children_html_parts = []

        for child in self.children:
            children_html_parts.append(child.to_html())

        content = "".join(children_html_parts)

        html_props = self.props_to_html()

        if html_props:
            return f"<{self.tag} {html_props}>{content}</{self.tag}>"
        else:
            return f"<{self.tag}>{content}</{self.tag}>"