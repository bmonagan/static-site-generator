def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []

    for block in blocks:
        cblock = block.strip()
        if cblock != "":
            cleaned_blocks.append(cblock)
    
    
    
    return cleaned_blocks





md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

blocks = ["This is **bolded** paragraph","This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line","- This is a list\n- with items"]

cblocks = markdown_to_blocks(md)
assert blocks == cblocks
print(cblocks)