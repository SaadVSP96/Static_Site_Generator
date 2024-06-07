class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method should be overridden by child classes to render as HTML.")

    def props_to_html(self):
        """This method returns a string that represents the HTML 
        attributes of the node."""
        if self.props is None:
            return ""
        attribute_str = ""
        for prop in self.props:
            attribute_str += f' {prop}="{self.props[prop]}"'
        return attribute_str
    
    def __repr__(self) -> str:
        """a __repr__ method that returns a string representation
        of the HTMLNode object"""
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


# New class extending the HTMLNode class for leafnodes
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> None:
        if not value:
            raise ValueError("LeafNode requires a value")
        # Calling the constructor of the HTMLNode using super(), setting children to None
        super().__init__(tag, value, None, props)
        self.children = None    # Ensuring children are not allowed

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes require a value.")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


# New class extending the HTMLNode class for leafnodes
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children:list, props: dict = None) -> None:
        if not children:
            raise ValueError("ParentNode must have children")
        # Calling the constructor of the HTMLNode using super(), setting value to None
        super().__init__(tag, None, children, props)
        self.value = None    # Ensuring children are not allowed

    def to_html(self):
        children_html = []
        def helper(html_list):
            if not self.tag:
                raise ValueError("Parent node must have tag")
            if not self.children:
                raise ValueError("ParentNode must have children")
            for child in self.children:
                html_list.append(child.to_html())
        helper(children_html)
        # Join the list into a single string
        children_html = ''.join(children_html)
        return f"<{self.tag}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

lfn = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
print(lfn.to_html())

print()

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
print(node.to_html())