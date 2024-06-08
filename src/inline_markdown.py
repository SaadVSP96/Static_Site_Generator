from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes: TextNode, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.TEXT_TYPE != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.TEXT.split(delimiter)
        if len(sections) % 2 ==0:
            raise ValueError("Invalid Mrkdown, Formatted Section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

