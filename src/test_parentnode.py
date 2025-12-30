import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_multiple_childrens(self):
        grandchild_node = LeafNode("b", "grandchild")
        second_grandchildren = LeafNode ("bese", "piloto")
        child_node = ParentNode("span", [grandchild_node, second_grandchildren])
        second_child = LeafNode("second", "content of the second")
        parent_node = ParentNode("div", [child_node, second_child])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><bese>piloto</bese></span><second>content of the second</second></div>"
        )

if __name__ == "__main__":
    unittest.main()