from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str=None, props: dict=None) -> 'LeafNode':
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError(f"Leafnode: {self}\nNo value associated with leaf node")

        if self.tag == None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
