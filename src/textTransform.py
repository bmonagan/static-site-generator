from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in (
        TextType.TEXT, TextType.BOLD, TextType.ITALIC,
        TextType.CODE, TextType.LINK, TextType.IMAGE
    ):
        raise Exception(f"Invalid text type: {text_node.text_type}")

    nvalue = text_node.text
    ntag = None
    nprops = None

    if text_node.text_type == TextType.TEXT:
        ntag = None

    elif text_node.text_type == TextType.BOLD:
        ntag = "b"

    elif text_node.text_type == TextType.ITALIC:
        ntag = "i"

    elif text_node.text_type == TextType.CODE:
        ntag = "code"

    elif text_node.text_type == TextType.LINK:
        ntag = "a"
        nprops = {"href": text_node.url}

    elif text_node.text_type == TextType.IMAGE:
        ntag = "img"
        nvalue = ""
        nprops = {"src": text_node.url, "alt": text_node.text}

    return LeafNode(tag=ntag, value=nvalue, props=nprops)