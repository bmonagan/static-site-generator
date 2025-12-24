import re
from textnode import TextNode,TextType
from extraction import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        matched = (extract_markdown_images(node.text))
        paired_labels_set = {label for label, _ in matched}
        sections = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        i = 0
        while i < len(sections):
            if sections[i] in paired_labels_set:
                node = TextNode(sections[i],TextType.IMAGE,sections[i+1])
                i += 2     
            else:
                if sections[i] == None or sections[i] == "":
                    i += 1 
                    continue
                node = TextNode(sections[i],TextType.TEXT)
                i += 1 
            
            split_nodes.append(node)
        new_nodes.extend(split_nodes)

            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        matched = (extract_markdown_links(node.text))
        paired_labels_set = {label for label, _ in matched}
        sections = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        i = 0
        while i < len(sections):
            if sections[i] in paired_labels_set:
                node = TextNode(sections[i],TextType.LINK,sections[i+1])
                i += 2     
            else:
                if sections[i] == None or sections[i] == "":
                    i += 1 
                    continue
                node = TextNode(sections[i],TextType.TEXT)
                i += 1 
            
            split_nodes.append(node)
        new_nodes.extend(split_nodes)

            
    return new_nodes