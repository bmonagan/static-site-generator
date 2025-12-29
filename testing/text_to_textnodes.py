from markdown_split import split_nodes_image,split_nodes_link
from textnode import TextNode,TextType
from splitnodes import split_nodes_delimiter
def text_to_textnodes(text):
    node = TextNode(text,TextType.TEXT)
    old_nodes = [node]
    
    markdown_openers = {
        TextType.BOLD: "**",
        TextType.ITALIC: "_",
        TextType.CODE: "`"
        }
    for k,v in markdown_openers.items():
        old_nodes = split_nodes_delimiter(old_nodes,v,k)  
    
    link_split = split_nodes_link(old_nodes)
    print(link_split)
    result = split_nodes_image(link_split)
    
   
    
    return result