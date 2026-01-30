import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    splitted_markdown = markdown.splitlines()
    for line in splitted_markdown:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
        
    raise Exception("File has no H1 title")



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    dir_path = os.path.dirname(dest_path)
    if dir_path != "":
        os.makedirs(dir_path, exist_ok=True)
    
    file = open(from_path, "r")        # open markdown file
    markdown_content = file.read()     # read its contents and make a variable from them
    file.close()                       # close it
    
    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    page_html = template_content.replace("{{ Title }}", title)
    page_html = page_html.replace("{{ Content }}", html_content)
    
    html_page_file = open(dest_path, "w")   # open file for writing
    html_page_file.write(page_html)         # write the HTML string
    html_page_file.close()                  # close the file
