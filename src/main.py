from textnode import TextNode,TextType
from file_management import copy_static_to_public
from page_generation import generate_pages_recursive
def main():
    copy_static_to_public()
    print("Static files copied to public directory successfully.")

    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="public")
    print("All pages generated successfully.")

    


if __name__ == "__main__":
    main()

