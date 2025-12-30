from text_to_textnodes import text_to_textnodes
from textTransform import text_node_to_html_node
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        converted = text_node_to_html_node(node)
        children.append(converted)
    
    return children






md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

print(text_to_children(md))