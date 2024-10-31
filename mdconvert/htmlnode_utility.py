from mdconvert.mdblocks import markdown_to_blocks, block_to_block_type
from mdconvert.textnode_utility import text_node_to_html_node, text_to_textnodes
from mdconvert.parentnode import ParentNode


def markdown_to_html_str(markdown: str) -> str:
    html_document = ""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        trimmed_block = _trim_block(block, block_type)
        text_nodes = text_to_textnodes(trimmed_block, block_type)
        child_html_nodes = []
        for text_node in text_nodes:
            child_html_node = text_node_to_html_node(text_node)
            child_html_nodes.append(child_html_node)
        parent_node = ParentNode(child_html_nodes, tag=block_type)
        block_html_string = parent_node.to_html()
        html_document += block_html_string
    return html_document

def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "h1":
            return _trim_block(block, block_type)
    raise ValueError(f"Could not find title (header 1) in document: {markdown}")

def _trim_block(block: str, blocktype: str) -> str:
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
            return block[2:]
        case "ul":
            trimmed_lines = []
            for line in block.split("\n"):
                trimmed_line = f"<li>{line[2:]}</li>"
                trimmed_lines.append(trimmed_line)
            return "".join(trimmed_lines)
        case "ol":
            trimmed_lines = []
            for line in block.split("\n"):
                trimmed_line = f"<li>{line[3:]}</li>"
                trimmed_lines.append(trimmed_line)
            return "".join(trimmed_lines)
        case _:
            raise ValueError("BlockType not found")
