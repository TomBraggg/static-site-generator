from mdconvert.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children: list[HTMLNode], tag: str=None, props: dict=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("No tag associated with parent node")
        if not self.children:
            raise ValueError("No children associated with parent node")
        tree_string = f'<{self.tag}{self.props_to_html()}>' 
        for child in self.children:
            tree_string += child.to_html()
        tree_string += f'</{self.tag}>'
        return tree_string
