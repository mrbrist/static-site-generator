from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    match block:
        case s if re.search(r"^(#{1,6})\s+(.+)$", s):
            return BlockType.HEADING
        case s if s.startswith("```") and s.endswith("```"):
            return BlockType.CODE
        case s if s.startswith(">"):
            return BlockType.QUOTE
        case s if s.startswith("- "):
            return BlockType.ULIST
        case s if re.search(r"^\d+\.\s+.+$", s, re.MULTILINE):
            return BlockType.OLIST
        case _:
            return BlockType.PARAGRAPH
        