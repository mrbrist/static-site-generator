class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")
    
    def props_to_html(self, props):
        string = ""
        if props is not None:
            for key, value in props.items():
                if key is not None:
                    string += f'{key}="{value}" '
        return string
        
    
    def __eq__(self, other):
        if other.tag == self.tag and other.value == self.value and other.children == self.children and other.props == self.props:
            return True
        return False
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.tag = tag
        self.value = value
        self.props = props

    def props_to_html(self, props):
        return super().props_to_html(props).strip()

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value!")
        if self.tag is None:
            return self.value
        
        if self.props is not None:
            return f"<{self.tag} {self.props_to_html(self.props)}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        self.tag = tag
        self.children = children
        self.props = props

    def props_to_html(self, props):
        return super().props_to_html(props).strip()

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag set")
        if len(self.children) == 0:
            raise ValueError("No children set")
            
        children_html = ""
        for c in self.children:
            children_html += c.to_html()
        
        if self.props is not None:
            return f"<{self.tag} {self.props_to_html(self.props)}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"