block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(md_block: list[str]):
    # Check if it's a heading (only need to check the first line)
    if md_block.startswith("#"):
        return block_type_heading
    elif md_block.startswith("```") and md_block.endswith("```") :
        return block_type_code
    elif all (line.startswith(">") for line in md_block):
        return block_type_quote
    elif all (line.startswith("* ") for line in md_block):
        return block_type_unordered_list
    elif all (line.startswith("- ") for line in md_block):
        return block_type_unordered_list
    elif all(line.split(".")[0].isdigit() and \
        (i == 0 and line.split(".")[0] == "1" or i > 0 and line.split(".")[0] == str(i+1))
        for i, line in enumerate(md_block)):
        return block_type_ordered_list
    else:
        return block_type_paragraph
