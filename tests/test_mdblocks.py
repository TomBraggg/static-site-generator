import unittest
import mdconvert.mdblocks as mdblocks


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
        blocks = mdblocks.markdown_to_blocks(markdown)
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
        blocks = mdblocks.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_para(self):
        block = "This is just a paragraph lol\nThis is the second line"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.PARAGRAPH.value
        self.assertEqual(block_type, expected_result)

    def test_block_to_block_type_code(self):
        block = "```This is some amazing code brev\nMultiline code no way```"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.CODE.value
        self.assertEqual(block_type, expected_result)

    def test_block_to_block_type_quote(self):
        block = ">This is my quote\n>You either win or you learn"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.QUOTE.value
        self.assertEqual(block_type, expected_result)

    def test_block_to_block_type_unordered_list_1(self):
        block = "- This is my unordered list\n- How disorderly"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.UNORDERED_LIST.value
        self.assertEqual(block_type, expected_result)

    def test_block_to_block_type_unordered_list_2(self):
        block = "* This is my unordered list\n* How disorderly"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.UNORDERED_LIST.value
        self.assertEqual(block_type, expected_result)

    def test_block_to_block_type_ordered_list_1(self):
        block = "1. I\n2. Will\n3. Have\n4. Order!"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.ORDERED_LIST.value
        self.assertEqual(block_type, expected_result)

    def test_block_to_block_type_ordered_list_2(self):
        block = "1. I\n3. Won't\n4. Have\n5. Order!"
        block_type = mdblocks.block_to_block_type(block)
        expected_result = mdblocks.BlockType.PARAGRAPH.value
        self.assertEqual(block_type, expected_result)


if __name__ == "__main__":
    unittest.main()
