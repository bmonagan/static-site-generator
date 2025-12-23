from textnode import TextNode,TextType
f
def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        section = node.split(delimiter)
        split_nodes = []
        for i in range(len(section)):
            part = section[i]
            if part == "":
                continue
            if i % 2 == 0:
                node = TextNode(part, TextType.TEXT)
            else:
                node = TextNode(part, text_type)
                split_nodes.append(node)
        new_nodes.extend(split_nodes)
    
    return new_nodes


