from block_type import BlockType, block_to_block_type
from markdown_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_children import text_to_children
from textnode import TextNode, TextType
from textTransform import text_node_to_html_node
from block_type_to_html_tag import block_type_to_html_tag


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    if not blocks:
        raise ValueError("Must be a non-empty markdown")
    complete_children = []
    for block in blocks:
        parent_tag_type = block_to_block_type(block)
        parent_tag = block_type_to_html_tag(parent_tag_type)
        if parent_tag_type == BlockType.CODE:
            code_node = TextNode(block, TextType.CODE)
            code_htmlnode = text_node_to_html_node(code_node)
            complete_children.append(code_htmlnode) 
        else:
            normalized_text = block #block.replace("\n", " ")
            children_nodes = text_to_children(normalized_text)
            smaller_parent = ParentNode(tag = parent_tag, children = children_nodes)
            complete_children.append(smaller_parent)
    parent_html_node = ParentNode(tag= "div", children= complete_children)
    
    return parent_html_node



md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
desired_output =  "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"

output = markdown_to_html_node(md).to_html()
print(output)
assert output == desired_output