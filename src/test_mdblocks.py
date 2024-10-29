import unittest
from mdblocks import *


class TestMDBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text.
This is the same paragraph on a new line!

* This is a list
* Item 1
* Item 2
"""
        blocks = markdown_to_blocks(markdown)
        heading = "# This is a heading"
        paragraph = "This is a paragraph of text.\nThis is the same paragraph on a new line!"
        bullets = "* This is a list\n* Item 1\n* Item 2"
        expected_result = [heading, paragraph, bullets]
        self.assertListEqual(blocks, expected_result)

def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


if __name__ == "__main__":
    unittest.main()
