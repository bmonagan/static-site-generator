from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    #Assumes we have a markdown with a len > 0
    md_len = len(markdown)

    if markdown[0] == "#":
        return BlockType.HEADING
    elif md_len > 6 and markdown[:3] == markdown[md_len-3 : md_len] == "```":
        return BlockType.CODE
    line_split = markdown.split("\n")
    if all(len(line) > 2 and line[0:2]  == "> " for line in line_split):
        return BlockType.QUOTE
    elif all(line[0] == "-" for line in line_split ):
        return BlockType.UNORDERED_LIST
    elif all(line[0].isnumeric() for line in line_split):
        dot_index = line_split[0].find(".")
        if dot_index == -1:
                return BlockType.PARAGRAPH
        current_num = int(line_split[0][0:dot_index])
        for line in line_split[1:]:
            dot_index = line.find(".")
            if dot_index == -1:
                return BlockType.PARAGRAPH
            line_number = int(line[0:dot_index])
            if line_number != current_num + 1:
                return BlockType.PARAGRAPH
            current_num = line_number
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

blocks = ["This is **bolded** paragraph","This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line","- This is a list\n- with items"]

for block in blocks:
    res = block_to_block_type(block)
    print(res)
        
    
     
            
            