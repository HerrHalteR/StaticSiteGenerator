import os
import shutil

from copystatic import sync_static_to_public
from pages import generate_page


def main():
    source_path = "./static"
    dest_path = "./public"

    sync_static_to_public(source_path, dest_path)

    generate_page(
        "content/index.md",
        "template.html",
        "public/index.html",
    )


if __name__ == "__main__":
    main()