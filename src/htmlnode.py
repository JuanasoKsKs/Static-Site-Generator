class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        text = ""
        if self.props is None:
            return ""
        for atribute in self.props:
            text += f' {atribute}="{self.props[atribute]}"'
        return text

    def __repr__(self):
        """atributes = ""
        if self.props != None:
            for atribute in self.props:
                atributes += f" {atribute}: {self.props[atribute]}"
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{atributes})"""
        #This was an attempt to show the atributes as a dictionary in different lines
        #(I soon realized that there's no need to complicate things more than needed)
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("the LeafNode must have a vale")
        if self.tag == None:
            return self.value
        if self.tag == "a":
            return f'<a{self.props_to_html()}>{self.value}</a>'
        if self.tag == "img":
            return f'<img{self.props_to_html()} />'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html():
        if self.tag == None:
            raise ValueError("A Tag value is required")
        if self.children == None:
            raise ValueError("Children/s are required")
        