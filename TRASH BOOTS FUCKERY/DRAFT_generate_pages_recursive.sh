function generate_pages_recursive(content_dir, template_path, dest_dir):
    list all entries in content_dir
    for each entry in entries:
        if entry is a file:
            if entry name ends with ".md":
                source_path = join(content_dir, entry name)        # e.g. content/blog/tom/index.md
                html_name = entry name with ".md" -> ".html"       # e.g. index.html
                dest_path = join(dest_dir, html_name)              # e.g. public/blog/tom/index.html
                call generate_page(source_path, template_path, dest_path)

        else if entry is a directory:
            sub_content_dir = join(content_dir, entry name)        # e.g. content/blog/tom
            sub_dest_dir = join(dest_dir, entry name)              # e.g. public/blog/tom
            create sub_dest_dir if it does not exist
            call generate_pages_recursive(sub_content_dir, template_path, sub_dest_dir)


function main():
    source_path = "./static"
    dest_path = "./public"
    call sync_static_to_public(source_path, dest_path)

    call generate_pages_recursive("content", "template.html", "public")

---
os.listdir: lists the files inside the given directory
os.path.join: concatenate path segments
os.path.isfile: returns true if the given path is a file
pathlib.Path: the Path class
---

startswith Full Tooltip

def startswith(prefix: str | Tuple[str, ...], start: int | None = ..., end: int | None = ...) -> bool
"""
Return True if the string starts with the specified prefix, False otherwise.
With optional start, test string beginning at that position.
With optional end, stop comparing at that position.
prefix can also be a tuple of strings to try.
"""

---

endswith Full Tooltip

def endswith(suffix: str | Tuple[str, ...], start: int | None = ..., end: int | None = ...) -> bool
"""
Return True if the string ends with the specified suffix, False otherwise.
With optional start, test string beginning at that position.
With optional end, stop comparing at that position.
suffix can also be a tuple of strings to try.
"""