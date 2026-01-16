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

    titlecontent = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    final_html = titlecontent.replace("href=/", f'href="{from_path}').replace("src=/", f'src="{from_path}/')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_html)
    print(f"Page generated successfully at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isdir(entry_path):
            # Recursively process subdirectories
            generate_pages_recursive(entry_path, template_path, os.path.join(dest_dir_path, entry))
        elif entry.endswith(".md"):
            # Generate page for markdown files
            dest_path = os.path.join(dest_dir_path, entry[:-3] + ".html")
            generate_page(entry_path, template_path, dest_path)