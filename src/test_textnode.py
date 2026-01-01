import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_NotEqual(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 =TextNode("This is a text node", TextType.BOLD, "sisiriski.com")
        self.assertNotEqual(node, node4)

    def test_DifferentTextType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_DifferentContent(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, None, https://www.boot.dev)", repr(node)
        )
    
    #===========Test Text to HTML Nodes ==========
    #=============================================
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("imagen de jax", TextType.IMAGE, "www.jax.com/jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.__repr__(), "LeafNode(img, img, {'src': 'www.jax.com/jpg', 'alt': 'imagen de jax'})")
        self.assertEqual(html_node.to_html(), '<img src="www.jax.com/jpg" alt="imagen de jax" />')
    
    def test_link(self):
        node = TextNode("link a la victoria", TextType.LINK, "www.victory.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.__repr__(), "LeafNode(a, link a la victoria, {'href': 'www.victory.com'})")
        self.assertEqual(html_node.to_html(),'<a href="www.victory.com">link a la victoria</a>')
        

if __name__ == "__main__":
    unittest.main() 