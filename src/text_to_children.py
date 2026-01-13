from text_to_textnodes import text_to_textnodes
from textTransform import text_node_to_html_node
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        converted = text_node_to_html_node(node)
        children.append(converted)
    
    return children