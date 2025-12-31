from block_type import BlockType

html_tag_map = {
    "PARAGRAPH": "p",
    "HEADING": "h1",  
    "CODE": "pre",    
    "QUOTE": "blockquote",
    "UNORDERED_LIST": "ul",
    "ORDERED_LIST": "ol"
}


def block_type_to_html_tag(block_type):
    if block_type not in html_tag_map:
        raise ValueError("Must be a block type")
    else:
        return html_tag_map[block_type]