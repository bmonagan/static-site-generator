from block_type import BlockType

html_tag_map = {
    BlockType.PARAGRAPH: "p",
    BlockType.HEADING: "h1",
    BlockType.CODE: "pre",
    BlockType.QUOTE: "blockquote",
    BlockType.UNORDERED_LIST: "ul",
    BlockType.ORDERED_LIST: "ol"
}


def block_type_to_html_tag(block_type):
    if block_type not in html_tag_map:
        raise ValueError("Must be a block type")
    else:
        return html_tag_map[block_type]