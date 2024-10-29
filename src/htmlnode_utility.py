from mdblocks import *
from parentnode import *
from leafnode import *
from htmlnode import *
from textnode_utility import *


def markdown_to_html_node(markdown):
    html_document = ""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        trimmed_block = trim_block(block, block_type)
        text_nodes = text_to_textnodes(trimmed_block)
        child_html_nodes = []
        for text_node in text_nodes:
            child_html_node = text_node_to_html_node(text_node)
            child_html_nodes.append(child_html_node)
        parent_node = ParentNode(child_html_nodes, tag=block_type)
        block_html_string = parent_node.to_html()
        html_document += block_html_string
    return html_document


        # Think i have the block as a string
        # Blocks could contain blocks
        # Need to embed the parent nodes with this

        # Markdown file to blocks (str)
        # Blocks can contain more blocks
        # Each Block is 1 string
        # Convert each block to list[textnodes]
        # Convert text nodes to HTML nodes
        # Convert HTML nodes to HTML String
        # Compount HTML Strings
        # Embed HTML string in block

        # Considerations
        # Headers increment 1 -> 6

def trim_block(block: str, blocktype: str) -> str:
    match blocktype:
        case "p":
            return block
        case "h1":
            return block[2:]
        case "h2":
            return block[3:]
        case "h3":
            return block[4:]
        case "h4":
            return block[5:]
        case "h5":
            return block[6:]
        case "h6":
            return block[7:]
        case "code":
            return block[4:-3]
        case "blockquote":
            return block[1:]
        case "ul":
            trimmed_lines = []
            for line in block.split("\n"):
                trimmed_line = line[2:]
                trimmed_lines.append(trimmed_line)
            return "\n".join(trimmed_lines)
        case "ol":
            trimmed_lines = []
            for line in block.split("\n"):
                trimmed_line = line[3:]
                trimmed_lines.append(trimmed_line)
            return "\n".join(trimmed_lines)
        case _:
            raise ValueError("BlockType not found")
