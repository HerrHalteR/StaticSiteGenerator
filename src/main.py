import os
import shutil

from copystatic import sync_static_to_public
from pages import generate_page


def generate_pages_recursive(content_dir, template_path, dest_dir):
    items_in_directory = os.listdir(content_dir)
    for item in items_in_directory:
        source_path = os.path.join(content_dir, item)
        if os.path.isfile(source_path):
            if not item.endswith(".md"):
                continue
            if item.endswith(".md"):
                html_name = item.replace(".md", ".html")
                dest_path = os.path.join(dest_dir, html_name)
                generate_page(source_path, template_path, dest_path)
                
        elif os.path.isdir(source_path):
            sub_content_dir = os.path.join(content_dir, item)        # e.g. content/blog/tom
            sub_dest_dir = os.path.join(dest_dir, item)              # e.g. public/blog/tom
            if not os.path.exists(sub_dest_dir):
                os.mkdir(sub_dest_dir)
            generate_pages_recursive(sub_content_dir, template_path, sub_dest_dir)


def main():
    source_path = "./static"
    dest_path = "./public"

    sync_static_to_public(source_path, dest_path)

    generate_pages_recursive(
        "content",
        "template.html",
        "public",
    )


if __name__ == "__main__":
    main()