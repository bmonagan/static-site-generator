from block_type import BlockType

html_tag_map = {
    BlockType.PARAGRAPH: "p",
    BlockType.HEADING: "h1",
    BlockType.CODE: "pre",
    BlockType.QUOTE: "blockquote",
    BlockType.UNORDERED_LIST: "ul",
    BlockType.ORDERED_LIST: "ol"
}

heading_tag_map = {
    1: "h1",
    2: "h2",
    3: "h3",
    4: "h4",
    5: "h5",
    6: "h6"
}


def block_type_to_html_tag(block_type, heading_level=None):
    if block_type == BlockType.HEADING:
        if heading_level is not None:
            return heading_tag_map.get(heading_level, "h1")
        return "h1"
    
    if block_type not in html_tag_map:
        raise ValueError("Must be a block type")
    else:
        return html_tag_map[block_type]