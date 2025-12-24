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



test = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
res = text_to_textnodes(test)
print(res)


desired_output = [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]

assert res == desired_output