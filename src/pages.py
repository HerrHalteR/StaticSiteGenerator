import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("File has no H1 title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # ensure dest directory exists
    dir_path = os.path.dirname(dest_path)
    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)

    # read markdown
    with open(from_path, "r") as f:
        markdown_content = f.read()

    # read template
    with open(template_path, "r") as f:
        template_content = f.read()

    # convert markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    # fill template
    page_html = template_content.replace("{{ Title }}", title)
    page_html = page_html.replace("{{ Content }}", html_content)

    # write output
    with open(dest_path, "w") as f:
        f.write(page_html)