def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []

    for block in blocks:
        cblock = block.strip()
        if cblock != "":
            cleaned_blocks.append(cblock)
    
    
    
    return cleaned_blocks