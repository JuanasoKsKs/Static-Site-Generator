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
        self.assertEqual('<img src="url/of/Camille.jpg" alt="Poster de Camille" />', node.to_html())

    def test_leaf_to_html(self):
        node = LeafNode("b", "this is bold")
        self.assertEqual(node.to_html(), "<b>this is bold</b>")

    def test_leaf_tohtml_notag(self):
        node = LeafNode(None, "empty")
        self.assertEqual("empty", node.to_html())

    def test_leaf_has_children_None(self):
        node = LeafNode("c", "this is invented")
        self.assertEqual(node.children, None)

if __name__ == "__main__":
    unittest.main()