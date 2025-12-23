from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self,tag =None,value=None, props=None):
        super().__init__(value,tag,props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return str(self.value)
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                html_props = self.props_to_html()
                return f"<{self.tag} {html_props}>{self.value}</{self.tag}>"

