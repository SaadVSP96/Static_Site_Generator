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


def split_nodes_image(old_nodes:list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.TEXT_TYPE != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.TEXT
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes:list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.TEXT_TYPE != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.TEXT
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    all_type_nodes = []
    main_node = TextNode(text, text_type_text, None)
    w_bold_nodes = split_nodes_delimiter([main_node], "**", text_type_bold)
    w_bold_italic_nodes = []
    for node in w_bold_nodes:
        w_bold_italic_nodes.extend(split_nodes_delimiter([node], "*", text_type_italic))
    w_bold_italic_code_nodes = []
    for node in w_bold_italic_nodes:
        w_bold_italic_code_nodes.extend(split_nodes_delimiter([node], "`", text_type_code))
    w_bold_italic_code_image_nodes = []
    for node in w_bold_italic_code_nodes:
        w_bold_italic_code_image_nodes.extend(split_nodes_image([node]))
    for node in w_bold_italic_code_image_nodes:
        all_type_nodes.extend(split_nodes_link([node]))
    return all_type_nodes

text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
print(text_to_textnodes(text))
