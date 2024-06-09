# let's outline the key tasks you need to complete:

# 1. Split a Markdown document into blocks.
# 2. Determine the type of each block.
# 3. Convert each block into an HTMLNode.
# 4. Create a function to convert the entire Markdown document into an HTMLNode.

from markdown_blocks import (   # type: ignore
    markdown_to_blocks, 
    block_to_block_type,
)

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

# Dealing with:
# 1. Split a Markdown document into blocks.
# function - markdown_to_blocks - already imported, now moving to testing it
# tests for 1:
def test_split_into_blocks():
    markdown_text = """
# Heading 1

This is a paragraph.

> This is a quote.

- List item 1
- List item 2

```python
print("This is a code block")
```
"""

    blocks = markdown_to_blocks(markdown_text)

    expected_blocks = [
"# Heading 1",
"This is a paragraph.",
"> This is a quote.",
"- List item 1\n- List item 2",
"```python\nprint(\"This is a code block\")\n```"
]

    assert blocks == expected_blocks, f"Expected {expected_blocks} but got {blocks}"
    print("test_split_into_blocks passed!")

# Dealing with:
# 2. Determine the type of each block.
# function - block_to_block_type - already imported, now moving on to testing it:
# tests for 2:
def test_determine_block_type():
    blocks = [
        "# Heading 1",
        "This is a paragraph.",
        "> This is a quote.",
        "- List item 1\n- List item 2",
        "```python\nprint(\"This is a code block\")\n```"
    ]

    expected_types = [
        "heading",
        "paragraph",
        "quote",
        "unordered_list",
        "code"
    ]

    block_types = [block_to_block_type(block) for block in blocks]

    assert block_types == expected_types, f"Expected {expected_types} but got {block_types}"
    print("test_determine_block_type passed!")

# Dealing with:
# 3. Convert each block into an HTMLNode.

def test_convert_blocks():
    blocks = [
        "# Heading 1",
        "This is a paragraph with a nested list:\n- List item 1\n- List item 2",
        "> This is a quote with a nested paragraph.\n\nThis is still part of the quote.",
        "```python\nprint(\"This is a code block\")\n```"
    ]

    expected_html = [
        "<h1>Heading 1</h1>",
        "<p>This is a paragraph with a nested list:</p><ul><li>List item 1</li><li>List item 2</li></ul>",
        "<blockquote>This is a quote with a nested paragraph.</blockquote><blockquote>This is still part of the quote.</blockquote>",
        "<pre><code>print(\"This is a code block\")</code></pre>"
    ]

    def convert_block(block):
        block_type = determine_block_type(block)
        if block_type == "heading":
            return convert_heading(block)
        elif block_type == "paragraph":
            return convert_paragraph(block)
        elif block_type == "quote":
            return convert_quote(block)
        elif block_type == "unordered_list":
            return convert_unordered_list(block)
        elif block_type == "code":
            return convert_code(block)

    html_blocks = [convert_block(block) for block in blocks]

    assert html_blocks == expected_html, f


if __name__ == "__main__":
    test_split_into_blocks()
    test_determine_block_type()