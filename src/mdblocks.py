from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block: str) -> str:
    if is_heading(block):
        return f"{BlockType.HEADING.value}{len(block.split()[0])}"
    elif is_code(block):
        return BlockType.CODE.value
    elif is_quote(block):
        return BlockType.QUOTE.value
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST.value
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST.value
    else:
        return BlockType.PARAGRAPH.value

def is_heading(block):
    return bool(re.match(r"^#{1,6} .+", block))

def is_code(block):
    return (block[:3] == "```" and block [-3:] == "```")

def is_quote(block):
    for line in block.split("\n"):
        if line[0] != ">":
            return False
    return True

def is_unordered_list(block):
    for line in block.split("\n"):
        if line[:2] != "* " and line[:2] != "- ":
            return False
    return True

def is_ordered_list(block):
    for i, line in enumerate(block.split("\n")):
        line_num = i + 1
        if line[:3] != f"{line_num}. ":
            return False
    return True
