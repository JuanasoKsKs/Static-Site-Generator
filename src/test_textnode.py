import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image


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

    def test_bold(self):
        node = TextNode("this is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        #self.assertNotEqual(node, node)
        self.assertEqual(html_node.__repr__(), "LeafNode(b, this is bold, None)")
        self.assertEqual(html_node.to_html(), "<b>this is bold</b>")
        
class TestInlineTextNode(unittest.TestCase):
    def test_bold_in_text(self):
        node = TextNode("this is **bold** text", TextType.TEXT)
        converted_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(converted_nodes, [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])

    def test_italic_in_text(self):
        node = TextNode("this is a text in _italic_ text", TextType.TEXT)
        converted_nodes = split_nodes_delimiter([node],"_",TextType.ITALIC)
        self.assertEqual(converted_nodes, [
            TextNode("this is a text in ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])

class TestExtractImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text_string = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
        result = extract_markdown_images(text_string)
        self.assertEqual(result, [("image", "https://i.imgur.com/zjjcJKZ.png"), ("second image", "https://i.imgur.com/3elNhQu.png")])

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    #==============EXTRACT IMAGES NODES FROM TEXT NODE================
    def test_split_node_images(self):
        node = TextNode( "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result,"!")

        


if __name__ == "__main__":
    unittest.main() 