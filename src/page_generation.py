import os
from extract_title import extract_title
from MDblock_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}{template_path}")
    markdown = open(from_path, "r").read()
    template = open(template_path, "r").read()
    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_html)
    print(f"Page generated successfully at {dest_path}")