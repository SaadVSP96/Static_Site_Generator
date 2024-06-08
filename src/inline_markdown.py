import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
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

def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    image_pattern = re.compile(r"(.*?)!\[(.*?)\]\((.*?)\)")

    for old_node in old_nodes:
        if old_node.TEXT_TYPE != text_type_text:
            new_nodes.append(old_node)
            continue

        pos = 0
        for match in image_pattern.finditer(old_node.TEXT):
            # Add the text before the image
            if match.group(1):
                new_nodes.append(TextNode(match.group(1), text_type_text))

            # Add the image
            new_nodes.append(TextNode(match.group(2), text_type_image, match.group(3)))

            # Update position
            pos = match.end()

        # Add any remaining text after the last match
        if pos < len(old_node.TEXT):
            new_nodes.append(TextNode(old_node.TEXT[pos:], text_type_text))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    link_pattern = re.compile(r"(.*?)\[(.*?)\]\((.*?)\)")

    for old_node in old_nodes:
        if old_node.TEXT_TYPE != text_type_text:
            new_nodes.append(old_node)
            continue

        pos = 0
        for match in link_pattern.finditer(old_node.TEXT):
            # Add the text before the link
            if match.group(1):
                new_nodes.append(TextNode(match.group(1), text_type_text))

            # Add the link
            new_nodes.append(TextNode(match.group(2), text_type_link, match.group(3)))

            # Update position
            pos = match.end()

        # Add any remaining text after the last match
        if pos < len(old_node.TEXT):
            new_nodes.append(TextNode(old_node.TEXT[pos:], text_type_text))

    return new_nodes

