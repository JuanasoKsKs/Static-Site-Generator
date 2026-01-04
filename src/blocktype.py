from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ","###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    result = True
    for line in lines:
        if not line.startswith("> "):
            result = False
            break
    if result:
        return BlockType.QUOTE
    result = True
    for line in lines:
        if not line.startswith("- "):
            result = False
            break
    if result:
        return BlockType.UNORDERED_LIST
    result = True
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            result = False
            break
    if result:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    