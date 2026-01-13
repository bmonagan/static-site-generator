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
        tag_type = block_to_block_type(block)
        parent_tag = block_type_to_html_tag(tag_type)
        
        if tag_type == BlockType.CODE:
            # 1. Strip ```, 2. Create <code> children, 3. Wrap in <pre> parent.
            # This handles the special structure and stripping.
            code_text = block.strip()
            if code_text.startswith("```"):
                code_text = code_text[3:]
            if code_text.endswith("```"):
                code_text = code_text[:-3]
            code_text = code_text.strip()
            # Strip leading indentation from each line
            lines = code_text.split("\n")
            dedented_lines = [line.lstrip() for line in lines]
            code_text = "\n".join(dedented_lines) + "\n"
            code_node = TextNode(code_text, TextType.CODE)
            code_htmlnode = text_node_to_html_node(code_node)
            parent = ParentNode(tag=parent_tag, children=[code_htmlnode])
            complete_children.append(parent)
        
        
        elif tag_type in [BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]:
            # 1. Process line by line, 2. Strip list markers, 3. Create <li> children, 
            # 4. Wrap all <li>'s in <ul> or <ol> parent.
            lines = block.split("\n")
            list_items = []
            for line in lines:
                line = line.strip()
                if tag_type == BlockType.UNORDERED_LIST:
                    if line.startswith("- "):
                        line = line[2:]
                    elif line.startswith("* "):
                        line = line[2:]
                elif tag_type == BlockType.ORDERED_LIST:
                    # Strip numbering like "1. ", "2. ", etc.
                    dot_index = line.find(". ")
                    if dot_index != -1:
                        line = line[dot_index + 2:]
                
                children_nodes = text_to_children(line)
                li_node = ParentNode(tag="li", children=children_nodes)
                list_items.append(li_node)
            
            parent = ParentNode(tag=parent_tag, children=list_items)
            complete_children.append(parent)
            
        elif tag_type == BlockType.HEADING:
            # 1. Strip the leading '#' characters and space.
            # 2. Proceed with inline processing on the remaining text.
            # 3. Create the <hX> parent.
            heading_text = block.lstrip("#").strip()
            children_nodes = text_to_children(heading_text)
            parent = ParentNode(tag=parent_tag, children=children_nodes)
            complete_children.append(parent)

        elif tag_type == BlockType.QUOTE:
            # 1. Strip the leading '> ' from each line.
            # 2. Combine the lines (or process separately).
            # 3. Create the <blockquote> parent.
            lines = block.split("\n")
            quote_lines = []
            for line in lines:
                if line.startswith("> "):
                    quote_lines.append(line[2:])
                else:
                    quote_lines.append(line)
            quote_text = " ".join(quote_lines)
            children_nodes = text_to_children(quote_text)
            parent = ParentNode(tag=parent_tag, children=children_nodes)
            complete_children.append(parent)
            
        else: # BlockType.PARAGRAPH
            # This is your current generic logic, which is fine for paragraphs.
            normalized_text = block.replace("\n", " ")
            # Normalize multiple spaces to single space
            normalized_text = " ".join(normalized_text.split())
            children_nodes = text_to_children(normalized_text)
            parent = ParentNode(tag=parent_tag, children=children_nodes)
            complete_children.append(parent)
    
    parent_html_node = ParentNode(tag="div", children=complete_children)
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