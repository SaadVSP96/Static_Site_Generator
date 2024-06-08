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
    for old_node in old_nodes:
        matches = re.findall(r"(.*?)!\[(.*?)\]\((.*?)\)", old_node.TEXT)
        for match in matches:
            i = 0
            while i < len(match):
                if not match[i]:
                    i +=1 
                    continue
                elif match[i] and ("image" not in match[i]):
                    new_nodes.append(TextNode(match[i], text_type_text))
                    i += 1
                elif "image" in match[i]:
                    new_nodes.append(TextNode(match[i], text_type_image, match[i+1]))
                    i += 2
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        matches = re.findall(r"(.*?)\[(.*?)\]\((.*?)\)", old_node.TEXT)
        for match in matches:
            i = 0
            while i < len(match):
                if not match[i]:
                    i +=1 
                    continue
                elif match[i] and ("link" not in match[i]):
                    new_nodes.append(TextNode(match[i], text_type_text))
                    i += 1
                elif "link" in match[i]:
                    new_nodes.append(TextNode(match[i], text_type_link, match[i+1]))
                    i += 2
    return new_nodes


node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
new_nodes = split_nodes_image([node])
print(new_nodes)

node = TextNode(
    "Some text with a [link](https://example.com) and another [second link](https://example.org)",
    text_type_text,
)
new_nodes = split_nodes_link([node])
print(new_nodes)