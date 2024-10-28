import re
from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> str:
    match text_node.text_type:
        case TextType.TEXT: 
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, tag="b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, tag="i")
        case TextType.CODE:
            return LeafNode(text_node.text, tag="code")
        case TextType.LINK:
            return LeafNode(text_node.text, tag="a", props={
                "href": text_node.url,
            })
        case TextType.IMAGE:
            return LeafNode("", tag="img", props={
                "src": text_node.url,
                "alt": text_node.text,
            })
        case _:
           raise Exception(f"Text type {text_node.text_type} not found") 

def split_nodes_delimeter(old_nodes: TextNode, delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        new_node_segments = []
        if node.text_type != text_type.TEXT:
            pass
        if delimiter not in node.text or node.text.count("`") != 2:
            new_nodes.append([node])
            continue
            # raise Exception(f"Could not find the relevent delimeter pair for text_type:'{node.text_type}' in text '{node.text}'")

        split_node = node.text.split(delimiter)
        new_node_segments.append(TextNode(split_node[0], TextType.TEXT))
        new_node_segments.append(TextNode(f"{split_node[1]}", text_type))
        new_node_segments.append(TextNode(split_node[2], TextType.TEXT))
        new_nodes.append(new_node_segments)

    return new_nodes

def extract_markdown_images(text):
    md_images = re.findall("!\[(.*?)\]\((.*?)\)", text)
    return md_images
