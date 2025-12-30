from block_type import BlockType, block_to_block_type
from markdown_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode
from text_to_children import text_to_children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    if not blocks:
        raise ValueError("Must be a non-empty markdown")
    print(blocks)
    for block in blocks:
        parent_tag = block_to_block_type(block)
        if parent_tag == BlockType.CODE:
            # textnode -> text node to html node
        else:
            children_nodes = text_to_children(block)
        



md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

markdown_to_html_node(md)