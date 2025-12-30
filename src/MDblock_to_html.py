from block_type import BlockType, block_to_block_type
from markdown_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    if not blocks:
        raise ValueError("Must be a non-empty markdown")
    print(blocks)
    for block in blocks:
        parent_tag = block_to_block_type(block)
        split_nodes = text_to_textnodes(block)
        print(split_nodes)
        # parent_node = ParentNode(parent_tag,split_nodes)
        # parent_html = parent_node.to_html()
        # print(parent_html)
        # blocks are html parents
        # each additional thing inside is a 

        



md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

markdown_to_html_node(md)