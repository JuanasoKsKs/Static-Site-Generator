import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, World")
        self.assertEqual(node.to_html(), "<p>Hello, World</p>")

    def test_leaf_link_to_html(self):
        node = LeafNode("a", "Link to pro!!", {"href": "https://www.sisiriski.page.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.sisiriski.page.com">Link to pro!!</a>')

    def test_leaf_image_to_html(self):
        node = LeafNode(
            tag="img",
            value="Default",
            props={"src": "url/of/Camille.jpg", "alt":  "Poster de Camille",}
        )
        print("passsssssssssssssssssssssss")
        self.assertEqual('<img src="url/of/Camille.jpg" alt="Poster de Camille" />', node.to_html())

    def test_leaf_to_html(self):
            node = LeafNode("b", "this is bold")
            self.assertEqual(node.to_html(), "<b>this is bold</b>")
