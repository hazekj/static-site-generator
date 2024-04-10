import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html2(self):
        node = ParentNode(
            None, [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")]
        )
        with self.assertRaises(ValueError, msg="Must have tag"):
            node.to_html()

    def test_to_html3(self):
        node = ParentNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html4(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(
                            "div", "italic text", {"class": "divider", "id": "divisor"}
                        )
                    ],
                    {"id": "para"},
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<div><p id="para"><div class="divider" id="divisor">italic text</div></p>Normal text</div>',
        )


if __name__ == "__main__":
    unittest.main()
