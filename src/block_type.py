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
    if all(line[0]  == ">" for line in line_split):
        return BlockType.QUOTE
    elif all(line[0] == "-" for line in line_split ):
        return BlockType.UNORDERED_LIST
    elif all(line[0].isnumeric() for line in line_split):
        if line_split[0][1] != ".":
            return BlockType.PARAGRAPH
        list_num = line_split[0][0]
        for line in line_split[1:]:
            if line[0] != list_num + 1 or line[1] != ".":
                return BlockType.PARAGRAPH
            list_num = line[0]
            
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

blocks = ["This is **bolded** paragraph","This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line","- This is a list\n- with items"]

for block in blocks:
    res = block_to_block_type(block)
    print(res)
        
    
     
            
            