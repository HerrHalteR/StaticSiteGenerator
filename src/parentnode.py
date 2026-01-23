from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: 'tag' has no value")
        if self.children is None:
            raise ValueError("Invalid HTML: 'children' has no value")
        return f"<{self.tag}{self.props_to_html()}>{self.children.to_html()}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"
    
