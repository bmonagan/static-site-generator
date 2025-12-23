from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self,tag =None,value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        
        if not self.tag:
            return str(self.value)
        
        else:
            html_props = self.props_to_html() 
           
            if html_props:
                return f"<{self.tag} {html_props}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

