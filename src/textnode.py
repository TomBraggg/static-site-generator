from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text: str, enum: TextType, url: str=None) -> 'TextNode':
        self.text = text
        self.text_type = enum
        self.url = url

    def __eq__(self, node) -> bool:
        return (self.text == node.text and
                self.text_type == node.text_type and
                self.url == node.url)

    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type}, {self.url})' if self.url else f'TextNode({self.text}, {self.text_type})'
