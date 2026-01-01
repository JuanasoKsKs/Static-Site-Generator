from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html_node(self):
        return text_node_to_html_node(self)

        
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid Type")
    if text_node.text_type.value == "img":
        return LeafNode(text_node.text_type.value, "img", {
            "src": text_node.url,
            "alt": text_node.text
        } )
    if text_node.text_type.value == "a":
        return LeafNode(text_node.text_type.value, text_node.text, {"href": text_node.url})
    return LeafNode(text_node.text_type.value, text_node.text)
    


