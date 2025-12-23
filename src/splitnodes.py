from textnode import TextNode,TextType
import re 
def split_nodes_delimiter(old_nodes,delimiter,text_type):
    
    split_nodes = re.split(r'(?<=`)', old_nodes)
    deli = False
    result = []
    for node in split_nodes:
        if deli:
            if node[-1] != delimiter:
                raise ValueError("Must have a paired delimeter")
            else:
                result.append(TextNode(node[:-1], text_type))
                deli = False
            
        if node[-1] == delimiter:
            deli = True
            result.append(TextNode(node[:-1]),TextType.TEXT)
        else:
            result.append(TextNode(node),TextType.TEXT)
    
    return result


