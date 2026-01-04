import unittest
from blocktype import BlockType, block_to_block_type
from functions import markdown_to_blocks

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

> esto
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