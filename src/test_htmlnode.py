import unittest
from htmlnode import HTMLNode  # type: ignore

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("p", "text in paragraph", ["c1", "c2", "c3"],
                            {"href": "https://www.google.com", "target": "_blank"})
        html_node2 = HTMLNode("p", "text in paragraph", ["c1", "c2", "c3"],
                            {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html_node, html_node2)

    def test_eq_false(self):
        html_node = HTMLNode("p", "text in paragraph", ["c1", "c2", "c3"],
                             {"href": "https://www.google.com", "target": "_blank"})
        html_node2 = HTMLNode("q", "text not in paragraph", ["d1", "d2", "d3"],
                              {"href": "https://www.googlewoo.com", "target": "_full"})
        self.assertNotEqual(html_node, html_node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

if __name__ == "__main__":
    unittest.main()
