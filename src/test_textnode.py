import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_NotEqual(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 =TextNode("This is different", TextType.BOLD, "sisiriski.com")
        self.assertNotEqual(node, node4)

    def test_DifferentTextType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_DifferentContent(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()