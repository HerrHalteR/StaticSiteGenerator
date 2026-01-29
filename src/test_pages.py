import unittest
import os
import tempfile
from pages import extract_title, generate_page


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_uses_first_h1_only(self):
        md = """
# First title

# Second title that should be ignored
"""
        actual = extract_title(md)
        self.assertEqual(actual, "First title")

    def test_works_with_more_content(self):
        md = """
# title

this is a bunch

of text

- and
- a
- list
"""
        actual = extract_title(md)
        self.assertEqual(actual, "title")

    def test_raises_if_no_title(self):
        md = """
no title here
"""
        with self.assertRaises(Exception):
            extract_title(md)

# add to src/test_pages.py
import os
import tempfile
import unittest

from pages import extract_title, generate_page

class TestGeneratePage(unittest.TestCase):
    def test_generate_page_basic(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            md_path = os.path.join(tmpdir, "index.md")
            tpl_path = os.path.join(tmpdir, "template.html")
            dest_path = os.path.join(tmpdir, "public", "index.html")

            # simple markdown and template
            with open(md_path, "w") as f:
                f.write("# Hello\n\nThis is *content*.")
            with open(tpl_path, "w") as f:
                f.write("<title>{{ Title }}</title><body>{{ Content }}</body>")

            generate_page(md_path, tpl_path, dest_path)

            with open(dest_path, "r") as f:
                html = f.read()

            self.assertIn("<title>Hello</title>", html)
            self.assertIn("<body>", html)    # content converted + inserted


if __name__ == "__main__":
    unittest.main()