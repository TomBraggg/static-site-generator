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
        split_segments = node.text.split(delimiter)
        for i, segment in enumerate(split_segments):
            current_type = text_type if i == 1 else text_type.TEXT
            new_node_segments.append(TextNode(segment, current_type))
        new_nodes.append(new_node_segments)
    return new_nodes

def extract_markdown_images(text: str) -> str:
    md_images = re.findall("!\[(.*?)\]\((.*?)\)", text)
    return md_images

def extract_markdown_links(text: str) -> str:
    md_images = re.findall("\[(.*?)\]\((.*?)\)", text)
    return md_images

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        image_alts_urls = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT or len(image_alts_urls) == 0:
            new_nodes.append([node])
            continue
        new_node_segments = []
        original_text = node.text
        for i, alt_url in enumerate(image_alts_urls):
            image_alt = alt_url[0]
            image_url = alt_url[1]
            sections = original_text.split(f"![{image_alt}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_node_segments.append(TextNode(sections[0], TextType.TEXT))
            new_node_segments.append(TextNode(image_alt, TextType.IMAGE, image_url))
            original_text = sections[1]
        if original_text != "":
            new_node_segments.append(TextNode(original_text, TextType.TEXT))
        new_nodes.append(new_node_segments)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        image_alts_urls = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT or len(image_alts_urls) == 0:
            new_nodes.append([node])
            continue
        new_node_segments = []
        original_text = node.text
        for i, alt_url in enumerate(image_alts_urls):
            image_alt = alt_url[0]
            image_url = alt_url[1]
            sections = original_text.split(f"[{image_alt}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_node_segments.append(TextNode(sections[0], TextType.TEXT))
            new_node_segments.append(TextNode(image_alt, TextType.LINK, image_url))
            original_text = sections[1]
        if original_text != "":
            new_node_segments.append(TextNode(original_text, TextType.TEXT))
        new_nodes.append(new_node_segments)
    return new_nodes
