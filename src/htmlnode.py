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
        #(I soon realized that theres no need to complicate things more thatn needed)
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"