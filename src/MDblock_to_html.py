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
        # new version to fill out.
        if tag_type == BlockType.CODE:
        # 1. Strip ```, 2. Create <code> children, 3. Wrap in <pre> parent.
        # This handles the special structure and stripping.
        
        elif tag_type in [BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]:
            # 1. Process line by line, 2. Strip list markers, 3. Create <li> children, 
            # 4. Wrap all <li>'s in <ul> or <ol> parent.
            
        elif tag_type == BlockType.HEADING:
            # 1. Strip the leading '#' characters and space.
            # 2. Proceed with inline processing on the remaining text.
            # 3. Create the <hX> parent.

        elif tag_type == BlockType.QUOTE:
            # 1. Strip the leading '> ' from each line.
            # 2. Combine the lines (or process separately).
            # 3. Create the <blockquote> parent.
            
        else: # BlockType.PARAGRAPH
            # This is your current generic logic, which is fine for paragraphs.
            # normalized_text = block.replace("\n", " ")
            # ... create <p> parent
    ## OLDER BROKEN VERSION ##
    #     parent_tag_type = block_to_block_type(block)
    #     parent_tag = block_type_to_html_tag(parent_tag_type)
    #     if parent_tag_type == BlockType.CODE:
    #         code_node = TextNode(block, TextType.CODE)
    #         code_htmlnode = text_node_to_html_node(code_node)
    #         complete_children.append(code_htmlnode) 
    #     else:
    #         normalized_text = block #block.replace("\n", " ")
    #         children_nodes = text_to_children(normalized_text)
    #         smaller_parent = ParentNode(tag = parent_tag, children = children_nodes)
    #         complete_children.append(smaller_parent)
    # parent_html_node = ParentNode(tag= "div", children= complete_children)
    
    # return parent_html_node



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