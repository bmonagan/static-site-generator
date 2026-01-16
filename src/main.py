import sys
from textnode import TextNode,TextType
from file_management import copy_static_to_public
from page_generation import generate_pages_recursive
def main():
    copy_static_to_public()
    print("Static files copied to public directory successfully.")
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="public",basepath=basepath)
    print("All pages generated successfully.")

    


if __name__ == "__main__":
    main()

