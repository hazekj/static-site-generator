import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div", "Hello", None, {"id": "first", "href": "https://www.me.com"}
        )
        self.assertEqual(node.props_to_html(), ' id="first" href="https://www.me.com"')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Click here", {"href": "www.me.com"})
        self.assertEqual(node.to_html(), '<a href="www.me.com">Click here</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Rawr text")
        self.assertEqual(node.to_html(), "Rawr text")

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")


if __name__ == "__main__":
    unittest.main()
