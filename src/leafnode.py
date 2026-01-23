from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):    # tag & value have NO default values, making them REQUIRED. But 'props' still defaults to None as per the assignment
        super().__init__(tag, value, None, props)  # Since a "Leaf" cannot have children, we hardcode that as None when calling super().__init__.
        
def to_html(self):
    if self.value is None: # Your guard clause
        raise ValueError("Invalid HTML: no value")
    if self.tag is None:
        return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"