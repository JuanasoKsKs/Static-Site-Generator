from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode, HTMLNode
def main():
    dummy = TextNode("Anchor text", TextType.LINK, "Juanaso.com/Sisiriski")
    dummy2 = HTMLNode("p", "values", None, None)
    dummy3 = LeafNode("p", "values", None)
    dummy4 = ParentNode("p", [dummy2, dummy3], None)
    print(dummy)
    print(dummy2)
    print(dummy3)
    print(dummy4)

main()