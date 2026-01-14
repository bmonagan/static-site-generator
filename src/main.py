from textnode import TextNode,TextType
from file_management import copy_static_to_public
from page_generation import generate_page
def main():
    copy_static_to_public()
    print("Static files copied to public directory successfully.")

    generate_page(from_path="./content/index.md", template_path="./template.html", dest_path="./public/index.html")

    


if __name__ == "__main__":
    main()

