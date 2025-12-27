def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        block.strip()
    
    
    
    return blocks





md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        

print(markdown_to_blocks(md))