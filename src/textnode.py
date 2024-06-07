
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