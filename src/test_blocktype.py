import unittest
from blocktype import BlockType, block_to_block_type
from functions import markdown_to_blocks, markdown_to_html_node, text_to_children

class TestBlockType(unittest.TestCase):
    def test_blocktype(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

1. primero
2. segundo
3. lo que sigue

> esto`
> deberia 
> de resaltar

# Heading 1
## Heading 2

```
el codigo al final
```

2. parece lista pero
3. es un parrafo porque no inicia en 1

"""
        blocks = markdown_to_blocks(md)
        result = []
        for block in blocks:
            result.append(block_to_block_type(block))

        self.assertEqual(len(result), 8)
        self.assertEqual(result[0], BlockType.PARAGRAPH)
        self.assertEqual(result[1], BlockType.PARAGRAPH)
        self.assertEqual(result[2], BlockType.UNORDERED_LIST)
        self.assertEqual(result[3], BlockType.ORDERED_LIST)
        self.assertEqual(result[4], BlockType.QUOTE)
        self.assertEqual(result[5], BlockType.HEADING)
        self.assertEqual(result[6], BlockType.CODE)
        self.assertEqual(result[7], BlockType.PARAGRAPH)

class MarkdownToHTMLNodes(unittest.TestCase):
    def test_conversion(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        parent = markdown_to_html_node(md)
        html = parent.to_html()
        self.assertEqual(html, 
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_quote(self):
        md = """
normal text

> quote
> test
"""
        parent = markdown_to_html_node(md)
        html = parent.to_html()
        self.assertEqual(html, '<div><p>normal text</p><blockquote>quote\ntest</blockquote></div>')

