from htmlnode import HTMLNode, LeafNode, ParentNode 

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None) -> None:
        self.TEXT = TEXT
        self.TEXT_TYPE = TEXT_TYPE
        self.URL = URL
    
    def __eq__(self, other_TN) -> bool:
        """An __eq__ method that returns True if all of 
        the properties of two TextNode objects are equal."""
        if isinstance(other_TN, TextNode):
            return (self.TEXT == other_TN.TEXT and
            self.TEXT_TYPE == other_TN.TEXT_TYPE and
            self.URL == other_TN.URL)
        return False
    
    def __repr__(self) -> str:
        """a __repr__ method that returns a string representation
        of the TextNode object"""
        return f"TextNode({self.TEXT}, {self.TEXT_TYPE}, {self.URL})"
    
def text_node_to_html_node(text_node: TextNode):
    """A function to convert a TextNode to an HTMLNode.
    Well, to be specific, converting to a LeafNode."""
    if text_node.TEXT_TYPE == text_type_text:
        html_node = LeafNode(None, text_node.TEXT, None)
    elif text_node.TEXT_TYPE == text_type_bold:
        html_node = LeafNode("b", text_node.TEXT, None)
    elif text_node.TEXT_TYPE == text_type_italic:
        html_node = LeafNode("i", text_node.TEXT, None)
    elif text_node.TEXT_TYPE == text_type_code:
        html_node = LeafNode("code", text_node.TEXT, None)
    elif text_node.TEXT_TYPE == text_type_link:
        if hasattr(text_node,"URL"):
            html_node = LeafNode("a", text_node.TEXT, {"href": text_node.URL})
        else:
            raise AttributeError("TextNode of type 'link' must have a 'URL'")
    elif text_node.TEXT_TYPE == text_type_image:
        if hasattr(text_node, "URL") and hasattr(text_node, "TEXT"):
            html_node = LeafNode("img", text_node.TEXT, {"src": text_node.URL, "alt": text_node.TEXT})
        else:
            raise AttributeError("TextNode of type 'image' must have 'URL' and 'TEXT'")
    else:
        raise ValueError("improper textnode type supplied")
    
    return html_node

