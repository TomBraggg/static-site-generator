from page_generator import *


content_path = "content"
template_path = "template.html"
destination_path = "public"

def main():
    start()
    generate_page_recursive(content_path, template_path, destination_path)


if __name__ == "__main__":
    main()
