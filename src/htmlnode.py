class HTMLNode:
    def __init__(self,tag =None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None: 
            return ""
        html_string = ""
        for k, v in self.props.items():
            html_string += f' {k}="{v}"'
        
        return html_string.strip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value},{self.children}, {self.props})"