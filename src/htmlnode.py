class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # case 1: no tag → just raw text/value
        if self.tag is None:
            if self.value is None:
                return ""
            return str(self.value)

        # build children HTML if any
        children_html = ""
        if self.children:
            children_html = "".join(child.to_html() for child in self.children)

        # if we have children, ignore value and use children instead
        inner = children_html if children_html else (self.value or "")

        return f"<{self.tag}{self.props_to_html()}>{inner}</{self.tag}>"

    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for key, value in self.props.items():
            output += f' {key}="{value}"'
        return output

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"