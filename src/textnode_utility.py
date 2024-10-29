import re
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
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

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimeter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimeter(nodes, '*', TextType.ITALIC)
    nodes = split_nodes_delimeter(nodes, '`', TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimeter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(section, TextType.TEXT))
            else:
                split_nodes.append(TextNode(section, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text: str) -> str:
    md_images = re.findall("!\[(.*?)\]\((.*?)\)", text)
    return md_images

def extract_markdown_links(text: str) -> str:
    md_images = re.findall("\[(.*?)\]\((.*?)\)", text)
    return md_images

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        image_alts_urls = extract_markdown_images(old_node.text)
        if old_node.text_type != TextType.TEXT or len(image_alts_urls) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for i, alt_url in enumerate(image_alts_urls):
            image_alt = alt_url[0]
            image_url = alt_url[1]
            sections = original_text.split(f"![{image_alt}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        image_alts_urls = extract_markdown_links(old_node.text)
        if old_node.text_type != TextType.TEXT or len(image_alts_urls) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for i, alt_url in enumerate(image_alts_urls):
            link_alt = alt_url[0]
            link_url = alt_url[1]
            sections = original_text.split(f"[{link_alt}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
