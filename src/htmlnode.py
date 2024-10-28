class HTMLNode():
    def __init__(self, tag: str=None, value: str=None, children: list['HTMLNode']=None, props: dict=None) -> 'HTMLNode':
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self)-> str:
        prop_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                prop_string += f' {key}="{value}"'
        return prop_string
    
    def __eq__(self, node) -> bool:
        return (self.tag == node.tag and
                self.value == node.value and
                self.children == node.children and
                self.props == node.props)
    
    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
